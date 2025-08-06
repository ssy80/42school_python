

def ft_filter(fn, it):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    if fn is None:
        return iter([x for x in it if x])
    else:
        return iter([x for x in it if fn(x)])