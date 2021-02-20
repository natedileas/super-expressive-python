## Meta Notes:

I was looking for a new project to work on. I remembered that I had seen super-expressive on hacker news, and thought it would be a cool thing to port. I'm going to do my best to write down design decisions in this document for my own sanity. I googled for a python port, but couldn't find one -- which was very good for my mental health.

# 2/16/2021

## general design principles

- regexes are easy to write but hard to read
    + especially when deepy nested or "exotic" things are used
- regexes are usually stored as strings, so don't benefit as much from editor language support or version control
    + this implies it's a good idea to use the language idioms that are available 
- regexes encode a lot of information in a small format - good and bad
- regexes have low overhead and great cross-language support (mostly)
- when regexes change, the reason for the change is often lost

therefore, a form of regexes which is more readable, follows the implementation language idioms, and is commentable, is a good idea.

**ideas**:
- comments in the middle of a regex?
- it would be cool to be provide a "labeling" function which could generate the code from a given regex, as part of a debugging suite, in addition to a labeled regex -> minimal

## A Little Less Meta - initial syntax + structure ideas

I haven't read the original code yet. As far as I can guess, it's a class with members that map to a regex string, append to an internal variable when called, which gets written out with `toRegex()`. This will probably work as a model, but I might want to imagine some alternatives as well. Step 1 is to read the code and confirm my suspicions.

Update: I read the code, and the structure is essentially what I expected.

There's also a couple of potential issues with the syntax, Here's an example from the super-expressive readme:

```
const myRegex = SuperExpressive()
  .startOfInput
  .optional.string('0x')
  .capture
    .exactly(4).anyOf
      .range('A', 'F')
      .range('a', 'f')
      .range('0', '9')
    .end()
  .end()
  .endOfInput
  .toRegex();

// Produces the following regular expression:
/^(?:0x)?([A-Fa-f0-9]{4})$/
```

There's a couple problems with copying this systax (I learned this is called the fluent interface pattern and it is discouraged by G. Van Rossum)[https://en.wikipedia.org/wiki/Fluent_interface#Python] exactly in python. First, python requires line continuation characters (`\`) outside of brackets. I think the solution to this is to do a different pattern. Second, it uses camel case (I didn't say they were all big problems).

A potential python-ized syntax of this example might look like this:

    # this is incredibly ugly.
    from superexpressive import SuperExpressive
    pattern = SuperExpressive().start_of_input.optional('0x').capture.exactly(4).any_of.range('A', 'F').range('a', 'f').range('0', '9').end.end.end_of_input.regex()

Another might be:

    # this is less ugly. 
    # but in order to be useful, you basically have to pollute the namespace with a bunch of stuff. 
    # also, the distinction between a constant and a function is kinda broken.
    # also, if I went with the keyword argument approach, valid combinations would get really hairy. even though I hate the .end syntax, this might be a worse alternative
    import superexpressive as se
    from superexpressive import *
    pattern = se.to_regex(
        start_of_input, 
        optional('0x'), 
        capture(
            range(('A', 'F'), ('a', 'f'), ('0', '9')),
            exactly(4), 
            ),
        end_of_input
        )

    # YASI - yet another (terrible) syntax idea
    import superexpressive as se
    pattern = se.desc_to_regex('start.optional.string.0x.capture.')

    # this is incredibly ugly part 2
    from superexpressive import SuperExpressive
    pattern = SuperExpressive().start_of_input().optional('0x').capture.exactly(4).any_of.range('A', 'F').range('a', 'f').range('0', '9').end.end.end_of_input.regex()

I also read the `re` module source to check if some of these constants already exist. They don't, but there's some really good comments in there that form the module help docs.

## Miscellaneous concerns

 - licence: original is MIT. mine probably should be as well; check other ports
 - tdd? nah, that's for nerds
 - 

## Conclusions

After following the Feynmann method, except for the second bit, I've decided to go with the syntax option behind door number 2, the bag-o'-methods style. Next step, a prototype which will never be rewritten -- a real product.

# 2/17/2020

## prototype

Following python's idioms means changing the way this code works, a lot. Biggest differences are styling and syntax.

IT WORKS!

    >>> import superexpressive as se
    >>> se.to_regex(se.START_OF_INPUT, se.optional('0x'), se.capture(se.range(('a', 'f'), ('A', 'F'), ('0', '9')), se.exactly(4)), se.END_OF_INPUT)
    '^(?:0x)?([a-fA-F0-9]{4})?$'

## Release to pip notes

I read [this](https://setuptools.readthedocs.io/en/latest/userguide/quickstart.html) and found that python packaing has changed a bit since I last did this. Now, `pyproject.toml` and `setup.cfg` are the replacement for `setup.py`.

This is how to make a release. Needs `pep517` and `twine` installed.

    python -m pep517.build .
    twine check .\dist\*   # check if there are any issues
    twine upload

[It works!](https://pypi.org/project/super-expressive-python/)


## doctest - I'm at the document / I'm at the testing plan / I'm at the combination document and testing plan

I've never used doctest before. But it seems like a good fit for this project. I want to be able to generate markdown to append to my readme so that it will will always be in sync. Sphinx apidoc is a good fit for this, then I can run doctest readme.md and be done with it. That way, my docs and test source will be in one place, and it can be munged as needed.

    pip install sphinx sphinx-markdown-builder
    sphinx-apidoc -o Sphinx-docs . sphinx-apidoc --full -A 'Nathan Dileas'; cd Sphinx-docs;
    # uncomment sys path hack in conf.py
    make markdown
    # now steal stuff from the generated markdown file

stolen unapologetically from: https://stackoverflow.com/questions/36237477/python-docstrings-to-github-readme-md


## TODOs

- x - license
- x - read regex module, this just implements a better regex engine, not a better interface
- x - docstrings / other documentation
- x- rename `range()`  to something better
- x- tests / check error messages
    + make sure to do negative tests.
- x - type hints
- translate the javascript examples into the readme and make sure they work
- inline flags
- all special characters from re documentation
- reverse mapping. this will probably be hard, because it's essentially writing a regex engine. 
- pr to add my port to the readme of the original?
- think about whether the repitition specifiers should be terminal, or operate on their antecedent

# 2/18/2021 - 2/19/2021 - Time to Clean


