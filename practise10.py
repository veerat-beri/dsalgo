from abc import ABC
from threading import Lock


class SingletonMixin(ABC):
    __singleton_instance = None
    __lock = Lock()

    # @classmethod
    # def get_instance(cls, *args, **kwargs):
    def __new__(cls, *args, **kwargs):
        if cls.__singleton_instance is None:
            cls.__lock.acquire()
            if cls.__singleton_instance is None:
                # cls.__singleton_instance = cls(*args, **kwargs)
                cls.__singleton_instance = super().__new__(cls, *args, **kwargs)
            cls.__lock.release()
        return cls.__singleton_instance


class A(SingletonMixin):
# class A():
    def __init__(self):
        self.__random = 'r'


a = A()
b = A()

print(id(a) == id(b))
print(vars(a))
