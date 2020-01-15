def html_code(language="", start=False, end=False):
    if start: return f'\n<pre><code class="{language}">\n'
    elif end: return f'\n</code></pre>\n'

def convert_to_code(md_source):
    '''
    converts something like this: 

    ```python
    #this is a syntax highlighted code block

    import rangeen
    print(rangeen.danger("No file found!"))
    ```
    to this:

    <pre>
    <code class="python">
    #this is a syntax highlighted code block

    import rangeen
    print(rangeen.danger("No file found!"))
    </code>
    </pre>

    '''
    backtick_count = 0
    backtick = "`"
    start_index, end_index = None, None
    code_start_index, code_end_index, language = None, None, ""
    for index, char in enumerate(md_source):
        if char == backtick:
            backtick_count += 1
            if backtick_count == 3:
                backtick_count = 0
                if start_index == None:
                    start_index = index - 2
                else:
                    end_index = index
                    code_end_index = index - 3
                    break
            elif len(md_source) > index+1 and md_source[index+1] != backtick:
                backtick_count = 0

        elif start_index != None and code_start_index == None:
            if char == '\n' and len(md_source) > index+1:
                code_start_index = index + 1
            elif char in ('\t', '\r', ' '): pass
            else: language += char
    if all((
            start_index is not None,
            end_index is not None,
            code_start_index is not None,
            code_end_index is not None,
          )):
        md_source = md_source[:start_index] + \
                    html_code(language=language, start=True) + \
                    md_source[code_start_index:code_end_index+1] + \
                    html_code(end=True) + \
                    md_source[end_index+1:]
    return md_source

def md_to_code(md):
    backtick_count = md.count("```")
    while backtick_count%2 == 0 and backtick_count!=0:
        md = convert_to_code(md)
        backtick_count = md.count("```")
    return md

def _test():
    with open("pages/index.md") as fp:
        html = md_to_code(fp.read())
        print(html)

if __name__ == '__main__':
    _test()
