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


class GroupStatBucketLearnedInformation(Base):
	"""NOT DEFINED
	The GroupStatBucketLearnedInformation class encapsulates a list of groupStatBucketLearnedInformation resources that is managed by the system.
	A list of resources can be retrieved from the server using the GroupStatBucketLearnedInformation.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'groupStatBucketLearnedInformation'

	def __init__(self, parent):
		super(GroupStatBucketLearnedInformation, self).__init__(parent)

	@property
	def ByteCount(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('byteCount')

	@property
	def DataPathId(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('dataPathId')

	@property
	def DataPathIdAsHex(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('dataPathIdAsHex')

	@property
	def GroupId(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('groupId')

	@property
	def LocalIp(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('localIp')

	@property
	def PacketCount(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('packetCount')

	@property
	def RemoteIp(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('remoteIp')

	def find(self, ByteCount=None, DataPathId=None, DataPathIdAsHex=None, GroupId=None, LocalIp=None, PacketCount=None, RemoteIp=None):
		"""Finds and retrieves groupStatBucketLearnedInformation data from the server.

		All named parameters support regex and can be used to selectively retrieve groupStatBucketLearnedInformation data from the server.
		By default the find method takes no parameters and will retrieve all groupStatBucketLearnedInformation data from the server.

		Args:
			ByteCount (str): NOT DEFINED
			DataPathId (str): NOT DEFINED
			DataPathIdAsHex (str): NOT DEFINED
			GroupId (str): NOT DEFINED
			LocalIp (str): NOT DEFINED
			PacketCount (str): NOT DEFINED
			RemoteIp (str): NOT DEFINED

		Returns:
			self: This instance with matching groupStatBucketLearnedInformation data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of groupStatBucketLearnedInformation data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the groupStatBucketLearnedInformation data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
