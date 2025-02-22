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


class EapoUdpOptions(Base):
	"""
	The EapoUdpOptions class encapsulates a list of eapoUdpOptions resources that is be managed by the user.
	A list of resources can be retrieved from the server using the EapoUdpOptions.find() method.
	The list can be managed by the user by using the EapoUdpOptions.add() and EapoUdpOptions.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'eapoUdpOptions'

	def __init__(self, parent):
		super(EapoUdpOptions, self).__init__(parent)

	@property
	def DutMac(self):
		"""The MAC address of a DUT port to which the PCPU is connected. This is needed when using ICMP, DHCP_ICMP internal triggers.

		Returns:
			str
		"""
		return self._get_attribute('dutMac')
	@DutMac.setter
	def DutMac(self, value):
		self._set_attribute('dutMac', value)

	@property
	def IcmpTriggerTargetAddress(self):
		"""The target address where ICMP messages are sent.

		Returns:
			str
		"""
		return self._get_attribute('icmpTriggerTargetAddress')
	@IcmpTriggerTargetAddress.setter
	def IcmpTriggerTargetAddress(self, value):
		self._set_attribute('icmpTriggerTargetAddress', value)

	@property
	def MaxClientsPerSecond(self):
		"""The number interfaces to setup per second.

		Returns:
			number
		"""
		return self._get_attribute('maxClientsPerSecond')
	@MaxClientsPerSecond.setter
	def MaxClientsPerSecond(self, value):
		self._set_attribute('maxClientsPerSecond', value)

	@property
	def MaxOutstandingRequests(self):
		"""The maximum number of sessions that can be negotiated at one moment.

		Returns:
			number
		"""
		return self._get_attribute('maxOutstandingRequests')
	@MaxOutstandingRequests.setter
	def MaxOutstandingRequests(self, value):
		self._set_attribute('maxOutstandingRequests', value)

	@property
	def ObjectId(self):
		"""Unique identifier for this object

		Returns:
			str
		"""
		return self._get_attribute('objectId')

	@property
	def OverrideGlobalSetupRate(self):
		"""If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.

		Returns:
			bool
		"""
		return self._get_attribute('overrideGlobalSetupRate')
	@OverrideGlobalSetupRate.setter
	def OverrideGlobalSetupRate(self, value):
		self._set_attribute('overrideGlobalSetupRate', value)

	def update(self, DutMac=None, IcmpTriggerTargetAddress=None, MaxClientsPerSecond=None, MaxOutstandingRequests=None, OverrideGlobalSetupRate=None):
		"""Updates a child instance of eapoUdpOptions on the server.

		Args:
			DutMac (str): The MAC address of a DUT port to which the PCPU is connected. This is needed when using ICMP, DHCP_ICMP internal triggers.
			IcmpTriggerTargetAddress (str): The target address where ICMP messages are sent.
			MaxClientsPerSecond (number): The number interfaces to setup per second.
			MaxOutstandingRequests (number): The maximum number of sessions that can be negotiated at one moment.
			OverrideGlobalSetupRate (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, DutMac=None, IcmpTriggerTargetAddress=None, MaxClientsPerSecond=None, MaxOutstandingRequests=None, OverrideGlobalSetupRate=None):
		"""Adds a new eapoUdpOptions node on the server and retrieves it in this instance.

		Args:
			DutMac (str): The MAC address of a DUT port to which the PCPU is connected. This is needed when using ICMP, DHCP_ICMP internal triggers.
			IcmpTriggerTargetAddress (str): The target address where ICMP messages are sent.
			MaxClientsPerSecond (number): The number interfaces to setup per second.
			MaxOutstandingRequests (number): The maximum number of sessions that can be negotiated at one moment.
			OverrideGlobalSetupRate (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.

		Returns:
			self: This instance with all currently retrieved eapoUdpOptions data using find and the newly added eapoUdpOptions data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the eapoUdpOptions data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, DutMac=None, IcmpTriggerTargetAddress=None, MaxClientsPerSecond=None, MaxOutstandingRequests=None, ObjectId=None, OverrideGlobalSetupRate=None):
		"""Finds and retrieves eapoUdpOptions data from the server.

		All named parameters support regex and can be used to selectively retrieve eapoUdpOptions data from the server.
		By default the find method takes no parameters and will retrieve all eapoUdpOptions data from the server.

		Args:
			DutMac (str): The MAC address of a DUT port to which the PCPU is connected. This is needed when using ICMP, DHCP_ICMP internal triggers.
			IcmpTriggerTargetAddress (str): The target address where ICMP messages are sent.
			MaxClientsPerSecond (number): The number interfaces to setup per second.
			MaxOutstandingRequests (number): The maximum number of sessions that can be negotiated at one moment.
			ObjectId (str): Unique identifier for this object
			OverrideGlobalSetupRate (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.

		Returns:
			self: This instance with matching eapoUdpOptions data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of eapoUdpOptions data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the eapoUdpOptions data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

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
