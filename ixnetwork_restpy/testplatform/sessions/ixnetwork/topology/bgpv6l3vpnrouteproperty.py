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


class BgpV6L3VpnRouteProperty(Base):
	"""BGP+ L3-VPN Route Range Properties
	The BgpV6L3VpnRouteProperty class encapsulates a list of bgpV6L3VpnRouteProperty resources that is be managed by the user.
	A list of resources can be retrieved from the server using the BgpV6L3VpnRouteProperty.find() method.
	The list can be managed by the user by using the BgpV6L3VpnRouteProperty.add() and BgpV6L3VpnRouteProperty.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'bgpV6L3VpnRouteProperty'

	def __init__(self, parent):
		super(BgpV6L3VpnRouteProperty, self).__init__(parent)

	@property
	def BgpAsPathSegmentList(self):
		"""An instance of the BgpAsPathSegmentList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpaspathsegmentlist.BgpAsPathSegmentList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpaspathsegmentlist import BgpAsPathSegmentList
		return BgpAsPathSegmentList(self)

	@property
	def BgpClusterIdList(self):
		"""An instance of the BgpClusterIdList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpclusteridlist.BgpClusterIdList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpclusteridlist import BgpClusterIdList
		return BgpClusterIdList(self)

	@property
	def BgpCommunitiesList(self):
		"""An instance of the BgpCommunitiesList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpcommunitieslist.BgpCommunitiesList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpcommunitieslist import BgpCommunitiesList
		return BgpCommunitiesList(self)

	@property
	def BgpExtendedCommunitiesList(self):
		"""An instance of the BgpExtendedCommunitiesList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpextendedcommunitieslist.BgpExtendedCommunitiesList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpextendedcommunitieslist import BgpExtendedCommunitiesList
		return BgpExtendedCommunitiesList(self)

	@property
	def BgpNonVPNRRLargeCommunitiesList(self):
		"""An instance of the BgpNonVPNRRLargeCommunitiesList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpnonvpnrrlargecommunitieslist.BgpNonVPNRRLargeCommunitiesList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpnonvpnrrlargecommunitieslist import BgpNonVPNRRLargeCommunitiesList
		return BgpNonVPNRRLargeCommunitiesList(self)

	@property
	def CMacProperties(self):
		"""An instance of the CMacProperties class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties.CMacProperties)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties import CMacProperties
		return CMacProperties(self)

	@property
	def EvpnIPv4PrefixRange(self):
		"""An instance of the EvpnIPv4PrefixRange class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange.EvpnIPv4PrefixRange)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange import EvpnIPv4PrefixRange
		return EvpnIPv4PrefixRange(self)

	@property
	def EvpnIPv6PrefixRange(self):
		"""An instance of the EvpnIPv6PrefixRange class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange.EvpnIPv6PrefixRange)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange import EvpnIPv6PrefixRange
		return EvpnIPv6PrefixRange(self)

	@property
	def OverridePeerAsSetMode(self):
		"""Override Peer AS# Set Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('OverridePeerAsSetMode')

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def AdvSrv6SidInIgp(self):
		"""Advertise SRv6 SID Locator in IGP (ISIS)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('advSrv6SidInIgp')

	@property
	def AdvertiseNexthopAsV4(self):
		"""Advertise Nexthop as V4

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('advertiseNexthopAsV4')

	@property
	def AggregatorAs(self):
		"""Aggregator AS

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('aggregatorAs')

	@property
	def AggregatorId(self):
		"""Aggregator ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('aggregatorId')

	@property
	def AggregatorIdMode(self):
		"""Aggregator ID Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('aggregatorIdMode')

	@property
	def AsNumSuffixRange(self):
		"""Supported Formats: value value1-value2 Values or value ranges separated by comma(,). e.g. 100,150-200,400,600-800 etc. Cannot be kept empty. Should be >= (Max Number of AS Path Segments) x (Max AS Numbers Per Segment)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('asNumSuffixRange')

	@property
	def AsPathASString(self):
		"""Displays configured AS paths. Random AS paths are appended after Non-Random AS paths when configured. Each row displays the AS Path configured for the 1st route of a Route Range.

		Returns:
			list(str)
		"""
		return self._get_attribute('asPathASString')

	@property
	def AsPathPerRoute(self):
		"""When there are multiple routes in a route range, this option decides whether to use same or different AS paths randomly generated for all the routes within that route range. For the Different option, each route will be sent in different update messages.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('asPathPerRoute')

	@property
	def AsRandomSeed(self):
		"""Seed value decides the way the AS Values are generated. To generate different AS Paths for different Route ranges, select unique Seed Values.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('asRandomSeed')

	@property
	def AsSegDist(self):
		"""Type of AS Segment generated. If user selects Random, then any of the four types (AS-SET, AS-SEQ, AS-SET-CONFEDERATION, AS-SEQ-CONFEDERATION) will get randomly generated.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('asSegDist')

	@property
	def AsSetMode(self):
		"""AS# Set Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('asSetMode')

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def Delay(self):
		"""Delay in Seconds

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('delay')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def DistinguisherAsNumber(self):
		"""L3VPN RR Distinguisher AS Number (2-byte or 4-Byte)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('distinguisherAsNumber')

	@property
	def DistinguisherAssignedNumber(self):
		"""L3VPN RR Distinguisher Assigned Number

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('distinguisherAssignedNumber')

	@property
	def DistinguisherIpAddress(self):
		"""L3VPN RR Distinguisher IP Address

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('distinguisherIpAddress')

	@property
	def DistinguisherType(self):
		"""L3VPN RR Distinguisher Type

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('distinguisherType')

	@property
	def Downtime(self):
		"""Downtime In Seconds

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('downtime')

	@property
	def EnableAggregatorId(self):
		"""Enable Aggregator ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableAggregatorId')

	@property
	def EnableAsPathSegments(self):
		"""Enable Non-Random AS Path Segments

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableAsPathSegments')

	@property
	def EnableAtomicAggregate(self):
		"""Enable Atomic Aggregate

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableAtomicAggregate')

	@property
	def EnableCluster(self):
		"""Enable Cluster

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableCluster')

	@property
	def EnableCommunity(self):
		"""Enable Community

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableCommunity')

	@property
	def EnableExtendedCommunity(self):
		"""Enable Extended Community

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableExtendedCommunity')

	@property
	def EnableFlapping(self):
		"""Enable Flapping

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableFlapping')

	@property
	def EnableIpv6Receiver(self):
		"""Enable IPv6 Receiver

		Returns:
			bool
		"""
		return self._get_attribute('enableIpv6Receiver')
	@EnableIpv6Receiver.setter
	def EnableIpv6Receiver(self, value):
		self._set_attribute('enableIpv6Receiver', value)

	@property
	def EnableIpv6Sender(self):
		"""Enable IPv6 Sender

		Returns:
			bool
		"""
		return self._get_attribute('enableIpv6Sender')
	@EnableIpv6Sender.setter
	def EnableIpv6Sender(self, value):
		self._set_attribute('enableIpv6Sender', value)

	@property
	def EnableLargeCommunities(self):
		"""Enable Large Communities Attribute

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableLargeCommunities')

	@property
	def EnableLocalPreference(self):
		"""Enable Local Preference

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableLocalPreference')

	@property
	def EnableMultiExitDiscriminator(self):
		"""Enable Multi Exit

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableMultiExitDiscriminator')

	@property
	def EnableNextHop(self):
		"""Enable Next Hop

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableNextHop')

	@property
	def EnableOrigin(self):
		"""Enable Origin

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableOrigin')

	@property
	def EnableOriginatorId(self):
		"""Enable Originator ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableOriginatorId')

	@property
	def EnableRandomAsPath(self):
		"""Enables generation/advertisement of Random AS Path Segments.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableRandomAsPath')

	@property
	def EnableSrv6Sid(self):
		"""Enable SRv6 SID With VPN Route

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableSrv6Sid')

	@property
	def EnableWeight(self):
		"""Enable Weight

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableWeight')

	@property
	def FlapFromRouteIndex(self):
		"""Flap From Route Index

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('flapFromRouteIndex')

	@property
	def FlapToRouteIndex(self):
		"""Flap To Route Index

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('flapToRouteIndex')

	@property
	def IncludeRdInNextHopLength(self):
		"""If RD is included in NH Len then NH Len is NH size + RD size else NH len is NH size.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeRdInNextHopLength')

	@property
	def IncludeSourceAsExtComm(self):
		"""Include Source AS ExtComm

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeSourceAsExtComm')

	@property
	def IncludeVrfRouteImportExtComm(self):
		"""Include VRF Route Import ExtComm

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeVrfRouteImportExtComm')

	@property
	def Ipv4NextHop(self):
		"""IPv4 Next Hop

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv4NextHop')

	@property
	def Ipv6NextHop(self):
		"""IPv6 Next Hop

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6NextHop')

	@property
	def LabelEnd(self):
		"""L3VPN RR Label End

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('labelEnd')

	@property
	def LabelMode(self):
		"""L3VPN RR Label Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('labelMode')

	@property
	def LabelSpaceId(self):
		"""L3VPN RR Label Space ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('labelSpaceId')

	@property
	def LabelStart(self):
		"""L3VPN RR Label Start

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('labelStart')

	@property
	def LabelStep(self):
		"""L3VPN RR Label Step

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('labelStep')

	@property
	def LocalPreference(self):
		"""Local Preference

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('localPreference')

	@property
	def MaxASNumPerSegment(self):
		"""Maximum Number Of AS Numbers generated per Segment

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('maxASNumPerSegment')

	@property
	def MaxNoOfASPathSegmentsPerRouteRange(self):
		"""Maximum Number Of AS Path Segments Per Route Range.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('maxNoOfASPathSegmentsPerRouteRange')

	@property
	def MinASNumPerSegment(self):
		"""Minimum Number Of AS Numbers generated per Segments.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('minASNumPerSegment')

	@property
	def MinNoOfASPathSegmentsPerRouteRange(self):
		"""Minimum Number Of AS Path Segments Per Route Range.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('minNoOfASPathSegmentsPerRouteRange')

	@property
	def MultiExitDiscriminator(self):
		"""Multi Exit

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('multiExitDiscriminator')

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
	def NextHopIPType(self):
		"""Set Next Hop IP Type

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('nextHopIPType')

	@property
	def NextHopIncrementMode(self):
		"""Next Hop Increment Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('nextHopIncrementMode')

	@property
	def NextHopType(self):
		"""Set Next Hop

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('nextHopType')

	@property
	def NoOfASPathSegmentsPerRouteRange(self):
		"""Number Of non-random or manually configured AS Path Segments Per Route Range

		Returns:
			number
		"""
		return self._get_attribute('noOfASPathSegmentsPerRouteRange')
	@NoOfASPathSegmentsPerRouteRange.setter
	def NoOfASPathSegmentsPerRouteRange(self, value):
		self._set_attribute('noOfASPathSegmentsPerRouteRange', value)

	@property
	def NoOfClusters(self):
		"""Number of Clusters

		Returns:
			number
		"""
		return self._get_attribute('noOfClusters')
	@NoOfClusters.setter
	def NoOfClusters(self, value):
		self._set_attribute('noOfClusters', value)

	@property
	def NoOfCommunities(self):
		"""Number of Communities

		Returns:
			number
		"""
		return self._get_attribute('noOfCommunities')
	@NoOfCommunities.setter
	def NoOfCommunities(self, value):
		self._set_attribute('noOfCommunities', value)

	@property
	def NoOfExternalCommunities(self):
		"""Number of Extended Communities

		Returns:
			number
		"""
		return self._get_attribute('noOfExternalCommunities')
	@NoOfExternalCommunities.setter
	def NoOfExternalCommunities(self, value):
		self._set_attribute('noOfExternalCommunities', value)

	@property
	def NoOfLargeCommunities(self):
		"""Number of Large Communities (Should be in the range 1-32)

		Returns:
			number
		"""
		return self._get_attribute('noOfLargeCommunities')
	@NoOfLargeCommunities.setter
	def NoOfLargeCommunities(self, value):
		self._set_attribute('noOfLargeCommunities', value)

	@property
	def Origin(self):
		"""Origin

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('origin')

	@property
	def OriginatorId(self):
		"""Originator ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('originatorId')

	@property
	def PackingFrom(self):
		"""Packing From

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('packingFrom')

	@property
	def PackingTo(self):
		"""Packing To

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('packingTo')

	@property
	def PartialFlap(self):
		"""Partial Flap

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('partialFlap')

	@property
	def SendSRv6SIDOptionalInfo(self):
		"""If we need to advertise SRv6 SID Optional Information (Service Information sub-TLV) which is specified in next column(s)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sendSRv6SIDOptionalInfo')

	@property
	def Srv6EndpointBehavior(self):
		"""SRv6 Endpoint Behavior field Value for all routes in this Route Range

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6EndpointBehavior')

	@property
	def Srv6SIDOptionalInformation(self):
		"""SRv6 SID Optional Information field Value (Service Information sub-TLV) for all routes in this Route Range

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6SIDOptionalInformation')

	@property
	def Srv6SidFlags(self):
		"""SRv6 SID Flags field Value for all route in this Route Range

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6SidFlags')

	@property
	def Srv6SidFuncAllocType(self):
		"""DEPRECATED SRv6 Func Allocation Type

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6SidFuncAllocType')

	@property
	def Srv6SidLoc(self):
		"""SRv6 SID. It consists of Locator, Func and Args

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6SidLoc')

	@property
	def Srv6SidLocLen(self):
		"""SRv6 SID Locator Length to be advertised in IGP

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6SidLocLen')

	@property
	def Srv6SidLocMetric(self):
		"""SRv6 SID Locator Metric for advertisement in IGP

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6SidLocMetric')

	@property
	def Srv6SidReserved(self):
		"""SRv6 SID Reserved Value (SRv6 SID Service TLV Level)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6SidReserved')

	@property
	def Srv6SidReserved1(self):
		"""SRv6 SID Reserved1 Field for Service Information sub-TLV

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6SidReserved1')

	@property
	def Srv6SidReserved2(self):
		"""SRv6 SID Reserved2 Field for Service Information sub-TLV

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6SidReserved2')

	@property
	def Srv6SidStep(self):
		"""Route Range SRv6 SID Step

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6SidStep')

	@property
	def Uptime(self):
		"""Uptime In Seconds

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('uptime')

	@property
	def UseAsIpv6UmhRoutes(self):
		"""Use As IPv6 UMH Routes

		Returns:
			bool
		"""
		return self._get_attribute('useAsIpv6UmhRoutes')
	@UseAsIpv6UmhRoutes.setter
	def UseAsIpv6UmhRoutes(self, value):
		self._set_attribute('useAsIpv6UmhRoutes', value)

	@property
	def UseAsUmhRoutes(self):
		"""DEPRECATED Use As UMH Routes

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('useAsUmhRoutes')

	@property
	def UseTraditionalNlri(self):
		"""Use Traditional NLRI

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('useTraditionalNlri')

	@property
	def Weight(self):
		"""Weight

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('weight')

	def update(self, EnableIpv6Receiver=None, EnableIpv6Sender=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExternalCommunities=None, NoOfLargeCommunities=None, UseAsIpv6UmhRoutes=None):
		"""Updates a child instance of bgpV6L3VpnRouteProperty on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			EnableIpv6Receiver (bool): Enable IPv6 Receiver
			EnableIpv6Sender (bool): Enable IPv6 Sender
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of non-random or manually configured AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExternalCommunities (number): Number of Extended Communities
			NoOfLargeCommunities (number): Number of Large Communities (Should be in the range 1-32)
			UseAsIpv6UmhRoutes (bool): Use As IPv6 UMH Routes

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, EnableIpv6Receiver=None, EnableIpv6Sender=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExternalCommunities=None, NoOfLargeCommunities=None, UseAsIpv6UmhRoutes=None):
		"""Adds a new bgpV6L3VpnRouteProperty node on the server and retrieves it in this instance.

		Args:
			EnableIpv6Receiver (bool): Enable IPv6 Receiver
			EnableIpv6Sender (bool): Enable IPv6 Sender
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of non-random or manually configured AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExternalCommunities (number): Number of Extended Communities
			NoOfLargeCommunities (number): Number of Large Communities (Should be in the range 1-32)
			UseAsIpv6UmhRoutes (bool): Use As IPv6 UMH Routes

		Returns:
			self: This instance with all currently retrieved bgpV6L3VpnRouteProperty data using find and the newly added bgpV6L3VpnRouteProperty data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the bgpV6L3VpnRouteProperty data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, AsPathASString=None, Count=None, DescriptiveName=None, EnableIpv6Receiver=None, EnableIpv6Sender=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExternalCommunities=None, NoOfLargeCommunities=None, UseAsIpv6UmhRoutes=None):
		"""Finds and retrieves bgpV6L3VpnRouteProperty data from the server.

		All named parameters support regex and can be used to selectively retrieve bgpV6L3VpnRouteProperty data from the server.
		By default the find method takes no parameters and will retrieve all bgpV6L3VpnRouteProperty data from the server.

		Args:
			AsPathASString (list(str)): Displays configured AS paths. Random AS paths are appended after Non-Random AS paths when configured. Each row displays the AS Path configured for the 1st route of a Route Range.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
			EnableIpv6Receiver (bool): Enable IPv6 Receiver
			EnableIpv6Sender (bool): Enable IPv6 Sender
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfASPathSegmentsPerRouteRange (number): Number Of non-random or manually configured AS Path Segments Per Route Range
			NoOfClusters (number): Number of Clusters
			NoOfCommunities (number): Number of Communities
			NoOfExternalCommunities (number): Number of Extended Communities
			NoOfLargeCommunities (number): Number of Large Communities (Should be in the range 1-32)
			UseAsIpv6UmhRoutes (bool): Use As IPv6 UMH Routes

		Returns:
			self: This instance with matching bgpV6L3VpnRouteProperty data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of bgpV6L3VpnRouteProperty data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the bgpV6L3VpnRouteProperty data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, OverridePeerAsSetMode=None, Active=None, AdvSrv6SidInIgp=None, AdvertiseNexthopAsV4=None, AggregatorAs=None, AggregatorId=None, AggregatorIdMode=None, AsNumSuffixRange=None, AsPathPerRoute=None, AsRandomSeed=None, AsSegDist=None, AsSetMode=None, Delay=None, DistinguisherAsNumber=None, DistinguisherAssignedNumber=None, DistinguisherIpAddress=None, DistinguisherType=None, Downtime=None, EnableAggregatorId=None, EnableAsPathSegments=None, EnableAtomicAggregate=None, EnableCluster=None, EnableCommunity=None, EnableExtendedCommunity=None, EnableFlapping=None, EnableLargeCommunities=None, EnableLocalPreference=None, EnableMultiExitDiscriminator=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, EnableRandomAsPath=None, EnableSrv6Sid=None, EnableWeight=None, FlapFromRouteIndex=None, FlapToRouteIndex=None, IncludeRdInNextHopLength=None, IncludeSourceAsExtComm=None, IncludeVrfRouteImportExtComm=None, Ipv4NextHop=None, Ipv6NextHop=None, LabelEnd=None, LabelMode=None, LabelSpaceId=None, LabelStart=None, LabelStep=None, LocalPreference=None, MaxASNumPerSegment=None, MaxNoOfASPathSegmentsPerRouteRange=None, MinASNumPerSegment=None, MinNoOfASPathSegmentsPerRouteRange=None, MultiExitDiscriminator=None, NextHopIPType=None, NextHopIncrementMode=None, NextHopType=None, Origin=None, OriginatorId=None, PackingFrom=None, PackingTo=None, PartialFlap=None, SendSRv6SIDOptionalInfo=None, Srv6EndpointBehavior=None, Srv6SIDOptionalInformation=None, Srv6SidFlags=None, Srv6SidFuncAllocType=None, Srv6SidLoc=None, Srv6SidLocLen=None, Srv6SidLocMetric=None, Srv6SidReserved=None, Srv6SidReserved1=None, Srv6SidReserved2=None, Srv6SidStep=None, Uptime=None, UseAsUmhRoutes=None, UseTraditionalNlri=None, Weight=None):
		"""Base class infrastructure that gets a list of bgpV6L3VpnRouteProperty device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			OverridePeerAsSetMode (str): optional regex of OverridePeerAsSetMode
			Active (str): optional regex of active
			AdvSrv6SidInIgp (str): optional regex of advSrv6SidInIgp
			AdvertiseNexthopAsV4 (str): optional regex of advertiseNexthopAsV4
			AggregatorAs (str): optional regex of aggregatorAs
			AggregatorId (str): optional regex of aggregatorId
			AggregatorIdMode (str): optional regex of aggregatorIdMode
			AsNumSuffixRange (str): optional regex of asNumSuffixRange
			AsPathPerRoute (str): optional regex of asPathPerRoute
			AsRandomSeed (str): optional regex of asRandomSeed
			AsSegDist (str): optional regex of asSegDist
			AsSetMode (str): optional regex of asSetMode
			Delay (str): optional regex of delay
			DistinguisherAsNumber (str): optional regex of distinguisherAsNumber
			DistinguisherAssignedNumber (str): optional regex of distinguisherAssignedNumber
			DistinguisherIpAddress (str): optional regex of distinguisherIpAddress
			DistinguisherType (str): optional regex of distinguisherType
			Downtime (str): optional regex of downtime
			EnableAggregatorId (str): optional regex of enableAggregatorId
			EnableAsPathSegments (str): optional regex of enableAsPathSegments
			EnableAtomicAggregate (str): optional regex of enableAtomicAggregate
			EnableCluster (str): optional regex of enableCluster
			EnableCommunity (str): optional regex of enableCommunity
			EnableExtendedCommunity (str): optional regex of enableExtendedCommunity
			EnableFlapping (str): optional regex of enableFlapping
			EnableLargeCommunities (str): optional regex of enableLargeCommunities
			EnableLocalPreference (str): optional regex of enableLocalPreference
			EnableMultiExitDiscriminator (str): optional regex of enableMultiExitDiscriminator
			EnableNextHop (str): optional regex of enableNextHop
			EnableOrigin (str): optional regex of enableOrigin
			EnableOriginatorId (str): optional regex of enableOriginatorId
			EnableRandomAsPath (str): optional regex of enableRandomAsPath
			EnableSrv6Sid (str): optional regex of enableSrv6Sid
			EnableWeight (str): optional regex of enableWeight
			FlapFromRouteIndex (str): optional regex of flapFromRouteIndex
			FlapToRouteIndex (str): optional regex of flapToRouteIndex
			IncludeRdInNextHopLength (str): optional regex of includeRdInNextHopLength
			IncludeSourceAsExtComm (str): optional regex of includeSourceAsExtComm
			IncludeVrfRouteImportExtComm (str): optional regex of includeVrfRouteImportExtComm
			Ipv4NextHop (str): optional regex of ipv4NextHop
			Ipv6NextHop (str): optional regex of ipv6NextHop
			LabelEnd (str): optional regex of labelEnd
			LabelMode (str): optional regex of labelMode
			LabelSpaceId (str): optional regex of labelSpaceId
			LabelStart (str): optional regex of labelStart
			LabelStep (str): optional regex of labelStep
			LocalPreference (str): optional regex of localPreference
			MaxASNumPerSegment (str): optional regex of maxASNumPerSegment
			MaxNoOfASPathSegmentsPerRouteRange (str): optional regex of maxNoOfASPathSegmentsPerRouteRange
			MinASNumPerSegment (str): optional regex of minASNumPerSegment
			MinNoOfASPathSegmentsPerRouteRange (str): optional regex of minNoOfASPathSegmentsPerRouteRange
			MultiExitDiscriminator (str): optional regex of multiExitDiscriminator
			NextHopIPType (str): optional regex of nextHopIPType
			NextHopIncrementMode (str): optional regex of nextHopIncrementMode
			NextHopType (str): optional regex of nextHopType
			Origin (str): optional regex of origin
			OriginatorId (str): optional regex of originatorId
			PackingFrom (str): optional regex of packingFrom
			PackingTo (str): optional regex of packingTo
			PartialFlap (str): optional regex of partialFlap
			SendSRv6SIDOptionalInfo (str): optional regex of sendSRv6SIDOptionalInfo
			Srv6EndpointBehavior (str): optional regex of srv6EndpointBehavior
			Srv6SIDOptionalInformation (str): optional regex of srv6SIDOptionalInformation
			Srv6SidFlags (str): optional regex of srv6SidFlags
			Srv6SidFuncAllocType (str): optional regex of srv6SidFuncAllocType
			Srv6SidLoc (str): optional regex of srv6SidLoc
			Srv6SidLocLen (str): optional regex of srv6SidLocLen
			Srv6SidLocMetric (str): optional regex of srv6SidLocMetric
			Srv6SidReserved (str): optional regex of srv6SidReserved
			Srv6SidReserved1 (str): optional regex of srv6SidReserved1
			Srv6SidReserved2 (str): optional regex of srv6SidReserved2
			Srv6SidStep (str): optional regex of srv6SidStep
			Uptime (str): optional regex of uptime
			UseAsUmhRoutes (str): optional regex of useAsUmhRoutes
			UseTraditionalNlri (str): optional regex of useTraditionalNlri
			Weight (str): optional regex of weight

		Returns:
			list(int): A list of device ids that meets the regex criteria provided in the method parameters

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._get_ngpf_device_ids(locals())

	def AgeOutRoutes(self, *args, **kwargs):
		"""Executes the ageOutRoutes operation on the server.

		Age out percentage of BGP Routes in a Route Range

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		ageOutRoutes(Percentage:number)
			Args:
				args[0] is Percentage (number): This parameter requires a percentage of type kInteger

		ageOutRoutes(Percentage:number, SessionIndices:list)
			Args:
				args[0] is Percentage (number): This parameter requires a percentage of type kInteger
				args[1] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		ageOutRoutes(SessionIndices:string, Percentage:number)
			Args:
				args[0] is SessionIndices (str): This parameter requires a percentage of type kInteger
				args[1] is Percentage (number): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('ageOutRoutes', payload=payload, response_object=None)

	def Ageoutroutes(self, *args, **kwargs):
		"""Executes the ageoutroutes operation on the server.

		Completely/Partially age out routes contained in this route range.

		ageoutroutes(Arg2:list, Arg3:number)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
				args[1] is Arg3 (number): What percentage of routes to age out. 100% means all routes.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('ageoutroutes', payload=payload, response_object=None)

	def EnableIpv4Receiver(self, *args, **kwargs):
		"""Executes the enableIpv4Receiver operation on the server.

		Activate or Deactivate Ipv4 Multicast Receiver Site

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		enableIpv4Receiver()

		enableIpv4Receiver(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		enableIpv4Receiver(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('enableIpv4Receiver', payload=payload, response_object=None)

	def EnableIpv4Sender(self, *args, **kwargs):
		"""Executes the enableIpv4Sender operation on the server.

		Activate or Deactivate Ipv4 Multicast Sender Site

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		enableIpv4Sender()

		enableIpv4Sender(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		enableIpv4Sender(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('enableIpv4Sender', payload=payload, response_object=None)

	def EnableIpv6Receiver(self, *args, **kwargs):
		"""Executes the enableIpv6Receiver operation on the server.

		Activate or Deactivate Ipv6 Multicast Receiver Site

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		enableIpv6Receiver()

		enableIpv6Receiver(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		enableIpv6Receiver(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('enableIpv6Receiver', payload=payload, response_object=None)

	def EnableIpv6Sender(self, *args, **kwargs):
		"""Executes the enableIpv6Sender operation on the server.

		Activate or Deactivate Ipv6 Multicast Sender Site

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		enableIpv6Sender()

		enableIpv6Sender(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		enableIpv6Sender(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('enableIpv6Sender', payload=payload, response_object=None)

	def ReadvertiseRoutes(self, *args, **kwargs):
		"""Executes the readvertiseRoutes operation on the server.

		Re-advertise Aged out BGP Routes in a Route Range

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		readvertiseRoutes()

		readvertiseRoutes(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		readvertiseRoutes(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('readvertiseRoutes', payload=payload, response_object=None)

	def Readvertiseroutes(self, *args, **kwargs):
		"""Executes the readvertiseroutes operation on the server.

		Readvertise only the aged-out routes contained in this route range.

		readvertiseroutes(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('readvertiseroutes', payload=payload, response_object=None)

	def Start(self, *args, **kwargs):
		"""Executes the start operation on the server.

		Start BGP Route Range

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

		Stop BGP Route Range

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

	def UseAsIpv4UmhRoutes(self, *args, **kwargs):
		"""Executes the useAsIpv4UmhRoutes operation on the server.

		Activate Deactivate Ipv4 UMH Route Selection

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		useAsIpv4UmhRoutes()

		useAsIpv4UmhRoutes(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		useAsIpv4UmhRoutes(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('useAsIpv4UmhRoutes', payload=payload, response_object=None)

	def UseAsIpv6UmhRoutes(self, *args, **kwargs):
		"""Executes the useAsIpv6UmhRoutes operation on the server.

		Activate Deactivate Ipv6 UMH Route Selection

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		useAsIpv6UmhRoutes()

		useAsIpv6UmhRoutes(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		useAsIpv6UmhRoutes(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('useAsIpv6UmhRoutes', payload=payload, response_object=None)
