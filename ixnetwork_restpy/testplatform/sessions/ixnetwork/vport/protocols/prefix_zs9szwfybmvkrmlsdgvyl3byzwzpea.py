# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Prefix(Base):
	"""Filters based on route prefix information.
	The Prefix class encapsulates a required prefix resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'prefix'

	def __init__(self, parent):
		super(Prefix, self).__init__(parent)

	@property
	def Prefix(self):
		"""Controls the prefix attributes that are filtered on.

		Returns:
			list(dict(arg1:str,arg2:bool,arg3:number,arg4:number))
		"""
		return self._get_attribute('prefix')
	@Prefix.setter
	def Prefix(self, value):
		self._set_attribute('prefix', value)

	def update(self, Prefix=None):
		"""Updates a child instance of prefix on the server.

		Args:
			Prefix (list(dict(arg1:str,arg2:bool,arg3:number,arg4:number))): Controls the prefix attributes that are filtered on.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
