# -*- coding: utf-8 -*-

debug = False

# 喜好配置
# 按顺序
favorite = ['yyets', 'cmct', '衣柜', 'fix']
# 不分序
blacklist = []
# 语言
# chs_eng 简英
# chs     简体
# cht_eng 繁英
# cht     繁体
# eng     英文
lang = ['chs_eng', 'chs', 'cht_eng', 'cht', 'eng']
# 格式
extension = ['ass', 'ssa', 'srt', 'sub']

author_alias = {
    'yyets': ['yyets', '人人'],
    'fix': ['fix', 'f.i.x'],
}

lang_alias = {
    # ('中英', ''),  ('双语', '')??????
    'chs_eng': [('简体', '英文'), ('chs', 'eng'), ('中英', '简体'), ('简', '英')],
    'cht_eng': [('繁体', '英文'), ('繁體', '英文'), ('cht', 'eng'), ('中英', '繁体'), ('繁', '英'), ],
    'chs': ['简体', 'chs', '简', ],
    'cht': ['繁体', '繁體', 'cht', '繁', ],
    'eng': ['英文', 'eng', '英']
}


if __name__ == '__main__':
    pass
