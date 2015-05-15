class Singleton(object):
    """
    Class Singleton the simplest design pattern is the singleton,
    which is a way to provide one and only one object of a particular type.
    Based on tornado.ioloop.IOLoop.instance() approach.
    See https://github.com/facebook/tornado
    """
    _lock = threading.Lock()
    __singleton_instance = None

    @classmethod
    def getInstance(cls):
        with cls._lock:
            if not cls.__singleton_instance:
                cls.__singleton_instance = cls()

            return cls.__singleton_instance

