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


class DhcpV6DiscoveredInfo(Base):
	"""The Dynamic Host Configuration Protocol Version 6 (DHCPv6) Discovered Information is based on RFC 3315. When the protocol interface is set for DHCPv6 and enabled, DHCPv6 negotiations will be started.
	The DhcpV6DiscoveredInfo class encapsulates a required dhcpV6DiscoveredInfo resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'dhcpV6DiscoveredInfo'

	def __init__(self, parent):
		super(DhcpV6DiscoveredInfo, self).__init__(parent)

	@property
	def IaRebindTime(self):
		"""(Read Only) The rebind timer value (in seconds) specified by the DHCPv6 Server.

		Returns:
			number
		"""
		return self._get_attribute('iaRebindTime')

	@property
	def IaRenewTime(self):
		"""(Read Only) The renew timer value (in seconds) specified by the DHCPv6 Server.

		Returns:
			number
		"""
		return self._get_attribute('iaRenewTime')

	@property
	def Ipv6Address(self):
		"""(Read Only) A learned/allocated IPv6 address for this interface.

		Returns:
			list(str)
		"""
		return self._get_attribute('ipv6Address')

	@property
	def IsDhcpV6LearnedInfoRefreshed(self):
		"""(Read Only) When true, the DHCPv6 discovered information is refreshed automatically.

		Returns:
			bool
		"""
		return self._get_attribute('isDhcpV6LearnedInfoRefreshed')

	@property
	def ProtocolInterface(self):
		"""(Read Only) An Ixia protocol interface that is negotiating with the DHCPv6 Server.

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=interface)
		"""
		return self._get_attribute('protocolInterface')

	@property
	def Tlvs(self):
		"""(Read Only) The identifier or 'tag' for this DHCPv6 option. The DHCPv6 option value field may contain data for configuration parameter information.

		Returns:
			list(dict(arg1:number,arg2:str))
		"""
		return self._get_attribute('tlvs')
