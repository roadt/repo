#!/usr/bin/env python3
#
# This is a complex version of lilac.py for building
# a package from AUR.
#
# You can do something before/after building a package,
# including modify the 'pkgver' and 'md5sum' in PKBUILD.
#
# This is especially useful when a AUR package is
# out-of-date and you want to build a new one, or you
# want to build a package directly from sourceforge but
# using PKGBUILD from AUR.
#
# See also:
# [1] ruby-sass/lilac.py
# [2] aufs3-util-lily-git/lilac.py
# [3] octave-general/lilac.py
#

from lilaclib import *

build_prefix = 'extra-x86_64'
depends = ['python2-pypandoc-git']

def pre_build():
  # obtain base PKGBUILD, e.g.
  aur_pre_build()

  for line in edit_file('PKGBUILD'):
    # edit PKGBUILD
    if 'depends=' in line:
        print('#'+line)
        print(line.replace(')',' \'python2-setuptools\')'))
    else:
        print(line)

def post_build():
  # do something after the package has successfully been built
  aur_post_build()

# do some cleanup here after building the package, regardless of result
# def post_build_always(success):
#   pass

if __name__ == '__main__':
  single_main()
