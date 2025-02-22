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


class Ip(Base):
	"""This object holds the list of statically-configured IP addresses for the port.
	The Ip class encapsulates a list of ip resources that is be managed by the user.
	A list of resources can be retrieved from the server using the Ip.find() method.
	The list can be managed by the user by using the Ip.add() and Ip.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'ip'

	def __init__(self, parent):
		super(Ip, self).__init__(parent)

	@property
	def Count(self):
		"""The total number of addresses to create for this range of IP addresses.

		Returns:
			number
		"""
		return self._get_attribute('count')
	@Count.setter
	def Count(self, value):
		self._set_attribute('count', value)

	@property
	def Enabled(self):
		"""Enables this IP address entry.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def IpStart(self):
		"""The first IP address in the range.

		Returns:
			str
		"""
		return self._get_attribute('ipStart')
	@IpStart.setter
	def IpStart(self, value):
		self._set_attribute('ipStart', value)

	@property
	def IpType(self):
		"""The Internet Protocol (IP version).

		Returns:
			str(ipv4|ipv6)
		"""
		return self._get_attribute('ipType')
	@IpType.setter
	def IpType(self, value):
		self._set_attribute('ipType', value)

	@property
	def Mask(self):
		"""The number of bits in the network mask to be used to extract network and subnetwork information from the IP address.

		Returns:
			number
		"""
		return self._get_attribute('mask')
	@Mask.setter
	def Mask(self, value):
		self._set_attribute('mask', value)

	@property
	def ProtocolInterface(self):
		"""There may be multiple interfaces listed.

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=interface)
		"""
		return self._get_attribute('protocolInterface')
	@ProtocolInterface.setter
	def ProtocolInterface(self, value):
		self._set_attribute('protocolInterface', value)

	@property
	def Step(self):
		"""The increment value to be used for each additional address, to create a range of IP addresses.

		Returns:
			number
		"""
		return self._get_attribute('step')
	@Step.setter
	def Step(self, value):
		self._set_attribute('step', value)

	@property
	def TrafficGroupId(self):
		"""The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficGroup)
		"""
		return self._get_attribute('trafficGroupId')
	@TrafficGroupId.setter
	def TrafficGroupId(self, value):
		self._set_attribute('trafficGroupId', value)

	def update(self, Count=None, Enabled=None, IpStart=None, IpType=None, Mask=None, ProtocolInterface=None, Step=None, TrafficGroupId=None):
		"""Updates a child instance of ip on the server.

		Args:
			Count (number): The total number of addresses to create for this range of IP addresses.
			Enabled (bool): Enables this IP address entry.
			IpStart (str): The first IP address in the range.
			IpType (str(ipv4|ipv6)): The Internet Protocol (IP version).
			Mask (number): The number of bits in the network mask to be used to extract network and subnetwork information from the IP address.
			ProtocolInterface (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=interface)): There may be multiple interfaces listed.
			Step (number): The increment value to be used for each additional address, to create a range of IP addresses.
			TrafficGroupId (str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Count=None, Enabled=None, IpStart=None, IpType=None, Mask=None, ProtocolInterface=None, Step=None, TrafficGroupId=None):
		"""Adds a new ip node on the server and retrieves it in this instance.

		Args:
			Count (number): The total number of addresses to create for this range of IP addresses.
			Enabled (bool): Enables this IP address entry.
			IpStart (str): The first IP address in the range.
			IpType (str(ipv4|ipv6)): The Internet Protocol (IP version).
			Mask (number): The number of bits in the network mask to be used to extract network and subnetwork information from the IP address.
			ProtocolInterface (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=interface)): There may be multiple interfaces listed.
			Step (number): The increment value to be used for each additional address, to create a range of IP addresses.
			TrafficGroupId (str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.

		Returns:
			self: This instance with all currently retrieved ip data using find and the newly added ip data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the ip data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Count=None, Enabled=None, IpStart=None, IpType=None, Mask=None, ProtocolInterface=None, Step=None, TrafficGroupId=None):
		"""Finds and retrieves ip data from the server.

		All named parameters support regex and can be used to selectively retrieve ip data from the server.
		By default the find method takes no parameters and will retrieve all ip data from the server.

		Args:
			Count (number): The total number of addresses to create for this range of IP addresses.
			Enabled (bool): Enables this IP address entry.
			IpStart (str): The first IP address in the range.
			IpType (str(ipv4|ipv6)): The Internet Protocol (IP version).
			Mask (number): The number of bits in the network mask to be used to extract network and subnetwork information from the IP address.
			ProtocolInterface (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=interface)): There may be multiple interfaces listed.
			Step (number): The increment value to be used for each additional address, to create a range of IP addresses.
			TrafficGroupId (str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.

		Returns:
			self: This instance with matching ip data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of ip data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the ip data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
