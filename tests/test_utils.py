from grepz.utils import padded_and_windowed, split_items


def test_split_items() -> None:
    items = (None, None, 1, 2, 3, 4, None, None, None)
    assert split_items(items, 4, 4) == ((1, 2), 3, (4,))


def test_padded_and_windowed() -> None:
    items = tuple(range(5))
    result = list(padded_and_windowed(items, 2, 2))
    assert result == [
        ((), 0, (1, 2)),
        ((0,), 1, (2, 3)),
        ((0, 1), 2, (3, 4)),
        ((1, 2), 3, (4,)),
        ((2, 3), 4, ()),
    ]
