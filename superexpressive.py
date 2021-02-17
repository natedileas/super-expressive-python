# import re


def to_regex(*args):
    pattern = "".join(args)
    # TODO compile or check for validity or something
    return pattern


def from_regex(pattern):
    """it would be cool to be provide a "labeling" function which could generate
    the code from a given regex, as part of a debugging suite
    """
    pass


def optional(*args):
    return f'(?:{"".join(args)})?'


def capture(*args, name=None):
    name = f"?<{name}>" if name is not None else ""
    return f'({name}{"".join(args)})?'


def group(*args):
    return f'(?:{"".join(args)})'


def range(*args, negate=False):
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


ANY_CHAR = "."
WHITESPACE_CHAR = r"\s"
NON_WHITESPACE_CHAR = r"\S"
DIGIT = r"\d"
NON_DIGIT = r"\d"
WORD = r"\w"
NON_WORD = r"\W"
WORD_BOUNDARY = r"\b"
NON_WORD_BOUNDARY = r"\B"
NEWLINE = r"\n"
CARRIAGE_RETURN = r"\r"
TAB = r"\t"
NULL_BYTE = None
ONE_OR_MORE = r"+"
ONE_OR_MORE_LAZY = r"+?"
ZERO_OR_MORE = r"*"
ZERO_OR_MORE_LAZY = r"*?"
OPTIONAL = r"?"
START_OF_INPUT = r"^"
END_OF_INPUT = r"$"
# SPECIAL_CHARS = []

"""
flags:
.allowMultipleMatches
.lineByLine
.caseInsensitive
.sticky
.unicode
.singleLine

special characters:
.anyChar
.whitespaceChar
.nonWhitespaceChar
.digit
.nonDigit
.word
.nonWord
.wordBoundary
.nonWordBoundary
.newline
.carriageReturn
.tab
.nullByte
.optional
.zeroOrMore
.zeroOrMoreLazy
.oneOrMore
.oneOrMoreLazy
.startOfInput
.endOfInput

functions:
.anyOf
.capture
.backreference(index)
.namedBackreference(index)
.group
.assertAhead
.assertNotAhead
.assertBehind
.assertNotBehind
.exactly(n)
.atLeast(n)
.between(x, y)
.betweenLazy(x, y)
.anyOfChars(chars)
.anythingButChars(chars)
.anythingButString(str)
.anythingButRange(a, b)
.range(a, b)

.toRegexString()

"""
