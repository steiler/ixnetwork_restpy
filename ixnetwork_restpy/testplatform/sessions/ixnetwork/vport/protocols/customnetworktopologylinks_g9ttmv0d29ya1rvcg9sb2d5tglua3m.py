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


class CustomNetworkTopologyLinks(Base):
	"""NOT DEFINED
	The CustomNetworkTopologyLinks class encapsulates a list of customNetworkTopologyLinks resources that is be managed by the user.
	A list of resources can be retrieved from the server using the CustomNetworkTopologyLinks.find() method.
	The list can be managed by the user by using the CustomNetworkTopologyLinks.add() and CustomNetworkTopologyLinks.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'customNetworkTopologyLinks'

	def __init__(self, parent):
		super(CustomNetworkTopologyLinks, self).__init__(parent)

	@property
	def Enabled(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def LinkMetric(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('linkMetric')
	@LinkMetric.setter
	def LinkMetric(self, value):
		self._set_attribute('linkMetric', value)

	@property
	def LinkNodeSystemId(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('linkNodeSystemId')
	@LinkNodeSystemId.setter
	def LinkNodeSystemId(self, value):
		self._set_attribute('linkNodeSystemId', value)

	def update(self, Enabled=None, LinkMetric=None, LinkNodeSystemId=None):
		"""Updates a child instance of customNetworkTopologyLinks on the server.

		Args:
			Enabled (bool): NOT DEFINED
			LinkMetric (number): NOT DEFINED
			LinkNodeSystemId (str): NOT DEFINED

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Enabled=None, LinkMetric=None, LinkNodeSystemId=None):
		"""Adds a new customNetworkTopologyLinks node on the server and retrieves it in this instance.

		Args:
			Enabled (bool): NOT DEFINED
			LinkMetric (number): NOT DEFINED
			LinkNodeSystemId (str): NOT DEFINED

		Returns:
			self: This instance with all currently retrieved customNetworkTopologyLinks data using find and the newly added customNetworkTopologyLinks data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the customNetworkTopologyLinks data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Enabled=None, LinkMetric=None, LinkNodeSystemId=None):
		"""Finds and retrieves customNetworkTopologyLinks data from the server.

		All named parameters support regex and can be used to selectively retrieve customNetworkTopologyLinks data from the server.
		By default the find method takes no parameters and will retrieve all customNetworkTopologyLinks data from the server.

		Args:
			Enabled (bool): NOT DEFINED
			LinkMetric (number): NOT DEFINED
			LinkNodeSystemId (str): NOT DEFINED

		Returns:
			self: This instance with matching customNetworkTopologyLinks data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of customNetworkTopologyLinks data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the customNetworkTopologyLinks data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
