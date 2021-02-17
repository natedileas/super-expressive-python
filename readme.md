# super-expressive-python

This is a python port of [super-expressive](https://github.com/francisrstokes/super-expressive).

Notes on implementation choices are in [notes.md](notes.md).

## Example

    >>> import superexpressive as se
    >>> se.to_regex(se.START_OF_INPUT, se.optional('0x'), se.capture(se.range(('a', 'f'), ('A', 'F'), ('0', '9')), se.exactly(4)), se.END_OF_INPUT)
    '^(?:0x)?([a-fA-F0-9]{4})?$'

## Installation

    pip install super-expressive-python

## Usage

TODO
