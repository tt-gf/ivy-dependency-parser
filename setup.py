from setuptools import setup
import ivydepparse

setup(name='ivydepparse',
      version=ivydepparse.__version__,
      install_requires=['PyGithub'],
      description='Ivy Dependency Parser',
      long_description=open('README').read(),
      keywords=['ivydepparse',
                'ivy',
                'dependency',
                'dependencies',
                'parser',
                'xml',
                'cmake'],
      author='TT-GF Team',
      author_email='aurelien.lourot@tomtom.com',
      url='https://github.com/tt-gf/ivy-dependency-parser',
      download_url='https://github.com/tt-gf/ivy-dependency-parser/tarball/'
                   + ivydepparse.__version__,
      license='public domain',
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'License :: Public Domain',
                   'Natural Language :: English',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Software Development :: Build Tools',
                   'Topic :: System :: Software Distribution',
                   'Topic :: Text Processing :: Markup :: XML',
                   'Topic :: Utilities'],
      packages=['ivydepparse'],
      entry_points="""
[console_scripts]
ivydepparse = ivydepparse.ivydepparse:main
""")
