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


class Options(Base):
	"""Global NDP settings, per port
	The Options class encapsulates a required options resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'options'

	def __init__(self, parent):
		super(Options, self).__init__(parent)

	@property
	def ActOnGratArp(self):
		"""When enabled, the ARP refresh timer in kernel will be set to initial value configured by the user when GratArp message is received.

		Returns:
			bool
		"""
		return self._get_attribute('actOnGratArp')
	@ActOnGratArp.setter
	def ActOnGratArp(self, value):
		self._set_attribute('actOnGratArp', value)

	@property
	def ArpRefreshInterval(self):
		"""The time interval in seconds taken by IxNetwork to refresh IPv4 address cache. By default, it is set to 60 seconds

		Returns:
			number
		"""
		return self._get_attribute('arpRefreshInterval')
	@ArpRefreshInterval.setter
	def ArpRefreshInterval(self, value):
		self._set_attribute('arpRefreshInterval', value)

	@property
	def DadEnabled(self):
		"""When enabled, IPv6 server will reply to NDP DAD NS messages with Neighbor Advertisement packets.

		Returns:
			bool
		"""
		return self._get_attribute('dadEnabled')
	@DadEnabled.setter
	def DadEnabled(self, value):
		self._set_attribute('dadEnabled', value)

	@property
	def DadTransmits(self):
		"""Number of Neighbor Solicitations to send until assuming no routers are present.

		Returns:
			number
		"""
		return self._get_attribute('dadTransmits')
	@DadTransmits.setter
	def DadTransmits(self, value):
		self._set_attribute('dadTransmits', value)

	@property
	def IgnoreMldQueries(self):
		"""When enabled IPv6 emulation will not respond to MLD queries with Solicited node membership reports.

		Returns:
			bool
		"""
		return self._get_attribute('ignoreMldQueries')
	@IgnoreMldQueries.setter
	def IgnoreMldQueries(self, value):
		self._set_attribute('ignoreMldQueries', value)

	@property
	def Ipv4McastSolicit(self):
		"""Maximum number of ARP requests to send to resolve one MAC address.

		Returns:
			number
		"""
		return self._get_attribute('ipv4McastSolicit')
	@Ipv4McastSolicit.setter
	def Ipv4McastSolicit(self, value):
		self._set_attribute('ipv4McastSolicit', value)

	@property
	def Ipv4RetransTime(self):
		"""Number of milliseconds to wait between ARP requests.

		Returns:
			number
		"""
		return self._get_attribute('ipv4RetransTime')
	@Ipv4RetransTime.setter
	def Ipv4RetransTime(self, value):
		self._set_attribute('ipv4RetransTime', value)

	@property
	def Mcast_solicit(self):
		"""Number of Neighbor Solicitations to send until giving up on link layer address resolution.

		Returns:
			number
		"""
		return self._get_attribute('mcast_solicit')
	@Mcast_solicit.setter
	def Mcast_solicit(self, value):
		self._set_attribute('mcast_solicit', value)

	@property
	def NsRefreshInterval(self):
		"""The time interval in seconds taken by IxNetwork to refresh IPv6 address cache. By default, it is set to 60 seconds

		Returns:
			number
		"""
		return self._get_attribute('nsRefreshInterval')
	@NsRefreshInterval.setter
	def NsRefreshInterval(self, value):
		self._set_attribute('nsRefreshInterval', value)

	@property
	def ObjectId(self):
		"""Unique identifier for this object

		Returns:
			str
		"""
		return self._get_attribute('objectId')

	@property
	def RetransTime(self):
		"""Number of milliseconds to wait between Neighbor Solicitations.

		Returns:
			number
		"""
		return self._get_attribute('retransTime')
	@RetransTime.setter
	def RetransTime(self, value):
		self._set_attribute('retransTime', value)

	@property
	def RouterSolicitationDelay(self):
		"""Number of seconds to wait after interface is brought up before sending Router Solicitations. When an IPv6 link-local address is added to an interface, first NS can be sent after no more than the value of this setting seconds.

		Returns:
			number
		"""
		return self._get_attribute('routerSolicitationDelay')
	@RouterSolicitationDelay.setter
	def RouterSolicitationDelay(self, value):
		self._set_attribute('routerSolicitationDelay', value)

	@property
	def RouterSolicitationInterval(self):
		"""Number of seconds to wait between Router Solicitations.

		Returns:
			number
		"""
		return self._get_attribute('routerSolicitationInterval')
	@RouterSolicitationInterval.setter
	def RouterSolicitationInterval(self, value):
		self._set_attribute('routerSolicitationInterval', value)

	@property
	def RouterSolicitations(self):
		"""Number of Router Solicitations to send until assuming no routers are present.

		Returns:
			number
		"""
		return self._get_attribute('routerSolicitations')
	@RouterSolicitations.setter
	def RouterSolicitations(self, value):
		self._set_attribute('routerSolicitations', value)

	def update(self, ActOnGratArp=None, ArpRefreshInterval=None, DadEnabled=None, DadTransmits=None, IgnoreMldQueries=None, Ipv4McastSolicit=None, Ipv4RetransTime=None, Mcast_solicit=None, NsRefreshInterval=None, RetransTime=None, RouterSolicitationDelay=None, RouterSolicitationInterval=None, RouterSolicitations=None):
		"""Updates a child instance of options on the server.

		Args:
			ActOnGratArp (bool): When enabled, the ARP refresh timer in kernel will be set to initial value configured by the user when GratArp message is received.
			ArpRefreshInterval (number): The time interval in seconds taken by IxNetwork to refresh IPv4 address cache. By default, it is set to 60 seconds
			DadEnabled (bool): When enabled, IPv6 server will reply to NDP DAD NS messages with Neighbor Advertisement packets.
			DadTransmits (number): Number of Neighbor Solicitations to send until assuming no routers are present.
			IgnoreMldQueries (bool): When enabled IPv6 emulation will not respond to MLD queries with Solicited node membership reports.
			Ipv4McastSolicit (number): Maximum number of ARP requests to send to resolve one MAC address.
			Ipv4RetransTime (number): Number of milliseconds to wait between ARP requests.
			Mcast_solicit (number): Number of Neighbor Solicitations to send until giving up on link layer address resolution.
			NsRefreshInterval (number): The time interval in seconds taken by IxNetwork to refresh IPv6 address cache. By default, it is set to 60 seconds
			RetransTime (number): Number of milliseconds to wait between Neighbor Solicitations.
			RouterSolicitationDelay (number): Number of seconds to wait after interface is brought up before sending Router Solicitations. When an IPv6 link-local address is added to an interface, first NS can be sent after no more than the value of this setting seconds.
			RouterSolicitationInterval (number): Number of seconds to wait between Router Solicitations.
			RouterSolicitations (number): Number of Router Solicitations to send until assuming no routers are present.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def CustomProtocolStack(self, *args, **kwargs):
		"""Executes the customProtocolStack operation on the server.

		Create custom protocol stack under /vport/protocolStack

		customProtocolStack(Arg2:list, Arg3:enum)
			Args:
				args[0] is Arg2 (list(str)): List of plugin types to be added in the new custom stack
				args[1] is Arg3 (str(kAppend|kMerge|kOverwrite)): Append, merge or overwrite existing protocol stack

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('customProtocolStack', payload=payload, response_object=None)

	def DisableProtocolStack(self, *args, **kwargs):
		"""Executes the disableProtocolStack operation on the server.

		Disable a protocol under protocolStack using the class name

		disableProtocolStack(Arg2:string)string
			Args:
				args[0] is Arg2 (str): Protocol class name to disable

			Returns:
				str: Status of the exec

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('disableProtocolStack', payload=payload, response_object=None)

	def EnableProtocolStack(self, *args, **kwargs):
		"""Executes the enableProtocolStack operation on the server.

		Enable a protocol under protocolStack using the class name

		enableProtocolStack(Arg2:string)string
			Args:
				args[0] is Arg2 (str): Protocol class name to enable

			Returns:
				str: Status of the exec

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('enableProtocolStack', payload=payload, response_object=None)
