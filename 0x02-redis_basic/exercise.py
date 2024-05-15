#!/usr/bin/env python3
"""
exercise.py : Redis module
"""
import sys
from functools import wraps
from typing import Union, Optional, Callable
from uuid import uuid4

import redis

UnionOfTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """
    Description: Decorator function to count \
            the number of calls to a method.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrap
        :param self:
        :param args:
        :param kwargs:
        :return:
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Add its input parameters to one list in Redis \
            and store its output into another list.

    :param method: The method to be decorated.
    :return: The decorated method.
    """
    key = method.__qualname__
    i = "".join([key, ":inputs"])
    o = "".join([key, ":outputs"])

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        self._redis.rpush(i, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(o, str(res))
        return res

    return wrapper


class Cache:
    """
    Cache redis class
    """

    def __init__(self):
        """
        Constructor of the Redis model
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: UnionOfTypes) -> str:
        """
        Store data in the cache and return its key.

        Args:
            data (Union[object, List[object]]): \
                    The data to be stored in the cache.

        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> UnionOfTypes:
        """
        Retrieve data from the cache using the provided key.

        Args:
            key (str): The key associated with the data.
            fn (Optional[Callable]): A function to apply (default: None).

        Returns:
            Union[object, None]: The retrieved data, optionally processed.
        """
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_int(self: bytes) -> int:
        """
        Convert bytes to an integer.

        Returns:
            int: The integer representation of the bytes.
        """
        return int.from_bytes(self, sys.byteorder)

    def get_str(self: bytes) -> str:
        """
        Decode bytes to a string using utf-8 encoding.

        Returns:
            str: The decoded string.
        """
        return self.decode("utf-8")
