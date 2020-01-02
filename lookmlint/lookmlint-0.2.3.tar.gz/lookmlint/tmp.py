from . import lookml
import re


def date_issues(field, timeframes=None):
    timeframes = set() if timeframes is None else set(timeframes)
    field_timeframes = set()

    if field.is_hidden:
        return {}

    if hasattr(field, 'timeframes') and field.timeframes is not None:
        field_timeframes = set(field.timeframes)

    missing_timeframes = list(timeframes.difference(field_timeframes))
    fix_category = ''
    fix_category_id = 0

    if missing_timeframes:
        if hasattr(field, 'timeframes') and field.timeframes is not None:
            fix_category = 'Add additional timeframes'
            fix_category_id = 1
        if hasattr(field, 'timeframes') and field.timeframes is None:
            fix_category = 'Add all timeframes'
            fix_category_id = 2
        if not hasattr(field, 'timeframes'):
            fix_category = 'Change dimension to dimension_group and add all timeframes'
            fix_category_id = 3
        return {'fix_category': fix_category, 'fix_category_id': fix_category_id, 'current_timeframes': list(field_timeframes), 'missing_timeframes': missing_timeframes}

    return missing_timeframes

def add_additional_timeframes(view, field, timeframes_to_add):
    repo_path = "/Users/michael.shay/PycharmProjects/looker-bigquery/"
    view_to_edit = view + '.view.lkml'

    with open(repo_path + view_to_edit, 'r+') as file:
        view_text = file.read()

    start_of_field_attr = re.search("dimension_group(\s*):(\s*)" + field + "(\s*){",view_text).end()
    timeframes = re.compile("timeframes(\s*):(\s*)\[.*?\]", re.DOTALL)
    timeframes_to_update = timeframes.search(view_text[start_of_field_attr:len(view_text)]).span()
    view_text = view_text.replace(view_text[start_of_field_attr+timeframes_to_update[0]:start_of_field_attr+timeframes_to_update[1]], 'timeframes: [\n      ' + ',\n      '.join(timeframes_to_add) + '\n    ]')

    with open(repo_path + view_to_edit, 'w') as file:
        file.write(view_text)

def add_all_timeframes(view, field, timeframes_to_add):
    repo_path = "/Users/michael.shay/PycharmProjects/looker-bigquery/"
    view_to_edit = view + '.view.lkml'

    with open(repo_path + view_to_edit, 'r+') as file:
        view_text = file.read()

    start_of_field_attr = re.search("dimension_group(\s*):(\s*)" + field + "(\s*){",view_text).end()
    timeframes = re.compile("type(\s*):(\s*)time", re.DOTALL)
    timeframes_to_update = timeframes.search(view_text[start_of_field_attr:len(view_text)]).span()
    view_text = view_text.replace(view_text[start_of_field_attr+timeframes_to_update[0]:start_of_field_attr+timeframes_to_update[1]], 'type: time\n    timeframes: [\n      ' + ',\n      '.join(timeframes_to_add) + '\n    ]')

    with open(repo_path + view_to_edit, 'w') as file:
        file.write(view_text)


def fix_fields(view, timeframes=None):
    timeframes = [] if timeframes is None else timeframes
    results = {}
    for f in view.fields:
        if f.type not in ('date', 'date_time', 'time'):
            continue
        issues = date_issues(f, timeframes)
        if not issues:
            continue
        fix_category_id = issues.get('fix_category_id')
        current_timeframes = set(issues.get('current_timeframes'))
        missing_timeframes = set(issues.get('missing_timeframes'))
        timeframes_to_add = sorted(list(missing_timeframes.union(current_timeframes)))
        if fix_category_id == 1:
            add_additional_timeframes(view.name, f.name, timeframes_to_add)
        if fix_category_id == 2:
            add_all_timeframes(view.name, f.name, timeframes_to_add)
        if fix_category_id == 3:
            continue # manually fix these
        results[f.display_label()] = issues
    return results


def fix_dates():
    repo_path = "/Users/michael.shay/PycharmProjects/looker-bigquery"
    lkml = lookml.LookML(repo_path)
    timeframes = ['date', 'day_of_month', 'day_of_week', 'month', 'month_name', 'quarter', 'time', 'week', 'week_of_year', 'year']
    for v in lkml.views:
        fix_fields(v, timeframes)
