ivydepparse.py - Ivy Dependency Parser
======================================

Parsing an Ivy module descriptor (``ivy.xml``) for its dependencies from
a tool like CMake can be tough. This script takes a descriptor on the
standard input and prints its dependencies in an easily parsable format.

Installation
------------

::

    $ sudo pip install ivydepparse

Usage
-----

::

    $ ivydepparse < ivy.xml

Example
-------

`ivy-example.xml <ivy-example.xml>`_:

::

    ...
        <dependency org="com.ttgf" name="myGreatDep" rev="1.2.3" conf="debug;release"/>
        <dependency org="com.ttgf" name="myGreatDep" rev="1.2.3" conf="other"/>
        <dependency org="com.ttgf" name="myGreatDebugDep" rev="2.3.4" conf="debug"/>
    ...

results in

::

    $ ivydepparse < ivy-example.xml
    org=com.ttgf|name=myGreatDebugDep|rev=2.3.4|conf=debug;org=com.ttgf|name=myGreatDep|rev=1.2.3|conf=debug,release,other

Details
-------

The output is a one-liner, a semicolon-separated list of dependencies.
Each dependency is a pipe-separated list of attributes as
``name=value``.

If any value contains one of our separators, they get escaped as
follows:

-  ``;`` is replaced by ``,``
-  ``|`` is replaced by ``:``
-  ``=`` is replaced by ``:``

For each dependency, all attributes are guaranteed to be present and in
that order: ``org``, ``name``, ``rev``, ``conf``.

Attributes can be empty. An empty attribute appears as ``name=``.

Dependencies having the same key (org/name/rev) will be output as one single dependency.

The order inside ``conf`` in the output is not specified.

The order of the dependencies in the output is not specified.

Changelog
---------

**1.0.1** (2015-09-30):

-  Dependencies with same key are now aggregated.

**1.0.0** (2015-09-30):

-  Initial version.
