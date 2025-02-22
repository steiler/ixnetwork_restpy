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


class SwitchMeterLearnedInfo(Base):
	"""NOT DEFINED
	The SwitchMeterLearnedInfo class encapsulates a list of switchMeterLearnedInfo resources that is managed by the system.
	A list of resources can be retrieved from the server using the SwitchMeterLearnedInfo.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'switchMeterLearnedInfo'

	def __init__(self, parent):
		super(SwitchMeterLearnedInfo, self).__init__(parent)

	@property
	def SwitchMeterBandLearnedInfo(self):
		"""An instance of the SwitchMeterBandLearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchmeterbandlearnedinfo_y2hnzxrlckjhbmrmzwfybmvksw5mbw.SwitchMeterBandLearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchmeterbandlearnedinfo_y2hnzxrlckjhbmrmzwfybmvksw5mbw import SwitchMeterBandLearnedInfo
		return SwitchMeterBandLearnedInfo(self)

	@property
	def BytesInInput(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('bytesInInput')

	@property
	def DatapathId(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('datapathId')

	@property
	def DatapathIdAsHex(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('datapathIdAsHex')

	@property
	def DurationNSec(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('durationNSec')

	@property
	def DurationSec(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('durationSec')

	@property
	def FlowCount(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('flowCount')

	@property
	def LocalIp(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('localIp')

	@property
	def MeterConfigurationFlags(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('meterConfigurationFlags')

	@property
	def MeterId(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('meterId')

	@property
	def NumOfBands(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('numOfBands')

	@property
	def PacketsInInput(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('packetsInInput')

	def find(self, BytesInInput=None, DatapathId=None, DatapathIdAsHex=None, DurationNSec=None, DurationSec=None, FlowCount=None, LocalIp=None, MeterConfigurationFlags=None, MeterId=None, NumOfBands=None, PacketsInInput=None):
		"""Finds and retrieves switchMeterLearnedInfo data from the server.

		All named parameters support regex and can be used to selectively retrieve switchMeterLearnedInfo data from the server.
		By default the find method takes no parameters and will retrieve all switchMeterLearnedInfo data from the server.

		Args:
			BytesInInput (number): NOT DEFINED
			DatapathId (str): NOT DEFINED
			DatapathIdAsHex (str): NOT DEFINED
			DurationNSec (number): NOT DEFINED
			DurationSec (number): NOT DEFINED
			FlowCount (number): NOT DEFINED
			LocalIp (str): NOT DEFINED
			MeterConfigurationFlags (str): NOT DEFINED
			MeterId (number): NOT DEFINED
			NumOfBands (number): NOT DEFINED
			PacketsInInput (number): NOT DEFINED

		Returns:
			self: This instance with matching switchMeterLearnedInfo data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of switchMeterLearnedInfo data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the switchMeterLearnedInfo data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
