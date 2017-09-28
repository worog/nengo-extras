import urllib

from nengo.utils.compat import pickle, PY2


urlretrieve = urllib.urlretrieve if PY2 else urllib.request.urlretrieve


if PY2:
    from cStringIO import StringIO  # noqa: F401
    import Queue as queue  # noqa: F401
else:
    from io import StringIO  # noqa: F401
    import queue  # noqa: F401


def cmp(a, b):  # same as python2's builtin cmp, not available in python3
    return (a > b) - (a < b)


def pickle_load(file, *args, **kwargs):
    if not PY2:
        kwargs.setdefault('encoding', 'latin1')
    return pickle.load(file, *args, **kwargs)


def pickle_load_bytes(file, *args, **kwargs):
    if not PY2:
        kwargs.setdefault('encoding', 'bytes')
    return pickle.load(file, *args, **kwargs)
