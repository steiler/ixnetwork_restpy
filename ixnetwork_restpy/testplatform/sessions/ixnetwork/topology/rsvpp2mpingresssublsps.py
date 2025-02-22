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


class RsvpP2mpIngressSubLsps(Base):
	"""RSVP-TE P2MP Head (Ingress) Sub LSPs
	The RsvpP2mpIngressSubLsps class encapsulates a required rsvpP2mpIngressSubLsps resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'rsvpP2mpIngressSubLsps'

	def __init__(self, parent):
		super(RsvpP2mpIngressSubLsps, self).__init__(parent)

	@property
	def RsvpEROSubObjectsList(self):
		"""An instance of the RsvpEROSubObjectsList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvperosubobjectslist.RsvpEROSubObjectsList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvperosubobjectslist import RsvpEROSubObjectsList
		return RsvpEROSubObjectsList(self)

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def AppendLeaf(self):
		"""Append Leaf

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('appendLeaf')

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
	def EnableEro(self):
		"""Enable ERO

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableEro')

	@property
	def LeafIp(self):
		"""Leaf IP

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('leafIp')

	@property
	def LocalIp(self):
		"""Local IP

		Returns:
			list(str)
		"""
		return self._get_attribute('localIp')

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
	def NumberOfEroSubObjects(self):
		"""Number Of ERO Sub-Objects

		Returns:
			number
		"""
		return self._get_attribute('numberOfEroSubObjects')
	@NumberOfEroSubObjects.setter
	def NumberOfEroSubObjects(self, value):
		self._set_attribute('numberOfEroSubObjects', value)

	@property
	def P2mpIdAsIp(self):
		"""P2MP ID As IP

		Returns:
			list(str)
		"""
		return self._get_attribute('p2mpIdAsIp')

	@property
	def P2mpIdAsNum(self):
		"""P2MP ID displayed in Integer format

		Returns:
			list(str)
		"""
		return self._get_attribute('p2mpIdAsNum')

	@property
	def PrefixLengthOfDut(self):
		"""Prefix Length of DUT

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('prefixLengthOfDut')

	@property
	def PrefixLengthOfLeaf(self):
		"""Prefix Length of Leaf

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('prefixLengthOfLeaf')

	@property
	def PrependDut(self):
		"""Prepend DUT

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('prependDut')

	@property
	def SendAsEro(self):
		"""Send As ERO

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sendAsEro')

	@property
	def SendAsSero(self):
		"""Send As SERO

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sendAsSero')

	@property
	def SessionInformation(self):
		"""Logs additional information about the RSVP session state

		Returns:
			list(str[lastErrLSPAdmissionControlFailure|lastErrLSPBadAdSpecValue|lastErrLSPBadExplicitRoute|lastErrLSPBadFlowspecValue|lastErrLSPBadInitialSubobject|lastErrLSPBadLooseNode|lastErrLSPBadStrictNode|lastErrLSPBadTSpecValue|lastErrLSPDelayBoundNotMet|lastErrLSPMPLSAllocationFailure|lastErrLSPMTUTooBig|lastErrLSPNonRSVPRouter|lastErrLSPNoRouteAvailable|lastErrLSPPathErr|lastErrLSPPathTearSent|lastErrLSPRequestedBandwidthUnavailable|lastErrLSPReservationTearReceived|lastErrLSPReservationTearSent|lastErrLSPReservationTimeout|lastErrLSPRoutingLoops|lastErrLSPRoutingProblem|lastErrLSPRSVPSystemError|lastErrLSPServiceConflict|lastErrLSPServiceUnsupported|lastErrLSPTrafficControlError|lastErrLSPTrafficControlSystemError|lastErrLSPTrafficOrganizationError|lastErrLSPTrafficServiceError|lastErrLSPUnknownObjectClass|lastErrLSPUnknownObjectCType|lastErrLSPUnsupportedL3PID|lSPAdmissionControlFailure|lSPBadAdSpecValue|lSPBadExplicitRoute|lSPBadFlowspecValue|lSPBadInitialSubobject|lSPBadLooseNode|lSPBadStrictNode|lSPBadTSpecValue|lSPDelayBoundNotMet|lSPMPLSAllocationFailure|lSPMTUTooBig|lSPNonRSVPRouter|lSPNoRouteAvailable|lSPPathErr|lSPPathTearSent|lSPRequestedBandwidthUnavailable|lSPReservationNotReceived|lSPReservationTearReceived|lSPReservationTearSent|lSPReservationTimeout|lSPRoutingLoops|lSPRoutingProblem|lSPRSVPSystemError|lSPServiceConflict|lSPServiceUnsupported|lSPTrafficControlError|lSPTrafficControlSystemError|lSPTrafficOrganizationError|lSPTrafficServiceError|lSPUnknownObjectClass|lSPUnknownObjectCType|lSPUnsupportedL3PID|mbbCompleted|mbbTriggered|none])
		"""
		return self._get_attribute('sessionInformation')

	@property
	def State(self):
		"""State

		Returns:
			list(str[down|none|notStarted|up])
		"""
		return self._get_attribute('state')

	def update(self, Name=None, NumberOfEroSubObjects=None):
		"""Updates a child instance of rsvpP2mpIngressSubLsps on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfEroSubObjects (number): Number Of ERO Sub-Objects

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def get_device_ids(self, PortNames=None, Active=None, AppendLeaf=None, EnableEro=None, LeafIp=None, PrefixLengthOfDut=None, PrefixLengthOfLeaf=None, PrependDut=None, SendAsEro=None, SendAsSero=None):
		"""Base class infrastructure that gets a list of rsvpP2mpIngressSubLsps device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			Active (str): optional regex of active
			AppendLeaf (str): optional regex of appendLeaf
			EnableEro (str): optional regex of enableEro
			LeafIp (str): optional regex of leafIp
			PrefixLengthOfDut (str): optional regex of prefixLengthOfDut
			PrefixLengthOfLeaf (str): optional regex of prefixLengthOfLeaf
			PrependDut (str): optional regex of prependDut
			SendAsEro (str): optional regex of sendAsEro
			SendAsSero (str): optional regex of sendAsSero

		Returns:
			list(int): A list of device ids that meets the regex criteria provided in the method parameters

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._get_ngpf_device_ids(locals())

	def ExcludeEroOrSero(self, *args, **kwargs):
		"""Executes the excludeEroOrSero operation on the server.

		Prune Ingress P2MP SubLSP

		excludeEroOrSero(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('excludeEroOrSero', payload=payload, response_object=None)

	def GraftSubLsp(self, *args, **kwargs):
		"""Executes the graftSubLsp operation on the server.

		Activate/Enable Tunnel selected SubLsp Ranges

		graftSubLsp(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('graftSubLsp', payload=payload, response_object=None)

	def IncludeEroOrSero(self, *args, **kwargs):
		"""Executes the includeEroOrSero operation on the server.

		Graft Ingress P2MP SubLSP

		includeEroOrSero(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('includeEroOrSero', payload=payload, response_object=None)

	def PruneSubLsp(self, *args, **kwargs):
		"""Executes the pruneSubLsp operation on the server.

		Deactivate/Disable selected Tunnel SubLsp Ranges

		pruneSubLsp(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('pruneSubLsp', payload=payload, response_object=None)
