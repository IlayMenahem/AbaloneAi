"""useful decorators"""
import timeit
from functools import wraps

def loggg(func_in=None, *, show_name=True, show_time=True):
    """
    writes the name of the function and how much time
    it took for the function to finish
    """
    def example(f):
        @wraps(f)
        def func(*args, **kwargs):
            start = timeit.timeit()
            result = f(*args, **kwargs)
            end = timeit.timeit()
            print(end - start)
            print(f.__name__)
            print(result)
            return result
        return func

    if func_in is None:
        return example
    return example(func_in)
