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


class Oam(Base):
	"""The Layer 1 Configuration is being configured for an Ethernet port and OAM is selected as the Payload Type.
	The Oam class encapsulates a required oam resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'oam'

	def __init__(self, parent):
		super(Oam, self).__init__(parent)

	@property
	def EnableTlvOption(self):
		"""If true, enables the tlv option.

		Returns:
			bool
		"""
		return self._get_attribute('enableTlvOption')
	@EnableTlvOption.setter
	def EnableTlvOption(self, value):
		self._set_attribute('enableTlvOption', value)

	@property
	def Enabled(self):
		"""If true, enables OAM for the Ten Gig Lan port.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def IdleTimer(self):
		"""The timer used to ensure OAM sub layer adheres to maximum number of OAMPDUs per second and emits at least one OAMPDU per second. The default is 1, minimum value is 1 and maximum value is 10.

		Returns:
			number
		"""
		return self._get_attribute('idleTimer')
	@IdleTimer.setter
	def IdleTimer(self, value):
		self._set_attribute('idleTimer', value)

	@property
	def LinkEvents(self):
		"""If true, enables link event interpreting support in Ixia port.

		Returns:
			bool
		"""
		return self._get_attribute('linkEvents')
	@LinkEvents.setter
	def LinkEvents(self, value):
		self._set_attribute('linkEvents', value)

	@property
	def Loopback(self):
		"""If true, enables the loopback. when an ixia port goes to loopback mode, then all non oam packets coming to that port gets looped back.

		Returns:
			bool
		"""
		return self._get_attribute('loopback')
	@Loopback.setter
	def Loopback(self, value):
		self._set_attribute('loopback', value)

	@property
	def MacAddress(self):
		"""Mac address of the local DTE. By default, the mac address is automatically generated from card, port and other related information.

		Returns:
			str
		"""
		return self._get_attribute('macAddress')
	@MacAddress.setter
	def MacAddress(self, value):
		self._set_attribute('macAddress', value)

	@property
	def MaxOAMPDUSize(self):
		"""Indicates the maximum OAMPDU size supported by local DTE. The default is 1500, minimum is 64, and maximum is 1500 in octets.

		Returns:
			number
		"""
		return self._get_attribute('maxOAMPDUSize')
	@MaxOAMPDUSize.setter
	def MaxOAMPDUSize(self, value):
		self._set_attribute('maxOAMPDUSize', value)

	@property
	def OrganizationUniqueIdentifier(self):
		"""This three-octet field contains a 24-bit Organizationally Unique Identifier. The default value is 00-01-00. Any three octets hex value can be given.

		Returns:
			str
		"""
		return self._get_attribute('organizationUniqueIdentifier')
	@OrganizationUniqueIdentifier.setter
	def OrganizationUniqueIdentifier(self, value):
		self._set_attribute('organizationUniqueIdentifier', value)

	@property
	def TlvType(self):
		"""Indicates the tlv type.

		Returns:
			str
		"""
		return self._get_attribute('tlvType')
	@TlvType.setter
	def TlvType(self, value):
		self._set_attribute('tlvType', value)

	@property
	def TlvValue(self):
		"""Enters the tlv value.

		Returns:
			str
		"""
		return self._get_attribute('tlvValue')
	@TlvValue.setter
	def TlvValue(self, value):
		self._set_attribute('tlvValue', value)

	@property
	def VendorSpecificInformation(self):
		"""Contains the vendor specific information that is used to differentiate a vendor's product modes/version. Default is 00000000.

		Returns:
			str
		"""
		return self._get_attribute('vendorSpecificInformation')
	@VendorSpecificInformation.setter
	def VendorSpecificInformation(self, value):
		self._set_attribute('vendorSpecificInformation', value)

	def update(self, EnableTlvOption=None, Enabled=None, IdleTimer=None, LinkEvents=None, Loopback=None, MacAddress=None, MaxOAMPDUSize=None, OrganizationUniqueIdentifier=None, TlvType=None, TlvValue=None, VendorSpecificInformation=None):
		"""Updates a child instance of oam on the server.

		Args:
			EnableTlvOption (bool): If true, enables the tlv option.
			Enabled (bool): If true, enables OAM for the Ten Gig Lan port.
			IdleTimer (number): The timer used to ensure OAM sub layer adheres to maximum number of OAMPDUs per second and emits at least one OAMPDU per second. The default is 1, minimum value is 1 and maximum value is 10.
			LinkEvents (bool): If true, enables link event interpreting support in Ixia port.
			Loopback (bool): If true, enables the loopback. when an ixia port goes to loopback mode, then all non oam packets coming to that port gets looped back.
			MacAddress (str): Mac address of the local DTE. By default, the mac address is automatically generated from card, port and other related information.
			MaxOAMPDUSize (number): Indicates the maximum OAMPDU size supported by local DTE. The default is 1500, minimum is 64, and maximum is 1500 in octets.
			OrganizationUniqueIdentifier (str): This three-octet field contains a 24-bit Organizationally Unique Identifier. The default value is 00-01-00. Any three octets hex value can be given.
			TlvType (str): Indicates the tlv type.
			TlvValue (str): Enters the tlv value.
			VendorSpecificInformation (str): Contains the vendor specific information that is used to differentiate a vendor's product modes/version. Default is 00000000.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
