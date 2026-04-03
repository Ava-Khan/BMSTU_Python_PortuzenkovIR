from .. import module_a  # относительный импорт из родительского пакета

__all__ = ['avg', 'filter_even', 'min_max', 'flatten']


def avg(lst):
    return sum(lst) / len(lst) if lst else 0


def filter_even(lst):
    # использует is_even из module_a
    return [x for x in lst if module_a.is_even(x)]


def min_max(lst):
    return min(lst), max(lst)


def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
