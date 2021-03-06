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
Match any of the given arguments.

```python
>>> import superexpressive as se
>>> se.any_of('A', 'F', 'dkja')
'(?:A|F|dkja)'
```

# TODO: is a non-capturing group really neccesary here?


* **Return type**

    `str`



### superexpressive.any_of_chars(\*args)
A length 1 item that matches any of the included characters.

```python
>>> import superexpressive as se
>>> se.any_of_chars('A', 'F', 'dkja')
'[AFdkja]'
```


* **Return type**

    `str`



### superexpressive.anything_but_chars(\*args)
A length 1 item that matches anything but the included characters.

```python
>>> import superexpressive as se
>>> se.anything_but_chars('A', 'F', 'dkja')
'[^AFdkja]'
```


* **Return type**

    `str`



### superexpressive.anything_but_range(\*args)
An item that matches anything but a range of characters.

```python
>>> import superexpressive as se
>>> se.anything_but_range(('A', 'F'))
'[^A-F]'
```


* **Return type**

    `str`



### superexpressive.anything_but_string(string)
Match anything except the provided string.

```python
>>> import superexpressive as se
>>> se.anything_but_string('test')
'(?:[^t][^e][^s][^t])'
```


* **Return type**

    `str`



### superexpressive.assert_ahead(\*args)
Check, but do not consume, that the regex matches the next part of the string.

```python
>>> import superexpressive as se
>>> se.assert_ahead('test')
'(?=test)'
```

# TODO: actual example of using this


* **Return type**

    `str`



### superexpressive.assert_behind(\*args)
Check, that the regex matches the previous part of the string.

```python
>>> import superexpressive as se
>>> se.assert_behind('test')
'(?<=test)'
```

# TODO: actual example of using this


* **Return type**

    `str`



### superexpressive.assert_not_ahead(\*args)
Check, but do not consume, that the regex does not match the next part of the string.

```python
>>> import superexpressive as se
>>> se.assert_not_ahead('test')
'(?!test)'
```

# TODO: actual example of using this


* **Return type**

    `str`



### superexpressive.assert_not_behind(\*args)
Check, that the regex does not match the previous part of the string.

```python
>>> import superexpressive as se
>>> se.assert_not_behind('test')
'(?<!test)'
```

# TODO: actual example of using this


* **Return type**

    `str`



### superexpressive.at_least(length)
Match the previous pattern at least length times, greedily.

```python
>>> import superexpressive as se
>>> se.at_least(4)
'{4,}'
```

```python
>>> import superexpressive as se
>>> se.DIGIT + se.at_least(6)
'\\d{6,}'
```


* **Return type**

    `str`



### superexpressive.back_reference(index)
Refer to an earlier captured group by 1-based index.

```python
>>> import superexpressive as se
>>> se.back_reference(2)
'\\2'
```

# TODO: actual example of using this


* **Return type**

    `str`



### superexpressive.between(minl, maxl)
Match the previous pattern at between minl and maxl times, greedily.

```python
>>> import superexpressive as se
>>> se.between(4,8)
'{4,8}'
```

```python
>>> import superexpressive as se
>>> se.DIGIT + se.between(6,8)
'\\d{6,8}'
```


* **Return type**

    `str`



### superexpressive.capture(\*args, name=None)
A group that captures its contents.

```python
>>> import superexpressive as se
>>> se.capture(se.range(("a", "f"), ("0", "9")), 'XXX')
'([a-f0-9]XXX)'
```


* **Return type**

    `str`



### superexpressive.exactly(length)
Match the previous pattern exactly length times.

```python
>>> import superexpressive as se
>>> se.exactly(4)
'{4}'
```

```python
>>> import superexpressive as se
>>> se.DIGIT + se.exactly(6)
'\\d{6}'
```


* **Return type**

    `str`



### superexpressive.from_regex(pattern)
it would be cool to be provide a “labeling” function which could generate
the code from a given regex, as part of a debugging suite


* **Return type**

    `str`



### superexpressive.group(\*args)
A group that does not capture its contents.

```python
>>> import superexpressive as se
>>> se.group(se.range(("a", "f"), ("0", "9")), 'XXX')
'(?:[a-f0-9]XXX)'
```


* **Return type**

    `str`



### superexpressive.named_back_reference(name)
Refer to an earlier captured group by name.

```python
>>> import superexpressive as se
>>> se.named_back_reference('test')
'\\k<test>'
```

# TODO: actual example of using this


* **Return type**

    `str`



### superexpressive.optional(\*args)
A optional non-capturing group of the items inside.

```python
>>> import superexpressive as se
>>> se.optional(se.DIGIT)
'(?:\\d)?'
```


* **Return type**

    `str`



### superexpressive.range(\*args, negate=False)
An item that matches a range of characters by ascii code.

```python
>>> import superexpressive as se
>>> se.range(('A', 'F'))
'[A-F]'
```


* **Return type**

    `str`



### superexpressive.re_flags_to_string(flags=0)
Turn a set of re flags into a string suitable for inclusion in a regex.

```python
>>> import superexpressive as se
>>> se.re_flags_to_string(re.A)
'(?a)'
```

```python
>>> import superexpressive as se
>>> se.re_flags_to_string(re.IGNORECASE | re.LOCALE)
'(?iL)'
```

```python
>>> import superexpressive as se
>>> se.re_flags_to_string()
''
```


* **Return type**

    `str`



### superexpressive.to_regex(\*args, flags=0, compile=True)
Turn a collection of strings into a regex.

If compile is True, return a re.compile object. If false, return a regex 

    string in the python style.

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

```python
>>> import superexpressive as se
>>> se.to_regex(compile=False)
''
```

# TODO: More tests, like flags


* **Return type**

    `Union`[`str`, `compile`]
