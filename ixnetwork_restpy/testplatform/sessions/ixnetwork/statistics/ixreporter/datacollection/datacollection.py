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


class DataCollection(Base):
	"""DEPRECATED Specifies the collection of data.
	The DataCollection class encapsulates a required dataCollection resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'dataCollection'

	def __init__(self, parent):
		super(DataCollection, self).__init__(parent)

	@property
	def Enable(self):
		"""If it is true, enables collection of data

		Returns:
			bool
		"""
		return self._get_attribute('Enable')
	@Enable.setter
	def Enable(self, value):
		self._set_attribute('Enable', value)

	@property
	def LastRunId(self):
		"""Specifies the identifier for last run.

		Returns:
			number
		"""
		return self._get_attribute('LastRunId')

	def update(self, Enable=None):
		"""Updates a child instance of dataCollection on the server.

		Args:
			Enable (bool): If it is true, enables collection of data

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
