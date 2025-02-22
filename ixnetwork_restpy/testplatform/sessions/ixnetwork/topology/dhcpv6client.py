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


class Dhcpv6client(Base):
	"""DHCPv6 Client protocol.
	The Dhcpv6client class encapsulates a list of dhcpv6client resources that is be managed by the user.
	A list of resources can be retrieved from the server using the Dhcpv6client.find() method.
	The list can be managed by the user by using the Dhcpv6client.add() and Dhcpv6client.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'dhcpv6client'

	def __init__(self, parent):
		super(Dhcpv6client, self).__init__(parent)

	@property
	def Bfdv6Interface(self):
		"""An instance of the Bfdv6Interface class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv6interface.Bfdv6Interface)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv6interface import Bfdv6Interface
		return Bfdv6Interface(self)

	@property
	def BgpIpv6Peer(self):
		"""An instance of the BgpIpv6Peer class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6peer.BgpIpv6Peer)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6peer import BgpIpv6Peer
		return BgpIpv6Peer(self)

	@property
	def Dhcp6Iana(self):
		"""An instance of the Dhcp6Iana class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana.Dhcp6Iana)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana import Dhcp6Iana
		return Dhcp6Iana(self)._select()

	@property
	def Dhcp6Iana1(self):
		"""An instance of the Dhcp6Iana1 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana1.Dhcp6Iana1)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana1 import Dhcp6Iana1
		return Dhcp6Iana1(self)._select()

	@property
	def Dhcp6Iana2(self):
		"""An instance of the Dhcp6Iana2 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana2.Dhcp6Iana2)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana2 import Dhcp6Iana2
		return Dhcp6Iana2(self)._select()

	@property
	def Dhcp6Iana3(self):
		"""An instance of the Dhcp6Iana3 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana3.Dhcp6Iana3)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana3 import Dhcp6Iana3
		return Dhcp6Iana3(self)._select()

	@property
	def Dhcp6Iana4(self):
		"""An instance of the Dhcp6Iana4 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana4.Dhcp6Iana4)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana4 import Dhcp6Iana4
		return Dhcp6Iana4(self)._select()

	@property
	def Dhcp6Iana5(self):
		"""An instance of the Dhcp6Iana5 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana5.Dhcp6Iana5)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana5 import Dhcp6Iana5
		return Dhcp6Iana5(self)._select()

	@property
	def Dhcp6Iana6(self):
		"""An instance of the Dhcp6Iana6 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana6.Dhcp6Iana6)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana6 import Dhcp6Iana6
		return Dhcp6Iana6(self)._select()

	@property
	def Dhcp6Iana7(self):
		"""An instance of the Dhcp6Iana7 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana7.Dhcp6Iana7)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iana7 import Dhcp6Iana7
		return Dhcp6Iana7(self)._select()

	@property
	def Dhcp6Iapd(self):
		"""An instance of the Dhcp6Iapd class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd.Dhcp6Iapd)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd import Dhcp6Iapd
		return Dhcp6Iapd(self)._select()

	@property
	def Dhcp6Iapd1(self):
		"""An instance of the Dhcp6Iapd1 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd1.Dhcp6Iapd1)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd1 import Dhcp6Iapd1
		return Dhcp6Iapd1(self)._select()

	@property
	def Dhcp6Iapd2(self):
		"""An instance of the Dhcp6Iapd2 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd2.Dhcp6Iapd2)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd2 import Dhcp6Iapd2
		return Dhcp6Iapd2(self)._select()

	@property
	def Dhcp6Iapd3(self):
		"""An instance of the Dhcp6Iapd3 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd3.Dhcp6Iapd3)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd3 import Dhcp6Iapd3
		return Dhcp6Iapd3(self)._select()

	@property
	def Dhcp6Iapd4(self):
		"""An instance of the Dhcp6Iapd4 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd4.Dhcp6Iapd4)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd4 import Dhcp6Iapd4
		return Dhcp6Iapd4(self)._select()

	@property
	def Dhcp6Iapd5(self):
		"""An instance of the Dhcp6Iapd5 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd5.Dhcp6Iapd5)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd5 import Dhcp6Iapd5
		return Dhcp6Iapd5(self)._select()

	@property
	def Dhcp6Iapd6(self):
		"""An instance of the Dhcp6Iapd6 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd6.Dhcp6Iapd6)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd6 import Dhcp6Iapd6
		return Dhcp6Iapd6(self)._select()

	@property
	def Dhcp6Iapd7(self):
		"""An instance of the Dhcp6Iapd7 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd7.Dhcp6Iapd7)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6iapd7 import Dhcp6Iapd7
		return Dhcp6Iapd7(self)._select()

	@property
	def Dhcp6LearnedInfo(self):
		"""An instance of the Dhcp6LearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6learnedinfo.Dhcp6LearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcp6learnedinfo import Dhcp6LearnedInfo
		return Dhcp6LearnedInfo(self)._select()

	@property
	def MldHost(self):
		"""An instance of the MldHost class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldhost.MldHost)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldhost import MldHost
		return MldHost(self)

	@property
	def MldQuerier(self):
		"""An instance of the MldQuerier class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldquerier.MldQuerier)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mldquerier import MldQuerier
		return MldQuerier(self)

	@property
	def Ospfv3(self):
		"""An instance of the Ospfv3 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3.Ospfv3)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3 import Ospfv3
		return Ospfv3(self)

	@property
	def PimV6Interface(self):
		"""An instance of the PimV6Interface class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv6interface.PimV6Interface)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv6interface import PimV6Interface
		return PimV6Interface(self)

	@property
	def Tag(self):
		"""An instance of the Tag class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag.Tag)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag import Tag
		return Tag(self)

	@property
	def TlvProfile(self):
		"""An instance of the TlvProfile class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile.TlvProfile)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.tlvprofile import TlvProfile
		return TlvProfile(self)

	@property
	def Vxlanv6(self):
		"""An instance of the Vxlanv6 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlanv6.Vxlanv6)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlanv6 import Vxlanv6
		return Vxlanv6(self)

	@property
	def ComputedIapdAddresses(self):
		"""The computed IPv6 addresses.

		Returns:
			list(str)
		"""
		return self._get_attribute('computedIapdAddresses')

	@property
	def ConnectedVia(self):
		"""DEPRECATED List of layers this layer used to connect to the wire

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])
		"""
		return self._get_attribute('connectedVia')
	@ConnectedVia.setter
	def ConnectedVia(self, value):
		self._set_attribute('connectedVia', value)

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def CustomLinkLocalAddress(self):
		"""Configures the Manual Link-Local IPv6 Address for the DHCPv6 Client.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('customLinkLocalAddress')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def Dhcp6DuidEnterpriseId(self):
		"""The enterprise-number is the vendor's registered Private Enterprise Number as maintained by IANA.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('dhcp6DuidEnterpriseId')

	@property
	def Dhcp6DuidType(self):
		"""DHCP Unique Identifier Type.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('dhcp6DuidType')

	@property
	def Dhcp6DuidVendorId(self):
		"""The vendor-assigned unique ID for this range. This ID is incremented automaticaly for each DHCP client.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('dhcp6DuidVendorId')

	@property
	def Dhcp6GatewayAddress(self):
		"""Configures the Manual Gateway IPv6 Address for the DHCPv6 Client.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('dhcp6GatewayAddress')

	@property
	def Dhcp6GatewayMac(self):
		"""Configures the Manual Gateway MAC corresponding to the configured Manual Gateway IP of the DHCPv6 Client session.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('dhcp6GatewayMac')

	@property
	def Dhcp6IANACount(self):
		"""Number of IANA options to be included in a negotiation. This value must be smaller than Maximum Leases per Client.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('dhcp6IANACount')

	@property
	def Dhcp6IAPDCount(self):
		"""Number of IAPD options to be included in a negotiation. This value must be smaller than Maximum Leases per Client.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('dhcp6IAPDCount')

	@property
	def Dhcp6IaId(self):
		"""The identity association unique ID for this range.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('dhcp6IaId')

	@property
	def Dhcp6IaIdInc(self):
		"""Increment step for each IAID in a multiple IANA/IAPD case.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('dhcp6IaIdInc')

	@property
	def Dhcp6IaT1(self):
		"""The suggested time at which the client contacts the server from which the addresses were obtained to extend the lifetimes of the addresses assigned.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('dhcp6IaT1')

	@property
	def Dhcp6IaT2(self):
		"""The suggested time at which the client contacts any available server to extend the lifetimes of the addresses assigned.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('dhcp6IaT2')

	@property
	def Dhcp6IaType(self):
		"""Identity Association Type.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('dhcp6IaType')

	@property
	def Dhcp6UsePDGlobalAddress(self):
		"""Use DHCPc6-PD global addressing.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('dhcp6UsePDGlobalAddress')

	@property
	def DiscoveredAddresses(self):
		"""The discovered IPv6 addresses.

		Returns:
			list(str)
		"""
		return self._get_attribute('discoveredAddresses')

	@property
	def DiscoveredGateways(self):
		"""The discovered gateway IPv6 addresses.

		Returns:
			list(str)
		"""
		return self._get_attribute('discoveredGateways')

	@property
	def DiscoveredPrefix(self):
		"""The discovered IPv6 prefix.

		Returns:
			list(str)
		"""
		return self._get_attribute('discoveredPrefix')

	@property
	def DiscoveredPrefixLength(self):
		"""The length of the discovered IPv6 prefix.

		Returns:
			list(number)
		"""
		return self._get_attribute('discoveredPrefixLength')

	@property
	def EnableStateless(self):
		"""Enables DHCP stateless.

		Returns:
			bool
		"""
		return self._get_attribute('enableStateless')
	@EnableStateless.setter
	def EnableStateless(self, value):
		self._set_attribute('enableStateless', value)

	@property
	def Errors(self):
		"""A list of errors that have occurred

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
		"""
		return self._get_attribute('errors')

	@property
	def MaxNoPerClient(self):
		"""Maximum number of Addresses/Prefixes accepted by a Client in a negotiation.

		Returns:
			number
		"""
		return self._get_attribute('maxNoPerClient')
	@MaxNoPerClient.setter
	def MaxNoPerClient(self, value):
		self._set_attribute('maxNoPerClient', value)

	@property
	def Multiplier(self):
		"""Number of layer instances per parent instance (multiplier)

		Returns:
			number
		"""
		return self._get_attribute('multiplier')
	@Multiplier.setter
	def Multiplier(self, value):
		self._set_attribute('multiplier', value)

	@property
	def Name(self):
		"""Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	@property
	def NoOfAddresses(self):
		"""Number of Negotiated Addresses.

		Returns:
			list(number)
		"""
		return self._get_attribute('noOfAddresses')

	@property
	def NoOfPrefixes(self):
		"""Number of Negotiated Addresses.

		Returns:
			list(number)
		"""
		return self._get_attribute('noOfPrefixes')

	@property
	def RenewTimer(self):
		"""The used-defined lease renewal timer. The value is estimated in seconds and will override the lease renewal timer if it is not zero and is smaller than server-defined value.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('renewTimer')

	@property
	def SessionInfo(self):
		"""Logs additional information about the session state

		Returns:
			list(str[duidNak|excessiveTlvs|noAddrsAvail|noAddrsBelow|none|noPrefixAvail|nsFailed|partiallyNegotiated|rebindTimeout|relayDown|renewTimeout|requestTimeout|solicitTimeout])
		"""
		return self._get_attribute('sessionInfo')

	@property
	def SessionStatus(self):
		"""Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.

		Returns:
			list(str[down|notStarted|up])
		"""
		return self._get_attribute('sessionStatus')

	@property
	def StackedLayers(self):
		"""List of secondary (many to one) child layer protocols

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])
		"""
		return self._get_attribute('stackedLayers')
	@StackedLayers.setter
	def StackedLayers(self, value):
		self._set_attribute('stackedLayers', value)

	@property
	def StateCounts(self):
		"""A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up

		Returns:
			dict(total:number,notStarted:number,down:number,up:number)
		"""
		return self._get_attribute('stateCounts')

	@property
	def Status(self):
		"""Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			str(configured|error|mixed|notStarted|started|starting|stopping)
		"""
		return self._get_attribute('status')

	@property
	def UseCustomLinkLocalAddress(self):
		"""Enables users to manually set non-EUI link local addresses

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('useCustomLinkLocalAddress')

	@property
	def UseRapidCommit(self):
		"""Enables DHCP clients to negotiate leases with rapid commit.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('useRapidCommit')

	def update(self, ConnectedVia=None, EnableStateless=None, MaxNoPerClient=None, Multiplier=None, Name=None, StackedLayers=None):
		"""Updates a child instance of dhcpv6client on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			EnableStateless (bool): Enables DHCP stateless.
			MaxNoPerClient (number): Maximum number of Addresses/Prefixes accepted by a Client in a negotiation.
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, ConnectedVia=None, EnableStateless=None, MaxNoPerClient=None, Multiplier=None, Name=None, StackedLayers=None):
		"""Adds a new dhcpv6client node on the server and retrieves it in this instance.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			EnableStateless (bool): Enables DHCP stateless.
			MaxNoPerClient (number): Maximum number of Addresses/Prefixes accepted by a Client in a negotiation.
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			self: This instance with all currently retrieved dhcpv6client data using find and the newly added dhcpv6client data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the dhcpv6client data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, ComputedIapdAddresses=None, ConnectedVia=None, Count=None, DescriptiveName=None, DiscoveredAddresses=None, DiscoveredGateways=None, DiscoveredPrefix=None, DiscoveredPrefixLength=None, EnableStateless=None, Errors=None, MaxNoPerClient=None, Multiplier=None, Name=None, NoOfAddresses=None, NoOfPrefixes=None, SessionInfo=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
		"""Finds and retrieves dhcpv6client data from the server.

		All named parameters support regex and can be used to selectively retrieve dhcpv6client data from the server.
		By default the find method takes no parameters and will retrieve all dhcpv6client data from the server.

		Args:
			ComputedIapdAddresses (list(str)): The computed IPv6 addresses.
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
			DiscoveredAddresses (list(str)): The discovered IPv6 addresses.
			DiscoveredGateways (list(str)): The discovered gateway IPv6 addresses.
			DiscoveredPrefix (list(str)): The discovered IPv6 prefix.
			DiscoveredPrefixLength (list(number)): The length of the discovered IPv6 prefix.
			EnableStateless (bool): Enables DHCP stateless.
			Errors (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))): A list of errors that have occurred
			MaxNoPerClient (number): Maximum number of Addresses/Prefixes accepted by a Client in a negotiation.
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfAddresses (list(number)): Number of Negotiated Addresses.
			NoOfPrefixes (list(number)): Number of Negotiated Addresses.
			SessionInfo (list(str[duidNak|excessiveTlvs|noAddrsAvail|noAddrsBelow|none|noPrefixAvail|nsFailed|partiallyNegotiated|rebindTimeout|relayDown|renewTimeout|requestTimeout|solicitTimeout])): Logs additional information about the session state
			SessionStatus (list(str[down|notStarted|up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			self: This instance with matching dhcpv6client data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of dhcpv6client data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the dhcpv6client data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, CustomLinkLocalAddress=None, Dhcp6DuidEnterpriseId=None, Dhcp6DuidType=None, Dhcp6DuidVendorId=None, Dhcp6GatewayAddress=None, Dhcp6GatewayMac=None, Dhcp6IANACount=None, Dhcp6IAPDCount=None, Dhcp6IaId=None, Dhcp6IaIdInc=None, Dhcp6IaT1=None, Dhcp6IaT2=None, Dhcp6IaType=None, Dhcp6UsePDGlobalAddress=None, RenewTimer=None, UseCustomLinkLocalAddress=None, UseRapidCommit=None):
		"""Base class infrastructure that gets a list of dhcpv6client device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			CustomLinkLocalAddress (str): optional regex of customLinkLocalAddress
			Dhcp6DuidEnterpriseId (str): optional regex of dhcp6DuidEnterpriseId
			Dhcp6DuidType (str): optional regex of dhcp6DuidType
			Dhcp6DuidVendorId (str): optional regex of dhcp6DuidVendorId
			Dhcp6GatewayAddress (str): optional regex of dhcp6GatewayAddress
			Dhcp6GatewayMac (str): optional regex of dhcp6GatewayMac
			Dhcp6IANACount (str): optional regex of dhcp6IANACount
			Dhcp6IAPDCount (str): optional regex of dhcp6IAPDCount
			Dhcp6IaId (str): optional regex of dhcp6IaId
			Dhcp6IaIdInc (str): optional regex of dhcp6IaIdInc
			Dhcp6IaT1 (str): optional regex of dhcp6IaT1
			Dhcp6IaT2 (str): optional regex of dhcp6IaT2
			Dhcp6IaType (str): optional regex of dhcp6IaType
			Dhcp6UsePDGlobalAddress (str): optional regex of dhcp6UsePDGlobalAddress
			RenewTimer (str): optional regex of renewTimer
			UseCustomLinkLocalAddress (str): optional regex of useCustomLinkLocalAddress
			UseRapidCommit (str): optional regex of useRapidCommit

		Returns:
			list(int): A list of device ids that meets the regex criteria provided in the method parameters

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._get_ngpf_device_ids(locals())

	def Rebind(self, *args, **kwargs):
		"""Executes the rebind operation on the server.

		Rebind selected DHCPv6 items.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		rebind()

		rebind(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		rebind(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('rebind', payload=payload, response_object=None)

	def Renew(self, *args, **kwargs):
		"""Executes the renew operation on the server.

		Renew selected DHCPv6 items.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		renew()

		renew(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		renew(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('renew', payload=payload, response_object=None)

	def RestartDown(self, *args, **kwargs):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions that are in Down state.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		restartDown()

		restartDown(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		restartDown(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('restartDown', payload=payload, response_object=None)

	def SendPing(self, *args, **kwargs):
		"""Executes the sendPing operation on the server.

		Send ping for selected DHCPv6 items.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		sendPing(DestIP:string)list
			Args:
				args[0] is DestIP (str): This parameter requires a destIP of type kString

			Returns:
				list(dict(port:str[None|/api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

		sendPing(DestIP:string, SessionIndices:list)list
			Args:
				args[0] is DestIP (str): This parameter requires a destIP of type kString
				args[1] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

			Returns:
				list(dict(port:str[None|/api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

		sendPing(SessionIndices:string, DestIP:string)list
			Args:
				args[0] is SessionIndices (str): This parameter requires a destIP of type kString
				args[1] is DestIP (str): This parameter requires a string of session numbers 1-4;6;7-12

			Returns:
				list(dict(port:str[None|/api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendPing', payload=payload, response_object=None)

	def Start(self, *args, **kwargs):
		"""Executes the start operation on the server.

		Start selected protocols.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		start()

		start(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		start(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('start', payload=payload, response_object=None)

	def Stop(self, *args, **kwargs):
		"""Executes the stop operation on the server.

		Stop selected protocols.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		stop()

		stop(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		stop(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('stop', payload=payload, response_object=None)
