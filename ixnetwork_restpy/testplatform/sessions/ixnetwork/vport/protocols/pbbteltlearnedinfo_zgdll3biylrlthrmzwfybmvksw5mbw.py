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


class PbbTeLtLearnedInfo(Base):
	"""The pbbTeLtLearnedInfo object holds the PBB-TE link trace learned information.
	The PbbTeLtLearnedInfo class encapsulates a list of pbbTeLtLearnedInfo resources that is managed by the system.
	A list of resources can be retrieved from the server using the PbbTeLtLearnedInfo.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'pbbTeLtLearnedInfo'

	def __init__(self, parent):
		super(PbbTeLtLearnedInfo, self).__init__(parent)

	@property
	def LtLearnedHop(self):
		"""An instance of the LtLearnedHop class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ltlearnedhop_wfybmvksw5mby9sdexlyxjuzwrib3a.LtLearnedHop)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ltlearnedhop_wfybmvksw5mby9sdexlyxjuzwrib3a import LtLearnedHop
		return LtLearnedHop(self)

	@property
	def BVlan(self):
		"""(read only) The learned B-VLAN identifier.

		Returns:
			str
		"""
		return self._get_attribute('bVlan')

	@property
	def DstMacAddress(self):
		"""(read only) The learned destination MAC address.

		Returns:
			str
		"""
		return self._get_attribute('dstMacAddress')

	@property
	def HopCount(self):
		"""(read only) The learned number of hops in the link.

		Returns:
			number
		"""
		return self._get_attribute('hopCount')

	@property
	def Hops(self):
		"""(read only) The learned list of hops to reach the particular MEP (MAC address).

		Returns:
			str
		"""
		return self._get_attribute('hops')

	@property
	def MdLevel(self):
		"""(read only) The learned MD level for the periodic OAM.

		Returns:
			number
		"""
		return self._get_attribute('mdLevel')

	@property
	def ReplyStatus(self):
		"""(read only) The learned current reply status.

		Returns:
			str
		"""
		return self._get_attribute('replyStatus')

	@property
	def SrcMacAddress(self):
		"""(read only) The learned source MAC address.

		Returns:
			str
		"""
		return self._get_attribute('srcMacAddress')

	@property
	def TransactionId(self):
		"""(read only) The learned identifier sent with the LTM.

		Returns:
			number
		"""
		return self._get_attribute('transactionId')

	def find(self, BVlan=None, DstMacAddress=None, HopCount=None, Hops=None, MdLevel=None, ReplyStatus=None, SrcMacAddress=None, TransactionId=None):
		"""Finds and retrieves pbbTeLtLearnedInfo data from the server.

		All named parameters support regex and can be used to selectively retrieve pbbTeLtLearnedInfo data from the server.
		By default the find method takes no parameters and will retrieve all pbbTeLtLearnedInfo data from the server.

		Args:
			BVlan (str): (read only) The learned B-VLAN identifier.
			DstMacAddress (str): (read only) The learned destination MAC address.
			HopCount (number): (read only) The learned number of hops in the link.
			Hops (str): (read only) The learned list of hops to reach the particular MEP (MAC address).
			MdLevel (number): (read only) The learned MD level for the periodic OAM.
			ReplyStatus (str): (read only) The learned current reply status.
			SrcMacAddress (str): (read only) The learned source MAC address.
			TransactionId (number): (read only) The learned identifier sent with the LTM.

		Returns:
			self: This instance with matching pbbTeLtLearnedInfo data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of pbbTeLtLearnedInfo data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the pbbTeLtLearnedInfo data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
