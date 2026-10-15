"""Static review fixture for Tailmesh v3; not imported or executed by the project."""


def inclusive_page_numbers(first: int, last: int) -> list[int]:
    """Return every page from first through last, including both endpoints.

    Equal endpoints return one page; a reversed interval returns no pages.
    """
    if first > last:
        return []
    return list(range(first, last))
