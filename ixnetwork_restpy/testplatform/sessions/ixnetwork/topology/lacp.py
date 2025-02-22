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


class Lacp(Base):
	"""
	The Lacp class encapsulates a list of lacp resources that is be managed by the user.
	A list of resources can be retrieved from the server using the Lacp.find() method.
	The list can be managed by the user by using the Lacp.add() and Lacp.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'lacp'

	def __init__(self, parent):
		super(Lacp, self).__init__(parent)

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def ActorKey(self):
		"""Actor Key

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('actorKey')

	@property
	def ActorPortNumber(self):
		"""Actor Port Number

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('actorPortNumber')

	@property
	def ActorPortPriority(self):
		"""Actor Port Priority

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('actorPortPriority')

	@property
	def ActorSystemId(self):
		"""Actor System Id

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('actorSystemId')

	@property
	def ActorSystemPriority(self):
		"""Actor System Priority

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('actorSystemPriority')

	@property
	def AdministrativeKey(self):
		"""Administrative Key

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('administrativeKey')

	@property
	def AggregationFlagState(self):
		"""Aggregation Flag State

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('aggregationFlagState')

	@property
	def CollectingFlag(self):
		"""Collecting Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('collectingFlag')

	@property
	def CollectorsMaxdelay(self):
		"""Collectors Maximum Delay

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('collectorsMaxdelay')

	@property
	def ConnectedVia(self):
		"""DEPRECATED List of layers this layer used to connect to the wire

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])
		"""
		return self._get_attribute('connectedVia')
	@ConnectedVia.setter
	def ConnectedVia(self, value):
		self._set_attribute('connectedVia', value)

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
	def DistributingFlag(self):
		"""Distributing Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('distributingFlag')

	@property
	def Errors(self):
		"""A list of errors that have occurred

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
		"""
		return self._get_attribute('errors')

	@property
	def InterMarkerPDUDelay(self):
		"""Inter Marker PDU Delay (sec)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('interMarkerPDUDelay')

	@property
	def InterMarkerPDUDelayRandomMax(self):
		"""Inter Marker PDU Delay Random Max (sec)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('interMarkerPDUDelayRandomMax')

	@property
	def InterMarkerPDUDelayRandomMin(self):
		"""Inter Marker PDU Delay Random Min (sec)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('interMarkerPDUDelayRandomMin')

	@property
	def LacpActivity(self):
		"""LACP Actvity

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lacpActivity')

	@property
	def LacpduPeriodicTimeInterval(self):
		"""Lacp PDU Periodic Time Interval

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lacpduPeriodicTimeInterval')

	@property
	def LacpduTimeout(self):
		"""Lacp PDU Timeout

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lacpduTimeout')

	@property
	def MarkerRequestMode(self):
		"""Marker Request Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('markerRequestMode')

	@property
	def MarkerResponseWaitTime(self):
		"""Marker Response Wait Time (sec)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('markerResponseWaitTime')

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
	def PeriodicSendingOfMarkerRequest(self):
		"""Periodic Sending Of Marker Request

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('periodicSendingOfMarkerRequest')

	@property
	def SendMarkerRequestOnLagChange(self):
		"""Send Marker Request On Lag Change

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sendMarkerRequestOnLagChange')

	@property
	def SessionStatus(self):
		"""Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.

		Returns:
			list(str[down|notStarted|up])
		"""
		return self._get_attribute('sessionStatus')

	@property
	def SourceMac(self):
		"""Source MAC

		Returns:
			list(str)
		"""
		return self._get_attribute('sourceMac')

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

	@property
	def SupportRespondingToMarker(self):
		"""Support Responding To Marker

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('supportRespondingToMarker')

	@property
	def SynchronizationFlag(self):
		"""Synchronization Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('synchronizationFlag')

	def update(self, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None):
		"""Updates a child instance of lacp on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None):
		"""Adds a new lacp node on the server and retrieves it in this instance.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			self: This instance with all currently retrieved lacp data using find and the newly added lacp data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the lacp data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, Errors=None, Multiplier=None, Name=None, SessionStatus=None, SourceMac=None, StackedLayers=None, StateCounts=None, Status=None):
		"""Finds and retrieves lacp data from the server.

		All named parameters support regex and can be used to selectively retrieve lacp data from the server.
		By default the find method takes no parameters and will retrieve all lacp data from the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
			Errors (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))): A list of errors that have occurred
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			SessionStatus (list(str[down|notStarted|up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
			SourceMac (list(str)): Source MAC
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			self: This instance with matching lacp data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of lacp data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the lacp data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, Active=None, ActorKey=None, ActorPortNumber=None, ActorPortPriority=None, ActorSystemId=None, ActorSystemPriority=None, AdministrativeKey=None, AggregationFlagState=None, CollectingFlag=None, CollectorsMaxdelay=None, DistributingFlag=None, InterMarkerPDUDelay=None, InterMarkerPDUDelayRandomMax=None, InterMarkerPDUDelayRandomMin=None, LacpActivity=None, LacpduPeriodicTimeInterval=None, LacpduTimeout=None, MarkerRequestMode=None, MarkerResponseWaitTime=None, PeriodicSendingOfMarkerRequest=None, SendMarkerRequestOnLagChange=None, SupportRespondingToMarker=None, SynchronizationFlag=None):
		"""Base class infrastructure that gets a list of lacp device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			Active (str): optional regex of active
			ActorKey (str): optional regex of actorKey
			ActorPortNumber (str): optional regex of actorPortNumber
			ActorPortPriority (str): optional regex of actorPortPriority
			ActorSystemId (str): optional regex of actorSystemId
			ActorSystemPriority (str): optional regex of actorSystemPriority
			AdministrativeKey (str): optional regex of administrativeKey
			AggregationFlagState (str): optional regex of aggregationFlagState
			CollectingFlag (str): optional regex of collectingFlag
			CollectorsMaxdelay (str): optional regex of collectorsMaxdelay
			DistributingFlag (str): optional regex of distributingFlag
			InterMarkerPDUDelay (str): optional regex of interMarkerPDUDelay
			InterMarkerPDUDelayRandomMax (str): optional regex of interMarkerPDUDelayRandomMax
			InterMarkerPDUDelayRandomMin (str): optional regex of interMarkerPDUDelayRandomMin
			LacpActivity (str): optional regex of lacpActivity
			LacpduPeriodicTimeInterval (str): optional regex of lacpduPeriodicTimeInterval
			LacpduTimeout (str): optional regex of lacpduTimeout
			MarkerRequestMode (str): optional regex of markerRequestMode
			MarkerResponseWaitTime (str): optional regex of markerResponseWaitTime
			PeriodicSendingOfMarkerRequest (str): optional regex of periodicSendingOfMarkerRequest
			SendMarkerRequestOnLagChange (str): optional regex of sendMarkerRequestOnLagChange
			SupportRespondingToMarker (str): optional regex of supportRespondingToMarker
			SynchronizationFlag (str): optional regex of synchronizationFlag

		Returns:
			list(int): A list of device ids that meets the regex criteria provided in the method parameters

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._get_ngpf_device_ids(locals())

	def LacpStartPDU(self, *args, **kwargs):
		"""Executes the lacpStartPDU operation on the server.

		LACP Start PDU

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		lacpStartPDU()

		lacpStartPDU(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		lacpStartPDU(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('lacpStartPDU', payload=payload, response_object=None)

	def LacpStopPDU(self, *args, **kwargs):
		"""Executes the lacpStopPDU operation on the server.

		LACP Stop PDU

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		lacpStopPDU()

		lacpStopPDU(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		lacpStopPDU(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('lacpStopPDU', payload=payload, response_object=None)

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

	def SendMarker(self, *args, **kwargs):
		"""Executes the sendMarker operation on the server.

		Send Marker

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		sendMarker()

		sendMarker(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		sendMarker(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendMarker', payload=payload, response_object=None)

	def SendMarkerRequest(self, *args, **kwargs):
		"""Executes the sendMarkerRequest operation on the server.

		Send MArker on the Lacp Link.

		sendMarkerRequest(Arg2:list)list
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
		return self._execute('sendMarkerRequest', payload=payload, response_object=None)

	def Start(self, *args, **kwargs):
		"""Executes the start operation on the server.

		Start LACP

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

	def StartPDU(self, *args, **kwargs):
		"""Executes the startPDU operation on the server.

		Starts PDU on the Lacp Link.

		startPDU(Arg2:list)list
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
		return self._execute('startPDU', payload=payload, response_object=None)

	def Stop(self, *args, **kwargs):
		"""Executes the stop operation on the server.

		Stop LACP

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

	def StopPDU(self, *args, **kwargs):
		"""Executes the stopPDU operation on the server.

		Stop PDU on the Lacp Link.

		stopPDU(Arg2:list)list
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
		return self._execute('stopPDU', payload=payload, response_object=None)
