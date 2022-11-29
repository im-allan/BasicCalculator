from distutils.core import setup
import py2exe
import glob

import sys
sys.argv.append('py2exe')

data_files = [('assets', glob.glob('assets\*.*')),
              ]
py2exe_options = dict(
    ascii=True,  # Exclude encodings
    excludes=['_ssl',  # Exclude _ssl
              'pyreadline', 'difflib', 'doctest', 'locale',
              'optparse', 'pickle', 'calendar'],  # Exclude standard library
    dll_excludes=['msvcr71.dll'],  # Exclude msvcr71
    compressed=True,  # Compress library.zip
)


setup(name='Calculator',
      version='1.2.1',
      description='This is a portfolio project',
      author='Allan',
      windows=[
          {
              "script": "app.py",
              "icon_resources": [(1, "assets\calculator-ico.ico")]
          }
      ],
      data_files=data_files,
      options={'py2exe': py2exe_options},
      )
