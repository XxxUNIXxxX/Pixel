class SingletonMeta(type):
    def __init__(cls, *args, **kw):
        cls.instance = None
		def __call__(cls, *args, **kw):
     		if cls.instance is None:
     				cls.instance = super(SingletonMeta, cls).__call__(*args, **kw)
        return cls.instance

class C(object):
    __metaclass__ = SingletonMeta
