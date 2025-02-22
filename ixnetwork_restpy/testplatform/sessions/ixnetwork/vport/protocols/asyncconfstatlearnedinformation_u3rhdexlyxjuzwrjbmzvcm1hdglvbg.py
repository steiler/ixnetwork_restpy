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


class AsyncConfStatLearnedInformation(Base):
	"""NOT DEFINED
	The AsyncConfStatLearnedInformation class encapsulates a list of asyncConfStatLearnedInformation resources that is managed by the system.
	A list of resources can be retrieved from the server using the AsyncConfStatLearnedInformation.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'asyncConfStatLearnedInformation'

	def __init__(self, parent):
		super(AsyncConfStatLearnedInformation, self).__init__(parent)

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
	def ErrorCode(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('errorCode')

	@property
	def ErrorType(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('errorType')

	@property
	def FlowRemovedMaskMaster(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('flowRemovedMaskMaster')

	@property
	def FlowRemovedMaskSlave(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('flowRemovedMaskSlave')

	@property
	def Latency(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('latency')

	@property
	def LocalIp(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('localIp')

	@property
	def NegotiatedVersion(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('negotiatedVersion')

	@property
	def PacketInMaskMaster(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('packetInMaskMaster')

	@property
	def PacketInMaskSlave(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('packetInMaskSlave')

	@property
	def PortStatusMaskMaster(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('portStatusMaskMaster')

	@property
	def PortStatusMaskSlave(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('portStatusMaskSlave')

	@property
	def RemoteIp(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('remoteIp')

	@property
	def ReplyState(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('replyState')

	def find(self, DataPathId=None, DataPathIdAsHex=None, ErrorCode=None, ErrorType=None, FlowRemovedMaskMaster=None, FlowRemovedMaskSlave=None, Latency=None, LocalIp=None, NegotiatedVersion=None, PacketInMaskMaster=None, PacketInMaskSlave=None, PortStatusMaskMaster=None, PortStatusMaskSlave=None, RemoteIp=None, ReplyState=None):
		"""Finds and retrieves asyncConfStatLearnedInformation data from the server.

		All named parameters support regex and can be used to selectively retrieve asyncConfStatLearnedInformation data from the server.
		By default the find method takes no parameters and will retrieve all asyncConfStatLearnedInformation data from the server.

		Args:
			DataPathId (str): NOT DEFINED
			DataPathIdAsHex (str): NOT DEFINED
			ErrorCode (str): NOT DEFINED
			ErrorType (str): NOT DEFINED
			FlowRemovedMaskMaster (str): NOT DEFINED
			FlowRemovedMaskSlave (str): NOT DEFINED
			Latency (number): NOT DEFINED
			LocalIp (str): NOT DEFINED
			NegotiatedVersion (str): NOT DEFINED
			PacketInMaskMaster (str): NOT DEFINED
			PacketInMaskSlave (str): NOT DEFINED
			PortStatusMaskMaster (str): NOT DEFINED
			PortStatusMaskSlave (str): NOT DEFINED
			RemoteIp (str): NOT DEFINED
			ReplyState (str): NOT DEFINED

		Returns:
			self: This instance with matching asyncConfStatLearnedInformation data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of asyncConfStatLearnedInformation data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the asyncConfStatLearnedInformation data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
