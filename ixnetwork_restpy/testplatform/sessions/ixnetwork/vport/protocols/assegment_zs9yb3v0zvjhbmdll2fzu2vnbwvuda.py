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


class AsSegment(Base):
	"""This object controls the contruction of AS path segments.
	The AsSegment class encapsulates a required asSegment resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'asSegment'

	def __init__(self, parent):
		super(AsSegment, self).__init__(parent)

	@property
	def AsSegments(self):
		"""Used to construct AS list related items.

		Returns:
			list(dict(arg1:bool,arg2:str[unknown|asSet|asSequence|asConfedSet|asConfedSequence],arg3:list[number]))
		"""
		return self._get_attribute('asSegments')
	@AsSegments.setter
	def AsSegments(self, value):
		self._set_attribute('asSegments', value)

	def update(self, AsSegments=None):
		"""Updates a child instance of asSegment on the server.

		Args:
			AsSegments (list(dict(arg1:bool,arg2:str[unknown|asSet|asSequence|asConfedSet|asConfedSequence],arg3:list[number]))): Used to construct AS list related items.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
