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


class MacRanges(Base):
	"""This object contains the MAC range configuration.
	The MacRanges class encapsulates a list of macRanges resources that is be managed by the user.
	A list of resources can be retrieved from the server using the MacRanges.find() method.
	The list can be managed by the user by using the MacRanges.add() and MacRanges.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'macRanges'

	def __init__(self, parent):
		super(MacRanges, self).__init__(parent)

	@property
	def Count(self):
		"""The number of times to increment in this MAC range, starting with the address set in macAddress.

		Returns:
			number
		"""
		return self._get_attribute('count')
	@Count.setter
	def Count(self, value):
		self._set_attribute('count', value)

	@property
	def Enabled(self):
		"""If true, the MAC range is enabled.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def MacAddress(self):
		"""The MAC address of the first entry in the range.

		Returns:
			str
		"""
		return self._get_attribute('macAddress')
	@MacAddress.setter
	def MacAddress(self, value):
		self._set_attribute('macAddress', value)

	@property
	def Step(self):
		"""The amount to increment each MAC address in the range.

		Returns:
			str
		"""
		return self._get_attribute('step')
	@Step.setter
	def Step(self, value):
		self._set_attribute('step', value)

	@property
	def TrafficGroupId(self):
		"""Assigns a traffic group to the MAC range. The traffic group must be previously configured.

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficGroup)
		"""
		return self._get_attribute('trafficGroupId')
	@TrafficGroupId.setter
	def TrafficGroupId(self, value):
		self._set_attribute('trafficGroupId', value)

	def update(self, Count=None, Enabled=None, MacAddress=None, Step=None, TrafficGroupId=None):
		"""Updates a child instance of macRanges on the server.

		Args:
			Count (number): The number of times to increment in this MAC range, starting with the address set in macAddress.
			Enabled (bool): If true, the MAC range is enabled.
			MacAddress (str): The MAC address of the first entry in the range.
			Step (str): The amount to increment each MAC address in the range.
			TrafficGroupId (str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficGroup)): Assigns a traffic group to the MAC range. The traffic group must be previously configured.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Count=None, Enabled=None, MacAddress=None, Step=None, TrafficGroupId=None):
		"""Adds a new macRanges node on the server and retrieves it in this instance.

		Args:
			Count (number): The number of times to increment in this MAC range, starting with the address set in macAddress.
			Enabled (bool): If true, the MAC range is enabled.
			MacAddress (str): The MAC address of the first entry in the range.
			Step (str): The amount to increment each MAC address in the range.
			TrafficGroupId (str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficGroup)): Assigns a traffic group to the MAC range. The traffic group must be previously configured.

		Returns:
			self: This instance with all currently retrieved macRanges data using find and the newly added macRanges data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the macRanges data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Count=None, Enabled=None, MacAddress=None, Step=None, TrafficGroupId=None):
		"""Finds and retrieves macRanges data from the server.

		All named parameters support regex and can be used to selectively retrieve macRanges data from the server.
		By default the find method takes no parameters and will retrieve all macRanges data from the server.

		Args:
			Count (number): The number of times to increment in this MAC range, starting with the address set in macAddress.
			Enabled (bool): If true, the MAC range is enabled.
			MacAddress (str): The MAC address of the first entry in the range.
			Step (str): The amount to increment each MAC address in the range.
			TrafficGroupId (str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficGroup)): Assigns a traffic group to the MAC range. The traffic group must be previously configured.

		Returns:
			self: This instance with matching macRanges data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of macRanges data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the macRanges data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
