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


class TableUdf(Base):
	"""This object specifies the UDF table properties.
	The TableUdf class encapsulates a list of tableUdf resources that is managed by the system.
	A list of resources can be retrieved from the server using the TableUdf.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'tableUdf'

	def __init__(self, parent):
		super(TableUdf, self).__init__(parent)

	@property
	def Column(self):
		"""An instance of the Column class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.tableudf.column.column.Column)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.tableudf.column.column import Column
		return Column(self)

	@property
	def Enabled(self):
		"""If enabled, enables the UDF table for this flow group if it is supported.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	def update(self, Enabled=None):
		"""Updates a child instance of tableUdf on the server.

		Args:
			Enabled (bool): If enabled, enables the UDF table for this flow group if it is supported.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def find(self, Enabled=None):
		"""Finds and retrieves tableUdf data from the server.

		All named parameters support regex and can be used to selectively retrieve tableUdf data from the server.
		By default the find method takes no parameters and will retrieve all tableUdf data from the server.

		Args:
			Enabled (bool): If enabled, enables the UDF table for this flow group if it is supported.

		Returns:
			self: This instance with matching tableUdf data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of tableUdf data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the tableUdf data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
