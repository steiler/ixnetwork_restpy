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


class PbbTeLbLearnedInfo(Base):
	"""This object contains the PBB-TE loopback learned information.
	The PbbTeLbLearnedInfo class encapsulates a list of pbbTeLbLearnedInfo resources that is managed by the system.
	A list of resources can be retrieved from the server using the PbbTeLbLearnedInfo.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'pbbTeLbLearnedInfo'

	def __init__(self, parent):
		super(PbbTeLbLearnedInfo, self).__init__(parent)

	@property
	def BVlan(self):
		"""(read only) The VLAN identifier for the loopback message.

		Returns:
			str
		"""
		return self._get_attribute('bVlan')

	@property
	def DstMacAddress(self):
		"""(read only) The destination MAC address for the loopback message.

		Returns:
			str
		"""
		return self._get_attribute('dstMacAddress')

	@property
	def MdLevel(self):
		"""(read only) The MD level for the loopback message.

		Returns:
			number
		"""
		return self._get_attribute('mdLevel')

	@property
	def Reachability(self):
		"""(read only) If true, the Ping message was received and responded to.

		Returns:
			bool
		"""
		return self._get_attribute('reachability')

	@property
	def Rtt(self):
		"""(read only) The round trip time for the PBB-TE loopback message.

		Returns:
			number
		"""
		return self._get_attribute('rtt')

	@property
	def SrcMacAddress(self):
		"""(read only) The source MAC address for the loopback message.

		Returns:
			str
		"""
		return self._get_attribute('srcMacAddress')

	@property
	def TransactionId(self):
		"""(read only) The transaction identifier sent with the loopback message.

		Returns:
			number
		"""
		return self._get_attribute('transactionId')

	def find(self, BVlan=None, DstMacAddress=None, MdLevel=None, Reachability=None, Rtt=None, SrcMacAddress=None, TransactionId=None):
		"""Finds and retrieves pbbTeLbLearnedInfo data from the server.

		All named parameters support regex and can be used to selectively retrieve pbbTeLbLearnedInfo data from the server.
		By default the find method takes no parameters and will retrieve all pbbTeLbLearnedInfo data from the server.

		Args:
			BVlan (str): (read only) The VLAN identifier for the loopback message.
			DstMacAddress (str): (read only) The destination MAC address for the loopback message.
			MdLevel (number): (read only) The MD level for the loopback message.
			Reachability (bool): (read only) If true, the Ping message was received and responded to.
			Rtt (number): (read only) The round trip time for the PBB-TE loopback message.
			SrcMacAddress (str): (read only) The source MAC address for the loopback message.
			TransactionId (number): (read only) The transaction identifier sent with the loopback message.

		Returns:
			self: This instance with matching pbbTeLbLearnedInfo data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of pbbTeLbLearnedInfo data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the pbbTeLbLearnedInfo data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
