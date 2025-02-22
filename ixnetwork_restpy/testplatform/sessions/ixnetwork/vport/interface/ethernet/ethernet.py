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


class Ethernet(Base):
	"""Controls the general Ethernet interface properties.
	The Ethernet class encapsulates a required ethernet resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'ethernet'

	def __init__(self, parent):
		super(Ethernet, self).__init__(parent)

	@property
	def MacAddress(self):
		"""A 48-bit hardware address that uniquely identifies each node of a network.

		Returns:
			str
		"""
		return self._get_attribute('macAddress')
	@MacAddress.setter
	def MacAddress(self, value):
		self._set_attribute('macAddress', value)

	@property
	def Mtu(self):
		"""The maximum packet size, in bytes, that a particular interface can handle.

		Returns:
			number
		"""
		return self._get_attribute('mtu')
	@Mtu.setter
	def Mtu(self, value):
		self._set_attribute('mtu', value)

	@property
	def UidFromMac(self):
		"""The interface identifier is derived from the MAC address. The interface identifier u (universal/local) bit will be set to zero to indicate global scope.

		Returns:
			bool
		"""
		return self._get_attribute('uidFromMac')
	@UidFromMac.setter
	def UidFromMac(self, value):
		self._set_attribute('uidFromMac', value)

	def update(self, MacAddress=None, Mtu=None, UidFromMac=None):
		"""Updates a child instance of ethernet on the server.

		Args:
			MacAddress (str): A 48-bit hardware address that uniquely identifies each node of a network.
			Mtu (number): The maximum packet size, in bytes, that a particular interface can handle.
			UidFromMac (bool): The interface identifier is derived from the MAC address. The interface identifier u (universal/local) bit will be set to zero to indicate global scope.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
