import re


def remove_dups(input_str: str) -> str:
    """
    Args:
        input_str: String to be sanitised

    Returns: Sanitised string

    Notes:
        Using rex "([a-zA-Z])(?!\1)"
        Match each character in the string, against a-z, A-Z.
        if a character matches, in the negative lookahead determine if it matches.
        if the lookahead is true - throw away the match, else keep it.
        note: multiple matches!

        Curses be the pain of poorly documented methods.
        For future reference:
        https://docs.python.org/3/library/re.html#re.match - Performs only a single match
        https://docs.python.org/3/library/re.html#re.Pattern.search - Will happily return every match in the string
    """

    match = re.findall(r"([a-zA-Z])(?!\1)", input_str)
    if match is not None:
        return "".join(match)
    else:
        return input_str


if __name__ == '__main__':
    test = [remove_dups("aabbaaccab"), remove_dups("asd"), remove_dups("AAb")]
    print("\n".join([output_str for output_str in test]))
