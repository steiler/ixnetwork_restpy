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


class LinkLsaRoutes(Base):
	"""Link Lsa routes
	The LinkLsaRoutes class encapsulates a list of linkLsaRoutes resources that is managed by the system.
	A list of resources can be retrieved from the server using the LinkLsaRoutes.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'linkLsaRoutes'

	def __init__(self, parent):
		super(LinkLsaRoutes, self).__init__(parent)

	@property
	def Active(self):
		"""Whether this is to be advertised or not

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def DCBit(self):
		"""Demand Circuit bit

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('dCBit')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def EBit(self):
		"""bit describing how AS-external-LSAs are flooded

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('eBit')

	@property
	def LABit(self):
		"""Options-LA Bit(Local Address)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lABit')

	@property
	def LinkLocalAddress(self):
		"""128 Bits IPv6 address.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('linkLocalAddress')

	@property
	def LinkStateId(self):
		"""Link State Id of the simulated IPv6 network

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('linkStateId')

	@property
	def LinkStateIdStep(self):
		"""Link State Id Step for the LSAs to be generated for this set of IPv6 Inter-Area networks.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('linkStateIdStep')

	@property
	def MCBit(self):
		"""Options-MC Bit(Multicast)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('mCBit')

	@property
	def Metric(self):
		"""Metric

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('metric')

	@property
	def NBit(self):
		"""bit for handling Type 7 LSAs

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('nBit')

	@property
	def NUBit(self):
		"""Options-NU Bit(No Unicast)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('nUBit')

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
	def PBit(self):
		"""Options-P Bit(Propagate)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('pBit')

	@property
	def Prefix(self):
		"""Prefix Length

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('prefix')

	@property
	def RBit(self):
		"""Router bit

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('rBit')

	@property
	def RangeSize(self):
		"""Range Size

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('rangeSize')

	@property
	def ReservedBit6(self):
		"""(6) Reserved Bit

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('reservedBit6')

	@property
	def ReservedBit7(self):
		"""(7) Reserved Bit

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('reservedBit7')

	@property
	def RouterPriority(self):
		"""Router Priority

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('routerPriority')

	@property
	def UnusedBit4(self):
		"""Options-(4)Unused

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('unusedBit4')

	@property
	def UnusedBit5(self):
		"""Options-(5)Unused

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('unusedBit5')

	@property
	def UnusedBit6(self):
		"""Options-(6)Unused

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('unusedBit6')

	@property
	def UnusedBit7(self):
		"""Options-(7)Unused

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('unusedBit7')

	@property
	def V6Bit(self):
		"""bit for excluding the router/link from IPv6 routing calculations. If clear, router/link is excluded

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('v6Bit')

	@property
	def XBit(self):
		"""bit for forwarding of IP multicast datagrams

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('xBit')

	def update(self, Name=None):
		"""Updates a child instance of linkLsaRoutes on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def find(self, Count=None, DescriptiveName=None, Name=None):
		"""Finds and retrieves linkLsaRoutes data from the server.

		All named parameters support regex and can be used to selectively retrieve linkLsaRoutes data from the server.
		By default the find method takes no parameters and will retrieve all linkLsaRoutes data from the server.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			self: This instance with matching linkLsaRoutes data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of linkLsaRoutes data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the linkLsaRoutes data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, Active=None, DCBit=None, EBit=None, LABit=None, LinkLocalAddress=None, LinkStateId=None, LinkStateIdStep=None, MCBit=None, Metric=None, NBit=None, NUBit=None, NetworkAddress=None, PBit=None, Prefix=None, RBit=None, RangeSize=None, ReservedBit6=None, ReservedBit7=None, RouterPriority=None, UnusedBit4=None, UnusedBit5=None, UnusedBit6=None, UnusedBit7=None, V6Bit=None, XBit=None):
		"""Base class infrastructure that gets a list of linkLsaRoutes device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			Active (str): optional regex of active
			DCBit (str): optional regex of dCBit
			EBit (str): optional regex of eBit
			LABit (str): optional regex of lABit
			LinkLocalAddress (str): optional regex of linkLocalAddress
			LinkStateId (str): optional regex of linkStateId
			LinkStateIdStep (str): optional regex of linkStateIdStep
			MCBit (str): optional regex of mCBit
			Metric (str): optional regex of metric
			NBit (str): optional regex of nBit
			NUBit (str): optional regex of nUBit
			NetworkAddress (str): optional regex of networkAddress
			PBit (str): optional regex of pBit
			Prefix (str): optional regex of prefix
			RBit (str): optional regex of rBit
			RangeSize (str): optional regex of rangeSize
			ReservedBit6 (str): optional regex of reservedBit6
			ReservedBit7 (str): optional regex of reservedBit7
			RouterPriority (str): optional regex of routerPriority
			UnusedBit4 (str): optional regex of unusedBit4
			UnusedBit5 (str): optional regex of unusedBit5
			UnusedBit6 (str): optional regex of unusedBit6
			UnusedBit7 (str): optional regex of unusedBit7
			V6Bit (str): optional regex of v6Bit
			XBit (str): optional regex of xBit

		Returns:
			list(int): A list of device ids that meets the regex criteria provided in the method parameters

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._get_ngpf_device_ids(locals())

	def Advertise(self, *args, **kwargs):
		"""Executes the advertise operation on the server.

		Advertise selected routes

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		advertise()

		advertise(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		advertise(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('advertise', payload=payload, response_object=None)

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

	def Withdraw(self, *args, **kwargs):
		"""Executes the withdraw operation on the server.

		Withdraw selected routes

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		withdraw()

		withdraw(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		withdraw(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('withdraw', payload=payload, response_object=None)
