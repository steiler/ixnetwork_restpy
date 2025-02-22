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


class Layer23ProtocolRoutingFilter(Base):
	"""Lists the filtered ports and protocols.
	The Layer23ProtocolRoutingFilter class encapsulates a list of layer23ProtocolRoutingFilter resources that is be managed by the user.
	A list of resources can be retrieved from the server using the Layer23ProtocolRoutingFilter.find() method.
	The list can be managed by the user by using the Layer23ProtocolRoutingFilter.add() and Layer23ProtocolRoutingFilter.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'layer23ProtocolRoutingFilter'

	def __init__(self, parent):
		super(Layer23ProtocolRoutingFilter, self).__init__(parent)

	@property
	def PortFilterIds(self):
		"""Ports that have been filtered.

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availablePortFilter])
		"""
		return self._get_attribute('portFilterIds')
	@PortFilterIds.setter
	def PortFilterIds(self, value):
		self._set_attribute('portFilterIds', value)

	@property
	def ProtocolFilterIds(self):
		"""Protocols that have been filtered.

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableProtocolFilter])
		"""
		return self._get_attribute('protocolFilterIds')
	@ProtocolFilterIds.setter
	def ProtocolFilterIds(self, value):
		self._set_attribute('protocolFilterIds', value)

	def update(self, PortFilterIds=None, ProtocolFilterIds=None):
		"""Updates a child instance of layer23ProtocolRoutingFilter on the server.

		Args:
			PortFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availablePortFilter])): Ports that have been filtered.
			ProtocolFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableProtocolFilter])): Protocols that have been filtered.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, PortFilterIds=None, ProtocolFilterIds=None):
		"""Adds a new layer23ProtocolRoutingFilter node on the server and retrieves it in this instance.

		Args:
			PortFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availablePortFilter])): Ports that have been filtered.
			ProtocolFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableProtocolFilter])): Protocols that have been filtered.

		Returns:
			self: This instance with all currently retrieved layer23ProtocolRoutingFilter data using find and the newly added layer23ProtocolRoutingFilter data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the layer23ProtocolRoutingFilter data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, PortFilterIds=None, ProtocolFilterIds=None):
		"""Finds and retrieves layer23ProtocolRoutingFilter data from the server.

		All named parameters support regex and can be used to selectively retrieve layer23ProtocolRoutingFilter data from the server.
		By default the find method takes no parameters and will retrieve all layer23ProtocolRoutingFilter data from the server.

		Args:
			PortFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availablePortFilter])): Ports that have been filtered.
			ProtocolFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableProtocolFilter])): Protocols that have been filtered.

		Returns:
			self: This instance with matching layer23ProtocolRoutingFilter data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of layer23ProtocolRoutingFilter data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the layer23ProtocolRoutingFilter data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
