from argparse import ArgumentParser

from .search import search


def _define_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Yet another grep clone")
    parser.add_argument("pattern", help="Pattern to look for")
    parser.add_argument("files", nargs="*", help="Files to search")
    parser.add_argument(
        "-B",
        "--before-context",
        type=int,
        default=0,
        help="Lines of context before a match",
    )
    parser.add_argument(
        "-A",
        "--after-context",
        type=int,
        default=0,
        help="Lines of context after a match",
    )
    return parser


def main() -> None:
    """Execute a search from the CLI."""
    parser = _define_parser()
    args = parser.parse_args()
    search(**vars(args))
