# -*- coding: utf-8 -*-
"""
XDG Trash implementation
"""

import os
import shutil
from time import strftime
from .base import BaseTrash

HOME = os.path.expanduser("~")
XDG_DATA_HOME = os.environ.get("XDG_DATA_HOME", os.path.join(HOME, ".local", "share"))

TRASH_INFO_TEMPLATE = """[Trash Info]
Path=%(path)s
DeletionDate=%(deletionDate)s
"""

class Trash(BaseTrash):
	def __init__(self, path=""):
		if not path:
			path = os.path.join(XDG_DATA_HOME, "Trash")
		self._path = path

	def _cleanup(self, name):
		self._deleteInfo(name)
		self._deleteFile(name)

	def _deleteFile(self, name):
		path = os.path.join(self.filesPath(), name)
		if os.path.exists(path):
			os.remove(path)

	def _deleteInfo(self, name):
		path = os.path.join(self.infoPath(), name + ".trashinfo")
		if os.path.exists(path):
			os.remove(path)

	def _writeInfo(self, name, path, deletionDate):
		with open(os.path.join(self.infoPath(), name + ".trashinfo"), "w") as f:
			f.write(TRASH_INFO_TEMPLATE % {"path": path, "deletionDate": deletionDate})
		return f.name

	def files(self):
		return os.listdir(self.filesPath())

	def filesPath(self):
		return os.path.join(self.path(), "files")

	def infoPath(self):
		return os.path.join(self.path(), "info")

	def trash(self, path):
		if not os.path.exists(path):
			raise IOError("No such file or directory")

		name = os.path.basename(path)
		if os.path.exists(os.path.join(self.filesPath(), name)):
			_name = name + ".1"
			i = 1
			while os.path.exists(os.path.join(self.filesPath(), _name)):
				i += 1
				_name = "%s.%i" % (name, i)
			name = _name

		self._writeInfo(name=name, path=path, deletionDate=strftime("%Y-%m-%dT%H:%M:%S"))
		try:
			shutil.move(path, os.path.join(self.filesPath(), name))
		except Exception:
			self._cleanup(name)
			raise

	def path(self):
		return self._path
