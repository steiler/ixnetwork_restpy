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


class SimInterfaceIPv6Config(Base):
	"""Data associated with simulated IPv6 interface link configuration inside a Network Topology.
	The SimInterfaceIPv6Config class encapsulates a list of simInterfaceIPv6Config resources that is managed by the system.
	A list of resources can be retrieved from the server using the SimInterfaceIPv6Config.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'simInterfaceIPv6Config'

	def __init__(self, parent):
		super(SimInterfaceIPv6Config, self).__init__(parent)

	@property
	def Ospfv3PseudoInterface(self):
		"""An instance of the Ospfv3PseudoInterface class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3pseudointerface.Ospfv3PseudoInterface)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3pseudointerface import Ospfv3PseudoInterface
		return Ospfv3PseudoInterface(self)

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def EnableIp(self):
		"""Enable IPv6

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableIp')

	@property
	def FromIP(self):
		"""128 Bits IPv6 address.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('fromIP')

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
	def SubnetPrefixLength(self):
		"""Subnet Prefix Length

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('subnetPrefixLength')

	@property
	def ToIP(self):
		"""128 Bits IPv6 address.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('toIP')

	def update(self, Name=None):
		"""Updates a child instance of simInterfaceIPv6Config on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def find(self, Count=None, DescriptiveName=None, Name=None):
		"""Finds and retrieves simInterfaceIPv6Config data from the server.

		All named parameters support regex and can be used to selectively retrieve simInterfaceIPv6Config data from the server.
		By default the find method takes no parameters and will retrieve all simInterfaceIPv6Config data from the server.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			self: This instance with matching simInterfaceIPv6Config data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of simInterfaceIPv6Config data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the simInterfaceIPv6Config data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, EnableIp=None, FromIP=None, SubnetPrefixLength=None, ToIP=None):
		"""Base class infrastructure that gets a list of simInterfaceIPv6Config device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			EnableIp (str): optional regex of enableIp
			FromIP (str): optional regex of fromIP
			SubnetPrefixLength (str): optional regex of subnetPrefixLength
			ToIP (str): optional regex of toIP

		Returns:
			list(int): A list of device ids that meets the regex criteria provided in the method parameters

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._get_ngpf_device_ids(locals())

	def Start(self):
		"""Executes the start operation on the server.

		Start CPF control plane (equals to promote to negotiated state).

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		return self._execute('start', payload=payload, response_object=None)

	def Stop(self):
		"""Executes the stop operation on the server.

		Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		return self._execute('stop', payload=payload, response_object=None)
