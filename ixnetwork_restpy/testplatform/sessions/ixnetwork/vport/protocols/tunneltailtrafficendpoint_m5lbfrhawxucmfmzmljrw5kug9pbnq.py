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


class TunnelTailTrafficEndPoint(Base):
	"""The tunnelTailTrafficEndpoint configures the IP addresses to be used in the Destination IP field in traffic to be sent over the LSPs terminating on this Tail Range.
	The TunnelTailTrafficEndPoint class encapsulates a list of tunnelTailTrafficEndPoint resources that is be managed by the user.
	A list of resources can be retrieved from the server using the TunnelTailTrafficEndPoint.find() method.
	The list can be managed by the user by using the TunnelTailTrafficEndPoint.add() and TunnelTailTrafficEndPoint.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'tunnelTailTrafficEndPoint'

	def __init__(self, parent):
		super(TunnelTailTrafficEndPoint, self).__init__(parent)

	@property
	def EndPointType(self):
		"""Indicates the end point type. One of IPv4 or IPv6.

		Returns:
			str(ipv4|ipv6|17|18)
		"""
		return self._get_attribute('endPointType')
	@EndPointType.setter
	def EndPointType(self, value):
		self._set_attribute('endPointType', value)

	@property
	def IpCount(self):
		"""This indicates that the number of Destination IPs to which the traffic sent over the P2MP RSVP-TE tunnel is destined. The minimum and default value is 1.

		Returns:
			number
		"""
		return self._get_attribute('ipCount')
	@IpCount.setter
	def IpCount(self, value):
		self._set_attribute('ipCount', value)

	@property
	def IpStart(self):
		"""The Start Destination IP Address for traffic that is sent over the P2MP RSVP-TE tunnel. Normally, this is an IPv4 or IPv6 Multicast address.

		Returns:
			str
		"""
		return self._get_attribute('ipStart')
	@IpStart.setter
	def IpStart(self, value):
		self._set_attribute('ipStart', value)

	def update(self, EndPointType=None, IpCount=None, IpStart=None):
		"""Updates a child instance of tunnelTailTrafficEndPoint on the server.

		Args:
			EndPointType (str(ipv4|ipv6|17|18)): Indicates the end point type. One of IPv4 or IPv6.
			IpCount (number): This indicates that the number of Destination IPs to which the traffic sent over the P2MP RSVP-TE tunnel is destined. The minimum and default value is 1.
			IpStart (str): The Start Destination IP Address for traffic that is sent over the P2MP RSVP-TE tunnel. Normally, this is an IPv4 or IPv6 Multicast address.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, EndPointType=None, IpCount=None, IpStart=None):
		"""Adds a new tunnelTailTrafficEndPoint node on the server and retrieves it in this instance.

		Args:
			EndPointType (str(ipv4|ipv6|17|18)): Indicates the end point type. One of IPv4 or IPv6.
			IpCount (number): This indicates that the number of Destination IPs to which the traffic sent over the P2MP RSVP-TE tunnel is destined. The minimum and default value is 1.
			IpStart (str): The Start Destination IP Address for traffic that is sent over the P2MP RSVP-TE tunnel. Normally, this is an IPv4 or IPv6 Multicast address.

		Returns:
			self: This instance with all currently retrieved tunnelTailTrafficEndPoint data using find and the newly added tunnelTailTrafficEndPoint data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the tunnelTailTrafficEndPoint data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, EndPointType=None, IpCount=None, IpStart=None):
		"""Finds and retrieves tunnelTailTrafficEndPoint data from the server.

		All named parameters support regex and can be used to selectively retrieve tunnelTailTrafficEndPoint data from the server.
		By default the find method takes no parameters and will retrieve all tunnelTailTrafficEndPoint data from the server.

		Args:
			EndPointType (str(ipv4|ipv6|17|18)): Indicates the end point type. One of IPv4 or IPv6.
			IpCount (number): This indicates that the number of Destination IPs to which the traffic sent over the P2MP RSVP-TE tunnel is destined. The minimum and default value is 1.
			IpStart (str): The Start Destination IP Address for traffic that is sent over the P2MP RSVP-TE tunnel. Normally, this is an IPv4 or IPv6 Multicast address.

		Returns:
			self: This instance with matching tunnelTailTrafficEndPoint data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of tunnelTailTrafficEndPoint data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the tunnelTailTrafficEndPoint data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
