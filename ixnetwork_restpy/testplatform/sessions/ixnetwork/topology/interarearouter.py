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


class InterAreaRouter(Base):
	"""External routes without external metric
	The InterAreaRouter class encapsulates a list of interAreaRouter resources that is managed by the system.
	A list of resources can be retrieved from the server using the InterAreaRouter.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'interAreaRouter'

	def __init__(self, parent):
		super(InterAreaRouter, self).__init__(parent)

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
	def DestRouterId(self):
		"""Destination Router Id

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('destRouterId')

	@property
	def DestRouterIdPrefix(self):
		"""Destination Router Id Step

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('destRouterIdPrefix')

	@property
	def EBit(self):
		"""bit describing how AS-external-LSAs are flooded

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('eBit')

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
		"""bit for forwarding of IP multicast datagrams

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
	def RBit(self):
		"""Router bit

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('rBit')

	@property
	def RangeSize(self):
		"""Count

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
	def V6Bit(self):
		"""bit for excluding the router/link from IPv6 routing calculations. If clear, router/link is excluded

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('v6Bit')

	def update(self, Name=None):
		"""Updates a child instance of interAreaRouter on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def find(self, Count=None, DescriptiveName=None, Name=None):
		"""Finds and retrieves interAreaRouter data from the server.

		All named parameters support regex and can be used to selectively retrieve interAreaRouter data from the server.
		By default the find method takes no parameters and will retrieve all interAreaRouter data from the server.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			self: This instance with matching interAreaRouter data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of interAreaRouter data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the interAreaRouter data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, Active=None, DCBit=None, DestRouterId=None, DestRouterIdPrefix=None, EBit=None, LinkStateId=None, LinkStateIdStep=None, MCBit=None, Metric=None, NBit=None, RBit=None, RangeSize=None, ReservedBit6=None, ReservedBit7=None, V6Bit=None):
		"""Base class infrastructure that gets a list of interAreaRouter device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			Active (str): optional regex of active
			DCBit (str): optional regex of dCBit
			DestRouterId (str): optional regex of destRouterId
			DestRouterIdPrefix (str): optional regex of destRouterIdPrefix
			EBit (str): optional regex of eBit
			LinkStateId (str): optional regex of linkStateId
			LinkStateIdStep (str): optional regex of linkStateIdStep
			MCBit (str): optional regex of mCBit
			Metric (str): optional regex of metric
			NBit (str): optional regex of nBit
			RBit (str): optional regex of rBit
			RangeSize (str): optional regex of rangeSize
			ReservedBit6 (str): optional regex of reservedBit6
			ReservedBit7 (str): optional regex of reservedBit7
			V6Bit (str): optional regex of v6Bit

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
