# Release a new version

## Run the unit tests

See [test/README.md](test/README.md)

## Increase the version number

In [ivydepparse/\__init\__.py](ivydepparse/__init__.py) to `7.8.9` in this example.

## Extend the changelog

In [README.md](README.md)

## Generate the package to be published

```
$ python setup.py sdist
```

And check that the resulting `dist/ivydepparse-7.8.9.tar.gz` looks well-formed.

## Install the package locally

```
$ sudo pip install dist/ivydepparse-7.8.9.tar.gz
```

and test it briefly, e.g.

```
$ ivydepparse < ivy-example.xml
```

## Commit your changes, create a git tag and push

```
$ git add -u
$ git commit -m "Version 7.8.9"
$ git push
$ git tag "7.8.9"
$ git push --tags
```

## Push the package to PyPI Test

Create `~/.pypirc` as follows:

```
[distutils]
index-servers =
    pypi
    pypitest

[pypi]
repository: https://pypi.python.org/pypi
username:ttgf
password:mypassword

[pypitest]
repository: https://testpypi.python.org/pypi
username:ttgf
password:mypassword
```

and push:

```
$ python setup.py sdist upload -r pypitest
```

> **NOTE:** if this fails because the project doesn't exist in PyPI Test anymore, register it again:
>
> ```
> $ python setup.py register -r pypitest
> ```

Finally check that the package looks well-formed at `https://testpypi.python.org/pypi/ivydepparse/7.8.9`

## Push the package to PyPI

```
$ python setup.py sdist upload
```

and check that the package looks well-formed at `https://pypi.python.org/pypi/ivydepparse/7.8.9`

Finally check that the package can be installed from PyPI:

```
$ sudo pip install ivydepparse
```
