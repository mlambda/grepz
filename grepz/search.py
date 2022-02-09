from io import StringIO
from re import compile as re_compile
from typing import Iterable

from colorama import Fore, Style

from .utils import padded_and_windowed


def search(
    pattern: str,
    files: Iterable[str],
    before_context: int = 0,
    after_context: int = 0,
) -> None:
    """
    Search for a pattern in files.

    :param pattern: Pattern to look for in files.
    :param files: Files in which to look for.
    :before_context: Lines to display before a match, for context.
    :after_context: Lines to display after a match, for context.
    """
    compiled = re_compile(pattern)
    for filepath in files:
        with open(filepath, encoding="utf8") as fh:
            for left_context, line, right_context in padded_and_windowed(
                fh, before_context, after_context
            ):
                match = compiled.search(line)
                if match is not None:
                    with StringIO() as string_io:
                        for line in left_context:
                            string_io.write(f"{filepath}:{line}")
                        string_io.write(f"{Fore.RED}{filepath}:{line}{Style.RESET_ALL}")
                        for line in right_context:
                            string_io.write(f"{filepath}:{line}")
                        print(string_io.getvalue().rstrip("\n"))
                        print("***")
