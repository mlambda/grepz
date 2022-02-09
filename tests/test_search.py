from pathlib import Path
from typing import Any, Iterator

from pytest import fixture

from grepz.search import search


@fixture
def files() -> Iterator[str]:
    return (str(f) for f in (Path(__file__).parent / "assets").iterdir())


def test_search(files: Iterator[str], capsys: Any) -> None:
    search("ham", files)
    captured = capsys.readouterr()
    assert "a.txt:ham" in captured.out
    assert "b.txt:ham" not in captured.out
    assert "c.txt:ham" in captured.out
