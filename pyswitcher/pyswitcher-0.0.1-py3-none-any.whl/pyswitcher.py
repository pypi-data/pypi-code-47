"""
Switch/case support for python."""
def switch(
    value,
    case:dict,
    default,
    *args,**kwargs
):
    """Switch case.
    usage:
    v=switch(
        value,
        {
            case1: func1,
            case2: func2,
            ...: ...
        },
        [defaultfunc,]
        *args,
        **kwargs
    )
    equals:
    if value==case1:
        v=func1(*args,**kwargs)
    elif value==case2:
        v=func1(*args,**kwargs)
    else:
        v=default(*args,**kwargs)
    """
    return case.get(value,default)(*args,**kwargs)
