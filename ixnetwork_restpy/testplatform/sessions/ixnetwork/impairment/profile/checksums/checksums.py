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


class Checksums(Base):
	"""Checksum handling for both incoming and outgoing packets.
	The Checksums class encapsulates a required checksums resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'checksums'

	def __init__(self, parent):
		super(Checksums, self).__init__(parent)

	@property
	def AlwaysCorrectWhenModifying(self):
		"""If true, and one or more field modifiers are enabled on this profile, then always correct the L2 FCS, IPv4 header checksum, and checksums for protocols over IPv4/IPv6.

		Returns:
			bool
		"""
		return self._get_attribute('alwaysCorrectWhenModifying')
	@AlwaysCorrectWhenModifying.setter
	def AlwaysCorrectWhenModifying(self, value):
		self._set_attribute('alwaysCorrectWhenModifying', value)

	@property
	def CorrectTxChecksumOverIp(self):
		"""If true, correct the checksum for the following protocols over IPv4/IPv6: TCP, UDP, ICMP, IGMP, ICMPv6, MLD, PIM, OSPF, RSVP.

		Returns:
			bool
		"""
		return self._get_attribute('correctTxChecksumOverIp')
	@CorrectTxChecksumOverIp.setter
	def CorrectTxChecksumOverIp(self, value):
		self._set_attribute('correctTxChecksumOverIp', value)

	@property
	def CorrectTxIpv4Checksum(self):
		"""If true, correct the IPv4 header checksum in outgoing IPv4 packets.

		Returns:
			bool
		"""
		return self._get_attribute('correctTxIpv4Checksum')
	@CorrectTxIpv4Checksum.setter
	def CorrectTxIpv4Checksum(self, value):
		self._set_attribute('correctTxIpv4Checksum', value)

	@property
	def CorrectTxL2FcsErrors(self):
		"""If true, correct the L2 frame check sequence in outgoing packets.

		Returns:
			bool
		"""
		return self._get_attribute('correctTxL2FcsErrors')
	@CorrectTxL2FcsErrors.setter
	def CorrectTxL2FcsErrors(self, value):
		self._set_attribute('correctTxL2FcsErrors', value)

	@property
	def DropRxL2FcsErrors(self):
		"""If true, drop incoming packets with L2 frame check sequence errors.

		Returns:
			bool
		"""
		return self._get_attribute('dropRxL2FcsErrors')
	@DropRxL2FcsErrors.setter
	def DropRxL2FcsErrors(self, value):
		self._set_attribute('dropRxL2FcsErrors', value)

	def update(self, AlwaysCorrectWhenModifying=None, CorrectTxChecksumOverIp=None, CorrectTxIpv4Checksum=None, CorrectTxL2FcsErrors=None, DropRxL2FcsErrors=None):
		"""Updates a child instance of checksums on the server.

		Args:
			AlwaysCorrectWhenModifying (bool): If true, and one or more field modifiers are enabled on this profile, then always correct the L2 FCS, IPv4 header checksum, and checksums for protocols over IPv4/IPv6.
			CorrectTxChecksumOverIp (bool): If true, correct the checksum for the following protocols over IPv4/IPv6: TCP, UDP, ICMP, IGMP, ICMPv6, MLD, PIM, OSPF, RSVP.
			CorrectTxIpv4Checksum (bool): If true, correct the IPv4 header checksum in outgoing IPv4 packets.
			CorrectTxL2FcsErrors (bool): If true, correct the L2 frame check sequence in outgoing packets.
			DropRxL2FcsErrors (bool): If true, drop incoming packets with L2 frame check sequence errors.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
