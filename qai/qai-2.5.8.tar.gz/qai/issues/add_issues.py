from qai.qconnect.qallback import qallback

def parse_old_format(el):
    segment = el["data"]["content"]["segment"]
    metadata = el["data"]["meta"]
    language = el["data"]["content"]["languageCode"].split("-")[0]
    return segment, metadata, language


def parse_new_format(el):
    segment = el["content"]["segment"]
    metadata = el["meta"]
    language = el["content"]["languageCode"].split("-")[0]
    return segment, metadata, language


def add_issues_to_new_format(el, issues):
    el["issues"] = issues
    return el


def add_issues_to_old_format(el, issues):
    el["data"]["issues"] = issues
    return el


def mock_batch_output(els):
    # Mock no issue batch prediction output
    output_els = []
    for el in els:
        try:
            segment, metadata, language = parse_new_format(el)
            el = add_issues_to_new_format(el, [])  # issues = []
        except KeyError:
            el = add_issues_to_old_format(el, [])
        output_els.append(el)
    return output_els


def add_issues_format_insensitive(instance, el, validator, debug=False, verbose=False):
    # We should pull some of this code out soon
    # Why write it then? because I don't trust the calling services
    # to do what Yakiv says will happen
    try:
        segment, metadata, language = parse_new_format(el)
        new_format = True
    except KeyError:
        print("could not parse in new format, trying old format")
        segment, metadata, language = parse_old_format(el)
        new_format = False

    # try except in case of unforseen problems
    try:
        # envisioned scenario
        # here we would like the validation
        # if validator says "no, shall not pass" 
        # -> we don't callback, just return issues = []
        if verbose:
            print( f"Segment: {segment}")

        if validator(segment):
        #if not validator.has_html(segment): 
            issues = qallback(instance, segment, metadata, language)
        else:
            issues = []
    except:
        print(f"Error log for segment {segment}")

        # Qallback already failed
        # In debug mode we want to see errors so we call it again
        if debug:
            issues = qallback(instance, segment, metadata, language)

        issues = []

    finally:
        if new_format:
            el = add_issues_to_new_format(el, issues)
        else:
            el = add_issues_to_old_format(el, issues)
    return el


def add_issues_format_insensitive_batch(instance, els, debug=False,verbose=False):

    # Format 1-by-1 but pass batched
    # Dependand service should take care of metdata and language
    # Consistent issue format, otherwise empty response
    # Assumption: same meta and language

    input_els = []

    output_els = []

    try:
        new_format = True
        for el in els:
            segment, metadata, language = parse_new_format(el)
            input_els.append(segment)
            
    except KeyError:
        print("could not parse in new format, trying old format")
        new_format = False
        for el in els:
            segment, metadata, language = parse_old_format(el)
            input_els.append(segment)

    except:
        print("inconsistent issues format, mocking empty response")
        return mock_batch_output(els)

    try:
        if verbose:
            print( f"Segment: {input_els}")
        el_issues = qallback(instance, input_els, metadata, language)
    except:
        print("error log for batch of segments, mocking empty response")
        # Qallback already failed
        # In debug mode we want to see errors so we call it again
        if debug:
            el_issues = qallback(instance, input_els, metadata, language)
        return mock_batch_output(els)

    if new_format:
        for el_issue, el in zip(el_issues, els):
            output_els.append(add_issues_to_new_format(el, el_issue))
    else:
        for el_issue, el in zip(el_issues, els):
            output_els.append(add_issues_to_old_format(el, el_issue))
    return output_els
