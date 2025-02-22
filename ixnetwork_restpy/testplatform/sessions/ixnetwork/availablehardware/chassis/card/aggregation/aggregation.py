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


class Aggregation(Base):
	"""The Card resource group.
	The Aggregation class encapsulates a list of aggregation resources that is managed by the system.
	A list of resources can be retrieved from the server using the Aggregation.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'aggregation'

	def __init__(self, parent):
		super(Aggregation, self).__init__(parent)

	@property
	def ActivePort(self):
		"""DEPRECATED Deprecated. Use activePorts instead.

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=port)
		"""
		return self._get_attribute('activePort')

	@property
	def ActivePorts(self):
		"""All active ports from Resource Group.

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=port])
		"""
		return self._get_attribute('activePorts')

	@property
	def AvailableModes(self):
		"""Gets the supported resource group modes.

		Returns:
			list(str[normal|tenGig|fortyGig|singleMode|dualMode|hundredGigNonFanOut|fortyGigFanOut|threeByTenGigFanOut|eightByTenGigFanOut|fourByTwentyFiveGigNonFanOut|twoByTwentyFiveGigNonFanOut|oneByFiftyGigNonFanOut|fortyGigNonFanOut|oneByTenGigFanOut|fourByTenGigFanOut|incompatibleMode|hundredGigCapturePlayback|fortyGigCapturePlayback|novusHundredGigNonFanOut|novusFourByTwentyFiveGigNonFanOut|novusTwoByFiftyGigNonFanOut|novusOneByFortyGigNonFanOut|novusFourByTenGigNonFanOut|krakenOneByFourHundredGigNonFanOut|krakenOneByTwoHundredGigNonFanOut|krakenTwoByOneHundredGigFanOut|krakenFourByFiftyGigFanOut|aresOneOneByFourHundredGigNonFanOut|aresOneTwoByTwoHundredGigFanOut|aresOneFourByOneHundredGigFanOut|aresOneEightByFiftyGigFanOut])
		"""
		return self._get_attribute('availableModes')

	@property
	def Mode(self):
		"""Resource Group mode.

		Returns:
			str(normal|tenGig|fortyGig|singleMode|dualMode|hundredGigNonFanOut|fortyGigFanOut|threeByTenGigFanOut|eightByTenGigFanOut|fourByTwentyFiveGigNonFanOut|twoByTwentyFiveGigNonFanOut|oneByFiftyGigNonFanOut|fortyGigNonFanOut|oneByTenGigFanOut|fourByTenGigFanOut|incompatibleMode|hundredGigCapturePlayback|fortyGigCapturePlayback|novusHundredGigNonFanOut|novusFourByTwentyFiveGigNonFanOut|novusTwoByFiftyGigNonFanOut|novusOneByFortyGigNonFanOut|novusFourByTenGigNonFanOut|krakenOneByFourHundredGigNonFanOut|krakenOneByTwoHundredGigNonFanOut|krakenTwoByOneHundredGigFanOut|krakenFourByFiftyGigFanOut|aresOneOneByFourHundredGigNonFanOut|aresOneTwoByTwoHundredGigFanOut|aresOneFourByOneHundredGigFanOut|aresOneEightByFiftyGigFanOut)
		"""
		return self._get_attribute('mode')
	@Mode.setter
	def Mode(self, value):
		self._set_attribute('mode', value)

	@property
	def ResourcePorts(self):
		"""All ports from Resource Group.

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=port])
		"""
		return self._get_attribute('resourcePorts')

	def update(self, Mode=None):
		"""Updates a child instance of aggregation on the server.

		Args:
			Mode (str(normal|tenGig|fortyGig|singleMode|dualMode|hundredGigNonFanOut|fortyGigFanOut|threeByTenGigFanOut|eightByTenGigFanOut|fourByTwentyFiveGigNonFanOut|twoByTwentyFiveGigNonFanOut|oneByFiftyGigNonFanOut|fortyGigNonFanOut|oneByTenGigFanOut|fourByTenGigFanOut|incompatibleMode|hundredGigCapturePlayback|fortyGigCapturePlayback|novusHundredGigNonFanOut|novusFourByTwentyFiveGigNonFanOut|novusTwoByFiftyGigNonFanOut|novusOneByFortyGigNonFanOut|novusFourByTenGigNonFanOut|krakenOneByFourHundredGigNonFanOut|krakenOneByTwoHundredGigNonFanOut|krakenTwoByOneHundredGigFanOut|krakenFourByFiftyGigFanOut|aresOneOneByFourHundredGigNonFanOut|aresOneTwoByTwoHundredGigFanOut|aresOneFourByOneHundredGigFanOut|aresOneEightByFiftyGigFanOut)): Resource Group mode.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def find(self, ActivePort=None, ActivePorts=None, AvailableModes=None, Mode=None, ResourcePorts=None):
		"""Finds and retrieves aggregation data from the server.

		All named parameters support regex and can be used to selectively retrieve aggregation data from the server.
		By default the find method takes no parameters and will retrieve all aggregation data from the server.

		Args:
			ActivePort (str(None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=port)): Deprecated. Use activePorts instead.
			ActivePorts (list(str[None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=port])): All active ports from Resource Group.
			AvailableModes (list(str[normal|tenGig|fortyGig|singleMode|dualMode|hundredGigNonFanOut|fortyGigFanOut|threeByTenGigFanOut|eightByTenGigFanOut|fourByTwentyFiveGigNonFanOut|twoByTwentyFiveGigNonFanOut|oneByFiftyGigNonFanOut|fortyGigNonFanOut|oneByTenGigFanOut|fourByTenGigFanOut|incompatibleMode|hundredGigCapturePlayback|fortyGigCapturePlayback|novusHundredGigNonFanOut|novusFourByTwentyFiveGigNonFanOut|novusTwoByFiftyGigNonFanOut|novusOneByFortyGigNonFanOut|novusFourByTenGigNonFanOut|krakenOneByFourHundredGigNonFanOut|krakenOneByTwoHundredGigNonFanOut|krakenTwoByOneHundredGigFanOut|krakenFourByFiftyGigFanOut|aresOneOneByFourHundredGigNonFanOut|aresOneTwoByTwoHundredGigFanOut|aresOneFourByOneHundredGigFanOut|aresOneEightByFiftyGigFanOut])): Gets the supported resource group modes.
			Mode (str(normal|tenGig|fortyGig|singleMode|dualMode|hundredGigNonFanOut|fortyGigFanOut|threeByTenGigFanOut|eightByTenGigFanOut|fourByTwentyFiveGigNonFanOut|twoByTwentyFiveGigNonFanOut|oneByFiftyGigNonFanOut|fortyGigNonFanOut|oneByTenGigFanOut|fourByTenGigFanOut|incompatibleMode|hundredGigCapturePlayback|fortyGigCapturePlayback|novusHundredGigNonFanOut|novusFourByTwentyFiveGigNonFanOut|novusTwoByFiftyGigNonFanOut|novusOneByFortyGigNonFanOut|novusFourByTenGigNonFanOut|krakenOneByFourHundredGigNonFanOut|krakenOneByTwoHundredGigNonFanOut|krakenTwoByOneHundredGigFanOut|krakenFourByFiftyGigFanOut|aresOneOneByFourHundredGigNonFanOut|aresOneTwoByTwoHundredGigFanOut|aresOneFourByOneHundredGigFanOut|aresOneEightByFiftyGigFanOut)): Resource Group mode.
			ResourcePorts (list(str[None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=port])): All ports from Resource Group.

		Returns:
			self: This instance with matching aggregation data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of aggregation data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the aggregation data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
