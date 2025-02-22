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


class SourceRange(Base):
	"""This object holds a list of source IPv4 addresses that multicast traffic should be included from or excluded from.
	The SourceRange class encapsulates a list of sourceRange resources that is be managed by the user.
	A list of resources can be retrieved from the server using the SourceRange.find() method.
	The list can be managed by the user by using the SourceRange.add() and SourceRange.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'sourceRange'

	def __init__(self, parent):
		super(SourceRange, self).__init__(parent)

	@property
	def Count(self):
		"""The number of IP addresses in the source range.

		Returns:
			number
		"""
		return self._get_attribute('count')
	@Count.setter
	def Count(self, value):
		self._set_attribute('count', value)

	@property
	def IpFrom(self):
		"""The first IP address in the source range.

		Returns:
			str
		"""
		return self._get_attribute('ipFrom')
	@IpFrom.setter
	def IpFrom(self, value):
		self._set_attribute('ipFrom', value)

	def update(self, Count=None, IpFrom=None):
		"""Updates a child instance of sourceRange on the server.

		Args:
			Count (number): The number of IP addresses in the source range.
			IpFrom (str): The first IP address in the source range.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Count=None, IpFrom=None):
		"""Adds a new sourceRange node on the server and retrieves it in this instance.

		Args:
			Count (number): The number of IP addresses in the source range.
			IpFrom (str): The first IP address in the source range.

		Returns:
			self: This instance with all currently retrieved sourceRange data using find and the newly added sourceRange data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the sourceRange data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Count=None, IpFrom=None):
		"""Finds and retrieves sourceRange data from the server.

		All named parameters support regex and can be used to selectively retrieve sourceRange data from the server.
		By default the find method takes no parameters and will retrieve all sourceRange data from the server.

		Args:
			Count (number): The number of IP addresses in the source range.
			IpFrom (str): The first IP address in the source range.

		Returns:
			self: This instance with matching sourceRange data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of sourceRange data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the sourceRange data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
