from collections import OrderedDict
import sys as _sys


_oforms, _aforms = None, None
_MAX_WIDTH_BEFORE_DESC = 24


def _split_desc(line):
    line = line
    delims = ('  ', '\t')
    # TODO: Error raising
    assert any(d in line for d in delims)
    for d in delims:
        if d in line:
            idx = line.find(d)
            head, desc = line[:idx], line[idx:]
            head, desc = head.strip(), desc.strip()
            return head, desc


def _gettype(typename):
    if typename in globals():
        return globals()[typename]
    if isinstance(__builtins__, dict):
        return __builtins__[typename]
    # TODO: Make sure if this is necessary
    else:
        return getattr(__builtins__, typename)


def _split_type_default(s):
    # Returns (truncated s, type, typename, default)
    if s.count(':') > 1 and s.count("=") > 1:
        # TODO: Make a special exception type
        raise Exception

    if ":" in s:
        typename = s.split(":")[1].split("=")[0]
        try:
            type = _gettype(typename)
        except AttributeError:
            # TODO: Make a special exception type
            raise Exception
    else:
        type = str
        typename = 'str'

    if "=" in s:
        default = eval(s.split("=")[1])
        if default is None:
            # TODO
            raise Exception("setting None as default is not allowed")
        if not isinstance(default, type):
            msg = "default value does not have"\
                  " the expected type {}".format(type)
            raise Exception(msg)
    else:
        default = None

    s = s.split(":")[0].split("=")[0]
    return s, type, typename, default


def _format_type_default(typename, default):
    if typename is None or typename is 'str':
        typename = ''
    else:
        typename = 'type: {}'.format(typename)

    if default is None:
        default = ''
    else:
        default = 'default: {}'.format(repr(default))

    if not typename and not default:
        return ''

    td = (a for a in (typename, default) if a)
    return ' ({})'.format(', '.join(td))


class OptForm:
    def __init__(self, line):
        self.short, self.long = None, None
        self.is_flag = True
        self.valname, self.valtype = None, str
        self.valtypename, self.default = None, None
        self.width_before_desc = 0

        # TODO: Error handling
        opts, desc = _split_desc(line.strip())
        assert desc
        self.desc = desc
        opts = opts.split()

        # TODO: Error handling
        for opt in opts:
            if opt.startswith('--'):
                assert not self.long and opt.count('-') == 2
                self.long = opt
            elif opt.startswith('-'):
                assert not self.short
                self.short = opt
            else:
                assert self.is_flag
                self.is_flag = False
                tmp = _split_type_default(opt)
                self.valname, self.valtype, self.valtypename, self.default = tmp

    def parse(self, arg):
        try:
            return self.valtype(arg)
        except ValueError:
            # TODO: Specialize exception
            raise Exception("expected '{}' type but Received {} type".format(
                self.valtype, type(arg)))

    @property
    def name(self):
        return self.long[2:] if self.long else self.short[1:]

    @property
    def short_long(self):
        short = self.short if self.short else ""
        long = self.long if self.long else ""
        pad = " " if short and long else ""
        return short + pad + long

    def __repr__(self):
        if self.valname is None:
            val = ''
        else:
            val = ' ' + self.valname
            if self.valtype is not str:
                val = val + ":" + self.valtypename
            if self.default is not None:
                val = val + "=" + repr(self.default)
        return 'OptForm("{short_long}{val}  {desc}")'.format(
            short_long=self.short_long, val=val, desc=self.desc)

    def __str__(self):
        sl = ' ' + self.short_long + '  '
        sl = '{:<{width}}'.format(
            sl, width=self.width_before_desc )
        td = _format_type_default(self.valtypename, self.default)
        desc = self.desc + td
        if len(sl) > _MAX_WIDTH_BEFORE_DESC:
            return '\n'.join((sl, desc))
        return sl + desc


# TODO: Move this to a more proper place
_help_form = OptForm('-h --help  show this help message and exit')


class RequiredArgForm:
    def __init__(self, line):
        # TODO: Error handling
        name, desc = _split_desc(line.strip())
        tmp = _split_type_default(name)
        self.name, self.type, self.typename, self.default = tmp
        self.desc = desc
        self.width_before_desc = 0

        if self.name.startswith('*'):
            self.varlen = True
            self.name = self.name[1:]
        else:
            self.varlen = False

    @property
    def varlen_name(self):
        return '*' + self.name if self.varlen else self.name

    def parse(self, *args):
        if self.varlen:
            return [self.type(a) for a in args]
        return self.type(args[0])

    def __repr__(self):
        typename = ":" + self.typename if self.type is not str else ""
        name = "*" + self.name if self.varlen else self.name
        return 'RequiredArgForm("{name}{type}  {desc}")'.format(
            name=name, type=typename, desc=self.desc)

    def __str__(self):
        name = ' ' + self.varlen_name + '  '
        name = '{:<{width}}'.format(
            name, width=self.width_before_desc)
        td = _format_type_default(self.typename, self.default)
        desc = self.desc + td
        if len(name) > _MAX_WIDTH_BEFORE_DESC:
            return '\n'.join((name, desc))
        return name + desc


def _make_forms(opts):
    seen = set()
    opt_forms, arg_forms = [], []
    for opt in opts:
        if opt.startswith('-'):
            form = OptForm(opt)
            opt_forms.append(form)
        else:
            form = RequiredArgForm(opt)
            arg_forms.append(form)

        if form.name in seen:
            # TODO: Specialize Exception
            raise Exception("conflicting option names")
        seen.add(form.name)

    return opt_forms, arg_forms


def _set_widths(forms):
    max_width = 0
    for form in forms:
        # one space and two spaces are added before and after the content
        if isinstance(form, OptForm):
            l = 1 + len(form.short_long) + 2
        else:
            l = 1 + len(form.name) + 2
        max_width = max(form.width_before_desc, max_width, l)

    for form in forms:
        form.width_before_desc = max_width


def _make_opt_dict(opt_forms):
    d = {}
    for form in opt_forms:
        if form.short:
            d[form.short] = form
        if form.long:
            d[form.long] = form
    return d


def add(option_string):
    global _oforms, _aforms
    opts = option_string.split('\n')
    opts = [l for l in opts if l]
    _oforms, _aforms = _make_forms(opts)
    _set_widths(_oforms)
    _set_widths(_aforms)


def help():
    global _oforms, _aforms

    if _oforms:
        opt_usage = []
        for form in _oforms:
            tmp = form.long if form.long else form.short
            opt_usage.append('[{}]'.format(tmp))
        opt_usage = ' '.join(opt_usage)
    else:
        opt_usage = ''

    if _aforms:
        arg_usage = ('{}'.format(form.varlen_name) for form in _aforms)
        arg_usage = ' '.join(arg_usage)
    else:
        arg_usage = ''

    usage = "usage: {} {} {}".format(
        _sys.argv[0], opt_usage, arg_usage)

    l = [usage]
    if _aforms:
        l.append("\nrequired arguments:")
        for form in _aforms:
            l.append(str(form))
    if _oforms:
        l.append("\noptions:")
        for form in _oforms:
            l.append(str(form))

    l.append('')
    return '\n'.join(l)


class Options:
    def __init__(self, **kwargs):
        self._options = OrderedDict()
        for k, v in kwargs.items():
            self._options[k] = v

    def add(self, key, val):
        self._options[key] = val

    def __getattr__(self, name):
        if name in self._options:
            return self._options[name]
        return None

    def __repr__(self):
        keys = sorted(self._options.keys())
        opts = self._options
        content = ", ".join(k + "=" + repr(v) for k, v in opts.items())
        return "Options({})".format(content)


def parse(argv: list = None, arg_forms=None, opt_forms=None):
    global _sys, _aforms, _oforms
    if not argv:
        argv = _sys.argv[1:]
    if not arg_forms:
        arg_forms = _aforms
    if not opt_forms:
        opt_forms = _oforms

    od = _make_opt_dict(opt_forms)
    options = Options()

    rev_argv = list(reversed(argv))

    # Parse options
    while argv:
        cur = rev_argv[-1]
        if cur.startswith('-'):
            try:
                form = od[cur]
            except KeyError:
                # TODO: specialize Exception
                raise Exception("unrecognized option '{}'".format(cur))

            rev_argv.pop()

            if form.is_flag:
                options.add(form.name, True)
            else:
                options.add(form.name, form.parse(rev_argv.pop()))
        else:
            break

    # Parse arguments
    for form in arg_forms:
        if form.varlen:
            if rev_argv:
                options.add(form.name, form.parse(*reversed(rev_argv)))
            break
        if not rev_argv:
            # TODO
            raise Exception("not enough arguments given")
        options.add(form.name, form.parse(rev_argv.pop()))

    return options
