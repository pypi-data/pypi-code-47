import re


def process_template_entry(var_provider, entry):
  def dash_to_whitespace_sub(m):
    s = var_provider(m.group('var_name'))
    s = s.replace('-', ' ')
    return s
  dash_to_whitespace_res = re.sub('(dash_to_whitespace\\((?P<var_name>.+?)\\))', dash_to_whitespace_sub, entry)
  if dash_to_whitespace_res != entry:
    return dash_to_whitespace_res
  else:
    return var_provider(entry)


def process_template(var_provider, template):
  def sub(m):
    entry = m.group(1)
    entry = entry[2:len(entry) - 1]
    return process_template_entry(var_provider, entry)
  return re.sub('(\\${.+?})', sub, template)


def get_pr_name(mappings, branch_name):
  def try_map(mapping):
    match = re.search(mapping['regex'], branch_name)
    if match is None:
      return None
    else:
      def var_provider(var_name):
        s = match.group(var_name)
        return "" if s is None else s
      return process_template(var_provider, mapping['template'])
  for mapping in mappings:
    res = try_map(mapping)
    if not res is None:
      return res
  return None
