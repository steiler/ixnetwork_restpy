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


class Wildcards(Base):
	"""Select the type of wildcard capability that the table will support.
	The Wildcards class encapsulates a required wildcards resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'wildcards'

	def __init__(self, parent):
		super(Wildcards, self).__init__(parent)

	@property
	def ArpDestinationHardwareAddress(self):
		"""If selected, Wildcards ARP Source Hardware Address is supported.

		Returns:
			bool
		"""
		return self._get_attribute('arpDestinationHardwareAddress')
	@ArpDestinationHardwareAddress.setter
	def ArpDestinationHardwareAddress(self, value):
		self._set_attribute('arpDestinationHardwareAddress', value)

	@property
	def ArpDestinationIpv4Address(self):
		"""If selected, Wildcards ARP Destination IPv4 Address is supported.

		Returns:
			bool
		"""
		return self._get_attribute('arpDestinationIpv4Address')
	@ArpDestinationIpv4Address.setter
	def ArpDestinationIpv4Address(self, value):
		self._set_attribute('arpDestinationIpv4Address', value)

	@property
	def ArpOpcode(self):
		"""If selected, Wildcards ARP Opcode is supported.

		Returns:
			bool
		"""
		return self._get_attribute('arpOpcode')
	@ArpOpcode.setter
	def ArpOpcode(self, value):
		self._set_attribute('arpOpcode', value)

	@property
	def ArpSourceHardwareAddress(self):
		"""If selected, Wildcards ARP Source Hardware Address is supported.

		Returns:
			bool
		"""
		return self._get_attribute('arpSourceHardwareAddress')
	@ArpSourceHardwareAddress.setter
	def ArpSourceHardwareAddress(self, value):
		self._set_attribute('arpSourceHardwareAddress', value)

	@property
	def ArpSourceIpv4Address(self):
		"""If selected, Wildcards ARP Source IPv4 Address is supported.

		Returns:
			bool
		"""
		return self._get_attribute('arpSourceIpv4Address')
	@ArpSourceIpv4Address.setter
	def ArpSourceIpv4Address(self, value):
		self._set_attribute('arpSourceIpv4Address', value)

	@property
	def EthernetDestination(self):
		"""If selected, Wildcards Ethernet Destination is supported.

		Returns:
			bool
		"""
		return self._get_attribute('ethernetDestination')
	@EthernetDestination.setter
	def EthernetDestination(self, value):
		self._set_attribute('ethernetDestination', value)

	@property
	def EthernetSource(self):
		"""If selected, Wildcards Ethernet Source is supported.

		Returns:
			bool
		"""
		return self._get_attribute('ethernetSource')
	@EthernetSource.setter
	def EthernetSource(self, value):
		self._set_attribute('ethernetSource', value)

	@property
	def EthernetType(self):
		"""If selected, Wildcards Ethernet Type is supported.

		Returns:
			bool
		"""
		return self._get_attribute('ethernetType')
	@EthernetType.setter
	def EthernetType(self, value):
		self._set_attribute('ethernetType', value)

	@property
	def Experimenter(self):
		"""If selected, Wildcards Experimenter is supported.

		Returns:
			bool
		"""
		return self._get_attribute('experimenter')
	@Experimenter.setter
	def Experimenter(self, value):
		self._set_attribute('experimenter', value)

	@property
	def IcmpCode(self):
		"""If selected, Wildcards ICMP Code is supported.

		Returns:
			bool
		"""
		return self._get_attribute('icmpCode')
	@IcmpCode.setter
	def IcmpCode(self, value):
		self._set_attribute('icmpCode', value)

	@property
	def IcmpType(self):
		"""If selected, Wildcards ICMP Type is supported.

		Returns:
			bool
		"""
		return self._get_attribute('icmpType')
	@IcmpType.setter
	def IcmpType(self, value):
		self._set_attribute('icmpType', value)

	@property
	def Icmpv6Code(self):
		"""If selected, Wildcards ICMPv6 Code is supported.

		Returns:
			bool
		"""
		return self._get_attribute('icmpv6Code')
	@Icmpv6Code.setter
	def Icmpv6Code(self, value):
		self._set_attribute('icmpv6Code', value)

	@property
	def Icmpv6Type(self):
		"""If selected, Wildcards ICMPv6 Type is supported.

		Returns:
			bool
		"""
		return self._get_attribute('icmpv6Type')
	@Icmpv6Type.setter
	def Icmpv6Type(self, value):
		self._set_attribute('icmpv6Type', value)

	@property
	def InPort(self):
		"""If selected, Wildcards In Port is supported.

		Returns:
			bool
		"""
		return self._get_attribute('inPort')
	@InPort.setter
	def InPort(self, value):
		self._set_attribute('inPort', value)

	@property
	def IpDscp(self):
		"""If selected, Wildcards IP DSCP is supported.

		Returns:
			bool
		"""
		return self._get_attribute('ipDscp')
	@IpDscp.setter
	def IpDscp(self, value):
		self._set_attribute('ipDscp', value)

	@property
	def IpEcn(self):
		"""If selected, Wildcards IP ECN is supported.

		Returns:
			bool
		"""
		return self._get_attribute('ipEcn')
	@IpEcn.setter
	def IpEcn(self, value):
		self._set_attribute('ipEcn', value)

	@property
	def IpProtocol(self):
		"""If selected, Wildcards IP Protocol is supported.

		Returns:
			bool
		"""
		return self._get_attribute('ipProtocol')
	@IpProtocol.setter
	def IpProtocol(self, value):
		self._set_attribute('ipProtocol', value)

	@property
	def Ipv4Destination(self):
		"""If selected, Wildcards IPv4 Destination is supported.

		Returns:
			bool
		"""
		return self._get_attribute('ipv4Destination')
	@Ipv4Destination.setter
	def Ipv4Destination(self, value):
		self._set_attribute('ipv4Destination', value)

	@property
	def Ipv4Source(self):
		"""If selected, Wildcards IPv4 Source is supported.

		Returns:
			bool
		"""
		return self._get_attribute('ipv4Source')
	@Ipv4Source.setter
	def Ipv4Source(self, value):
		self._set_attribute('ipv4Source', value)

	@property
	def Ipv6Destination(self):
		"""If selected, Wildcards IPv6 Destination is supported.

		Returns:
			bool
		"""
		return self._get_attribute('ipv6Destination')
	@Ipv6Destination.setter
	def Ipv6Destination(self, value):
		self._set_attribute('ipv6Destination', value)

	@property
	def Ipv6ExtHeader(self):
		"""If selected, Wildcards IPv6 Ext Header is supported.

		Returns:
			bool
		"""
		return self._get_attribute('ipv6ExtHeader')
	@Ipv6ExtHeader.setter
	def Ipv6ExtHeader(self, value):
		self._set_attribute('ipv6ExtHeader', value)

	@property
	def Ipv6FlowLabel(self):
		"""If selected, Wildcards IPv6 Flow Label is supported.

		Returns:
			bool
		"""
		return self._get_attribute('ipv6FlowLabel')
	@Ipv6FlowLabel.setter
	def Ipv6FlowLabel(self, value):
		self._set_attribute('ipv6FlowLabel', value)

	@property
	def Ipv6NdSll(self):
		"""If selected, Wildcards IPv6 ND SLL is supported.

		Returns:
			bool
		"""
		return self._get_attribute('ipv6NdSll')
	@Ipv6NdSll.setter
	def Ipv6NdSll(self, value):
		self._set_attribute('ipv6NdSll', value)

	@property
	def Ipv6NdTarget(self):
		"""If selected, Wildcards IPv6 ND Target is supported.

		Returns:
			bool
		"""
		return self._get_attribute('ipv6NdTarget')
	@Ipv6NdTarget.setter
	def Ipv6NdTarget(self, value):
		self._set_attribute('ipv6NdTarget', value)

	@property
	def Ipv6NdTll(self):
		"""If selected, Wildcards IPv6 ND TLL is supported.

		Returns:
			bool
		"""
		return self._get_attribute('ipv6NdTll')
	@Ipv6NdTll.setter
	def Ipv6NdTll(self, value):
		self._set_attribute('ipv6NdTll', value)

	@property
	def Ipv6Source(self):
		"""If selected, Wildcards IPv6 Source is supported.

		Returns:
			bool
		"""
		return self._get_attribute('ipv6Source')
	@Ipv6Source.setter
	def Ipv6Source(self, value):
		self._set_attribute('ipv6Source', value)

	@property
	def Metadata(self):
		"""If selected, Wildcards Metadata is supported.

		Returns:
			bool
		"""
		return self._get_attribute('metadata')
	@Metadata.setter
	def Metadata(self, value):
		self._set_attribute('metadata', value)

	@property
	def MplsBos(self):
		"""If selected, Wildcards MPLS BoS is supported.

		Returns:
			bool
		"""
		return self._get_attribute('mplsBos')
	@MplsBos.setter
	def MplsBos(self, value):
		self._set_attribute('mplsBos', value)

	@property
	def MplsLabel(self):
		"""If selected, Wildcards MPLS Label is supported.

		Returns:
			bool
		"""
		return self._get_attribute('mplsLabel')
	@MplsLabel.setter
	def MplsLabel(self, value):
		self._set_attribute('mplsLabel', value)

	@property
	def MplsTc(self):
		"""If selected, Wildcards MPLS TC is supported.

		Returns:
			bool
		"""
		return self._get_attribute('mplsTc')
	@MplsTc.setter
	def MplsTc(self, value):
		self._set_attribute('mplsTc', value)

	@property
	def PbbIsid(self):
		"""If selected, Wildcards PBB ISID is supported.

		Returns:
			bool
		"""
		return self._get_attribute('pbbIsid')
	@PbbIsid.setter
	def PbbIsid(self, value):
		self._set_attribute('pbbIsid', value)

	@property
	def PhysicalInPort(self):
		"""If selected, Wildcards Physical In Port is supported.

		Returns:
			bool
		"""
		return self._get_attribute('physicalInPort')
	@PhysicalInPort.setter
	def PhysicalInPort(self, value):
		self._set_attribute('physicalInPort', value)

	@property
	def SctpDestination(self):
		"""If selected, Wildcards SCTP Destination is supported.

		Returns:
			bool
		"""
		return self._get_attribute('sctpDestination')
	@SctpDestination.setter
	def SctpDestination(self, value):
		self._set_attribute('sctpDestination', value)

	@property
	def SctpSource(self):
		"""If selected, Wildcards SCTP Source is supported.

		Returns:
			bool
		"""
		return self._get_attribute('sctpSource')
	@SctpSource.setter
	def SctpSource(self, value):
		self._set_attribute('sctpSource', value)

	@property
	def TcpDestination(self):
		"""If selected, Wildcards TCP Destination is supported.

		Returns:
			bool
		"""
		return self._get_attribute('tcpDestination')
	@TcpDestination.setter
	def TcpDestination(self, value):
		self._set_attribute('tcpDestination', value)

	@property
	def TcpSource(self):
		"""If selected, Wildcards TCP Source is supported.

		Returns:
			bool
		"""
		return self._get_attribute('tcpSource')
	@TcpSource.setter
	def TcpSource(self, value):
		self._set_attribute('tcpSource', value)

	@property
	def TunnelId(self):
		"""If selected, Wildcards Tunnel ID is supported.

		Returns:
			bool
		"""
		return self._get_attribute('tunnelId')
	@TunnelId.setter
	def TunnelId(self, value):
		self._set_attribute('tunnelId', value)

	@property
	def UdpDestination(self):
		"""If selected, Wildcards UDP Destination is supported.

		Returns:
			bool
		"""
		return self._get_attribute('udpDestination')
	@UdpDestination.setter
	def UdpDestination(self, value):
		self._set_attribute('udpDestination', value)

	@property
	def UdpSource(self):
		"""If selected, Wildcards UDP Source is supported.

		Returns:
			bool
		"""
		return self._get_attribute('udpSource')
	@UdpSource.setter
	def UdpSource(self, value):
		self._set_attribute('udpSource', value)

	@property
	def VlanId(self):
		"""If selected, Wildcards VLAN ID is supported.

		Returns:
			bool
		"""
		return self._get_attribute('vlanId')
	@VlanId.setter
	def VlanId(self, value):
		self._set_attribute('vlanId', value)

	@property
	def VlanPriority(self):
		"""If selected, Wildcards VLAN Priority is supported.

		Returns:
			bool
		"""
		return self._get_attribute('vlanPriority')
	@VlanPriority.setter
	def VlanPriority(self, value):
		self._set_attribute('vlanPriority', value)

	def update(self, ArpDestinationHardwareAddress=None, ArpDestinationIpv4Address=None, ArpOpcode=None, ArpSourceHardwareAddress=None, ArpSourceIpv4Address=None, EthernetDestination=None, EthernetSource=None, EthernetType=None, Experimenter=None, IcmpCode=None, IcmpType=None, Icmpv6Code=None, Icmpv6Type=None, InPort=None, IpDscp=None, IpEcn=None, IpProtocol=None, Ipv4Destination=None, Ipv4Source=None, Ipv6Destination=None, Ipv6ExtHeader=None, Ipv6FlowLabel=None, Ipv6NdSll=None, Ipv6NdTarget=None, Ipv6NdTll=None, Ipv6Source=None, Metadata=None, MplsBos=None, MplsLabel=None, MplsTc=None, PbbIsid=None, PhysicalInPort=None, SctpDestination=None, SctpSource=None, TcpDestination=None, TcpSource=None, TunnelId=None, UdpDestination=None, UdpSource=None, VlanId=None, VlanPriority=None):
		"""Updates a child instance of wildcards on the server.

		Args:
			ArpDestinationHardwareAddress (bool): If selected, Wildcards ARP Source Hardware Address is supported.
			ArpDestinationIpv4Address (bool): If selected, Wildcards ARP Destination IPv4 Address is supported.
			ArpOpcode (bool): If selected, Wildcards ARP Opcode is supported.
			ArpSourceHardwareAddress (bool): If selected, Wildcards ARP Source Hardware Address is supported.
			ArpSourceIpv4Address (bool): If selected, Wildcards ARP Source IPv4 Address is supported.
			EthernetDestination (bool): If selected, Wildcards Ethernet Destination is supported.
			EthernetSource (bool): If selected, Wildcards Ethernet Source is supported.
			EthernetType (bool): If selected, Wildcards Ethernet Type is supported.
			Experimenter (bool): If selected, Wildcards Experimenter is supported.
			IcmpCode (bool): If selected, Wildcards ICMP Code is supported.
			IcmpType (bool): If selected, Wildcards ICMP Type is supported.
			Icmpv6Code (bool): If selected, Wildcards ICMPv6 Code is supported.
			Icmpv6Type (bool): If selected, Wildcards ICMPv6 Type is supported.
			InPort (bool): If selected, Wildcards In Port is supported.
			IpDscp (bool): If selected, Wildcards IP DSCP is supported.
			IpEcn (bool): If selected, Wildcards IP ECN is supported.
			IpProtocol (bool): If selected, Wildcards IP Protocol is supported.
			Ipv4Destination (bool): If selected, Wildcards IPv4 Destination is supported.
			Ipv4Source (bool): If selected, Wildcards IPv4 Source is supported.
			Ipv6Destination (bool): If selected, Wildcards IPv6 Destination is supported.
			Ipv6ExtHeader (bool): If selected, Wildcards IPv6 Ext Header is supported.
			Ipv6FlowLabel (bool): If selected, Wildcards IPv6 Flow Label is supported.
			Ipv6NdSll (bool): If selected, Wildcards IPv6 ND SLL is supported.
			Ipv6NdTarget (bool): If selected, Wildcards IPv6 ND Target is supported.
			Ipv6NdTll (bool): If selected, Wildcards IPv6 ND TLL is supported.
			Ipv6Source (bool): If selected, Wildcards IPv6 Source is supported.
			Metadata (bool): If selected, Wildcards Metadata is supported.
			MplsBos (bool): If selected, Wildcards MPLS BoS is supported.
			MplsLabel (bool): If selected, Wildcards MPLS Label is supported.
			MplsTc (bool): If selected, Wildcards MPLS TC is supported.
			PbbIsid (bool): If selected, Wildcards PBB ISID is supported.
			PhysicalInPort (bool): If selected, Wildcards Physical In Port is supported.
			SctpDestination (bool): If selected, Wildcards SCTP Destination is supported.
			SctpSource (bool): If selected, Wildcards SCTP Source is supported.
			TcpDestination (bool): If selected, Wildcards TCP Destination is supported.
			TcpSource (bool): If selected, Wildcards TCP Source is supported.
			TunnelId (bool): If selected, Wildcards Tunnel ID is supported.
			UdpDestination (bool): If selected, Wildcards UDP Destination is supported.
			UdpSource (bool): If selected, Wildcards UDP Source is supported.
			VlanId (bool): If selected, Wildcards VLAN ID is supported.
			VlanPriority (bool): If selected, Wildcards VLAN Priority is supported.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
