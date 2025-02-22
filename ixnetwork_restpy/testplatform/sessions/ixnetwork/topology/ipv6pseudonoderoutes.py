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


class IPv6PseudoNodeRoutes(Base):
	"""Isis IPv6 pseudo node routes
	The IPv6PseudoNodeRoutes class encapsulates a list of IPv6PseudoNodeRoutes resources that is managed by the system.
	A list of resources can be retrieved from the server using the IPv6PseudoNodeRoutes.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'IPv6PseudoNodeRoutes'

	def __init__(self, parent):
		super(IPv6PseudoNodeRoutes, self).__init__(parent)

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
	def Active(self):
		"""Whether this is to be advertised or not

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def Algorithm(self):
		"""Algorithm

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('algorithm')

	@property
	def ConfigureSIDIndexLabel(self):
		"""Configure SID/Index/Label

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('configureSIDIndexLabel')

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
	def Ipv6EFlag(self):
		"""Explicit NULL flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6EFlag')

	@property
	def Ipv6LFlag(self):
		"""Local Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6LFlag')

	@property
	def Ipv6Metric(self):
		"""Route Metric

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6Metric')

	@property
	def Ipv6NFlag(self):
		"""Nodal prefix flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6NFlag')

	@property
	def Ipv6PFlag(self):
		"""No-PHP flag. If set, then the penultimate hop MUST NOT pop the Prefix-SID before delivering the packet to the node that advertised the Prefix-SID.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6PFlag')

	@property
	def Ipv6RFlag(self):
		"""Redistribution flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6RFlag')

	@property
	def Ipv6Redistribution(self):
		"""Redistribution

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6Redistribution')

	@property
	def Ipv6RouteOrigin(self):
		"""Route Origin

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6RouteOrigin')

	@property
	def Ipv6Srh(self):
		"""DEPRECATED Advertise IPv6 SID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6Srh')

	@property
	def Ipv6VFlag(self):
		"""Value Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6VFlag')

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
	def NetworkAddress(self):
		"""Prefixes of the simulated IPv6 network

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('networkAddress')

	@property
	def Prefix(self):
		"""Prefix Length

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('prefix')

	@property
	def RangeSize(self):
		"""Range Size

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('rangeSize')

	@property
	def SIDIndexLabel(self):
		"""SID/Index/Label

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sIDIndexLabel')

	def update(self, Name=None):
		"""Updates a child instance of IPv6PseudoNodeRoutes on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def find(self, Count=None, DescriptiveName=None, Name=None):
		"""Finds and retrieves IPv6PseudoNodeRoutes data from the server.

		All named parameters support regex and can be used to selectively retrieve IPv6PseudoNodeRoutes data from the server.
		By default the find method takes no parameters and will retrieve all IPv6PseudoNodeRoutes data from the server.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			self: This instance with matching IPv6PseudoNodeRoutes data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of IPv6PseudoNodeRoutes data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the IPv6PseudoNodeRoutes data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, Active=None, Algorithm=None, ConfigureSIDIndexLabel=None, Ipv6EFlag=None, Ipv6LFlag=None, Ipv6Metric=None, Ipv6NFlag=None, Ipv6PFlag=None, Ipv6RFlag=None, Ipv6Redistribution=None, Ipv6RouteOrigin=None, Ipv6Srh=None, Ipv6VFlag=None, NetworkAddress=None, Prefix=None, RangeSize=None, SIDIndexLabel=None):
		"""Base class infrastructure that gets a list of IPv6PseudoNodeRoutes device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			Active (str): optional regex of active
			Algorithm (str): optional regex of algorithm
			ConfigureSIDIndexLabel (str): optional regex of configureSIDIndexLabel
			Ipv6EFlag (str): optional regex of ipv6EFlag
			Ipv6LFlag (str): optional regex of ipv6LFlag
			Ipv6Metric (str): optional regex of ipv6Metric
			Ipv6NFlag (str): optional regex of ipv6NFlag
			Ipv6PFlag (str): optional regex of ipv6PFlag
			Ipv6RFlag (str): optional regex of ipv6RFlag
			Ipv6Redistribution (str): optional regex of ipv6Redistribution
			Ipv6RouteOrigin (str): optional regex of ipv6RouteOrigin
			Ipv6Srh (str): optional regex of ipv6Srh
			Ipv6VFlag (str): optional regex of ipv6VFlag
			NetworkAddress (str): optional regex of networkAddress
			Prefix (str): optional regex of prefix
			RangeSize (str): optional regex of rangeSize
			SIDIndexLabel (str): optional regex of sIDIndexLabel

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
