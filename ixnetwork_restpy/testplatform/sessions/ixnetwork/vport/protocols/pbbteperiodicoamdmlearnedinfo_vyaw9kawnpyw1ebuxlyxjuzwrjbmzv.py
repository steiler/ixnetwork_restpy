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


class PbbTePeriodicOamDmLearnedInfo(Base):
	"""The pbbTePeriodicOamDmLearnedInfo object holds the PBB-TE periodic OAM delay measurement learned information.
	The PbbTePeriodicOamDmLearnedInfo class encapsulates a list of pbbTePeriodicOamDmLearnedInfo resources that is managed by the system.
	A list of resources can be retrieved from the server using the PbbTePeriodicOamDmLearnedInfo.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'pbbTePeriodicOamDmLearnedInfo'

	def __init__(self, parent):
		super(PbbTePeriodicOamDmLearnedInfo, self).__init__(parent)

	@property
	def AverageDelayNanoSec(self):
		"""(read only) The learned average delay in nanoseconds.

		Returns:
			number
		"""
		return self._get_attribute('averageDelayNanoSec')

	@property
	def AverageDelaySec(self):
		"""(read only) The learned average delay in seconds.

		Returns:
			number
		"""
		return self._get_attribute('averageDelaySec')

	@property
	def AverageDelayVariationNanoSec(self):
		"""(read only) The learned most recent delay variation in nano seconds.

		Returns:
			number
		"""
		return self._get_attribute('averageDelayVariationNanoSec')

	@property
	def AverageDelayVariationSec(self):
		"""(read only) The learned most recent delay variation in seconds.

		Returns:
			number
		"""
		return self._get_attribute('averageDelayVariationSec')

	@property
	def BVlan(self):
		"""(read only) The learned B-VLAN identifier.

		Returns:
			str
		"""
		return self._get_attribute('bVlan')

	@property
	def DmmCountSent(self):
		"""(read only) The learned number of DMMs sent.

		Returns:
			number
		"""
		return self._get_attribute('dmmCountSent')

	@property
	def DstMacAddress(self):
		"""(read only) The learned destination MAC address.

		Returns:
			str
		"""
		return self._get_attribute('dstMacAddress')

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
	def OneDmReceivedCount(self):
		"""(read only) The learned number of DM received.

		Returns:
			number
		"""
		return self._get_attribute('oneDmReceivedCount')

	@property
	def RecentDelayNanoSec(self):
		"""(read only) The learned most recent delay measurement in nanoseconds.

		Returns:
			number
		"""
		return self._get_attribute('recentDelayNanoSec')

	@property
	def RecentDelaySec(self):
		"""(read only) The learned most recent delay measurement in seconds.

		Returns:
			number
		"""
		return self._get_attribute('recentDelaySec')

	@property
	def RecentDelayVariationNanoSec(self):
		"""(read only) The learned most recent delay variation in nano seconds.

		Returns:
			number
		"""
		return self._get_attribute('recentDelayVariationNanoSec')

	@property
	def RecentDelayVariationSec(self):
		"""(read only) The learned most recent delay variation in seconds.

		Returns:
			number
		"""
		return self._get_attribute('recentDelayVariationSec')

	@property
	def SrcMacAddress(self):
		"""(read only) The learned source MAC address.

		Returns:
			str
		"""
		return self._get_attribute('srcMacAddress')

	def find(self, AverageDelayNanoSec=None, AverageDelaySec=None, AverageDelayVariationNanoSec=None, AverageDelayVariationSec=None, BVlan=None, DmmCountSent=None, DstMacAddress=None, MdLevel=None, NoReplyCount=None, OneDmReceivedCount=None, RecentDelayNanoSec=None, RecentDelaySec=None, RecentDelayVariationNanoSec=None, RecentDelayVariationSec=None, SrcMacAddress=None):
		"""Finds and retrieves pbbTePeriodicOamDmLearnedInfo data from the server.

		All named parameters support regex and can be used to selectively retrieve pbbTePeriodicOamDmLearnedInfo data from the server.
		By default the find method takes no parameters and will retrieve all pbbTePeriodicOamDmLearnedInfo data from the server.

		Args:
			AverageDelayNanoSec (number): (read only) The learned average delay in nanoseconds.
			AverageDelaySec (number): (read only) The learned average delay in seconds.
			AverageDelayVariationNanoSec (number): (read only) The learned most recent delay variation in nano seconds.
			AverageDelayVariationSec (number): (read only) The learned most recent delay variation in seconds.
			BVlan (str): (read only) The learned B-VLAN identifier.
			DmmCountSent (number): (read only) The learned number of DMMs sent.
			DstMacAddress (str): (read only) The learned destination MAC address.
			MdLevel (number): (read only) The learned MD level for the periodic OAM.
			NoReplyCount (number): (read only) The learned number of periodic OAM no replies.
			OneDmReceivedCount (number): (read only) The learned number of DM received.
			RecentDelayNanoSec (number): (read only) The learned most recent delay measurement in nanoseconds.
			RecentDelaySec (number): (read only) The learned most recent delay measurement in seconds.
			RecentDelayVariationNanoSec (number): (read only) The learned most recent delay variation in nano seconds.
			RecentDelayVariationSec (number): (read only) The learned most recent delay variation in seconds.
			SrcMacAddress (str): (read only) The learned source MAC address.

		Returns:
			self: This instance with matching pbbTePeriodicOamDmLearnedInfo data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of pbbTePeriodicOamDmLearnedInfo data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the pbbTePeriodicOamDmLearnedInfo data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
