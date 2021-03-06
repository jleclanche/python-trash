#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
from distutils.core import setup

#README = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()

CLASSIFIERS = [
	"Development Status :: 5 - Production/Stable",
	"Intended Audience :: Developers",
	"License :: OSI Approved :: MIT License",
	"Programming Language :: Python",
]

setup(
	name = "python-trash",
	packages = ["trash", "trash.backends"],
	author = "Jerome Leclanche",
	author_email = "jerome@leclan.ch",
	classifiers = CLASSIFIERS,
	description = "Cross-platform trash implementation",
	download_url = "https://github.com/jleclanche/python-trash/tarball/master",
	#long_description = README,
	url = "https://github.com/jleclanche/python-trash",
	version = "1.0",
)
