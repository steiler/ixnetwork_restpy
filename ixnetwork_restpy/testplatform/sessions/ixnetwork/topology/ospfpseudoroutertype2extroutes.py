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


class OspfPseudoRouterType2ExtRoutes(Base):
	"""External routes with external metric
	The OspfPseudoRouterType2ExtRoutes class encapsulates a list of ospfPseudoRouterType2ExtRoutes resources that is managed by the system.
	A list of resources can be retrieved from the server using the OspfPseudoRouterType2ExtRoutes.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'ospfPseudoRouterType2ExtRoutes'

	def __init__(self, parent):
		super(OspfPseudoRouterType2ExtRoutes, self).__init__(parent)

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
	def EFlag(self):
		"""Explicit-Null Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('eFlag')

	@property
	def LFlag(self):
		"""Local or Global Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lFlag')

	@property
	def MFlag(self):
		"""Mapping Server Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('mFlag')

	@property
	def Metric(self):
		"""Metric

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('metric')

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
		"""Network addresses of the simulated IPv4 network

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('networkAddress')

	@property
	def NpFlag(self):
		"""No-PHP Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('npFlag')

	@property
	def PrefixLength(self):
		"""Prefix

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('prefixLength')

	@property
	def RangeSize(self):
		"""Range Size

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('rangeSize')

	@property
	def SidIndexLabel(self):
		"""SID/Index/Label

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sidIndexLabel')

	@property
	def VFlag(self):
		"""Value or Index Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('vFlag')

	def update(self, Name=None):
		"""Updates a child instance of ospfPseudoRouterType2ExtRoutes on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def find(self, Count=None, DescriptiveName=None, Name=None):
		"""Finds and retrieves ospfPseudoRouterType2ExtRoutes data from the server.

		All named parameters support regex and can be used to selectively retrieve ospfPseudoRouterType2ExtRoutes data from the server.
		By default the find method takes no parameters and will retrieve all ospfPseudoRouterType2ExtRoutes data from the server.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			self: This instance with matching ospfPseudoRouterType2ExtRoutes data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of ospfPseudoRouterType2ExtRoutes data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the ospfPseudoRouterType2ExtRoutes data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, Active=None, Algorithm=None, ConfigureSIDIndexLabel=None, EFlag=None, LFlag=None, MFlag=None, Metric=None, NetworkAddress=None, NpFlag=None, PrefixLength=None, RangeSize=None, SidIndexLabel=None, VFlag=None):
		"""Base class infrastructure that gets a list of ospfPseudoRouterType2ExtRoutes device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			Active (str): optional regex of active
			Algorithm (str): optional regex of algorithm
			ConfigureSIDIndexLabel (str): optional regex of configureSIDIndexLabel
			EFlag (str): optional regex of eFlag
			LFlag (str): optional regex of lFlag
			MFlag (str): optional regex of mFlag
			Metric (str): optional regex of metric
			NetworkAddress (str): optional regex of networkAddress
			NpFlag (str): optional regex of npFlag
			PrefixLength (str): optional regex of prefixLength
			RangeSize (str): optional regex of rangeSize
			SidIndexLabel (str): optional regex of sidIndexLabel
			VFlag (str): optional regex of vFlag

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
