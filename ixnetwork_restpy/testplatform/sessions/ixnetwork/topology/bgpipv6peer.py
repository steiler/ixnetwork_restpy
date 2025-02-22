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


class BgpIpv6Peer(Base):
	"""Bgp IPv6 Peer
	The BgpIpv6Peer class encapsulates a list of bgpIpv6Peer resources that is be managed by the user.
	A list of resources can be retrieved from the server using the BgpIpv6Peer.find() method.
	The list can be managed by the user by using the BgpIpv6Peer.add() and BgpIpv6Peer.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'bgpIpv6Peer'

	def __init__(self, parent):
		super(BgpIpv6Peer, self).__init__(parent)

	@property
	def BgpCustomAfiSafiv6(self):
		"""An instance of the BgpCustomAfiSafiv6 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpcustomafisafiv6.BgpCustomAfiSafiv6)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpcustomafisafiv6 import BgpCustomAfiSafiv6
		return BgpCustomAfiSafiv6(self)._select()

	@property
	def BgpEpePeerList(self):
		"""An instance of the BgpEpePeerList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpepepeerlist.BgpEpePeerList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpepepeerlist import BgpEpePeerList
		return BgpEpePeerList(self)._select()

	@property
	def BgpEthernetSegmentV6(self):
		"""An instance of the BgpEthernetSegmentV6 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpethernetsegmentv6.BgpEthernetSegmentV6)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpethernetsegmentv6 import BgpEthernetSegmentV6
		return BgpEthernetSegmentV6(self)._select()

	@property
	def BgpFlowSpecRangesList(self):
		"""An instance of the BgpFlowSpecRangesList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpflowspecrangeslist.BgpFlowSpecRangesList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpflowspecrangeslist import BgpFlowSpecRangesList
		return BgpFlowSpecRangesList(self)._select()

	@property
	def BgpFlowSpecRangesListV4(self):
		"""An instance of the BgpFlowSpecRangesListV4 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpflowspecrangeslistv4.BgpFlowSpecRangesListV4)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpflowspecrangeslistv4 import BgpFlowSpecRangesListV4
		return BgpFlowSpecRangesListV4(self)._select()

	@property
	def BgpFlowSpecRangesListV6(self):
		"""An instance of the BgpFlowSpecRangesListV6 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpflowspecrangeslistv6.BgpFlowSpecRangesListV6)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpflowspecrangeslistv6 import BgpFlowSpecRangesListV6
		return BgpFlowSpecRangesListV6(self)._select()

	@property
	def BgpIPv6EvpnEvi(self):
		"""An instance of the BgpIPv6EvpnEvi class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnevi.BgpIPv6EvpnEvi)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnevi import BgpIPv6EvpnEvi
		return BgpIPv6EvpnEvi(self)

	@property
	def BgpIPv6EvpnPbb(self):
		"""An instance of the BgpIPv6EvpnPbb class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnpbb.BgpIPv6EvpnPbb)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnpbb import BgpIPv6EvpnPbb
		return BgpIPv6EvpnPbb(self)

	@property
	def BgpIPv6EvpnVXLAN(self):
		"""An instance of the BgpIPv6EvpnVXLAN class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnvxlan.BgpIPv6EvpnVXLAN)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnvxlan import BgpIPv6EvpnVXLAN
		return BgpIPv6EvpnVXLAN(self)

	@property
	def BgpIPv6EvpnVXLANVpws(self):
		"""An instance of the BgpIPv6EvpnVXLANVpws class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnvxlanvpws.BgpIPv6EvpnVXLANVpws)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnvxlanvpws import BgpIPv6EvpnVXLANVpws
		return BgpIPv6EvpnVXLANVpws(self)

	@property
	def BgpIPv6EvpnVpws(self):
		"""An instance of the BgpIPv6EvpnVpws class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnvpws.BgpIPv6EvpnVpws)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6evpnvpws import BgpIPv6EvpnVpws
		return BgpIPv6EvpnVpws(self)

	@property
	def BgpIpv6AdL2Vpn(self):
		"""An instance of the BgpIpv6AdL2Vpn class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6adl2vpn.BgpIpv6AdL2Vpn)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6adl2vpn import BgpIpv6AdL2Vpn
		return BgpIpv6AdL2Vpn(self)

	@property
	def BgpIpv6L2Site(self):
		"""An instance of the BgpIpv6L2Site class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6l2site.BgpIpv6L2Site)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6l2site import BgpIpv6L2Site
		return BgpIpv6L2Site(self)

	@property
	def BgpIpv6MVrf(self):
		"""An instance of the BgpIpv6MVrf class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6mvrf.BgpIpv6MVrf)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv6mvrf import BgpIpv6MVrf
		return BgpIpv6MVrf(self)

	@property
	def BgpLsAsPathSegmentList(self):
		"""An instance of the BgpLsAsPathSegmentList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplsaspathsegmentlist.BgpLsAsPathSegmentList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplsaspathsegmentlist import BgpLsAsPathSegmentList
		return BgpLsAsPathSegmentList(self)

	@property
	def BgpLsClusterIdList(self):
		"""An instance of the BgpLsClusterIdList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplsclusteridlist.BgpLsClusterIdList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplsclusteridlist import BgpLsClusterIdList
		return BgpLsClusterIdList(self)

	@property
	def BgpLsCommunitiesList(self):
		"""An instance of the BgpLsCommunitiesList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplscommunitieslist.BgpLsCommunitiesList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplscommunitieslist import BgpLsCommunitiesList
		return BgpLsCommunitiesList(self)

	@property
	def BgpLsExtendedCommunitiesList(self):
		"""An instance of the BgpLsExtendedCommunitiesList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplsextendedcommunitieslist.BgpLsExtendedCommunitiesList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgplsextendedcommunitieslist import BgpLsExtendedCommunitiesList
		return BgpLsExtendedCommunitiesList(self)

	@property
	def BgpSRGBRangeSubObjectsList(self):
		"""An instance of the BgpSRGBRangeSubObjectsList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpsrgbrangesubobjectslist.BgpSRGBRangeSubObjectsList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpsrgbrangesubobjectslist import BgpSRGBRangeSubObjectsList
		return BgpSRGBRangeSubObjectsList(self)

	@property
	def BgpSRTEPoliciesListV6(self):
		"""An instance of the BgpSRTEPoliciesListV6 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpsrtepolicieslistv6.BgpSRTEPoliciesListV6)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpsrtepolicieslistv6 import BgpSRTEPoliciesListV6
		return BgpSRTEPoliciesListV6(self)._select()

	@property
	def BgpV6Vrf(self):
		"""An instance of the BgpV6Vrf class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpv6vrf.BgpV6Vrf)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpv6vrf import BgpV6Vrf
		return BgpV6Vrf(self)

	@property
	def Connector(self):
		"""An instance of the Connector class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector.Connector)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector import Connector
		return Connector(self)

	@property
	def LearnedInfo(self):
		"""An instance of the LearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo.LearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo import LearnedInfo
		return LearnedInfo(self)

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
	def ActAsRestarted(self):
		"""Act as restarted

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('actAsRestarted')

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def AdvSrv6SidInIgp(self):
		"""Advertise SRv6 SID in IGP

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('advSrv6SidInIgp')

	@property
	def AdvertiseEndOfRib(self):
		"""Advertise End-Of-RIB

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('advertiseEndOfRib')

	@property
	def AdvertiseEvpnRoutesForOtherVtep(self):
		"""Advertise EVPN routes for other VTEPS

		Returns:
			bool
		"""
		return self._get_attribute('advertiseEvpnRoutesForOtherVtep')
	@AdvertiseEvpnRoutesForOtherVtep.setter
	def AdvertiseEvpnRoutesForOtherVtep(self, value):
		self._set_attribute('advertiseEvpnRoutesForOtherVtep', value)

	@property
	def AdvertiseSRv6SID(self):
		"""Advertise SRv6 SID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('advertiseSRv6SID')

	@property
	def AdvertiseTunnelEncapsulationExtendedCommunity(self):
		"""Advertise Tunnel Encapsulation Extended Community

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('advertiseTunnelEncapsulationExtendedCommunity')

	@property
	def AlwaysIncludeTunnelEncExtCommunity(self):
		"""Always Include Tunnel Encapsulation Extended Community

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('alwaysIncludeTunnelEncExtCommunity')

	@property
	def AsSetMode(self):
		"""AS# Set Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('asSetMode')

	@property
	def Authentication(self):
		"""Authentication Type

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('authentication')

	@property
	def AutoGenSegmentLeftValue(self):
		"""If enabled then Segment Left field value will be auto generated

		Returns:
			bool
		"""
		return self._get_attribute('autoGenSegmentLeftValue')
	@AutoGenSegmentLeftValue.setter
	def AutoGenSegmentLeftValue(self, value):
		self._set_attribute('autoGenSegmentLeftValue', value)

	@property
	def BgpFsmState(self):
		"""Logs additional information about the BGP Peer State

		Returns:
			list(str[active|connect|error|established|idle|none|openConfirm|openSent])
		"""
		return self._get_attribute('bgpFsmState')

	@property
	def BgpId(self):
		"""BGP ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bgpId')

	@property
	def BgpLsAsSetMode(self):
		"""AS# Set Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bgpLsAsSetMode')

	@property
	def BgpLsEnableAsPathSegments(self):
		"""Enable AS Path Segments

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bgpLsEnableAsPathSegments')

	@property
	def BgpLsEnableCluster(self):
		"""Enable Cluster

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bgpLsEnableCluster')

	@property
	def BgpLsEnableExtendedCommunity(self):
		"""Enable Extended Community

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bgpLsEnableExtendedCommunity')

	@property
	def BgpLsNoOfASPathSegments(self):
		"""Number Of AS Path Segments Per Route Range

		Returns:
			number
		"""
		return self._get_attribute('bgpLsNoOfASPathSegments')
	@BgpLsNoOfASPathSegments.setter
	def BgpLsNoOfASPathSegments(self, value):
		self._set_attribute('bgpLsNoOfASPathSegments', value)

	@property
	def BgpLsNoOfClusters(self):
		"""Number of Clusters

		Returns:
			number
		"""
		return self._get_attribute('bgpLsNoOfClusters')
	@BgpLsNoOfClusters.setter
	def BgpLsNoOfClusters(self, value):
		self._set_attribute('bgpLsNoOfClusters', value)

	@property
	def BgpLsNoOfCommunities(self):
		"""Number of Communities

		Returns:
			number
		"""
		return self._get_attribute('bgpLsNoOfCommunities')
	@BgpLsNoOfCommunities.setter
	def BgpLsNoOfCommunities(self, value):
		self._set_attribute('bgpLsNoOfCommunities', value)

	@property
	def BgpLsOverridePeerAsSetMode(self):
		"""Override Peer AS# Set Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bgpLsOverridePeerAsSetMode')

	@property
	def CapabilityIpV4Mdt(self):
		"""IPv4 BGP MDT: AFI = 1, SAFI = 66

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpV4Mdt')

	@property
	def CapabilityIpV4Mpls(self):
		"""DEPRECATED IPv4 MPLS

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpV4Mpls')

	@property
	def CapabilityIpV4MplsVpn(self):
		"""IPv4 MPLS VPN Capability: AFI=1,SAFI=128

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpV4MplsVpn')

	@property
	def CapabilityIpV4Multicast(self):
		"""IPv4 Multicast Capability: AFI=1,SAFI=2

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpV4Multicast')

	@property
	def CapabilityIpV4MulticastVpn(self):
		"""IP MCAST-VPN: AFI = 1, SAFI = 5

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpV4MulticastVpn')

	@property
	def CapabilityIpV4Unicast(self):
		"""IPv4 Unicast Capability: AFI=1,SAFI=1

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpV4Unicast')

	@property
	def CapabilityIpV6Mpls(self):
		"""DEPRECATED IPv6 MPLS

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpV6Mpls')

	@property
	def CapabilityIpV6MplsVpn(self):
		"""IPv6 MPLS VPN Capability: AFI=2,SAFI=128

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpV6MplsVpn')

	@property
	def CapabilityIpV6Multicast(self):
		"""IPv6 Multicast Capability: AFI=2,SAFI=2

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpV6Multicast')

	@property
	def CapabilityIpV6MulticastVpn(self):
		"""IP6 MCAST-VPN: AFI = 2, SAFI = 5

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpV6MulticastVpn')

	@property
	def CapabilityIpV6Unicast(self):
		"""IPv6 Unicast Capability: AFI=2,SAFI=1

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpV6Unicast')

	@property
	def CapabilityIpv4MplsAddPath(self):
		"""IPv4 MPLS Add Path Capability

		Returns:
			bool
		"""
		return self._get_attribute('capabilityIpv4MplsAddPath')
	@CapabilityIpv4MplsAddPath.setter
	def CapabilityIpv4MplsAddPath(self, value):
		self._set_attribute('capabilityIpv4MplsAddPath', value)

	@property
	def CapabilityIpv4UnicastAddPath(self):
		"""Check box for IPv4 Unicast Add Path

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpv4UnicastAddPath')

	@property
	def CapabilityIpv6MplsAddPath(self):
		"""IPv6 MPLS Add Path Capability

		Returns:
			bool
		"""
		return self._get_attribute('capabilityIpv6MplsAddPath')
	@CapabilityIpv6MplsAddPath.setter
	def CapabilityIpv6MplsAddPath(self, value):
		self._set_attribute('capabilityIpv6MplsAddPath', value)

	@property
	def CapabilityIpv6UnicastAddPath(self):
		"""Check box for IPv6 Unicast Add Path

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityIpv6UnicastAddPath')

	@property
	def CapabilityLinkStateNonVpn(self):
		"""Link State Non-VPN Capability: AFI=16388,SAFI=71

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityLinkStateNonVpn')

	@property
	def CapabilityNHEncodingCapabilities(self):
		"""Extended Next Hop Encoding Capability which needs to be used when advertising IPv4 or VPN-IPv4 routes over IPv6 Core

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityNHEncodingCapabilities')

	@property
	def CapabilityRouteConstraint(self):
		"""Route Constraint Capability: AFI=1,SAFI=132

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityRouteConstraint')

	@property
	def CapabilityRouteRefresh(self):
		"""Route Refresh

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityRouteRefresh')

	@property
	def CapabilitySRTEPoliciesV4(self):
		"""IPv4 SR TE Policy Capability: AFI=1,SAFI=73

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilitySRTEPoliciesV4')

	@property
	def CapabilitySRTEPoliciesV6(self):
		"""IPv6 SR TE Policy Capability: AFI=2,SAFI=73

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilitySRTEPoliciesV6')

	@property
	def CapabilityVpls(self):
		"""VPLS Capability: AFI = 25, SAFI = 65

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityVpls')

	@property
	def Capabilityipv4UnicastFlowSpec(self):
		"""IPv4 Unicast Flow Spec Capability: AFI=1,SAFI=133

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityipv4UnicastFlowSpec')

	@property
	def Capabilityipv6UnicastFlowSpec(self):
		"""IPv6 Unicast Flow Spec Capability: AFI=2,SAFI=133

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('capabilityipv6UnicastFlowSpec')

	@property
	def ConfigureKeepaliveTimer(self):
		"""Configure Keepalive Timer

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('configureKeepaliveTimer')

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
	def CopyTtl(self):
		"""Copy TTL from customer packet to outer IPv6 header

		Returns:
			bool
		"""
		return self._get_attribute('copyTtl')
	@CopyTtl.setter
	def CopyTtl(self, value):
		self._set_attribute('copyTtl', value)

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def CustomSidType(self):
		"""moved to port data in bgp/srv6 Custom SID Type

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('customSidType')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def DiscardIxiaGeneratedRoutes(self):
		"""Discard Ixia Generated Routes

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('discardIxiaGeneratedRoutes')

	@property
	def DowntimeInSec(self):
		"""Downtime in Seconds

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('downtimeInSec')

	@property
	def DutIp(self):
		"""DUT IP

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('dutIp')

	@property
	def EnSRv6DataPlane(self):
		"""Ingress Peer Supports SRv6 VPN

		Returns:
			bool
		"""
		return self._get_attribute('enSRv6DataPlane')
	@EnSRv6DataPlane.setter
	def EnSRv6DataPlane(self, value):
		self._set_attribute('enSRv6DataPlane', value)

	@property
	def Enable4ByteAs(self):
		"""Enable 4-Byte AS

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enable4ByteAs')

	@property
	def EnableBfdRegistration(self):
		"""Enable BFD Registration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableBfdRegistration')

	@property
	def EnableBgpId(self):
		"""Enable BGP ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableBgpId')

	@property
	def EnableBgpIdSameAsRouterId(self):
		"""BGP ID Same as Router ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableBgpIdSameAsRouterId')

	@property
	def EnableBgpLsCommunity(self):
		"""Enable Community

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableBgpLsCommunity')

	@property
	def EnableEpeTraffic(self):
		"""Enable EPE Traffic

		Returns:
			bool
		"""
		return self._get_attribute('enableEpeTraffic')
	@EnableEpeTraffic.setter
	def EnableEpeTraffic(self, value):
		self._set_attribute('enableEpeTraffic', value)

	@property
	def EnableGracefulRestart(self):
		"""Enable Graceful Restart

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableGracefulRestart')

	@property
	def EnableLlgr(self):
		"""Enable LLGR

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableLlgr')

	@property
	def EnableReducedEncapsulation(self):
		"""Enable Reduced Encapsulation in Data-Plane for SRv6

		Returns:
			bool
		"""
		return self._get_attribute('enableReducedEncapsulation')
	@EnableReducedEncapsulation.setter
	def EnableReducedEncapsulation(self, value):
		self._set_attribute('enableReducedEncapsulation', value)

	@property
	def Errors(self):
		"""A list of errors that have occurred

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
		"""
		return self._get_attribute('errors')

	@property
	def EthernetSegmentsCountV6(self):
		"""Number of Ethernet Segments

		Returns:
			number
		"""
		return self._get_attribute('ethernetSegmentsCountV6')
	@EthernetSegmentsCountV6.setter
	def EthernetSegmentsCountV6(self, value):
		self._set_attribute('ethernetSegmentsCountV6', value)

	@property
	def Evpn(self):
		"""EVPN Capability: AFI = 25, SAFI = 70

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('evpn')

	@property
	def FilterEvpn(self):
		"""Check box for EVPN filter

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterEvpn')

	@property
	def FilterIpV4Mpls(self):
		"""Filter IPv4 MPLS

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpV4Mpls')

	@property
	def FilterIpV4MplsVpn(self):
		"""Filter IPv4 MPLS VPN

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpV4MplsVpn')

	@property
	def FilterIpV4Multicast(self):
		"""Filter IPv4 Multicast

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpV4Multicast')

	@property
	def FilterIpV4MulticastVpn(self):
		"""Filter IPv4 Multicast VPN

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpV4MulticastVpn')

	@property
	def FilterIpV4Unicast(self):
		"""Filter IPv4 Unicast

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpV4Unicast')

	@property
	def FilterIpV6Mpls(self):
		"""Filter IPv6 MPLS

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpV6Mpls')

	@property
	def FilterIpV6MplsVpn(self):
		"""Filter IPv6 MPLS VPN

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpV6MplsVpn')

	@property
	def FilterIpV6Multicast(self):
		"""Filter IPv6 Multicast

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpV6Multicast')

	@property
	def FilterIpV6MulticastVpn(self):
		"""Filter IPv6 Multicast VPN

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpV6MulticastVpn')

	@property
	def FilterIpV6Unicast(self):
		"""Filter IPv6 Unicast

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpV6Unicast')

	@property
	def FilterIpv4MulticastBgpMplsVpn(self):
		"""Check box for IPv4 Multicast BGP/MPLS VPN filter

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpv4MulticastBgpMplsVpn')

	@property
	def FilterIpv4UnicastFlowSpec(self):
		"""Filter IPv4 Unicast Flow Spec

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpv4UnicastFlowSpec')

	@property
	def FilterIpv6MulticastBgpMplsVpn(self):
		"""Check box for IPv6 Multicast BGP/MPLS VPN filter

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpv6MulticastBgpMplsVpn')

	@property
	def FilterIpv6UnicastFlowSpec(self):
		"""Filter IPv6 Unicast Flow Spec

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterIpv6UnicastFlowSpec')

	@property
	def FilterLinkState(self):
		"""Filter Link State

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterLinkState')

	@property
	def FilterSRTEPoliciesV4(self):
		"""Enable IPv4 SR TE Policy Filter

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterSRTEPoliciesV4')

	@property
	def FilterSRTEPoliciesV6(self):
		"""Enable IPv6 SR TE Policy Filter

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterSRTEPoliciesV6')

	@property
	def FilterVpls(self):
		"""Filter VPLS

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('filterVpls')

	@property
	def Flap(self):
		"""Flap

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('flap')

	@property
	def HoldTimer(self):
		"""Hold Timer

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('holdTimer')

	@property
	def IpVrfToIpVrfType(self):
		"""IP-VRF-to-IP-VRF Model Type

		Returns:
			str(interfaceLess|interfacefullWithCorefacingIRB|interfacefullWithUnnumberedCorefacingIRB)
		"""
		return self._get_attribute('ipVrfToIpVrfType')
	@IpVrfToIpVrfType.setter
	def IpVrfToIpVrfType(self, value):
		self._set_attribute('ipVrfToIpVrfType', value)

	@property
	def Ipv4MplsAddPathMode(self):
		"""IPv4 MPLS Add Path Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv4MplsAddPathMode')

	@property
	def Ipv4MplsCapability(self):
		"""IPv4 MPLS Capability: AFI=1, SAFI=4

		Returns:
			bool
		"""
		return self._get_attribute('ipv4MplsCapability')
	@Ipv4MplsCapability.setter
	def Ipv4MplsCapability(self, value):
		self._set_attribute('ipv4MplsCapability', value)

	@property
	def Ipv4MulticastBgpMplsVpn(self):
		"""IP Multicast for BGP/MPLS IP VPN (UMH): AFI = 1, SAFI = 129

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv4MulticastBgpMplsVpn')

	@property
	def Ipv4MultipleMplsLabelsCapability(self):
		"""IPv4 Multiple MPLS Labels Capability: AFI=1, SAFI=4

		Returns:
			bool
		"""
		return self._get_attribute('ipv4MultipleMplsLabelsCapability')
	@Ipv4MultipleMplsLabelsCapability.setter
	def Ipv4MultipleMplsLabelsCapability(self, value):
		self._set_attribute('ipv4MultipleMplsLabelsCapability', value)

	@property
	def Ipv4UnicastAddPathMode(self):
		"""IPv4 Unicast Add Path Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv4UnicastAddPathMode')

	@property
	def Ipv6MplsAddPathMode(self):
		"""IPv6 MPLS Add Path Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6MplsAddPathMode')

	@property
	def Ipv6MplsCapability(self):
		"""IPv6 MPLS Capability: AFI=2, SAFI=4

		Returns:
			bool
		"""
		return self._get_attribute('ipv6MplsCapability')
	@Ipv6MplsCapability.setter
	def Ipv6MplsCapability(self, value):
		self._set_attribute('ipv6MplsCapability', value)

	@property
	def Ipv6MulticastBgpMplsVpn(self):
		"""IP6 Multicast for BGP/MPLS IP VPN (UMH): AFI = 2, SAFI = 129

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6MulticastBgpMplsVpn')

	@property
	def Ipv6MultipleMplsLabelsCapability(self):
		"""IPv6 Multiple MPLS Labels Capability: AFI=2, SAFI=4

		Returns:
			bool
		"""
		return self._get_attribute('ipv6MultipleMplsLabelsCapability')
	@Ipv6MultipleMplsLabelsCapability.setter
	def Ipv6MultipleMplsLabelsCapability(self, value):
		self._set_attribute('ipv6MultipleMplsLabelsCapability', value)

	@property
	def Ipv6UnicastAddPathMode(self):
		"""IPv6 Unicast Add Path Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6UnicastAddPathMode')

	@property
	def IrbInterfaceLabel(self):
		"""Label to be used for Route Type 2 carrying IRB MAC and/or IRB IP in Route Type 2

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('irbInterfaceLabel')

	@property
	def IrbIpv6Address(self):
		"""IRB IPv6 Address

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('irbIpv6Address')

	@property
	def KeepaliveTimer(self):
		"""Keepalive Timer

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('keepaliveTimer')

	@property
	def L3VPNEncapsulationType(self):
		"""L3VPN Traffic Encapsulation

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('l3VPNEncapsulationType')

	@property
	def LocalAs2Bytes(self):
		"""Local AS# (2-Bytes)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('localAs2Bytes')

	@property
	def LocalAs4Bytes(self):
		"""Local AS# (4-Bytes)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('localAs4Bytes')

	@property
	def LocalIpv6Ver2(self):
		"""Local IP

		Returns:
			list(str)
		"""
		return self._get_attribute('localIpv6Ver2')

	@property
	def LocalRouterID(self):
		"""Router ID

		Returns:
			list(str)
		"""
		return self._get_attribute('localRouterID')

	@property
	def MaxSidPerSrh(self):
		"""Max number of SIDs a SRH can have

		Returns:
			number
		"""
		return self._get_attribute('maxSidPerSrh')
	@MaxSidPerSrh.setter
	def MaxSidPerSrh(self, value):
		self._set_attribute('maxSidPerSrh', value)

	@property
	def Md5Key(self):
		"""MD5 Key

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('md5Key')

	@property
	def ModeOfBfdOperations(self):
		"""Mode of BFD Operations

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('modeOfBfdOperations')

	@property
	def MplsLabelsCountForIpv4MplsRoute(self):
		"""MPLS Labels Count For IPv4 MPLS Route

		Returns:
			number
		"""
		return self._get_attribute('mplsLabelsCountForIpv4MplsRoute')
	@MplsLabelsCountForIpv4MplsRoute.setter
	def MplsLabelsCountForIpv4MplsRoute(self, value):
		self._set_attribute('mplsLabelsCountForIpv4MplsRoute', value)

	@property
	def MplsLabelsCountForIpv6MplsRoute(self):
		"""MPLS Labels Count For IPv6 MPLS Route

		Returns:
			number
		"""
		return self._get_attribute('mplsLabelsCountForIpv6MplsRoute')
	@MplsLabelsCountForIpv6MplsRoute.setter
	def MplsLabelsCountForIpv6MplsRoute(self, value):
		self._set_attribute('mplsLabelsCountForIpv6MplsRoute', value)

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
	def NoOfEpePeers(self):
		"""Number of EPE Peers

		Returns:
			number
		"""
		return self._get_attribute('noOfEpePeers')
	@NoOfEpePeers.setter
	def NoOfEpePeers(self, value):
		self._set_attribute('noOfEpePeers', value)

	@property
	def NoOfExtendedCommunities(self):
		"""Number of Extended Communities

		Returns:
			number
		"""
		return self._get_attribute('noOfExtendedCommunities')
	@NoOfExtendedCommunities.setter
	def NoOfExtendedCommunities(self, value):
		self._set_attribute('noOfExtendedCommunities', value)

	@property
	def NoOfUserDefinedAfiSafi(self):
		"""Count of User defined AFI SAFI

		Returns:
			number
		"""
		return self._get_attribute('noOfUserDefinedAfiSafi')
	@NoOfUserDefinedAfiSafi.setter
	def NoOfUserDefinedAfiSafi(self, value):
		self._set_attribute('noOfUserDefinedAfiSafi', value)

	@property
	def NumBgpLsId(self):
		"""BGP LS Instance ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('numBgpLsId')

	@property
	def NumBgpLsInstanceIdentifier(self):
		"""IGP Multi instance unique identifier. 0 is default single-instance IGP. (e.g. for OSPFv3 it is possible to separately run 4 instances of OSPFv3 with peer, one advertising v4 only, another v6 only and other 2 mcast v4 and v6 respectively) .

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('numBgpLsInstanceIdentifier')

	@property
	def NumBgpUpdatesGeneratedPerIteration(self):
		"""Num BGP Updates Generated Per Iteration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('numBgpUpdatesGeneratedPerIteration')

	@property
	def NumberFlowSpecRangeV4(self):
		"""Number of IPv4 Flow Spec Ranges

		Returns:
			number
		"""
		return self._get_attribute('numberFlowSpecRangeV4')
	@NumberFlowSpecRangeV4.setter
	def NumberFlowSpecRangeV4(self, value):
		self._set_attribute('numberFlowSpecRangeV4', value)

	@property
	def NumberFlowSpecRangeV6(self):
		"""Number of IPv6 Flow Spec Ranges

		Returns:
			number
		"""
		return self._get_attribute('numberFlowSpecRangeV6')
	@NumberFlowSpecRangeV6.setter
	def NumberFlowSpecRangeV6(self, value):
		self._set_attribute('numberFlowSpecRangeV6', value)

	@property
	def NumberSRTEPolicies(self):
		"""Count of SR TE Policies

		Returns:
			number
		"""
		return self._get_attribute('numberSRTEPolicies')
	@NumberSRTEPolicies.setter
	def NumberSRTEPolicies(self, value):
		self._set_attribute('numberSRTEPolicies', value)

	@property
	def OperationalModel(self):
		"""Operational Model

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('operationalModel')

	@property
	def RestartTime(self):
		"""Restart Time

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('restartTime')

	@property
	def RoutersMacOrIrbMacAddress(self):
		"""Router's MAC/IRB MAC Address

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('routersMacOrIrbMacAddress')

	@property
	def SRGBRangeCount(self):
		"""SRGB Range Count

		Returns:
			number
		"""
		return self._get_attribute('sRGBRangeCount')
	@SRGBRangeCount.setter
	def SRGBRangeCount(self, value):
		self._set_attribute('sRGBRangeCount', value)

	@property
	def SegmentLeftValue(self):
		"""Segment Left value to be used in top SRH. This zero index based value start from egress node.

		Returns:
			number
		"""
		return self._get_attribute('segmentLeftValue')
	@SegmentLeftValue.setter
	def SegmentLeftValue(self, value):
		self._set_attribute('segmentLeftValue', value)

	@property
	def SendIxiaSignatureWithRoutes(self):
		"""Send Ixia Signature With Routes

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sendIxiaSignatureWithRoutes')

	@property
	def SessionInfo(self):
		"""Logs additional information about the session state

		Returns:
			list(str[aSRoutingLoopErrorRx|attributeFlagErrorRx|attributesLengthErrorRx|authenticationFailureErrorRx|badBGPIdentifierErrorRx|badMessageLengthErrorRx|badMessageTypeErrorRx|badPeerASErrorRx|bGPHeaderErrorRx|bGPHeaderErrorTx|bGPHoldTimerExpiredErrorRx|bGPOpenPacketErrorRx|bGPStateMachineErrorRx|bGPUpdatePacketErrorRx|ceaseErrorRx|ceaseNotificationErrorTx|connectionNotsynchronizedErrorRx|holdtimeExpiredErrorTx|invalidASPathErrorRx|invalidNetworkFieldErrorRx|invalidNextHopAttributeErrorRx|invalidOriginAttributeErrorRx|malformedAttributeListErrorRx|missingWellKnownAttributeErrorRx|none|openPacketErrTx|optionalAttributeErrorRx|stateMachineErrorTx|unacceptableHoldTimeErrorRx|unrecognizedWellKnownAttributeErrorRx|unspecifiedErrorRx|unspecifiedErrorTx|unspecifiedSubcodeErrorRx|unsupportedOptionalParameterErrorRx|unsupportedversionNumberErrorRx|updatePacketErrorTx])
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
	def Srv6SidFlags(self):
		"""SRv6 SID Flags Value

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6SidFlags')

	@property
	def Srv6SidLoc(self):
		"""SRv6 SID. It consists of Locator, Func and Args

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6SidLoc')

	@property
	def Srv6SidLocLen(self):
		"""SRv6 SID Locator Length

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6SidLocLen')

	@property
	def Srv6SidLocMetric(self):
		"""SRv6 SID Locator Metric

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6SidLocMetric')

	@property
	def Srv6SidReserved(self):
		"""SRv6 SID Reserved Value

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6SidReserved')

	@property
	def Srv6Ttl(self):
		"""TTL value to be used in outer IPv6 header

		Returns:
			number
		"""
		return self._get_attribute('srv6Ttl')
	@Srv6Ttl.setter
	def Srv6Ttl(self, value):
		self._set_attribute('srv6Ttl', value)

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
	def StaleTime(self):
		"""Stale Time/ LLGR Stale Time

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('staleTime')

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
	def TcpWindowSizeInBytes(self):
		"""TCP Window Size (in bytes)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('tcpWindowSizeInBytes')

	@property
	def Ttl(self):
		"""TTL

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ttl')

	@property
	def Type(self):
		"""Type

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('type')

	@property
	def UdpPortEndValue(self):
		"""UDP Port End Value

		Returns:
			number
		"""
		return self._get_attribute('udpPortEndValue')
	@UdpPortEndValue.setter
	def UdpPortEndValue(self, value):
		self._set_attribute('udpPortEndValue', value)

	@property
	def UdpPortStartValue(self):
		"""UDP Port Start Value

		Returns:
			number
		"""
		return self._get_attribute('udpPortStartValue')
	@UdpPortStartValue.setter
	def UdpPortStartValue(self, value):
		self._set_attribute('udpPortStartValue', value)

	@property
	def UpdateInterval(self):
		"""Update Interval

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('updateInterval')

	@property
	def UptimeInSec(self):
		"""Uptime in Seconds

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('uptimeInSec')

	@property
	def UseStaticPolicy(self):
		"""If enabled then SRTE policy will be advertised

		Returns:
			bool
		"""
		return self._get_attribute('useStaticPolicy')
	@UseStaticPolicy.setter
	def UseStaticPolicy(self, value):
		self._set_attribute('useStaticPolicy', value)

	@property
	def VplsEnableNextHop(self):
		"""VPLS Enable Next Hop

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('vplsEnableNextHop')

	@property
	def VplsNextHop(self):
		"""VPLS Next Hop

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('vplsNextHop')

	def update(self, AdvertiseEvpnRoutesForOtherVtep=None, AutoGenSegmentLeftValue=None, BgpLsNoOfASPathSegments=None, BgpLsNoOfClusters=None, BgpLsNoOfCommunities=None, CapabilityIpv4MplsAddPath=None, CapabilityIpv6MplsAddPath=None, ConnectedVia=None, CopyTtl=None, EnSRv6DataPlane=None, EnableEpeTraffic=None, EnableReducedEncapsulation=None, EthernetSegmentsCountV6=None, IpVrfToIpVrfType=None, Ipv4MplsCapability=None, Ipv4MultipleMplsLabelsCapability=None, Ipv6MplsCapability=None, Ipv6MultipleMplsLabelsCapability=None, MaxSidPerSrh=None, MplsLabelsCountForIpv4MplsRoute=None, MplsLabelsCountForIpv6MplsRoute=None, Multiplier=None, Name=None, NoOfEpePeers=None, NoOfExtendedCommunities=None, NoOfUserDefinedAfiSafi=None, NumberFlowSpecRangeV4=None, NumberFlowSpecRangeV6=None, NumberSRTEPolicies=None, SRGBRangeCount=None, SegmentLeftValue=None, Srv6Ttl=None, StackedLayers=None, UdpPortEndValue=None, UdpPortStartValue=None, UseStaticPolicy=None):
		"""Updates a child instance of bgpIpv6Peer on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			AdvertiseEvpnRoutesForOtherVtep (bool): Advertise EVPN routes for other VTEPS
			AutoGenSegmentLeftValue (bool): If enabled then Segment Left field value will be auto generated
			BgpLsNoOfASPathSegments (number): Number Of AS Path Segments Per Route Range
			BgpLsNoOfClusters (number): Number of Clusters
			BgpLsNoOfCommunities (number): Number of Communities
			CapabilityIpv4MplsAddPath (bool): IPv4 MPLS Add Path Capability
			CapabilityIpv6MplsAddPath (bool): IPv6 MPLS Add Path Capability
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			CopyTtl (bool): Copy TTL from customer packet to outer IPv6 header
			EnSRv6DataPlane (bool): Ingress Peer Supports SRv6 VPN
			EnableEpeTraffic (bool): Enable EPE Traffic
			EnableReducedEncapsulation (bool): Enable Reduced Encapsulation in Data-Plane for SRv6
			EthernetSegmentsCountV6 (number): Number of Ethernet Segments
			IpVrfToIpVrfType (str(interfaceLess|interfacefullWithCorefacingIRB|interfacefullWithUnnumberedCorefacingIRB)): IP-VRF-to-IP-VRF Model Type
			Ipv4MplsCapability (bool): IPv4 MPLS Capability: AFI=1, SAFI=4
			Ipv4MultipleMplsLabelsCapability (bool): IPv4 Multiple MPLS Labels Capability: AFI=1, SAFI=4
			Ipv6MplsCapability (bool): IPv6 MPLS Capability: AFI=2, SAFI=4
			Ipv6MultipleMplsLabelsCapability (bool): IPv6 Multiple MPLS Labels Capability: AFI=2, SAFI=4
			MaxSidPerSrh (number): Max number of SIDs a SRH can have
			MplsLabelsCountForIpv4MplsRoute (number): MPLS Labels Count For IPv4 MPLS Route
			MplsLabelsCountForIpv6MplsRoute (number): MPLS Labels Count For IPv6 MPLS Route
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfEpePeers (number): Number of EPE Peers
			NoOfExtendedCommunities (number): Number of Extended Communities
			NoOfUserDefinedAfiSafi (number): Count of User defined AFI SAFI
			NumberFlowSpecRangeV4 (number): Number of IPv4 Flow Spec Ranges
			NumberFlowSpecRangeV6 (number): Number of IPv6 Flow Spec Ranges
			NumberSRTEPolicies (number): Count of SR TE Policies
			SRGBRangeCount (number): SRGB Range Count
			SegmentLeftValue (number): Segment Left value to be used in top SRH. This zero index based value start from egress node.
			Srv6Ttl (number): TTL value to be used in outer IPv6 header
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			UdpPortEndValue (number): UDP Port End Value
			UdpPortStartValue (number): UDP Port Start Value
			UseStaticPolicy (bool): If enabled then SRTE policy will be advertised

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, AdvertiseEvpnRoutesForOtherVtep=None, AutoGenSegmentLeftValue=None, BgpLsNoOfASPathSegments=None, BgpLsNoOfClusters=None, BgpLsNoOfCommunities=None, CapabilityIpv4MplsAddPath=None, CapabilityIpv6MplsAddPath=None, ConnectedVia=None, CopyTtl=None, EnSRv6DataPlane=None, EnableEpeTraffic=None, EnableReducedEncapsulation=None, EthernetSegmentsCountV6=None, IpVrfToIpVrfType=None, Ipv4MplsCapability=None, Ipv4MultipleMplsLabelsCapability=None, Ipv6MplsCapability=None, Ipv6MultipleMplsLabelsCapability=None, MaxSidPerSrh=None, MplsLabelsCountForIpv4MplsRoute=None, MplsLabelsCountForIpv6MplsRoute=None, Multiplier=None, Name=None, NoOfEpePeers=None, NoOfExtendedCommunities=None, NoOfUserDefinedAfiSafi=None, NumberFlowSpecRangeV4=None, NumberFlowSpecRangeV6=None, NumberSRTEPolicies=None, SRGBRangeCount=None, SegmentLeftValue=None, Srv6Ttl=None, StackedLayers=None, UdpPortEndValue=None, UdpPortStartValue=None, UseStaticPolicy=None):
		"""Adds a new bgpIpv6Peer node on the server and retrieves it in this instance.

		Args:
			AdvertiseEvpnRoutesForOtherVtep (bool): Advertise EVPN routes for other VTEPS
			AutoGenSegmentLeftValue (bool): If enabled then Segment Left field value will be auto generated
			BgpLsNoOfASPathSegments (number): Number Of AS Path Segments Per Route Range
			BgpLsNoOfClusters (number): Number of Clusters
			BgpLsNoOfCommunities (number): Number of Communities
			CapabilityIpv4MplsAddPath (bool): IPv4 MPLS Add Path Capability
			CapabilityIpv6MplsAddPath (bool): IPv6 MPLS Add Path Capability
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			CopyTtl (bool): Copy TTL from customer packet to outer IPv6 header
			EnSRv6DataPlane (bool): Ingress Peer Supports SRv6 VPN
			EnableEpeTraffic (bool): Enable EPE Traffic
			EnableReducedEncapsulation (bool): Enable Reduced Encapsulation in Data-Plane for SRv6
			EthernetSegmentsCountV6 (number): Number of Ethernet Segments
			IpVrfToIpVrfType (str(interfaceLess|interfacefullWithCorefacingIRB|interfacefullWithUnnumberedCorefacingIRB)): IP-VRF-to-IP-VRF Model Type
			Ipv4MplsCapability (bool): IPv4 MPLS Capability: AFI=1, SAFI=4
			Ipv4MultipleMplsLabelsCapability (bool): IPv4 Multiple MPLS Labels Capability: AFI=1, SAFI=4
			Ipv6MplsCapability (bool): IPv6 MPLS Capability: AFI=2, SAFI=4
			Ipv6MultipleMplsLabelsCapability (bool): IPv6 Multiple MPLS Labels Capability: AFI=2, SAFI=4
			MaxSidPerSrh (number): Max number of SIDs a SRH can have
			MplsLabelsCountForIpv4MplsRoute (number): MPLS Labels Count For IPv4 MPLS Route
			MplsLabelsCountForIpv6MplsRoute (number): MPLS Labels Count For IPv6 MPLS Route
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfEpePeers (number): Number of EPE Peers
			NoOfExtendedCommunities (number): Number of Extended Communities
			NoOfUserDefinedAfiSafi (number): Count of User defined AFI SAFI
			NumberFlowSpecRangeV4 (number): Number of IPv4 Flow Spec Ranges
			NumberFlowSpecRangeV6 (number): Number of IPv6 Flow Spec Ranges
			NumberSRTEPolicies (number): Count of SR TE Policies
			SRGBRangeCount (number): SRGB Range Count
			SegmentLeftValue (number): Segment Left value to be used in top SRH. This zero index based value start from egress node.
			Srv6Ttl (number): TTL value to be used in outer IPv6 header
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			UdpPortEndValue (number): UDP Port End Value
			UdpPortStartValue (number): UDP Port Start Value
			UseStaticPolicy (bool): If enabled then SRTE policy will be advertised

		Returns:
			self: This instance with all currently retrieved bgpIpv6Peer data using find and the newly added bgpIpv6Peer data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the bgpIpv6Peer data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, AdvertiseEvpnRoutesForOtherVtep=None, AutoGenSegmentLeftValue=None, BgpFsmState=None, BgpLsNoOfASPathSegments=None, BgpLsNoOfClusters=None, BgpLsNoOfCommunities=None, CapabilityIpv4MplsAddPath=None, CapabilityIpv6MplsAddPath=None, ConnectedVia=None, CopyTtl=None, Count=None, DescriptiveName=None, EnSRv6DataPlane=None, EnableEpeTraffic=None, EnableReducedEncapsulation=None, Errors=None, EthernetSegmentsCountV6=None, IpVrfToIpVrfType=None, Ipv4MplsCapability=None, Ipv4MultipleMplsLabelsCapability=None, Ipv6MplsCapability=None, Ipv6MultipleMplsLabelsCapability=None, LocalIpv6Ver2=None, LocalRouterID=None, MaxSidPerSrh=None, MplsLabelsCountForIpv4MplsRoute=None, MplsLabelsCountForIpv6MplsRoute=None, Multiplier=None, Name=None, NoOfEpePeers=None, NoOfExtendedCommunities=None, NoOfUserDefinedAfiSafi=None, NumberFlowSpecRangeV4=None, NumberFlowSpecRangeV6=None, NumberSRTEPolicies=None, SRGBRangeCount=None, SegmentLeftValue=None, SessionInfo=None, SessionStatus=None, Srv6Ttl=None, StackedLayers=None, StateCounts=None, Status=None, UdpPortEndValue=None, UdpPortStartValue=None, UseStaticPolicy=None):
		"""Finds and retrieves bgpIpv6Peer data from the server.

		All named parameters support regex and can be used to selectively retrieve bgpIpv6Peer data from the server.
		By default the find method takes no parameters and will retrieve all bgpIpv6Peer data from the server.

		Args:
			AdvertiseEvpnRoutesForOtherVtep (bool): Advertise EVPN routes for other VTEPS
			AutoGenSegmentLeftValue (bool): If enabled then Segment Left field value will be auto generated
			BgpFsmState (list(str[active|connect|error|established|idle|none|openConfirm|openSent])): Logs additional information about the BGP Peer State
			BgpLsNoOfASPathSegments (number): Number Of AS Path Segments Per Route Range
			BgpLsNoOfClusters (number): Number of Clusters
			BgpLsNoOfCommunities (number): Number of Communities
			CapabilityIpv4MplsAddPath (bool): IPv4 MPLS Add Path Capability
			CapabilityIpv6MplsAddPath (bool): IPv6 MPLS Add Path Capability
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			CopyTtl (bool): Copy TTL from customer packet to outer IPv6 header
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
			EnSRv6DataPlane (bool): Ingress Peer Supports SRv6 VPN
			EnableEpeTraffic (bool): Enable EPE Traffic
			EnableReducedEncapsulation (bool): Enable Reduced Encapsulation in Data-Plane for SRv6
			Errors (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))): A list of errors that have occurred
			EthernetSegmentsCountV6 (number): Number of Ethernet Segments
			IpVrfToIpVrfType (str(interfaceLess|interfacefullWithCorefacingIRB|interfacefullWithUnnumberedCorefacingIRB)): IP-VRF-to-IP-VRF Model Type
			Ipv4MplsCapability (bool): IPv4 MPLS Capability: AFI=1, SAFI=4
			Ipv4MultipleMplsLabelsCapability (bool): IPv4 Multiple MPLS Labels Capability: AFI=1, SAFI=4
			Ipv6MplsCapability (bool): IPv6 MPLS Capability: AFI=2, SAFI=4
			Ipv6MultipleMplsLabelsCapability (bool): IPv6 Multiple MPLS Labels Capability: AFI=2, SAFI=4
			LocalIpv6Ver2 (list(str)): Local IP
			LocalRouterID (list(str)): Router ID
			MaxSidPerSrh (number): Max number of SIDs a SRH can have
			MplsLabelsCountForIpv4MplsRoute (number): MPLS Labels Count For IPv4 MPLS Route
			MplsLabelsCountForIpv6MplsRoute (number): MPLS Labels Count For IPv6 MPLS Route
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfEpePeers (number): Number of EPE Peers
			NoOfExtendedCommunities (number): Number of Extended Communities
			NoOfUserDefinedAfiSafi (number): Count of User defined AFI SAFI
			NumberFlowSpecRangeV4 (number): Number of IPv4 Flow Spec Ranges
			NumberFlowSpecRangeV6 (number): Number of IPv6 Flow Spec Ranges
			NumberSRTEPolicies (number): Count of SR TE Policies
			SRGBRangeCount (number): SRGB Range Count
			SegmentLeftValue (number): Segment Left value to be used in top SRH. This zero index based value start from egress node.
			SessionInfo (list(str[aSRoutingLoopErrorRx|attributeFlagErrorRx|attributesLengthErrorRx|authenticationFailureErrorRx|badBGPIdentifierErrorRx|badMessageLengthErrorRx|badMessageTypeErrorRx|badPeerASErrorRx|bGPHeaderErrorRx|bGPHeaderErrorTx|bGPHoldTimerExpiredErrorRx|bGPOpenPacketErrorRx|bGPStateMachineErrorRx|bGPUpdatePacketErrorRx|ceaseErrorRx|ceaseNotificationErrorTx|connectionNotsynchronizedErrorRx|holdtimeExpiredErrorTx|invalidASPathErrorRx|invalidNetworkFieldErrorRx|invalidNextHopAttributeErrorRx|invalidOriginAttributeErrorRx|malformedAttributeListErrorRx|missingWellKnownAttributeErrorRx|none|openPacketErrTx|optionalAttributeErrorRx|stateMachineErrorTx|unacceptableHoldTimeErrorRx|unrecognizedWellKnownAttributeErrorRx|unspecifiedErrorRx|unspecifiedErrorTx|unspecifiedSubcodeErrorRx|unsupportedOptionalParameterErrorRx|unsupportedversionNumberErrorRx|updatePacketErrorTx])): Logs additional information about the session state
			SessionStatus (list(str[down|notStarted|up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
			Srv6Ttl (number): TTL value to be used in outer IPv6 header
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			UdpPortEndValue (number): UDP Port End Value
			UdpPortStartValue (number): UDP Port Start Value
			UseStaticPolicy (bool): If enabled then SRTE policy will be advertised

		Returns:
			self: This instance with matching bgpIpv6Peer data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of bgpIpv6Peer data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the bgpIpv6Peer data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, ActAsRestarted=None, Active=None, AdvSrv6SidInIgp=None, AdvertiseEndOfRib=None, AdvertiseSRv6SID=None, AdvertiseTunnelEncapsulationExtendedCommunity=None, AlwaysIncludeTunnelEncExtCommunity=None, AsSetMode=None, Authentication=None, BgpId=None, BgpLsAsSetMode=None, BgpLsEnableAsPathSegments=None, BgpLsEnableCluster=None, BgpLsEnableExtendedCommunity=None, BgpLsOverridePeerAsSetMode=None, CapabilityIpV4Mdt=None, CapabilityIpV4Mpls=None, CapabilityIpV4MplsVpn=None, CapabilityIpV4Multicast=None, CapabilityIpV4MulticastVpn=None, CapabilityIpV4Unicast=None, CapabilityIpV6Mpls=None, CapabilityIpV6MplsVpn=None, CapabilityIpV6Multicast=None, CapabilityIpV6MulticastVpn=None, CapabilityIpV6Unicast=None, CapabilityIpv4UnicastAddPath=None, CapabilityIpv6UnicastAddPath=None, CapabilityLinkStateNonVpn=None, CapabilityNHEncodingCapabilities=None, CapabilityRouteConstraint=None, CapabilityRouteRefresh=None, CapabilitySRTEPoliciesV4=None, CapabilitySRTEPoliciesV6=None, CapabilityVpls=None, Capabilityipv4UnicastFlowSpec=None, Capabilityipv6UnicastFlowSpec=None, ConfigureKeepaliveTimer=None, CustomSidType=None, DiscardIxiaGeneratedRoutes=None, DowntimeInSec=None, DutIp=None, Enable4ByteAs=None, EnableBfdRegistration=None, EnableBgpId=None, EnableBgpIdSameAsRouterId=None, EnableBgpLsCommunity=None, EnableGracefulRestart=None, EnableLlgr=None, Evpn=None, FilterEvpn=None, FilterIpV4Mpls=None, FilterIpV4MplsVpn=None, FilterIpV4Multicast=None, FilterIpV4MulticastVpn=None, FilterIpV4Unicast=None, FilterIpV6Mpls=None, FilterIpV6MplsVpn=None, FilterIpV6Multicast=None, FilterIpV6MulticastVpn=None, FilterIpV6Unicast=None, FilterIpv4MulticastBgpMplsVpn=None, FilterIpv4UnicastFlowSpec=None, FilterIpv6MulticastBgpMplsVpn=None, FilterIpv6UnicastFlowSpec=None, FilterLinkState=None, FilterSRTEPoliciesV4=None, FilterSRTEPoliciesV6=None, FilterVpls=None, Flap=None, HoldTimer=None, Ipv4MplsAddPathMode=None, Ipv4MulticastBgpMplsVpn=None, Ipv4UnicastAddPathMode=None, Ipv6MplsAddPathMode=None, Ipv6MulticastBgpMplsVpn=None, Ipv6UnicastAddPathMode=None, IrbInterfaceLabel=None, IrbIpv6Address=None, KeepaliveTimer=None, L3VPNEncapsulationType=None, LocalAs2Bytes=None, LocalAs4Bytes=None, Md5Key=None, ModeOfBfdOperations=None, NumBgpLsId=None, NumBgpLsInstanceIdentifier=None, NumBgpUpdatesGeneratedPerIteration=None, OperationalModel=None, RestartTime=None, RoutersMacOrIrbMacAddress=None, SendIxiaSignatureWithRoutes=None, Srv6SidFlags=None, Srv6SidLoc=None, Srv6SidLocLen=None, Srv6SidLocMetric=None, Srv6SidReserved=None, StaleTime=None, TcpWindowSizeInBytes=None, Ttl=None, Type=None, UpdateInterval=None, UptimeInSec=None, VplsEnableNextHop=None, VplsNextHop=None):
		"""Base class infrastructure that gets a list of bgpIpv6Peer device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			ActAsRestarted (str): optional regex of actAsRestarted
			Active (str): optional regex of active
			AdvSrv6SidInIgp (str): optional regex of advSrv6SidInIgp
			AdvertiseEndOfRib (str): optional regex of advertiseEndOfRib
			AdvertiseSRv6SID (str): optional regex of advertiseSRv6SID
			AdvertiseTunnelEncapsulationExtendedCommunity (str): optional regex of advertiseTunnelEncapsulationExtendedCommunity
			AlwaysIncludeTunnelEncExtCommunity (str): optional regex of alwaysIncludeTunnelEncExtCommunity
			AsSetMode (str): optional regex of asSetMode
			Authentication (str): optional regex of authentication
			BgpId (str): optional regex of bgpId
			BgpLsAsSetMode (str): optional regex of bgpLsAsSetMode
			BgpLsEnableAsPathSegments (str): optional regex of bgpLsEnableAsPathSegments
			BgpLsEnableCluster (str): optional regex of bgpLsEnableCluster
			BgpLsEnableExtendedCommunity (str): optional regex of bgpLsEnableExtendedCommunity
			BgpLsOverridePeerAsSetMode (str): optional regex of bgpLsOverridePeerAsSetMode
			CapabilityIpV4Mdt (str): optional regex of capabilityIpV4Mdt
			CapabilityIpV4Mpls (str): optional regex of capabilityIpV4Mpls
			CapabilityIpV4MplsVpn (str): optional regex of capabilityIpV4MplsVpn
			CapabilityIpV4Multicast (str): optional regex of capabilityIpV4Multicast
			CapabilityIpV4MulticastVpn (str): optional regex of capabilityIpV4MulticastVpn
			CapabilityIpV4Unicast (str): optional regex of capabilityIpV4Unicast
			CapabilityIpV6Mpls (str): optional regex of capabilityIpV6Mpls
			CapabilityIpV6MplsVpn (str): optional regex of capabilityIpV6MplsVpn
			CapabilityIpV6Multicast (str): optional regex of capabilityIpV6Multicast
			CapabilityIpV6MulticastVpn (str): optional regex of capabilityIpV6MulticastVpn
			CapabilityIpV6Unicast (str): optional regex of capabilityIpV6Unicast
			CapabilityIpv4UnicastAddPath (str): optional regex of capabilityIpv4UnicastAddPath
			CapabilityIpv6UnicastAddPath (str): optional regex of capabilityIpv6UnicastAddPath
			CapabilityLinkStateNonVpn (str): optional regex of capabilityLinkStateNonVpn
			CapabilityNHEncodingCapabilities (str): optional regex of capabilityNHEncodingCapabilities
			CapabilityRouteConstraint (str): optional regex of capabilityRouteConstraint
			CapabilityRouteRefresh (str): optional regex of capabilityRouteRefresh
			CapabilitySRTEPoliciesV4 (str): optional regex of capabilitySRTEPoliciesV4
			CapabilitySRTEPoliciesV6 (str): optional regex of capabilitySRTEPoliciesV6
			CapabilityVpls (str): optional regex of capabilityVpls
			Capabilityipv4UnicastFlowSpec (str): optional regex of capabilityipv4UnicastFlowSpec
			Capabilityipv6UnicastFlowSpec (str): optional regex of capabilityipv6UnicastFlowSpec
			ConfigureKeepaliveTimer (str): optional regex of configureKeepaliveTimer
			CustomSidType (str): optional regex of customSidType
			DiscardIxiaGeneratedRoutes (str): optional regex of discardIxiaGeneratedRoutes
			DowntimeInSec (str): optional regex of downtimeInSec
			DutIp (str): optional regex of dutIp
			Enable4ByteAs (str): optional regex of enable4ByteAs
			EnableBfdRegistration (str): optional regex of enableBfdRegistration
			EnableBgpId (str): optional regex of enableBgpId
			EnableBgpIdSameAsRouterId (str): optional regex of enableBgpIdSameAsRouterId
			EnableBgpLsCommunity (str): optional regex of enableBgpLsCommunity
			EnableGracefulRestart (str): optional regex of enableGracefulRestart
			EnableLlgr (str): optional regex of enableLlgr
			Evpn (str): optional regex of evpn
			FilterEvpn (str): optional regex of filterEvpn
			FilterIpV4Mpls (str): optional regex of filterIpV4Mpls
			FilterIpV4MplsVpn (str): optional regex of filterIpV4MplsVpn
			FilterIpV4Multicast (str): optional regex of filterIpV4Multicast
			FilterIpV4MulticastVpn (str): optional regex of filterIpV4MulticastVpn
			FilterIpV4Unicast (str): optional regex of filterIpV4Unicast
			FilterIpV6Mpls (str): optional regex of filterIpV6Mpls
			FilterIpV6MplsVpn (str): optional regex of filterIpV6MplsVpn
			FilterIpV6Multicast (str): optional regex of filterIpV6Multicast
			FilterIpV6MulticastVpn (str): optional regex of filterIpV6MulticastVpn
			FilterIpV6Unicast (str): optional regex of filterIpV6Unicast
			FilterIpv4MulticastBgpMplsVpn (str): optional regex of filterIpv4MulticastBgpMplsVpn
			FilterIpv4UnicastFlowSpec (str): optional regex of filterIpv4UnicastFlowSpec
			FilterIpv6MulticastBgpMplsVpn (str): optional regex of filterIpv6MulticastBgpMplsVpn
			FilterIpv6UnicastFlowSpec (str): optional regex of filterIpv6UnicastFlowSpec
			FilterLinkState (str): optional regex of filterLinkState
			FilterSRTEPoliciesV4 (str): optional regex of filterSRTEPoliciesV4
			FilterSRTEPoliciesV6 (str): optional regex of filterSRTEPoliciesV6
			FilterVpls (str): optional regex of filterVpls
			Flap (str): optional regex of flap
			HoldTimer (str): optional regex of holdTimer
			Ipv4MplsAddPathMode (str): optional regex of ipv4MplsAddPathMode
			Ipv4MulticastBgpMplsVpn (str): optional regex of ipv4MulticastBgpMplsVpn
			Ipv4UnicastAddPathMode (str): optional regex of ipv4UnicastAddPathMode
			Ipv6MplsAddPathMode (str): optional regex of ipv6MplsAddPathMode
			Ipv6MulticastBgpMplsVpn (str): optional regex of ipv6MulticastBgpMplsVpn
			Ipv6UnicastAddPathMode (str): optional regex of ipv6UnicastAddPathMode
			IrbInterfaceLabel (str): optional regex of irbInterfaceLabel
			IrbIpv6Address (str): optional regex of irbIpv6Address
			KeepaliveTimer (str): optional regex of keepaliveTimer
			L3VPNEncapsulationType (str): optional regex of l3VPNEncapsulationType
			LocalAs2Bytes (str): optional regex of localAs2Bytes
			LocalAs4Bytes (str): optional regex of localAs4Bytes
			Md5Key (str): optional regex of md5Key
			ModeOfBfdOperations (str): optional regex of modeOfBfdOperations
			NumBgpLsId (str): optional regex of numBgpLsId
			NumBgpLsInstanceIdentifier (str): optional regex of numBgpLsInstanceIdentifier
			NumBgpUpdatesGeneratedPerIteration (str): optional regex of numBgpUpdatesGeneratedPerIteration
			OperationalModel (str): optional regex of operationalModel
			RestartTime (str): optional regex of restartTime
			RoutersMacOrIrbMacAddress (str): optional regex of routersMacOrIrbMacAddress
			SendIxiaSignatureWithRoutes (str): optional regex of sendIxiaSignatureWithRoutes
			Srv6SidFlags (str): optional regex of srv6SidFlags
			Srv6SidLoc (str): optional regex of srv6SidLoc
			Srv6SidLocLen (str): optional regex of srv6SidLocLen
			Srv6SidLocMetric (str): optional regex of srv6SidLocMetric
			Srv6SidReserved (str): optional regex of srv6SidReserved
			StaleTime (str): optional regex of staleTime
			TcpWindowSizeInBytes (str): optional regex of tcpWindowSizeInBytes
			Ttl (str): optional regex of ttl
			Type (str): optional regex of type
			UpdateInterval (str): optional regex of updateInterval
			UptimeInSec (str): optional regex of uptimeInSec
			VplsEnableNextHop (str): optional regex of vplsEnableNextHop
			VplsNextHop (str): optional regex of vplsNextHop

		Returns:
			list(int): A list of device ids that meets the regex criteria provided in the method parameters

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._get_ngpf_device_ids(locals())

	def BgpIPv4FlowSpecLearnedInfo(self, *args, **kwargs):
		"""Executes the bgpIPv4FlowSpecLearnedInfo operation on the server.

		Get IPv4 FlowSpec Learned Info

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		bgpIPv4FlowSpecLearnedInfo()

		bgpIPv4FlowSpecLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		bgpIPv4FlowSpecLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('bgpIPv4FlowSpecLearnedInfo', payload=payload, response_object=None)

	def BgpIPv6FlowSpecLearnedInfo(self, *args, **kwargs):
		"""Executes the bgpIPv6FlowSpecLearnedInfo operation on the server.

		Get IPv6 FlowSpec Learned Info

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		bgpIPv6FlowSpecLearnedInfo()

		bgpIPv6FlowSpecLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		bgpIPv6FlowSpecLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('bgpIPv6FlowSpecLearnedInfo', payload=payload, response_object=None)

	def BreakTCPSession(self, *args, **kwargs):
		"""Executes the breakTCPSession operation on the server.

		Break TCP Session

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		breakTCPSession(Notification_code:number, Notification_sub_code:number)
			Args:
				args[0] is Notification_code (number): This parameter requires a notification_code of type kInteger
				args[1] is Notification_sub_code (number): This parameter requires a notification_sub_code of type kInteger

		breakTCPSession(Notification_code:number, Notification_sub_code:number, SessionIndices:list)
			Args:
				args[0] is Notification_code (number): This parameter requires a notification_code of type kInteger
				args[1] is Notification_sub_code (number): This parameter requires a notification_sub_code of type kInteger
				args[2] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		breakTCPSession(SessionIndices:string, Notification_code:number, Notification_sub_code:number)
			Args:
				args[0] is SessionIndices (str): This parameter requires a notification_code of type kInteger
				args[1] is Notification_code (number): This parameter requires a notification_sub_code of type kInteger
				args[2] is Notification_sub_code (number): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('breakTCPSession', payload=payload, response_object=None)

	def Breaktcpsession(self, *args, **kwargs):
		"""Executes the breaktcpsession operation on the server.

		Break BGP Peer Range TCP Session.

		breaktcpsession(Arg2:list, Arg3:number, Arg4:number)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
				args[1] is Arg3 (number): Notification Code
				args[2] is Arg4 (number): Notification Sub Code

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('breaktcpsession', payload=payload, response_object=None)

	def ClearAllLearnedInfo(self, *args, **kwargs):
		"""Executes the clearAllLearnedInfo operation on the server.

		Clear All Learned Info

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		clearAllLearnedInfo()

		clearAllLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		clearAllLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('clearAllLearnedInfo', payload=payload, response_object=None)

	def ClearAllLearnedInfoInClient(self, *args, **kwargs):
		"""Executes the clearAllLearnedInfoInClient operation on the server.

		Clears ALL routes from GUI grid for the selected BGP Peers.

		clearAllLearnedInfoInClient(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('clearAllLearnedInfoInClient', payload=payload, response_object=None)

	def GetADVPLSLearnedInfo(self, *args, **kwargs):
		"""Executes the getADVPLSLearnedInfo operation on the server.

		Get ADVPLS Learned Info

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getADVPLSLearnedInfo()

		getADVPLSLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getADVPLSLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getADVPLSLearnedInfo(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getADVPLSLearnedInfo', payload=payload, response_object=None)

	def GetAllLearnedInfo(self, *args, **kwargs):
		"""Executes the getAllLearnedInfo operation on the server.

		Get All Learned Info

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getAllLearnedInfo()

		getAllLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getAllLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getAllLearnedInfo(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getAllLearnedInfo', payload=payload, response_object=None)

	def GetbgpIpv4FlowSpecLearnedInfoLearnedInfo(self, *args, **kwargs):
		"""Executes the getbgpIpv4FlowSpecLearnedInfoLearnedInfo operation on the server.

		getbgpIpv4FlowSpecLearnedInfoLearnedInfo(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

			Returns:
				list(str): Please provide a proper description here.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getbgpIpv4FlowSpecLearnedInfoLearnedInfo', payload=payload, response_object=None)

	def GetbgpIpv6FlowSpecLearnedInfoLearnedInfo(self, *args, **kwargs):
		"""Executes the getbgpIpv6FlowSpecLearnedInfoLearnedInfo operation on the server.

		getbgpIpv6FlowSpecLearnedInfoLearnedInfo(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

			Returns:
				list(str): Please provide a proper description here.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getbgpIpv6FlowSpecLearnedInfoLearnedInfo', payload=payload, response_object=None)

	def GetbgpSrTeLearnedInfoLearnedInfo(self, *args, **kwargs):
		"""Executes the getbgpSrTeLearnedInfoLearnedInfo operation on the server.

		getbgpSrTeLearnedInfoLearnedInfo(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin.An empty list indicates all instances in the plugin.

			Returns:
				list(str): Please provide a proper description here.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getbgpSrTeLearnedInfoLearnedInfo', payload=payload, response_object=None)

	def GetEVPNLearnedInfo(self, *args, **kwargs):
		"""Executes the getEVPNLearnedInfo operation on the server.

		Get EVPN Learned Info

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getEVPNLearnedInfo()

		getEVPNLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getEVPNLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getEVPNLearnedInfo(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getEVPNLearnedInfo', payload=payload, response_object=None)

	def GetIPv4LearnedInfo(self, *args, **kwargs):
		"""Executes the getIPv4LearnedInfo operation on the server.

		Get IPv4 Learned Info

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getIPv4LearnedInfo()

		getIPv4LearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getIPv4LearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getIPv4LearnedInfo(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getIPv4LearnedInfo', payload=payload, response_object=None)

	def GetIPv4MplsLearnedInfo(self, *args, **kwargs):
		"""Executes the getIPv4MplsLearnedInfo operation on the server.

		Fetches IPv4 MPLS routes learnt by this BGP peer.

		getIPv4MplsLearnedInfo(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getIPv4MplsLearnedInfo', payload=payload, response_object=None)

	def GetIpv4MvpnLearnedInfo(self, *args, **kwargs):
		"""Executes the getIpv4MvpnLearnedInfo operation on the server.

		Fetches MVPN MAC IP routes learnt by this BGP peer.

		getIpv4MvpnLearnedInfo(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getIpv4MvpnLearnedInfo', payload=payload, response_object=None)

	def GetIpv4UmhRoutesLearnedInfo(self, *args, **kwargs):
		"""Executes the getIpv4UmhRoutesLearnedInfo operation on the server.

		Fetches Umh Routes learned by this BGP peer.

		getIpv4UmhRoutesLearnedInfo(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getIpv4UmhRoutesLearnedInfo', payload=payload, response_object=None)

	def GetIPv4VpnLearnedInfo(self, *args, **kwargs):
		"""Executes the getIPv4VpnLearnedInfo operation on the server.

		Get IPv4 Vpn Learned Info

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getIPv4VpnLearnedInfo()

		getIPv4VpnLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getIPv4VpnLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getIPv4VpnLearnedInfo(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getIPv4VpnLearnedInfo', payload=payload, response_object=None)

	def GetIPv6LearnedInfo(self, *args, **kwargs):
		"""Executes the getIPv6LearnedInfo operation on the server.

		Get IPv6 Learned Info

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getIPv6LearnedInfo()

		getIPv6LearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getIPv6LearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getIPv6LearnedInfo(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getIPv6LearnedInfo', payload=payload, response_object=None)

	def GetIPv6MplsLearnedInfo(self, *args, **kwargs):
		"""Executes the getIPv6MplsLearnedInfo operation on the server.

		Gets IPv6 Mpls routes learnt by this BGP peer.

		getIPv6MplsLearnedInfo(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getIPv6MplsLearnedInfo', payload=payload, response_object=None)

	def GetIpv6MvpnLearnedInfo(self, *args, **kwargs):
		"""Executes the getIpv6MvpnLearnedInfo operation on the server.

		Fetches MVPN MAC IP routes learnt by this BGP peer.

		getIpv6MvpnLearnedInfo(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getIpv6MvpnLearnedInfo', payload=payload, response_object=None)

	def GetIpv6UmhRoutesLearnedInfo(self, *args, **kwargs):
		"""Executes the getIpv6UmhRoutesLearnedInfo operation on the server.

		Fetches Umh Route learned by this BGP peer.

		getIpv6UmhRoutesLearnedInfo(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getIpv6UmhRoutesLearnedInfo', payload=payload, response_object=None)

	def GetIPv6VpnLearnedInfo(self, *args, **kwargs):
		"""Executes the getIPv6VpnLearnedInfo operation on the server.

		Get IPv6 Vpn Learned Info

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getIPv6VpnLearnedInfo()

		getIPv6VpnLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getIPv6VpnLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getIPv6VpnLearnedInfo(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getIPv6VpnLearnedInfo', payload=payload, response_object=None)

	def GetLinkStateLearnedInfo(self, *args, **kwargs):
		"""Executes the getLinkStateLearnedInfo operation on the server.

		Get Link State Learned Info

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getLinkStateLearnedInfo()

		getLinkStateLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getLinkStateLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getLinkStateLearnedInfo(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getLinkStateLearnedInfo', payload=payload, response_object=None)

	def GetVPLSLearnedInfo(self, *args, **kwargs):
		"""Executes the getVPLSLearnedInfo operation on the server.

		Get VPLS Learned Info

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getVPLSLearnedInfo()

		getVPLSLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getVPLSLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getVPLSLearnedInfo(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getVPLSLearnedInfo', payload=payload, response_object=None)

	def GracefulRestart(self, *args, **kwargs):
		"""Executes the gracefulRestart operation on the server.

		Graceful restart Peers on selected Peer Ranges

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		gracefulRestart(Restart_time:number)
			Args:
				args[0] is Restart_time (number): This parameter requires a restart_time of type kInteger

		gracefulRestart(Restart_time:number, SessionIndices:list)
			Args:
				args[0] is Restart_time (number): This parameter requires a restart_time of type kInteger
				args[1] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		gracefulRestart(SessionIndices:string, Restart_time:number)
			Args:
				args[0] is SessionIndices (str): This parameter requires a restart_time of type kInteger
				args[1] is Restart_time (number): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('gracefulRestart', payload=payload, response_object=None)

	def Gracefulrestart(self, *args, **kwargs):
		"""Executes the gracefulrestart operation on the server.

		Graceful restart Peers on selected Peer Ranges.

		gracefulrestart(Arg2:list, Arg3:number)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
				args[1] is Arg3 (number): Restart After Time(in secs).

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('gracefulrestart', payload=payload, response_object=None)

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

	def ResumeKeepAlive(self, *args, **kwargs):
		"""Executes the resumeKeepAlive operation on the server.

		Resume sending KeepAlive

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		resumeKeepAlive()

		resumeKeepAlive(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		resumeKeepAlive(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('resumeKeepAlive', payload=payload, response_object=None)

	def Resumekeepalive(self, *args, **kwargs):
		"""Executes the resumekeepalive operation on the server.

		Start Sending Keep Alive Messages.

		resumekeepalive(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('resumekeepalive', payload=payload, response_object=None)

	def ResumeTCPSession(self, *args, **kwargs):
		"""Executes the resumeTCPSession operation on the server.

		Resume TCP Session

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		resumeTCPSession(Notification_code:number, Notification_sub_code:number)
			Args:
				args[0] is Notification_code (number): This parameter requires a notification_code of type kInteger
				args[1] is Notification_sub_code (number): This parameter requires a notification_sub_code of type kInteger

		resumeTCPSession(Notification_code:number, Notification_sub_code:number, SessionIndices:list)
			Args:
				args[0] is Notification_code (number): This parameter requires a notification_code of type kInteger
				args[1] is Notification_sub_code (number): This parameter requires a notification_sub_code of type kInteger
				args[2] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		resumeTCPSession(SessionIndices:string, Notification_code:number, Notification_sub_code:number)
			Args:
				args[0] is SessionIndices (str): This parameter requires a notification_code of type kInteger
				args[1] is Notification_code (number): This parameter requires a notification_sub_code of type kInteger
				args[2] is Notification_sub_code (number): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('resumeTCPSession', payload=payload, response_object=None)

	def Resumetcpsession(self, *args, **kwargs):
		"""Executes the resumetcpsession operation on the server.

		Resume BGP Peer Range TCP Session.

		resumetcpsession(Arg2:list, Arg3:number, Arg4:number)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
				args[1] is Arg3 (number): Notification Code
				args[2] is Arg4 (number): Notification Sub Code

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('resumetcpsession', payload=payload, response_object=None)

	def Start(self, *args, **kwargs):
		"""Executes the start operation on the server.

		Start BGP Peer

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

		Stop BGP Peer

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

	def StopKeepAlive(self, *args, **kwargs):
		"""Executes the stopKeepAlive operation on the server.

		Stop sending KeepAlive

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		stopKeepAlive()

		stopKeepAlive(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		stopKeepAlive(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('stopKeepAlive', payload=payload, response_object=None)

	def Stopkeepalive(self, *args, **kwargs):
		"""Executes the stopkeepalive operation on the server.

		Stop Sending Keep Alive Messages.

		stopkeepalive(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('stopkeepalive', payload=payload, response_object=None)
