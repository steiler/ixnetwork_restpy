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


class Ipv4Prefixes(Base):
	"""This object helps to set the prefixes count of IPv4 prefix type.
	The Ipv4Prefixes class encapsulates a list of ipv4Prefixes resources that is managed by the system.
	A list of resources can be retrieved from the server using the Ipv4Prefixes.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'ipv4Prefixes'

	def __init__(self, parent):
		super(Ipv4Prefixes, self).__init__(parent)

	@property
	def Age(self):
		"""The time since last refreshed.

		Returns:
			number
		"""
		return self._get_attribute('age')

	@property
	def HostName(self):
		"""The host name as retrieved from the related packets.

		Returns:
			str
		"""
		return self._get_attribute('hostName')

	@property
	def Ipv4Prefix(self):
		"""Mask width of IPv4 Prefix.

		Returns:
			str
		"""
		return self._get_attribute('ipv4Prefix')

	@property
	def LearnedVia(self):
		"""Learned via L1 Adjacency/L2 Adjacency.

		Returns:
			str
		"""
		return self._get_attribute('learnedVia')

	@property
	def LspId(self):
		"""The LSP number.

		Returns:
			str
		"""
		return self._get_attribute('lspId')

	@property
	def Metric(self):
		"""The route metric.

		Returns:
			number
		"""
		return self._get_attribute('metric')

	@property
	def SequenceNumber(self):
		"""Sequence number of the LSP containing the route.

		Returns:
			number
		"""
		return self._get_attribute('sequenceNumber')

	def find(self, Age=None, HostName=None, Ipv4Prefix=None, LearnedVia=None, LspId=None, Metric=None, SequenceNumber=None):
		"""Finds and retrieves ipv4Prefixes data from the server.

		All named parameters support regex and can be used to selectively retrieve ipv4Prefixes data from the server.
		By default the find method takes no parameters and will retrieve all ipv4Prefixes data from the server.

		Args:
			Age (number): The time since last refreshed.
			HostName (str): The host name as retrieved from the related packets.
			Ipv4Prefix (str): Mask width of IPv4 Prefix.
			LearnedVia (str): Learned via L1 Adjacency/L2 Adjacency.
			LspId (str): The LSP number.
			Metric (number): The route metric.
			SequenceNumber (number): Sequence number of the LSP containing the route.

		Returns:
			self: This instance with matching ipv4Prefixes data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of ipv4Prefixes data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the ipv4Prefixes data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
