from ipdb import set_trace

def with_metaclass(meta, base=object, BaseName = "NewBase"):
    return meta(BaseName, (base,), {})

class Variant(object):
    def __init__(self, vartype, checker = None, constructor = None, from_constructor = None):
        self.vartype = vartype
        self.checker = checker
        self.constructor = constructor
        self.from_constructor = from_constructor 

class InvalidVariantError(Exception):
    def __init__(self, expected_variant, called_with):
        Exception.__init__(self, "%s variant expected, but %s invoked" % (expected_variant, called_with))
        self.called_with = called_with
        self.expected_variant = expected_variant 

class UnionBase(object):
    def __init__(self, **kwargs):
        self._variant_value = None
        self._variant_type = None
        assert len(kwargs) <= 1
        for k,v in kwargs.items():
            self._variant_type = k
            self._variant_value = v

    @property
    def variant_value(self):
        return self._variant_value

    @property
    def variant_type(self):
        return self._variant_type

    def __hash__(self):
        return hash(self.__class__.__name__) + hash(self.variant_type) # + hash(self.variant_value)

    def __repr__(self):
        return "<%s.%s(%s) at %x>" % (self.__class__.__module__, self.__class__.__name__, self.variant_type, id(self))

    def __eq__(self, another):
        if another is None or not hasattr(another, "variant_value"): return False
        v1,v2 = self.variant_value, another.variant_value
        return type(v1) == type(v2) and v1 == v2

    def __getattr__(self, key):
        """ Forward lookups to variant value directly if it is missing in here. """
        return getattr(self.variant_value, key)

    @classmethod
    def hasvariant(cls, name):
        return name in (n for n,v in cls.__variants__)

    @classmethod
    def get_variant_type(cls, name):
        for n,v in cls.__variants__:
            if n == name:
                return cls.ensure_type(v)
        return None

    @classmethod
    def numvariants(cls):
        return len(cls.__variants__)

    @classmethod
    def add_variant(cls, vname, variant):
        if not variant.checker:
            variant.checker = "is_" + vname
        if not variant.constructor:
            variant.constructor = "as_" + vname
        if not variant.from_constructor:
            variant.from_constructor = "from_" + vname

        cls.__variants__.append((vname, variant))
        vtype,checker = variant.vartype, variant.checker
        setattr(cls, checker, cls._makechecker(vtype))
        setattr(cls, vname, cls._makeproperty(vname, vtype, checker))
        setattr(cls, variant.constructor, cls._make_constructor(vname, vtype))
        setattr(cls, variant.from_constructor, cls._make_from_constructor(vname, vtype))

    @classmethod
    def ensure_type(cls, vartype):
        if type(vartype) is str:
            ## types defined by string lazily so need resolution
            if "." not in vartype:
                thismod = cls.__module__ 
                vartype = thismod + "." + vartype
            parts = vartype.split(".")
            first,last = parts[:-1],parts[-1]
            module = ".".join(first)
            import importlib
            module = importlib.import_module(module)
            vartype = getattr(module, last)
        return vartype

    @classmethod
    def _makechecker(cls, vtype):
        return property(lambda x: isinstance(x._variant_value, cls.ensure_type(vtype)))

    @classmethod
    def _makeproperty(cls, vname, vtype, checker):
        def getter(self):
            if getattr(self, checker):
                return self._variant_value
            else:
                raise InvalidVariantError(self._variant_type, vname)
        def setter(self, value):
            vartype = self.__class__.ensure_type(vtype)
            if not issubclass(value.__class__, vartype):
                raise Exception(f"Expected value type to be {vartype}, found: {type(value)}")
            self._variant_type = vname
            self._variant_value = value
        return property(getter, setter)

    @classmethod
    def _make_constructor(cls, vname, vtype):
        def constructor(cls, *args, **kwargs):
            vartype = cls.ensure_type(vtype)
            value = vartype(*args, **kwargs)
            out = cls()
            out._variant_value = value
            out._variant_type = vname
            return out
        return classmethod(constructor)

    @classmethod
    def _make_from_constructor(cls, vname, vtype):
        def constructor(cls, value):
            if type(value) is not vtype:
                raise Exception(f"Expected value type to be {vtype}, found: {type(value)}")
            out = cls()
            out._variant_value = value
            out._variant_type = vname
            return out
        return classmethod(constructor)

class UnionMeta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)

        __variants__ = getattr(x, "__variants__", [])[:]
        setattr(x, "__variants__", __variants__)

        for vname,variant in dct.items():
            if isinstance(variant, Variant):
                x.add_variant(vname, variant)
        return x

class Union(with_metaclass(UnionMeta, UnionBase)):
    pass

def case(name):
    def decorator(func):
        func.__case_matching_on__ = name
        return func
    return decorator

class CaseMatcherMeta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        caseon = getattr(x, "__caseon__", None)
        if not caseon and name != "CaseMatcher":
            raise Exception("Case matcher MUST have a __caseon__ class attribute to indicate union type we can switch on")

        x.__cases__ = getattr(x, "__cases__", {}).copy()
        for _,casefunc in x.__dict__.items():
            if not hasattr(casefunc, "__case_matching_on__"): continue

            matched_on = casefunc.__case_matching_on__
            # TODO - Should we treat matched_on == None as the "default" case?

            if not caseon.hasvariant(matched_on):
                raise Exception("Selected union (%s) type does not have variant being matched on (%s)." % (caseon, matched_on))
            x.__cases__[matched_on] = casefunc

        if caseon and len(x.__cases__) != caseon.numvariants():
            cases = set(x.__cases__.keys())
            variants = set(f for f,_ in caseon.__variants__)
            diff = variants - cases
            if diff:
                raise Exception("Variants in union (%s) unmatched in CaseMatcher(%s.%s): [%s]" % (caseon, caseon.__module__, caseon.__name__, ", ".join(diff)))
        return x

class CaseMatcher(metaclass = CaseMatcherMeta):
    def select(self, expr : Union):
        if not expr: return None, None
        if not isinstance(expr, Union):
            set_trace()
            raise Exception(f"{expr} is not a Union instance")
        for vname, variant in expr.__variants__:
            if getattr(expr, variant.checker):
                return self.__cases__[vname], self.project(expr)
        set_trace()
        assert False, "Case not matched"

    def project(self, expr : Union):
        return expr.variant_value

    def __init__(self, *args, **kwargs):
        self.value = None
        if args or kwargs:
            self.value = self(*args, **kwargs)

    def __call__(self, value, *args, **kwargs):
        func, child = self.select(value)
        if func:
            return func(self, child, *args, **kwargs)
