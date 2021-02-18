# super-expressive-python

This is a python port of [super-expressive](https://github.com/francisrstokes/super-expressive). It allows regular expressions to be expressed in python syntax and idioms. This allows for better editor and version control support, and makes them easier to read and edit.

Notes on implementation choices are in [notes.md](notes.md).

## Example

```python
>>> import superexpressive as se
>>> se.to_regex(
...     se.START_OF_INPUT,
...     se.optional("0x"),
...     se.capture(se.range(("a", "f"), ("A", "F"), ("0", "9")), se.exactly(4)),
...     se.END_OF_INPUT,
...     compile=False
... )
'^(?:0x)?([a-fA-F0-9]{4})$'

```

## Installation

    pip install super-expressive-python

## API

### superexpressive.ANY_CHAR( = '.')
Matches any character except a newline.


### superexpressive.CARRIAGE_RETURN( = '\\\\r')
Matches a carriage return.


### superexpressive.DIGIT( = '\\\\d')
Matches any digit character, is the equivalent of range 0-9


### superexpressive.END_OF_INPUT( = '$')
Matches the end of the string or just before the newline at the end of the string.


### superexpressive.NEWLINE( = '\\\\n')
Matches a newline character.


### superexpressive.NON_DIGIT( = '\\\\d')
Matches any non-digit character, this is the inverse of DIGIT


### superexpressive.NON_WHITESPACE_CHAR( = '\\\\S')
Matches any non-whitespace character, this is the inverse of WHITESPACE_CHAR


### superexpressive.NON_WORD( = '\\\\W')
Matches the complement of WORD


### superexpressive.NON_WORD_BOUNDARY( = '\\\\B')
Matches the empty string, but not at the start or end of a word.


### superexpressive.ONE_OR_MORE( = '+')
Matches 1 or more (greedy) repetitions of the preceding expression


### superexpressive.ONE_OR_MORE_LAZY( = '+?')
Non-greedy match for one or more repetitions of the previous expression


### superexpressive.OPTIONAL( = '?')
Matches 0 or 1 (greedy) of the preceding RE.


### superexpressive.START_OF_INPUT( = '^')
Matches the start of the string.


### superexpressive.TAB( = '\\\\t')
Matches a tab character.


### superexpressive.WHITESPACE_CHAR( = '\\\\s')
Matches any whitespace character


### superexpressive.WORD( = '\\\\w')
Matches any alphanumeric character a-z, A-Z, 0-9, or underscore
in bytes patterns or string patterns with the ASCII flag.
In string patterns without the ASCII flag, it will match the
range of Unicode alphanumeric characters (letters plus digits
plus underscore).


### superexpressive.WORD_BOUNDARY( = '\\\\b')
Matches the empty string, but only at the start or end of a word.


### superexpressive.ZERO_OR_MORE( = '\*')
Matches 0 or more (greedy) repetitions of the preceding RE.
Greedy means that it will match as many repetitions as possible.


### superexpressive.ZERO_OR_MORE_LAZY( = '\*?')
Non-greedy version of the zero or more match


### superexpressive.any_of(\*args)

### superexpressive.any_of_chars(\*args)

### superexpressive.anything_but_chars(\*args)

### superexpressive.anything_but_range(\*args)

### superexpressive.anything_but_string(string)

### superexpressive.assert_ahead(\*args)

### superexpressive.assert_behind(\*args)

### superexpressive.assert_not_ahead(\*args)

### superexpressive.assert_not_behind(\*args)

### superexpressive.at_least(length)

### superexpressive.back_reference(index)

### superexpressive.between(minl, maxl)

### superexpressive.capture(\*args, name=None)
A group that captures its contents.

```python
>>> to_regex(capture(range(("a", "f"), ("0", "9")), 'XXX'), compile=False)
'([a-f0-9]XXX)'
```


### superexpressive.exactly(length)

### superexpressive.from_regex(pattern)
it would be cool to be provide a “labeling” function which could generate
the code from a given regex, as part of a debugging suite


### superexpressive.group(\*args)
A group that does not capture its contents.

```python
>>> to_regex(group(range(("a", "f"), ("0", "9")), 'XXX'), compile=False)
'(?:[a-f0-9]XXX)'
```


### superexpressive.named_back_reference(name)

### superexpressive.optional(\*args)
A optional non-capturing group of the items inside.

```python
>>> to_regex(optional(DIGIT), compile=False)
'(?:\\d)?'
```


### superexpressive.range(\*args, negate=False)
An item that matches a range of characters by ascii code.

```python
>>> import superexpressive as se
>>> se.to_regex(se.range(('A', 'F')), compile=False)
'[A-F]'
```


### superexpressive.re_flags_to_string(flags)

### superexpressive.to_regex(\*args, flags=0, compile=True)
Turn a collection of strings into a regex.
