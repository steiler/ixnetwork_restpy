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


class PeriodicOamLtLearnedInfo(Base):
	"""This object holds the periodic OAM link trace learned information.
	The PeriodicOamLtLearnedInfo class encapsulates a list of periodicOamLtLearnedInfo resources that is managed by the system.
	A list of resources can be retrieved from the server using the PeriodicOamLtLearnedInfo.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'periodicOamLtLearnedInfo'

	def __init__(self, parent):
		super(PeriodicOamLtLearnedInfo, self).__init__(parent)

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
	def AverageHopCount(self):
		"""(read only) The learned average hop count.

		Returns:
			number
		"""
		return self._get_attribute('averageHopCount')

	@property
	def CVlan(self):
		"""(read only) The learned C-VLAN identifier. (CFM only)

		Returns:
			str
		"""
		return self._get_attribute('cVlan')

	@property
	def CompleteReplyCount(self):
		"""(read only) The learned number of complete replies.

		Returns:
			number
		"""
		return self._get_attribute('completeReplyCount')

	@property
	def DstMacAddress(self):
		"""(read only) The learned destination MAC address.

		Returns:
			str
		"""
		return self._get_attribute('dstMacAddress')

	@property
	def LtmSentCount(self):
		"""(read only) The learned number of Link Trace messages sent.

		Returns:
			number
		"""
		return self._get_attribute('ltmSentCount')

	@property
	def MdLevel(self):
		"""(read only) The learned MD level.

		Returns:
			number
		"""
		return self._get_attribute('mdLevel')

	@property
	def NoReplyCount(self):
		"""(read only) The learned number of no replies.

		Returns:
			number
		"""
		return self._get_attribute('noReplyCount')

	@property
	def PartialReplyCount(self):
		"""(read only) The learned number of partial replies.

		Returns:
			number
		"""
		return self._get_attribute('partialReplyCount')

	@property
	def RecentHopCount(self):
		"""(read only) The learned recent hop count.

		Returns:
			number
		"""
		return self._get_attribute('recentHopCount')

	@property
	def RecentHops(self):
		"""(read only) The learned recent hops.

		Returns:
			str
		"""
		return self._get_attribute('recentHops')

	@property
	def RecentReplyStatus(self):
		"""(read only) The learned recent replies.

		Returns:
			str
		"""
		return self._get_attribute('recentReplyStatus')

	@property
	def SVlan(self):
		"""(read only) The learned S-VLAN identifier. (CFM only)

		Returns:
			str
		"""
		return self._get_attribute('sVlan')

	@property
	def SrcMacAddress(self):
		"""(read only) The learned source MAC address.

		Returns:
			str
		"""
		return self._get_attribute('srcMacAddress')

	def find(self, AverageHopCount=None, CVlan=None, CompleteReplyCount=None, DstMacAddress=None, LtmSentCount=None, MdLevel=None, NoReplyCount=None, PartialReplyCount=None, RecentHopCount=None, RecentHops=None, RecentReplyStatus=None, SVlan=None, SrcMacAddress=None):
		"""Finds and retrieves periodicOamLtLearnedInfo data from the server.

		All named parameters support regex and can be used to selectively retrieve periodicOamLtLearnedInfo data from the server.
		By default the find method takes no parameters and will retrieve all periodicOamLtLearnedInfo data from the server.

		Args:
			AverageHopCount (number): (read only) The learned average hop count.
			CVlan (str): (read only) The learned C-VLAN identifier. (CFM only)
			CompleteReplyCount (number): (read only) The learned number of complete replies.
			DstMacAddress (str): (read only) The learned destination MAC address.
			LtmSentCount (number): (read only) The learned number of Link Trace messages sent.
			MdLevel (number): (read only) The learned MD level.
			NoReplyCount (number): (read only) The learned number of no replies.
			PartialReplyCount (number): (read only) The learned number of partial replies.
			RecentHopCount (number): (read only) The learned recent hop count.
			RecentHops (str): (read only) The learned recent hops.
			RecentReplyStatus (str): (read only) The learned recent replies.
			SVlan (str): (read only) The learned S-VLAN identifier. (CFM only)
			SrcMacAddress (str): (read only) The learned source MAC address.

		Returns:
			self: This instance with matching periodicOamLtLearnedInfo data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of periodicOamLtLearnedInfo data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the periodicOamLtLearnedInfo data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
