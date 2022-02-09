from itertools import chain, repeat
from typing import Iterable, Optional, Tuple, TypeVar, cast

import deal
from more_itertools import windowed

_T = TypeVar("_T")


@deal.pre(lambda items, left, right: items[left] is not None)
def split_items(
    items: Tuple[Optional[_T], ...],
    left: int,
    right: int,
) -> Tuple[Tuple[_T, ...], _T, Tuple[_T, ...]]:
    """
    Split a series of values into a left context, a middle value and a right context.

    Assumes that the item at index left is not None. None values are discarded from the
    left and right contexts.

    :param items: Series of values to split.
    :param left: Size of the left context.
    :param right: Size of the right context.
    :return: A tuple with 3 elements: the left context, the middle value and the right
             value.
    """
    left_items = tuple(item for item in items[:left] if item is not None)
    right_items = tuple(item for item in items[left + 1 :] if item is not None)
    middle_item = cast(_T, items[left])
    return left_items, middle_item, right_items


def padded_and_windowed(
    iterable: Iterable[_T], left: int, right: int
) -> Iterable[Tuple[Tuple[_T, ...], _T, Tuple[_T, ...]]]:
    """
    Iterate in a windowed fashion, with padding on both sides.

    :param iterable: Iterable to use for the windowed iteration.
    :param left: Left padding to use.
    :param right: Right padding to use.
    :return: An iterable of tuples. Each tuple is a left context, a middle value and a
             right context.
    """
    padded = windowed(
        chain(repeat(None, left), iterable, repeat(None, right)), left + 1 + right
    )
    return (split_items(items, left, right) for items in padded)
