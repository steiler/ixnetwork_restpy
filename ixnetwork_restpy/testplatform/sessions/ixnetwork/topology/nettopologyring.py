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


class NetTopologyRing(Base):
	"""ring topology
	The NetTopologyRing class encapsulates a list of netTopologyRing resources that is be managed by the user.
	A list of resources can be retrieved from the server using the NetTopologyRing.find() method.
	The list can be managed by the user by using the NetTopologyRing.add() and NetTopologyRing.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'netTopologyRing'

	def __init__(self, parent):
		super(NetTopologyRing, self).__init__(parent)

	@property
	def IncludeEntryPoint(self):
		"""if true, entry node belongs to ring topology, otherwise it is outside of ring

		Returns:
			bool
		"""
		return self._get_attribute('includeEntryPoint')
	@IncludeEntryPoint.setter
	def IncludeEntryPoint(self, value):
		self._set_attribute('includeEntryPoint', value)

	@property
	def LinkMultiplier(self):
		"""number of links between two nodes

		Returns:
			number
		"""
		return self._get_attribute('linkMultiplier')
	@LinkMultiplier.setter
	def LinkMultiplier(self, value):
		self._set_attribute('linkMultiplier', value)

	@property
	def Nodes(self):
		"""number of nodes

		Returns:
			number
		"""
		return self._get_attribute('nodes')
	@Nodes.setter
	def Nodes(self, value):
		self._set_attribute('nodes', value)

	def update(self, IncludeEntryPoint=None, LinkMultiplier=None, Nodes=None):
		"""Updates a child instance of netTopologyRing on the server.

		Args:
			IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
			LinkMultiplier (number): number of links between two nodes
			Nodes (number): number of nodes

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, IncludeEntryPoint=None, LinkMultiplier=None, Nodes=None):
		"""Adds a new netTopologyRing node on the server and retrieves it in this instance.

		Args:
			IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
			LinkMultiplier (number): number of links between two nodes
			Nodes (number): number of nodes

		Returns:
			self: This instance with all currently retrieved netTopologyRing data using find and the newly added netTopologyRing data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the netTopologyRing data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, IncludeEntryPoint=None, LinkMultiplier=None, Nodes=None):
		"""Finds and retrieves netTopologyRing data from the server.

		All named parameters support regex and can be used to selectively retrieve netTopologyRing data from the server.
		By default the find method takes no parameters and will retrieve all netTopologyRing data from the server.

		Args:
			IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
			LinkMultiplier (number): number of links between two nodes
			Nodes (number): number of nodes

		Returns:
			self: This instance with matching netTopologyRing data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of netTopologyRing data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the netTopologyRing data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
