.. _Code Style:

Code Style
==========

Our code style page outlines what coding and style choices have been made for our documentation and code.
If you are interested in contributing to our documentation or code, please make contribution via pull
requests to the appropriate repository.  We appreciate any bug fixes you find or cool scripts you have
created that we can showcase as examples!

.. note:: Opening discourse as soon as possible is preferable when wanting to contribute to documentation. 

Python
------

Version
^^^^^^^

Python 3 will be used for development.

Style
^^^^^

We will use the `PEP8 guidelines <https://www.python.org/dev/peps/pep-0008/>`_ for code format.

We chose the following more precise rule where PEP 8 leaves some freedom:

* `We allow up to 100 characters per line (fifth paragraph) <https://www.python.org/dev/peps/pep-0008/#maximum-line-length>`_.
* `We pick single quotes over double quotes as long as no escaping is necessary <https://www.python.org/dev/peps/pep-0008/#string-quotes>`_.
* `We prefer hanging indents for continuation lines <https://www.python.org/dev/peps/pep-0008/#indentation>`_.


Markdown / reStructured Text
----------------------------

Style
^^^^^

The following standard to format text is intented to increase readability as well as versioning.

* *[.md, .rst only]* Each section title should be preceded by one empty line and succeeded by one empty line.

    * Rationale: It is easier to read to get an overview about the structure when screening the document.

* *[.rst only]* In restructured Text the headings should follow the hierarchy described in the `Sphinx style guide <'https://documentation-style-guide-sphinx.readthedocs.io/en/latest/style-guide.html#headings>`__:

    * ``#`` with overline (only once, used for the document title)
    * ``*`` with overline
    * ``=``
    * ``-``
    * ``^``
    * ``"``
    * Rationale: A consistent hierarchy expedites getting an idea about the nesting level when screening a document.

* *[.md only]* In Markdown the headings should follow the ATX-style described in the `Markdown syntax documentation <https://daringfireball.net/projects/markdown/syntax#header>`__

    * ATX-style headers use 1-6 hash characters (``#``) at the start of the line to denote header levels 1-6.
    * A space between the hases and the header title should be used (such as ``# Heading 1``) to make it easier to visually seperate them.
    * Justifiication for the ATX-style preference comes from the `Google Mardown style guide <https://github.com/google/styleguide/blob/gh-pages/docguide/style.md#atx-style-headings>`__
    * Rationale: ATX-style headers are easier to search and maintain, and make the first two header levels consistent with the other levels.

* *[any]* Each sentence must start on a new line.

    * Rationale: For longer paragraphs a single change in the beginning makes the difference unreadable since it carries forward through the whole paragraph.

* *[any]* Each sentence can optionally be wrapped to keep each line short.
* *[any]* The lines should not have any trailing white spaces.
* *[.md, .rst only]* A code block must be preceded and succeeded by an empty line.

    * Rationale: Whitespace is significant only directly before and directly after fenced code blocks. Following these instructions will ensure that highlighting works properly and consistantly.

* *[.md, .rst only]* A code block should specify a syntax (e.g. ``bash``).

General Notes
^^^^^^^^^^^^^

Documentation style tests should be part of testing before new releases are made.
