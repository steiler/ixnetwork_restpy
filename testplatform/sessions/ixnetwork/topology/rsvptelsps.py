# Copyright 1997 - 2018 by IXIA Keysight
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


class RsvpteLsps(Base):
	"""The RsvpteLsps class encapsulates a user managed rsvpteLsps node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the RsvpteLsps property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server using the find method.
	The internal properties list can be managed by the user by using the add and remove methods.
	"""

	_SDM_NAME = 'rsvpteLsps'

	def __init__(self, parent):
		super(RsvpteLsps, self).__init__(parent)

	@property
	def RsvpP2PEgressLsps(self):
		"""An instance of the RsvpP2PEgressLsps class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpp2pegresslsps.RsvpP2PEgressLsps)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpp2pegresslsps import RsvpP2PEgressLsps
		return RsvpP2PEgressLsps(self)._select()

	@property
	def RsvpP2PIngressLsps(self):
		"""An instance of the RsvpP2PIngressLsps class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpp2pingresslsps.RsvpP2PIngressLsps)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpp2pingresslsps import RsvpP2PIngressLsps
		return RsvpP2PIngressLsps(self)._select()

	@property
	def RsvpP2mpEgressLsps(self):
		"""An instance of the RsvpP2mpEgressLsps class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpp2mpegresslsps.RsvpP2mpEgressLsps)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpp2mpegresslsps import RsvpP2mpEgressLsps
		return RsvpP2mpEgressLsps(self)._select()

	@property
	def RsvpP2mpIngressLsps(self):
		"""An instance of the RsvpP2mpIngressLsps class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpp2mpingresslsps.RsvpP2mpIngressLsps)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpp2mpingresslsps import RsvpP2mpIngressLsps
		return RsvpP2mpIngressLsps(self)._select()

	@property
	def RsvpPcepExpectedInitiatedLsps(self):
		"""An instance of the RsvpPcepExpectedInitiatedLsps class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvppcepexpectedinitiatedlsps.RsvpPcepExpectedInitiatedLsps)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvppcepexpectedinitiatedlsps import RsvpPcepExpectedInitiatedLsps
		return RsvpPcepExpectedInitiatedLsps(self)._select()

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def ConnectedVia(self):
		"""List of layers this layer used to connect to the wire

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])
		"""
		return self._get_attribute('connectedVia')
	@ConnectedVia.setter
	def ConnectedVia(self, value):
		self._set_attribute('connectedVia', value)

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def EnableP2PEgress(self):
		"""Enable to configure P2P Egress LSPs

		Returns:
			bool
		"""
		return self._get_attribute('enableP2PEgress')
	@EnableP2PEgress.setter
	def EnableP2PEgress(self, value):
		self._set_attribute('enableP2PEgress', value)

	@property
	def Errors(self):
		"""A list of errors that have occurred

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
		"""
		return self._get_attribute('errors')

	@property
	def ExpectedPceInitiatedLspsCount(self):
		"""Number of Expected PCE Initiated RSVP-TE LSPs

		Returns:
			number
		"""
		return self._get_attribute('expectedPceInitiatedLspsCount')
	@ExpectedPceInitiatedLspsCount.setter
	def ExpectedPceInitiatedLspsCount(self, value):
		self._set_attribute('expectedPceInitiatedLspsCount', value)

	@property
	def IngressP2PLsps(self):
		"""Number of P2P Ingress LSPs configured per IPv4 Loopback

		Returns:
			number
		"""
		return self._get_attribute('ingressP2PLsps')
	@IngressP2PLsps.setter
	def IngressP2PLsps(self, value):
		self._set_attribute('ingressP2PLsps', value)

	@property
	def LocalIp(self):
		"""Local IP

		Returns:
			list(str)
		"""
		return self._get_attribute('localIp')

	@property
	def Multiplier(self):
		"""Number of layer instances per parent instance (multiplier)

		Returns:
			number
		"""
		return self._get_attribute('multiplier')
	@Multiplier.setter
	def Multiplier(self, value):
		self._set_attribute('multiplier', value)

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
	def P2mpEgressTunnelCount(self):
		"""Number of P2MP Egress Tunnels configured per IPv4 Loopback

		Returns:
			number
		"""
		return self._get_attribute('p2mpEgressTunnelCount')
	@P2mpEgressTunnelCount.setter
	def P2mpEgressTunnelCount(self, value):
		self._set_attribute('p2mpEgressTunnelCount', value)

	@property
	def P2mpIngressLspCount(self):
		"""Number of P2MP Ingress LSPs configured per IPv4 Loopback

		Returns:
			number
		"""
		return self._get_attribute('p2mpIngressLspCount')
	@P2mpIngressLspCount.setter
	def P2mpIngressLspCount(self, value):
		self._set_attribute('p2mpIngressLspCount', value)

	@property
	def SessionStatus(self):
		"""Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.

		Returns:
			list(str[down|notStarted|up])
		"""
		return self._get_attribute('sessionStatus')

	@property
	def StackedLayers(self):
		"""List of secondary (many to one) child layer protocols

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])
		"""
		return self._get_attribute('stackedLayers')
	@StackedLayers.setter
	def StackedLayers(self, value):
		self._set_attribute('stackedLayers', value)

	@property
	def StateCounts(self):
		"""A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up

		Returns:
			dict(total:number,notStarted:number,down:number,up:number)
		"""
		return self._get_attribute('stateCounts')

	@property
	def Status(self):
		"""Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			str(configured|error|mixed|notStarted|started|starting|stopping)
		"""
		return self._get_attribute('status')

	def add(self, ConnectedVia=None, EnableP2PEgress=None, ExpectedPceInitiatedLspsCount=None, IngressP2PLsps=None, Multiplier=None, Name=None, P2mpEgressTunnelCount=None, P2mpIngressLspCount=None, StackedLayers=None):
		"""Adds a new rsvpteLsps node on the server and retrieves it in this instance.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			EnableP2PEgress (bool): Enable to configure P2P Egress LSPs
			ExpectedPceInitiatedLspsCount (number): Number of Expected PCE Initiated RSVP-TE LSPs
			IngressP2PLsps (number): Number of P2P Ingress LSPs configured per IPv4 Loopback
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			P2mpEgressTunnelCount (number): Number of P2MP Egress Tunnels configured per IPv4 Loopback
			P2mpIngressLspCount (number): Number of P2MP Ingress LSPs configured per IPv4 Loopback
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			self: This instance with all currently retrieved rsvpteLsps data using find and the newly added rsvpteLsps data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the rsvpteLsps data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, EnableP2PEgress=None, Errors=None, ExpectedPceInitiatedLspsCount=None, IngressP2PLsps=None, LocalIp=None, Multiplier=None, Name=None, P2mpEgressTunnelCount=None, P2mpIngressLspCount=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
		"""Finds and retrieves rsvpteLsps data from the server.

		All named parameters support regex and can be used to selectively retrieve rsvpteLsps data from the server.
		By default the find method takes no parameters and will retrieve all rsvpteLsps data from the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableP2PEgress (bool): Enable to configure P2P Egress LSPs
			Errors (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))): A list of errors that have occurred
			ExpectedPceInitiatedLspsCount (number): Number of Expected PCE Initiated RSVP-TE LSPs
			IngressP2PLsps (number): Number of P2P Ingress LSPs configured per IPv4 Loopback
			LocalIp (list(str)): Local IP
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			P2mpEgressTunnelCount (number): Number of P2MP Egress Tunnels configured per IPv4 Loopback
			P2mpIngressLspCount (number): Number of P2MP Ingress LSPs configured per IPv4 Loopback
			SessionStatus (list(str[down|notStarted|up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			self: This instance with matching rsvpteLsps data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of rsvpteLsps data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the rsvpteLsps data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, Active=None):
		"""Base class infrastructure that gets a list of rsvpteLsps device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			Active (str): optional regex of active

		Returns:
			list(int): A list of device ids that meets the regex criteria provided in the method parameters

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._get_ngpf_device_ids(locals())

	def FetchAndUpdateConfigFromCloud(self, *args, **kwargs):
		"""Executes the fetchAndUpdateConfigFromCloud operation on the server.

		fetchAndUpdateConfigFromCloud(Mode:string)
			Args:
				args[0] is Mode (str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('fetchAndUpdateConfigFromCloud', payload=payload, response_object=None)

	def RestartDown(self, *args, **kwargs):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions that are in Down state.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		restartDown()

		restartDown(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		restartDown(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('restartDown', payload=payload, response_object=None)

	def Start(self, *args, **kwargs):
		"""Executes the start operation on the server.

		Start selected protocols.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		start()

		start(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		start(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('start', payload=payload, response_object=None)

	def Stop(self, *args, **kwargs):
		"""Executes the stop operation on the server.

		Stop selected protocols.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		stop()

		stop(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		stop(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('stop', payload=payload, response_object=None)
