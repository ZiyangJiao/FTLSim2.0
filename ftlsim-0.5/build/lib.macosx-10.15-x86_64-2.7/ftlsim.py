# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ftlsim
else:
    import _ftlsim

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class segment(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    n_valid = property(_ftlsim.segment_n_valid_get, _ftlsim.segment_n_valid_set)
    type = property(_ftlsim.segment_type_get, _ftlsim.segment_type_set)
    erase_counts = property(_ftlsim.segment_erase_counts_get, _ftlsim.segment_erase_counts_set)
    read_counts = property(_ftlsim.segment_read_counts_get, _ftlsim.segment_read_counts_set)

    def __init__(self, Np):
        _ftlsim.segment_swiginit(self, _ftlsim.new_segment(Np))
    __swig_destroy__ = _ftlsim.delete_segment

    def write(self, page, lba):
        return _ftlsim.segment_write(self, page, lba)

    def overwrite(self, page, lba):
        return _ftlsim.segment_overwrite(self, page, lba)

    def page(self, _page):
        return _ftlsim.segment_page(self, _page)

# Register segment in _ftlsim:
_ftlsim.segment_swigregister(segment)


def return_pool(arg1):
    return _ftlsim.return_pool(arg1)
class ftl(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    int_writes = property(_ftlsim.ftl_int_writes_get, _ftlsim.ftl_int_writes_set)
    ext_writes = property(_ftlsim.ftl_ext_writes_get, _ftlsim.ftl_ext_writes_set)
    nfree = property(_ftlsim.ftl_nfree_get, _ftlsim.ftl_nfree_set)
    minfree = property(_ftlsim.ftl_minfree_get, _ftlsim.ftl_minfree_set)
    get_input_pool = property(_ftlsim.ftl_get_input_pool_get, _ftlsim.ftl_get_input_pool_set)
    get_input_pool_arg = property(_ftlsim.ftl_get_input_pool_arg_get, _ftlsim.ftl_get_input_pool_arg_set)
    get_pool_to_clean = property(_ftlsim.ftl_get_pool_to_clean_get, _ftlsim.ftl_get_pool_to_clean_set)
    get_pool_to_clean_arg = property(_ftlsim.ftl_get_pool_to_clean_arg_get, _ftlsim.ftl_get_pool_to_clean_arg_set)
    wl_counts = property(_ftlsim.ftl_wl_counts_get, _ftlsim.ftl_wl_counts_set)
    wl_threshold = property(_ftlsim.ftl_wl_threshold_get, _ftlsim.ftl_wl_threshold_set)
    wl_activated = property(_ftlsim.ftl_wl_activated_get, _ftlsim.ftl_wl_activated_set)
    wl_writes = property(_ftlsim.ftl_wl_writes_get, _ftlsim.ftl_wl_writes_set)
    rr_counts = property(_ftlsim.ftl_rr_counts_get, _ftlsim.ftl_rr_counts_set)
    rr_threshold = property(_ftlsim.ftl_rr_threshold_get, _ftlsim.ftl_rr_threshold_set)
    rr_writes = property(_ftlsim.ftl_rr_writes_get, _ftlsim.ftl_rr_writes_set)
    ext_reads = property(_ftlsim.ftl_ext_reads_get, _ftlsim.ftl_ext_reads_set)

    def __init__(self, T, Np):
        _ftlsim.ftl_swiginit(self, _ftlsim.new_ftl(T, Np))

    def put_blk(self, blk):
        return _ftlsim.ftl_put_blk(self, blk)

    def get_blk(self):
        return _ftlsim.ftl_get_blk(self)

    def find_blk(self, lba):
        return _ftlsim.ftl_find_blk(self, lba)

    def find_page(self, lba):
        return _ftlsim.ftl_find_page(self, lba)

    def frontier(self, lba):
        return _ftlsim.ftl_frontier(self, lba)

    def run(self, addrs, count):
        return _ftlsim.ftl_run(self, addrs, count)

    def read(self, addrs):
        return _ftlsim.ftl_read(self, addrs)

    def write(self, addrs):
        return _ftlsim.ftl_write(self, addrs)
    __swig_destroy__ = _ftlsim.delete_ftl

# Register ftl in _ftlsim:
_ftlsim.ftl_swigregister(ftl)
cvar = _ftlsim.cvar

class pool(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    frontier = property(_ftlsim.pool_frontier_get, _ftlsim.pool_frontier_set)
    i = property(_ftlsim.pool_i_get, _ftlsim.pool_i_set)
    pages_valid = property(_ftlsim.pool_pages_valid_get, _ftlsim.pool_pages_valid_set)
    pages_invalid = property(_ftlsim.pool_pages_invalid_get, _ftlsim.pool_pages_invalid_set)
    length = property(_ftlsim.pool_length_get, _ftlsim.pool_length_set)
    next_pool = property(_ftlsim.pool_next_pool_get, _ftlsim.pool_next_pool_set)
    rate = property(_ftlsim.pool_rate_get, _ftlsim.pool_rate_set)

    def __init__(self, ftl, type, Np):
        _ftlsim.pool_swiginit(self, _ftlsim.new_pool(ftl, type, Np))

    def next_segment(self, s):
        return _ftlsim.pool_next_segment(self, s)

    def add_segment(self, blk):
        return _ftlsim.pool_add_segment(self, blk)

    def insert_segment(self, blk):
        return _ftlsim.pool_insert_segment(self, blk)

    def remove_segment(self):
        return _ftlsim.pool_remove_segment(self)

    def tail_segment(self):
        return _ftlsim.pool_tail_segment(self)

    def tail_util(self):
        return _ftlsim.pool_tail_util(self)

    def write(self, lba):
        return _ftlsim.pool_write(self, lba)
    __swig_destroy__ = _ftlsim.delete_pool

# Register pool in _ftlsim:
_ftlsim.pool_swigregister(pool)


def srand(seed):
    return _ftlsim.srand(seed)

def rand():
    return _ftlsim.rand()


