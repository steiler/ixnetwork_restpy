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


class Layer23TrafficPortFilter(Base):
	"""Filters associated with layer23TrafficPort view.
	The Layer23TrafficPortFilter class encapsulates a list of layer23TrafficPortFilter resources that is be managed by the user.
	A list of resources can be retrieved from the server using the Layer23TrafficPortFilter.find() method.
	The list can be managed by the user by using the Layer23TrafficPortFilter.add() and Layer23TrafficPortFilter.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'layer23TrafficPortFilter'

	def __init__(self, parent):
		super(Layer23TrafficPortFilter, self).__init__(parent)

	@property
	def PortFilterIds(self):
		"""Selected port filters from the availablePortFilter list.

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availablePortFilter])
		"""
		return self._get_attribute('portFilterIds')
	@PortFilterIds.setter
	def PortFilterIds(self, value):
		self._set_attribute('portFilterIds', value)

	def update(self, PortFilterIds=None):
		"""Updates a child instance of layer23TrafficPortFilter on the server.

		Args:
			PortFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availablePortFilter])): Selected port filters from the availablePortFilter list.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, PortFilterIds=None):
		"""Adds a new layer23TrafficPortFilter node on the server and retrieves it in this instance.

		Args:
			PortFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availablePortFilter])): Selected port filters from the availablePortFilter list.

		Returns:
			self: This instance with all currently retrieved layer23TrafficPortFilter data using find and the newly added layer23TrafficPortFilter data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the layer23TrafficPortFilter data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, PortFilterIds=None):
		"""Finds and retrieves layer23TrafficPortFilter data from the server.

		All named parameters support regex and can be used to selectively retrieve layer23TrafficPortFilter data from the server.
		By default the find method takes no parameters and will retrieve all layer23TrafficPortFilter data from the server.

		Args:
			PortFilterIds (list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availablePortFilter])): Selected port filters from the availablePortFilter list.

		Returns:
			self: This instance with matching layer23TrafficPortFilter data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of layer23TrafficPortFilter data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the layer23TrafficPortFilter data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
