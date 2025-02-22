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


class Ipv6MulticastVpn(Base):
	"""Helps to configure the attributes for the IPv6 Multicast VPN
	The Ipv6MulticastVpn class encapsulates a list of ipv6MulticastVpn resources that is managed by the system.
	A list of resources can be retrieved from the server using the Ipv6MulticastVpn.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'ipv6MulticastVpn'

	def __init__(self, parent):
		super(Ipv6MulticastVpn, self).__init__(parent)

	@property
	def CMcastRouteType(self):
		"""The c-multicast route type.

		Returns:
			str
		"""
		return self._get_attribute('cMcastRouteType')

	@property
	def GroupAddress(self):
		"""The IPv6 Multicast group address in the range of group addresses included in this Register message.

		Returns:
			str
		"""
		return self._get_attribute('groupAddress')

	@property
	def Neighbor(self):
		"""The neighbor address.

		Returns:
			str
		"""
		return self._get_attribute('neighbor')

	@property
	def OriginatingRouter(self):
		"""The originating router address.

		Returns:
			str
		"""
		return self._get_attribute('originatingRouter')

	@property
	def RouteDistinguisher(self):
		"""The route distinguisher for the route, for use with IPv6 multicast VPN address types.

		Returns:
			str
		"""
		return self._get_attribute('routeDistinguisher')

	@property
	def RouteKeyGroupAddress(self):
		"""The key group address of the route.

		Returns:
			str
		"""
		return self._get_attribute('routeKeyGroupAddress')

	@property
	def RouteKeyOriginatingRouter(self):
		"""The key originating address of the router.

		Returns:
			str
		"""
		return self._get_attribute('routeKeyOriginatingRouter')

	@property
	def RouteKeyRouteDistinguisher(self):
		"""The key route distinguisher for the route, for use with IPv6 multicast VPN address types.

		Returns:
			str
		"""
		return self._get_attribute('routeKeyRouteDistinguisher')

	@property
	def RouteKeyRsvpP2mpExtendedTunnelId(self):
		"""The key rsvp p2mp extended tunnel id for the route, for use with IPv6 multicast VPN address types.

		Returns:
			str
		"""
		return self._get_attribute('routeKeyRsvpP2mpExtendedTunnelId')

	@property
	def RouteKeyRsvpP2mpId(self):
		"""The key rsvp p2mp id for the route, for use with IPv6 multicast VPN address types.

		Returns:
			number
		"""
		return self._get_attribute('routeKeyRsvpP2mpId')

	@property
	def RouteKeyRsvpP2mpTunnelId(self):
		"""The key rsvp p2mp tunnel id for the route, for use with IPv6 multicast VPN address types.

		Returns:
			number
		"""
		return self._get_attribute('routeKeyRsvpP2mpTunnelId')

	@property
	def RouteKeySourceAddress(self):
		"""The key source address for the route, for use with IPv6 multicast VPN address types.

		Returns:
			str
		"""
		return self._get_attribute('routeKeySourceAddress')

	@property
	def RouteKeyTunnelType(self):
		"""The key tunnel type for the route, for use with IPv6 multicast VPN address types.

		Returns:
			str
		"""
		return self._get_attribute('routeKeyTunnelType')

	@property
	def RouteKeyUpstreamLabel(self):
		"""The key upstream label for the route, for use with IPv6 multicast VPN address types.

		Returns:
			number
		"""
		return self._get_attribute('routeKeyUpstreamLabel')

	@property
	def RouteType(self):
		"""The route type.

		Returns:
			str
		"""
		return self._get_attribute('routeType')

	@property
	def RsvpP2mpExtendedTunnelId(self):
		"""The rsvp p2mp extended tunnel id.

		Returns:
			str
		"""
		return self._get_attribute('rsvpP2mpExtendedTunnelId')

	@property
	def RsvpP2mpId(self):
		"""The rsvp p2mp id.

		Returns:
			number
		"""
		return self._get_attribute('rsvpP2mpId')

	@property
	def RsvpP2mpTunnelId(self):
		"""The rsvp p2mp tunnel id.

		Returns:
			number
		"""
		return self._get_attribute('rsvpP2mpTunnelId')

	@property
	def SourceAddress(self):
		"""The source address.

		Returns:
			str
		"""
		return self._get_attribute('sourceAddress')

	@property
	def SourceAs(self):
		"""The source AS number.

		Returns:
			number
		"""
		return self._get_attribute('sourceAs')

	@property
	def TunnelType(self):
		"""The tunnel type.

		Returns:
			str
		"""
		return self._get_attribute('tunnelType')

	@property
	def UpstreamLabel(self):
		"""The upstream label.

		Returns:
			number
		"""
		return self._get_attribute('upstreamLabel')

	def find(self, CMcastRouteType=None, GroupAddress=None, Neighbor=None, OriginatingRouter=None, RouteDistinguisher=None, RouteKeyGroupAddress=None, RouteKeyOriginatingRouter=None, RouteKeyRouteDistinguisher=None, RouteKeyRsvpP2mpExtendedTunnelId=None, RouteKeyRsvpP2mpId=None, RouteKeyRsvpP2mpTunnelId=None, RouteKeySourceAddress=None, RouteKeyTunnelType=None, RouteKeyUpstreamLabel=None, RouteType=None, RsvpP2mpExtendedTunnelId=None, RsvpP2mpId=None, RsvpP2mpTunnelId=None, SourceAddress=None, SourceAs=None, TunnelType=None, UpstreamLabel=None):
		"""Finds and retrieves ipv6MulticastVpn data from the server.

		All named parameters support regex and can be used to selectively retrieve ipv6MulticastVpn data from the server.
		By default the find method takes no parameters and will retrieve all ipv6MulticastVpn data from the server.

		Args:
			CMcastRouteType (str): The c-multicast route type.
			GroupAddress (str): The IPv6 Multicast group address in the range of group addresses included in this Register message.
			Neighbor (str): The neighbor address.
			OriginatingRouter (str): The originating router address.
			RouteDistinguisher (str): The route distinguisher for the route, for use with IPv6 multicast VPN address types.
			RouteKeyGroupAddress (str): The key group address of the route.
			RouteKeyOriginatingRouter (str): The key originating address of the router.
			RouteKeyRouteDistinguisher (str): The key route distinguisher for the route, for use with IPv6 multicast VPN address types.
			RouteKeyRsvpP2mpExtendedTunnelId (str): The key rsvp p2mp extended tunnel id for the route, for use with IPv6 multicast VPN address types.
			RouteKeyRsvpP2mpId (number): The key rsvp p2mp id for the route, for use with IPv6 multicast VPN address types.
			RouteKeyRsvpP2mpTunnelId (number): The key rsvp p2mp tunnel id for the route, for use with IPv6 multicast VPN address types.
			RouteKeySourceAddress (str): The key source address for the route, for use with IPv6 multicast VPN address types.
			RouteKeyTunnelType (str): The key tunnel type for the route, for use with IPv6 multicast VPN address types.
			RouteKeyUpstreamLabel (number): The key upstream label for the route, for use with IPv6 multicast VPN address types.
			RouteType (str): The route type.
			RsvpP2mpExtendedTunnelId (str): The rsvp p2mp extended tunnel id.
			RsvpP2mpId (number): The rsvp p2mp id.
			RsvpP2mpTunnelId (number): The rsvp p2mp tunnel id.
			SourceAddress (str): The source address.
			SourceAs (number): The source AS number.
			TunnelType (str): The tunnel type.
			UpstreamLabel (number): The upstream label.

		Returns:
			self: This instance with matching ipv6MulticastVpn data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of ipv6MulticastVpn data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the ipv6MulticastVpn data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
