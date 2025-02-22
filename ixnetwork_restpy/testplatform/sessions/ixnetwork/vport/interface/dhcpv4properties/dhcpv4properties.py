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


class DhcpV4Properties(Base):
	"""Controls the general DHCPv4 interface properties.
	The DhcpV4Properties class encapsulates a required dhcpV4Properties resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'dhcpV4Properties'

	def __init__(self, parent):
		super(DhcpV4Properties, self).__init__(parent)

	@property
	def ClientId(self):
		"""The user may optionally assign an identifier for the Client. This value must be unique on the subnet where the DHCP Client is located.

		Returns:
			str
		"""
		return self._get_attribute('clientId')
	@ClientId.setter
	def ClientId(self, value):
		self._set_attribute('clientId', value)

	@property
	def Enabled(self):
		"""If enabled, DHCP negotiation will be started and an IPv4 address learned from the DHCP server will be assigned automatically to the protocol interface.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def RenewTimer(self):
		"""The renew timer value specified by the DHCPv4 server.

		Returns:
			number
		"""
		return self._get_attribute('renewTimer')
	@RenewTimer.setter
	def RenewTimer(self, value):
		self._set_attribute('renewTimer', value)

	@property
	def RequestRate(self):
		"""(For rate control) The user-specified maximum number of Request messages that can be sent per second from the client to the DHCP server, requesting an IPv4 address. A value of zero (0) indicates that there will be no rate control, i.e., Requests will be sent as quickly as possible.

		Returns:
			number
		"""
		return self._get_attribute('requestRate')
	@RequestRate.setter
	def RequestRate(self, value):
		self._set_attribute('requestRate', value)

	@property
	def ServerId(self):
		"""This IPv4 address value is used to identify the DHCP Server and as a destination address from the client.

		Returns:
			str
		"""
		return self._get_attribute('serverId')
	@ServerId.setter
	def ServerId(self, value):
		self._set_attribute('serverId', value)

	@property
	def Tlvs(self):
		"""The type length value for DHCP.

		Returns:
			list(dict(arg1:number,arg2:str))
		"""
		return self._get_attribute('tlvs')
	@Tlvs.setter
	def Tlvs(self, value):
		self._set_attribute('tlvs', value)

	@property
	def VendorId(self):
		"""The optional, user-assigned Vendor ID (vendor class identifier).

		Returns:
			str
		"""
		return self._get_attribute('vendorId')
	@VendorId.setter
	def VendorId(self, value):
		self._set_attribute('vendorId', value)

	def update(self, ClientId=None, Enabled=None, RenewTimer=None, RequestRate=None, ServerId=None, Tlvs=None, VendorId=None):
		"""Updates a child instance of dhcpV4Properties on the server.

		Args:
			ClientId (str): The user may optionally assign an identifier for the Client. This value must be unique on the subnet where the DHCP Client is located.
			Enabled (bool): If enabled, DHCP negotiation will be started and an IPv4 address learned from the DHCP server will be assigned automatically to the protocol interface.
			RenewTimer (number): The renew timer value specified by the DHCPv4 server.
			RequestRate (number): (For rate control) The user-specified maximum number of Request messages that can be sent per second from the client to the DHCP server, requesting an IPv4 address. A value of zero (0) indicates that there will be no rate control, i.e., Requests will be sent as quickly as possible.
			ServerId (str): This IPv4 address value is used to identify the DHCP Server and as a destination address from the client.
			Tlvs (list(dict(arg1:number,arg2:str))): The type length value for DHCP.
			VendorId (str): The optional, user-assigned Vendor ID (vendor class identifier).

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
