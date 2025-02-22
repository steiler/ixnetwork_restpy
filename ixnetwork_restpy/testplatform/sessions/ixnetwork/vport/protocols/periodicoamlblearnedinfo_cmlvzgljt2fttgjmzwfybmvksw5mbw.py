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


class PeriodicOamLbLearnedInfo(Base):
	"""The periodicOamLtLearnedInfo object holds the periodic OAM loopback learned information.
	The PeriodicOamLbLearnedInfo class encapsulates a list of periodicOamLbLearnedInfo resources that is managed by the system.
	A list of resources can be retrieved from the server using the PeriodicOamLbLearnedInfo.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'periodicOamLbLearnedInfo'

	def __init__(self, parent):
		super(PeriodicOamLbLearnedInfo, self).__init__(parent)

	@property
	def AverageRtt(self):
		"""(read only) The learned average periodic OAM Round-Trip-Time.

		Returns:
			number
		"""
		return self._get_attribute('averageRtt')

	@property
	def CVlan(self):
		"""(read only) The learned periodic OAM C-VLAN identifier.

		Returns:
			str
		"""
		return self._get_attribute('cVlan')

	@property
	def DstMacAddress(self):
		"""(read only) The learned periodic OAM destination MAC address.

		Returns:
			str
		"""
		return self._get_attribute('dstMacAddress')

	@property
	def LbmSentCount(self):
		"""(read only) The learned number of periodic OAM loopback messages sent.

		Returns:
			number
		"""
		return self._get_attribute('lbmSentCount')

	@property
	def MdLevel(self):
		"""(read only) The learned MD level for the periodic OAM.

		Returns:
			number
		"""
		return self._get_attribute('mdLevel')

	@property
	def NoReplyCount(self):
		"""(read only) The learned number of periodic OAM no replies.

		Returns:
			number
		"""
		return self._get_attribute('noReplyCount')

	@property
	def RecentReachability(self):
		"""(read only) Indicates the status of the Ping.

		Returns:
			bool
		"""
		return self._get_attribute('recentReachability')

	@property
	def RecentRtt(self):
		"""(read only) Indicates the status of the round-trip-time

		Returns:
			number
		"""
		return self._get_attribute('recentRtt')

	@property
	def SVlan(self):
		"""(read only) The learned periodic OAM S-VLAN identifier.

		Returns:
			str
		"""
		return self._get_attribute('sVlan')

	@property
	def SrcMacAddress(self):
		"""(read only) The learned periodic OAM source MAC address.

		Returns:
			str
		"""
		return self._get_attribute('srcMacAddress')

	def find(self, AverageRtt=None, CVlan=None, DstMacAddress=None, LbmSentCount=None, MdLevel=None, NoReplyCount=None, RecentReachability=None, RecentRtt=None, SVlan=None, SrcMacAddress=None):
		"""Finds and retrieves periodicOamLbLearnedInfo data from the server.

		All named parameters support regex and can be used to selectively retrieve periodicOamLbLearnedInfo data from the server.
		By default the find method takes no parameters and will retrieve all periodicOamLbLearnedInfo data from the server.

		Args:
			AverageRtt (number): (read only) The learned average periodic OAM Round-Trip-Time.
			CVlan (str): (read only) The learned periodic OAM C-VLAN identifier.
			DstMacAddress (str): (read only) The learned periodic OAM destination MAC address.
			LbmSentCount (number): (read only) The learned number of periodic OAM loopback messages sent.
			MdLevel (number): (read only) The learned MD level for the periodic OAM.
			NoReplyCount (number): (read only) The learned number of periodic OAM no replies.
			RecentReachability (bool): (read only) Indicates the status of the Ping.
			RecentRtt (number): (read only) Indicates the status of the round-trip-time
			SVlan (str): (read only) The learned periodic OAM S-VLAN identifier.
			SrcMacAddress (str): (read only) The learned periodic OAM source MAC address.

		Returns:
			self: This instance with matching periodicOamLbLearnedInfo data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of periodicOamLbLearnedInfo data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the periodicOamLbLearnedInfo data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
