import json


# This method applies all the rules to an event and return a list of
# targets to which the event belongs
def rule_engine(event, rules):

    # Event Detail is a JSON string. Needs to be converted to Dict.
    event["Detail"] = json.loads(event["Detail"])
    targets = []
    for rule in rules:
        pattern = rule["pattern"]
        target = rule["target"]
        event_lower_case = {
            "detail-type": event["DetailType"],
            "detail": event["Detail"],
            "source": event["Source"],
            "resources": event["Resources"] if "Resources" in event else None,
            "time": event["Time"] if "Time" in event else None,
        }
        state = rule["state"]

        if state == "DISABLED":
            continue

        if match_pattern(pattern, event_lower_case):
            targets.append(target)

    return targets


"""
This method matches an event against a pattern according to AWS Event Bridge
Pattern matching
Check this for more information:
https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html
"""
# TODO Handling numbers at string level
# TODO Nesting for complex pattern matching
# "exists" is handled only if it's the first element in the list
def match_pattern(pattern, event):
    for key, value in pattern.items():

        # Flag to track whether "exists" is present or not
        flag = False

        # Check for exists
        if type(value) is list and len(value):
            if type(value[0]) is dict and "exists" in value[0]:
                is_exists = value[0]["exists"]
                flag = True
                # If exists is true then pattern matches event if:
                # 1. key should exist in event
                # 2. the corresponding value to key in event must be a leaf node
                if is_exists:
                    if key not in event or (
                        type(event[key]) is list or type(event[key]) is dict
                    ):
                        return False

                # If exists is false then pattern matches event if:
                # 1. key should not exist in event
                # 2. If key exists, the corresponding value to key in event must
                # not be a leaf node
                if not is_exists:
                    if (
                        key in event
                        and type(event[key]) is not dict
                        and type(event[key]) is not list
                    ):
                        return False

        # If flag is True, existence of key is checked according to rules of
        # "exists"
        if not flag:
            if key not in event:
                return False

            if type(value) is list and len(value):
                if type(event[key]) is dict:
                    return False

                if type(event[key]) is not list:
                    match = False
                    for pval in value:
                        if match_values(pval, event[key]):
                            match = True
                    if not match:
                        return False

                # Handling Arrays in EventBridge Event Patterns
                if type(event[key]) is list:
                    # Check for array intersection
                    if not intersection(value, event[key]):
                        return False

            elif type(value) is dict:
                if type(event[key]) is not dict:
                    return False

                if not match_pattern(value, event[key]):
                    return False
            else:
                print(
                    "Invalid pattern {}, {} should be a list or "
                    "dict".format(pattern, value)
                )
                return False

    return True


# This method matches values from pattern and event
# Uses complex Pattern matching rules
# https://docs.aws.amazon.com/eventbridge/latest/userguide/content-filtering
# -with-event-patterns.html
def match_values(pval, eval):
    if type(pval) is dict:
        # Prefix matching
        if "prefix" in pval:
            # Prefix matching only works on string-valued fields.
            if type(eval) is not str:
                return False
            if eval.startswith(pval["prefix"]):
                return True

        if "anything-but" in pval:
            if pval["anything-but"] is dict:
                print("Unsupported anything-but pattern: {}", pval)
                return False

            # You can use anything-but with strings and numeric values,
            # including lists that contain only strings, or only numbers.
            if pval["anything-but"] is list:
                if not all(
                    isinstance(item, str) for item in pval["anything-but"]
                ) or not all(isinstance(item, int) for item in pval["anything-but"]):
                    print(
                        "Inside anything but list, either all values are "
                        "number or string, mixed type is not supported: {"
                        "}",
                        pval,
                    )
                    return False

            # If the value matches, return false
            if pval["anything-but"] == eval and type(pval["anything-but"]) == type(
                eval
            ):
                return False
            # Return True is nothing is violated
            return True

    if pval == eval:
        return True

    return False


def intersection(pvalues, evalues):
    for pval in pvalues:
        for eval in evalues:
            if match_values(pval, eval):
                return True

    return False
