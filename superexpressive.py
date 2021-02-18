"""
This is a python port of super-expressive, a js library to make regular expressions easier to read and generate. 

"""
import re

__all__ = [
    "ANY_CHAR",
    "CARRIAGE_RETURN",
    "DIGIT",
    "END_OF_INPUT",
    "NEWLINE",
    "NON_DIGIT",
    "NON_WHITESPACE_CHAR",
    "NON_WORD",
    "NON_WORD_BOUNDARY",
    "NULL_BYTE",
    "ONE_OR_MORE",
    "ONE_OR_MORE_LAZY",
    "OPTIONAL",
    "START_OF_INPUT",
    "TAB",
    "WHITESPACE_CHAR",
    "WORD",
    "WORD_BOUNDARY",
    "ZERO_OR_MORE",
    "ZERO_OR_MORE_LAZY",
    "any_of",
    "any_of_chars",
    "anything_but_chars",
    "anything_but_range",
    "anything_but_string",
    "assert_ahead",
    "assert_behind",
    "assert_not_ahead",
    "assert_not_behind",
    "at_least",
    "back_reference",
    "between",
    "capture",
    "exactly",
    "from_regex",
    "group",
    "named_back_reference",
    "optional",
    "range",
    "re_flags_to_string",
    "to_regex",
]


def re_flags_to_string(flags):
    """"""
    possible_flags = {
        re.ASCII: "a",
        re.IGNORECASE: "i",
        re.LOCALE: "L",
        re.UNICODE: "u",
        re.MULTILINE: "m",
        re.DOTALL: "s",
        re.VERBOSE: "x",
    }

    flagchrs = ""
    for flagval, flagchr in possible_flags.items():
        if flags & flagval:
            flagchrs += flagchr

    return f"(?{flagchrs})" if flagchrs else ""


def to_regex(*args, flags=0, compile=True):
    """Turn a collection of strings into a regex."""
    pattern = "".join(args)

    if compile:
        return re.compile(pattern, flags=flags)
    else:
        flagstring = re_flags_to_string(flags)
        pattern = f"{flagstring}{pattern}"
        return pattern


def from_regex(pattern):
    """it would be cool to be provide a "labeling" function which could generate
    the code from a given regex, as part of a debugging suite
    """
    pass


def optional(*args):
    """A optional non-capturing group of the items inside.

    >>> to_regex(optional(DIGIT), compile=False)
    '(?:\\\\d)?'

    """
    return f'(?:{"".join(args)})?'


def capture(*args, name=None):
    """A group that captures its contents.

    >>> to_regex(capture(range(("a", "f"), ("0", "9")), 'XXX'), compile=False)
    '([a-f0-9]XXX)'

    """
    name = f"?<{name}>" if name is not None else ""
    return f'({name}{"".join(args)})'


def group(*args):
    """A group that does not capture its contents.

    >>> to_regex(group(range(("a", "f"), ("0", "9")), 'XXX'), compile=False)
    '(?:[a-f0-9]XXX)'
    """
    return f'(?:{"".join(args)})'


def range(*args, negate=False):
    """An item that matches a range of characters by ascii code.

    >>> import superexpressive as se
    >>> se.to_regex(se.range(('A', 'F')), compile=False)
    '[A-F]'

    """
    character_set = ""
    for arg in args:
        try:
            start, end = arg
            character_set += f"{start}-{end}"
        except:
            raise

    negate = "^" if negate else ""
    return f"[{negate}{character_set}]"


def anything_but_range(*args):
    return range(*args, negate=True)


def any_of_chars(*args):
    chars = "".join(args)
    return f"[{chars}]"


def anything_but_chars(*args):
    chars = "".join(args)
    return f"[^{chars}]"


def anything_but_string(string):
    return group("".join(f"[^{c}]" for c in string))


def exactly(length):
    return f"{{{length}}}"


def at_least(length):
    return f"{length},"


def between(minl, maxl):
    return f"{minl},{maxl}"


def any_of(*args):
    return group("|".join(args))


def back_reference(index):
    return f"\\{index}"


def named_back_reference(name):
    return f"\\k<{index}>"


def assert_ahead(*args):
    return f'(?={"".join(args)})'


def assert_not_ahead(*args):
    return f'(?!{"".join(args)})'


def assert_behind(*args):
    return f'(?<={"".join(args)})'


def assert_not_behind(*args):
    return f'(?<!{"".join(args)})'


#: Matches any character except a newline.
ANY_CHAR = "."
#: Matches any whitespace character
WHITESPACE_CHAR = r"\s"
#: Matches any non-whitespace character, this is the inverse of WHITESPACE_CHAR
NON_WHITESPACE_CHAR = r"\S"
#: Matches any digit character, is the equivalent of range 0-9
DIGIT = r"\d"
#: Matches any non-digit character, this is the inverse of DIGIT
NON_DIGIT = r"\d"
#: Matches any alphanumeric character a-z, A-Z, 0-9, or underscore
#: in bytes patterns or string patterns with the ASCII flag.
#: In string patterns without the ASCII flag, it will match the
#: range of Unicode alphanumeric characters (letters plus digits
#: plus underscore). 
WORD = r"\w"
#: Matches the complement of WORD
NON_WORD = r"\W"
#: Matches the empty string, but only at the start or end of a word.
WORD_BOUNDARY = r"\b"
#: Matches the empty string, but not at the start or end of a word.
NON_WORD_BOUNDARY = r"\B"
#: Matches a newline character.
NEWLINE = r"\n"
#: Matches a carriage return.
CARRIAGE_RETURN = r"\r"
#: Matches a tab character.
TAB = r"\t"
#: Matches 1 or more (greedy) repetitions of the preceding expression
ONE_OR_MORE = r"+"
#: Non-greedy match for one or more repetitions of the previous expression
ONE_OR_MORE_LAZY = r"+?"
#: Matches 0 or more (greedy) repetitions of the preceding RE.
#: Greedy means that it will match as many repetitions as possible.
ZERO_OR_MORE = r"*"
#: Non-greedy version of the zero or more match
ZERO_OR_MORE_LAZY = r"*?"
#: Matches 0 or 1 (greedy) of the preceding RE.
OPTIONAL = r"?"
#: Matches the start of the string.
START_OF_INPUT = r"^"
#: Matches the end of the string or just before the newline at the end of the string.
END_OF_INPUT = r"$"
