#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

if sys.platform == "win32":
	from .backends.windows import Trash
elif sys.platform == 'darwin':
	from .backends.osx import Trash
else:
	from .backends.xdg import Trash
