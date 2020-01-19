# coding:utf-8

def replace_var_in_dict(strcvar,val):
    '''
    【功能】使用字典类型变量val中的value替换字符串strcvar中的${val.key}
    【参数】strcvar:字符串，包含需要被替换的字符串
            val：字典类型，只包含一个键值对，用于替换strcvar中部分字符串的字符串
    【返回】替换后的字符串
    '''
    val = dict(val)
    for k in val:
        strcvar = str(strcvar).replace('${'+ k +'}',str(dict(val)[k]))
    print('strcvar=%s'% strcvar)
    strcvar = eval(strcvar)
    return strcvar

def replace_var_in_str(strcvar,val):
    '''
    【功能】使用字典类型变量val中的value替换字符串strcvar中的${val.key}
    【参数】strcvar:字符串，包含需要被替换的字符串
            val：字典类型，只包含一个键值对，用于替换strcvar中部分字符串的字符串
    【返回】替换后的字符串
    '''
    for k in val:
        strcvar = str(strcvar).replace('${'+ k +'}',str(dict(val)[k]))
    print('strcvar=%s'% strcvar)
    return strcvar

###===========================================================================================
if __name__=='__main__':
    strv = '/aa/${id}'
    val = {'id':'weiping'}
    val2 = {'A':123}
    replace_var_in_str(strv,val)