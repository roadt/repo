#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'
depends = ['python-aioconsole', 'python-terminaltables']

def pre_build():
  pypi_pre_build(depends=depends[:])

def post_build():
  pypi_post_build()
  update_aur_repo()

if __name__ == '__main__':
  single_main()
