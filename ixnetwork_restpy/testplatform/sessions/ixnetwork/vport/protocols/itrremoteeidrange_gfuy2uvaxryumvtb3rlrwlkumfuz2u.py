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


class ItrRemoteEidRange(Base):
	"""It gives details about the itr remote eid range
	The ItrRemoteEidRange class encapsulates a list of itrRemoteEidRange resources that is be managed by the user.
	A list of resources can be retrieved from the server using the ItrRemoteEidRange.find() method.
	The list can be managed by the user by using the ItrRemoteEidRange.add() and ItrRemoteEidRange.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'itrRemoteEidRange'

	def __init__(self, parent):
		super(ItrRemoteEidRange, self).__init__(parent)

	@property
	def Count(self):
		"""it gives details about the count

		Returns:
			number
		"""
		return self._get_attribute('count')
	@Count.setter
	def Count(self, value):
		self._set_attribute('count', value)

	@property
	def EnableMapReplyRecordSegmentMbit(self):
		"""If true, it enables Map reply record Segment Mbit

		Returns:
			bool
		"""
		return self._get_attribute('enableMapReplyRecordSegmentMbit')
	@EnableMapReplyRecordSegmentMbit.setter
	def EnableMapReplyRecordSegmentMbit(self, value):
		self._set_attribute('enableMapReplyRecordSegmentMbit', value)

	@property
	def Enabled(self):
		"""If true, it gives details about then protocol

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def Family(self):
		"""It gives details about the IP family it represents

		Returns:
			str(ipv4|ipv6)
		"""
		return self._get_attribute('family')
	@Family.setter
	def Family(self, value):
		self._set_attribute('family', value)

	@property
	def KeepQueryingUnlessResolved(self):
		"""If true, it keeps Querying Unless resolved

		Returns:
			bool
		"""
		return self._get_attribute('keepQueryingUnlessResolved')
	@KeepQueryingUnlessResolved.setter
	def KeepQueryingUnlessResolved(self, value):
		self._set_attribute('keepQueryingUnlessResolved', value)

	@property
	def MapResolvingInterval(self):
		"""It gives the map resolving interval

		Returns:
			number
		"""
		return self._get_attribute('mapResolvingInterval')
	@MapResolvingInterval.setter
	def MapResolvingInterval(self, value):
		self._set_attribute('mapResolvingInterval', value)

	@property
	def PrefixLength(self):
		"""it gives the prefix length

		Returns:
			number
		"""
		return self._get_attribute('prefixLength')
	@PrefixLength.setter
	def PrefixLength(self, value):
		self._set_attribute('prefixLength', value)

	@property
	def QueryIntervalUnlessResolved(self):
		"""It gives the query regarding the interval unless resolved

		Returns:
			number
		"""
		return self._get_attribute('queryIntervalUnlessResolved')
	@QueryIntervalUnlessResolved.setter
	def QueryIntervalUnlessResolved(self, value):
		self._set_attribute('queryIntervalUnlessResolved', value)

	@property
	def StartAddress(self):
		"""It gives details about the start address

		Returns:
			str
		"""
		return self._get_attribute('startAddress')
	@StartAddress.setter
	def StartAddress(self, value):
		self._set_attribute('startAddress', value)

	def update(self, Count=None, EnableMapReplyRecordSegmentMbit=None, Enabled=None, Family=None, KeepQueryingUnlessResolved=None, MapResolvingInterval=None, PrefixLength=None, QueryIntervalUnlessResolved=None, StartAddress=None):
		"""Updates a child instance of itrRemoteEidRange on the server.

		Args:
			Count (number): it gives details about the count
			EnableMapReplyRecordSegmentMbit (bool): If true, it enables Map reply record Segment Mbit
			Enabled (bool): If true, it gives details about then protocol
			Family (str(ipv4|ipv6)): It gives details about the IP family it represents
			KeepQueryingUnlessResolved (bool): If true, it keeps Querying Unless resolved
			MapResolvingInterval (number): It gives the map resolving interval
			PrefixLength (number): it gives the prefix length
			QueryIntervalUnlessResolved (number): It gives the query regarding the interval unless resolved
			StartAddress (str): It gives details about the start address

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Count=None, EnableMapReplyRecordSegmentMbit=None, Enabled=None, Family=None, KeepQueryingUnlessResolved=None, MapResolvingInterval=None, PrefixLength=None, QueryIntervalUnlessResolved=None, StartAddress=None):
		"""Adds a new itrRemoteEidRange node on the server and retrieves it in this instance.

		Args:
			Count (number): it gives details about the count
			EnableMapReplyRecordSegmentMbit (bool): If true, it enables Map reply record Segment Mbit
			Enabled (bool): If true, it gives details about then protocol
			Family (str(ipv4|ipv6)): It gives details about the IP family it represents
			KeepQueryingUnlessResolved (bool): If true, it keeps Querying Unless resolved
			MapResolvingInterval (number): It gives the map resolving interval
			PrefixLength (number): it gives the prefix length
			QueryIntervalUnlessResolved (number): It gives the query regarding the interval unless resolved
			StartAddress (str): It gives details about the start address

		Returns:
			self: This instance with all currently retrieved itrRemoteEidRange data using find and the newly added itrRemoteEidRange data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the itrRemoteEidRange data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Count=None, EnableMapReplyRecordSegmentMbit=None, Enabled=None, Family=None, KeepQueryingUnlessResolved=None, MapResolvingInterval=None, PrefixLength=None, QueryIntervalUnlessResolved=None, StartAddress=None):
		"""Finds and retrieves itrRemoteEidRange data from the server.

		All named parameters support regex and can be used to selectively retrieve itrRemoteEidRange data from the server.
		By default the find method takes no parameters and will retrieve all itrRemoteEidRange data from the server.

		Args:
			Count (number): it gives details about the count
			EnableMapReplyRecordSegmentMbit (bool): If true, it enables Map reply record Segment Mbit
			Enabled (bool): If true, it gives details about then protocol
			Family (str(ipv4|ipv6)): It gives details about the IP family it represents
			KeepQueryingUnlessResolved (bool): If true, it keeps Querying Unless resolved
			MapResolvingInterval (number): It gives the map resolving interval
			PrefixLength (number): it gives the prefix length
			QueryIntervalUnlessResolved (number): It gives the query regarding the interval unless resolved
			StartAddress (str): It gives details about the start address

		Returns:
			self: This instance with matching itrRemoteEidRange data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of itrRemoteEidRange data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the itrRemoteEidRange data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
