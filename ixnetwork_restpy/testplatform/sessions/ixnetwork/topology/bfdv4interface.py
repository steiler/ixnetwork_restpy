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


class Bfdv4Interface(Base):
	"""BFDv4 Interface (Device) level Configuration
	The Bfdv4Interface class encapsulates a list of bfdv4Interface resources that is be managed by the user.
	A list of resources can be retrieved from the server using the Bfdv4Interface.find() method.
	The list can be managed by the user by using the Bfdv4Interface.add() and Bfdv4Interface.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'bfdv4Interface'

	def __init__(self, parent):
		super(Bfdv4Interface, self).__init__(parent)

	@property
	def Bfdv4Session(self):
		"""An instance of the Bfdv4Session class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv4session.Bfdv4Session)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv4session import Bfdv4Session
		return Bfdv4Session(self)._select()

	@property
	def LearnedInfo(self):
		"""An instance of the LearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo.LearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo import LearnedInfo
		return LearnedInfo(self)

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def AggregateBfdSession(self):
		"""If enabled, all interfaces except on VNI 0 will be disabled and grayed-out.

		Returns:
			bool
		"""
		return self._get_attribute('aggregateBfdSession')
	@AggregateBfdSession.setter
	def AggregateBfdSession(self, value):
		self._set_attribute('aggregateBfdSession', value)

	@property
	def ConfigureEchoSourceIp(self):
		"""Selecting this check box enables the ability to configure the source address IP of echo message

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('configureEchoSourceIp')

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
	def EchoRxInterval(self):
		"""The minimum interval, in milliseconds, between received BFD Echo packets that this interface is capable of supporting. If this value is zero, the transmitting system does not support the receipt of BFD Echo packets

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('echoRxInterval')

	@property
	def EchoTimeOut(self):
		"""The interval, in milliseconds, that the interface waits for a response to the last Echo packet sent out

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('echoTimeOut')

	@property
	def EchoTxInterval(self):
		"""The minimum interval, in milliseconds, that the interface would like to use when transmitting BFD Echo packets

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('echoTxInterval')

	@property
	def EnableControlPlaneIndependent(self):
		"""This check box enables Control Plane Independent Mode. If set, the interface's BFD is implemented in the forwarding plane and can continue to function through disruptions in the control plane

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableControlPlaneIndependent')

	@property
	def EnableDemandMode(self):
		"""This check box enables Demand Mode. In this mode, it is assumed the interface has an independent way of verifying it has connectivity to the other system. Once a BFD session is established, the systems stop sending BFD Control packets, except when either system feels the need to verify connectivity explicitly. In this case, a short sequence of BFD Control packets is sent

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableDemandMode')

	@property
	def Errors(self):
		"""A list of errors that have occurred

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
		"""
		return self._get_attribute('errors')

	@property
	def FlapTxIntervals(self):
		"""The number of Tx packets sent from device after which session flaps for BFD. A value of zero means no flapping

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('flapTxIntervals')

	@property
	def IpDiffServ(self):
		"""IP DiffServ/TOSByte (Dec)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipDiffServ')

	@property
	def LocalRouterId(self):
		"""The BFD Router ID value, in IPv4 format.

		Returns:
			list(str)
		"""
		return self._get_attribute('localRouterId')

	@property
	def MinRxInterval(self):
		"""The minimum interval, in milliseconds, between received BFD Control packets that this interface is capable of supporting

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('minRxInterval')

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
	def NoOfSessions(self):
		"""The number of configured BFD sessions

		Returns:
			number
		"""
		return self._get_attribute('noOfSessions')
	@NoOfSessions.setter
	def NoOfSessions(self, value):
		self._set_attribute('noOfSessions', value)

	@property
	def PollInterval(self):
		"""The interval, in milliseconds, between exchanges of Control Messages in Demand Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('pollInterval')

	@property
	def SessionStatus(self):
		"""Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.

		Returns:
			list(str[down|notStarted|up])
		"""
		return self._get_attribute('sessionStatus')

	@property
	def SourceIp4(self):
		"""If Configure Echo Source-IP is selected, the IPv4 source address of the Echo Message

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sourceIp4')

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
	def TimeoutMultiplier(self):
		"""The negotiated transmit interval, multiplied by this value, provides the detection time for the interface

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('timeoutMultiplier')

	@property
	def TxInterval(self):
		"""The minimum interval, in milliseconds, that the interface would like to use when transmitting BFD Control packets

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('txInterval')

	@property
	def Vni(self):
		"""Corresponding VXLAN Protocol VNI.

		Returns:
			list(number)
		"""
		return self._get_attribute('vni')

	def update(self, AggregateBfdSession=None, ConnectedVia=None, Multiplier=None, Name=None, NoOfSessions=None, StackedLayers=None):
		"""Updates a child instance of bfdv4Interface on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			AggregateBfdSession (bool): If enabled, all interfaces except on VNI 0 will be disabled and grayed-out.
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfSessions (number): The number of configured BFD sessions
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, AggregateBfdSession=None, ConnectedVia=None, Multiplier=None, Name=None, NoOfSessions=None, StackedLayers=None):
		"""Adds a new bfdv4Interface node on the server and retrieves it in this instance.

		Args:
			AggregateBfdSession (bool): If enabled, all interfaces except on VNI 0 will be disabled and grayed-out.
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfSessions (number): The number of configured BFD sessions
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			self: This instance with all currently retrieved bfdv4Interface data using find and the newly added bfdv4Interface data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the bfdv4Interface data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, AggregateBfdSession=None, ConnectedVia=None, Count=None, DescriptiveName=None, Errors=None, LocalRouterId=None, Multiplier=None, Name=None, NoOfSessions=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None, Vni=None):
		"""Finds and retrieves bfdv4Interface data from the server.

		All named parameters support regex and can be used to selectively retrieve bfdv4Interface data from the server.
		By default the find method takes no parameters and will retrieve all bfdv4Interface data from the server.

		Args:
			AggregateBfdSession (bool): If enabled, all interfaces except on VNI 0 will be disabled and grayed-out.
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
			Errors (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))): A list of errors that have occurred
			LocalRouterId (list(str)): The BFD Router ID value, in IPv4 format.
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfSessions (number): The number of configured BFD sessions
			SessionStatus (list(str[down|notStarted|up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
			Vni (list(number)): Corresponding VXLAN Protocol VNI.

		Returns:
			self: This instance with matching bfdv4Interface data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of bfdv4Interface data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the bfdv4Interface data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, Active=None, ConfigureEchoSourceIp=None, EchoRxInterval=None, EchoTimeOut=None, EchoTxInterval=None, EnableControlPlaneIndependent=None, EnableDemandMode=None, FlapTxIntervals=None, IpDiffServ=None, MinRxInterval=None, PollInterval=None, SourceIp4=None, TimeoutMultiplier=None, TxInterval=None):
		"""Base class infrastructure that gets a list of bfdv4Interface device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			Active (str): optional regex of active
			ConfigureEchoSourceIp (str): optional regex of configureEchoSourceIp
			EchoRxInterval (str): optional regex of echoRxInterval
			EchoTimeOut (str): optional regex of echoTimeOut
			EchoTxInterval (str): optional regex of echoTxInterval
			EnableControlPlaneIndependent (str): optional regex of enableControlPlaneIndependent
			EnableDemandMode (str): optional regex of enableDemandMode
			FlapTxIntervals (str): optional regex of flapTxIntervals
			IpDiffServ (str): optional regex of ipDiffServ
			MinRxInterval (str): optional regex of minRxInterval
			PollInterval (str): optional regex of pollInterval
			SourceIp4 (str): optional regex of sourceIp4
			TimeoutMultiplier (str): optional regex of timeoutMultiplier
			TxInterval (str): optional regex of txInterval

		Returns:
			list(int): A list of device ids that meets the regex criteria provided in the method parameters

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._get_ngpf_device_ids(locals())

	def ClearLearnedInfo(self, *args, **kwargs):
		"""Executes the clearLearnedInfo operation on the server.

		Clear Learned Info

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		clearLearnedInfo()

		clearLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		clearLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		clearLearnedInfo(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('clearLearnedInfo', payload=payload, response_object=None)

	def DisableDemandMode(self, *args, **kwargs):
		"""Executes the disableDemandMode operation on the server.

		Disable Demand Mode

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		disableDemandMode(Arg2:list, Arg3:enum)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
				args[1] is Arg3 (str(ospf|ospfv3|bgp|ldp|rsvp|isis|pim|bfd)): Session used by Protocol

			Returns:
				list(str): ID to associate each async action invocation

		disableDemandMode(Arg2:enum)list
			Args:
				args[0] is Arg2 (str(ospf|ospfv3|bgp|ldp|rsvp|isis|pim|bfd)): Session used by Protocol

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('disableDemandMode', payload=payload, response_object=None)

	def EnableDemandMode(self, *args, **kwargs):
		"""Executes the enableDemandMode operation on the server.

		Enable Demand Mode

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		enableDemandMode(Arg2:list, Arg3:enum)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
				args[1] is Arg3 (str(ospf|ospfv3|bgp|ldp|rsvp|isis|pim|bfd)): Session used by Protocol

			Returns:
				list(str): ID to associate each async action invocation

		enableDemandMode(Arg2:enum)list
			Args:
				args[0] is Arg2 (str(ospf|ospfv3|bgp|ldp|rsvp|isis|pim|bfd)): Session used by Protocol

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('enableDemandMode', payload=payload, response_object=None)

	def GetLearnedInfo(self, *args, **kwargs):
		"""Executes the getLearnedInfo operation on the server.

		Get Learned Info

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		getLearnedInfo()

		getLearnedInfo(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		getLearnedInfo(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		getLearnedInfo(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('getLearnedInfo', payload=payload, response_object=None)

	def InitiatePoll(self, *args, **kwargs):
		"""Executes the initiatePoll operation on the server.

		Initiate Poll

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		initiatePoll(Arg2:list, Arg3:enum)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
				args[1] is Arg3 (str(ospf|ospfv3|bgp|ldp|rsvp|isis|pim|bfd)): Session used by Protocol

			Returns:
				list(str): ID to associate each async action invocation

		initiatePoll(Arg2:enum)list
			Args:
				args[0] is Arg2 (str(ospf|ospfv3|bgp|ldp|rsvp|isis|pim|bfd)): Session used by Protocol

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('initiatePoll', payload=payload, response_object=None)

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

	def ResumePDU(self, *args, **kwargs):
		"""Executes the resumePDU operation on the server.

		Resume PDU

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		resumePDU(Arg2:list, Arg3:enum)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
				args[1] is Arg3 (str(ospf|ospfv3|bgp|ldp|rsvp|isis|pim|bfd)): Session used by Protocol

			Returns:
				list(str): ID to associate each async action invocation

		resumePDU(Arg2:enum)list
			Args:
				args[0] is Arg2 (str(ospf|ospfv3|bgp|ldp|rsvp|isis|pim|bfd)): Session used by Protocol

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('resumePDU', payload=payload, response_object=None)

	def SetAdminDown(self, *args, **kwargs):
		"""Executes the setAdminDown operation on the server.

		Set Admin Down

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		setAdminDown(Arg2:list, Arg3:enum)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
				args[1] is Arg3 (str(ospf|ospfv3|bgp|ldp|rsvp|isis|pim|bfd)): Session used by Protocol

			Returns:
				list(str): ID to associate each async action invocation

		setAdminDown(Arg2:enum)list
			Args:
				args[0] is Arg2 (str(ospf|ospfv3|bgp|ldp|rsvp|isis|pim|bfd)): Session used by Protocol

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('setAdminDown', payload=payload, response_object=None)

	def SetAdminUp(self, *args, **kwargs):
		"""Executes the setAdminUp operation on the server.

		Set Admin Up

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		setAdminUp(Arg2:list, Arg3:enum)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
				args[1] is Arg3 (str(ospf|ospfv3|bgp|ldp|rsvp|isis|pim|bfd)): Session used by Protocol

			Returns:
				list(str): ID to associate each async action invocation

		setAdminUp(Arg2:enum)list
			Args:
				args[0] is Arg2 (str(ospf|ospfv3|bgp|ldp|rsvp|isis|pim|bfd)): Session used by Protocol

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('setAdminUp', payload=payload, response_object=None)

	def SetDiagnosticState(self, *args, **kwargs):
		"""Executes the setDiagnosticState operation on the server.

		Set Diagnostic State

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		setDiagnosticState(Arg2:list, Arg3:enum, Arg4:enum)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
				args[1] is Arg3 (str(ospf|ospfv3|bgp|ldp|rsvp|isis|pim|bfd)): Session used by Protocol
				args[2] is Arg4 (str(controlDetectionTimeExpired|echoFunctionFailed|neighbourSignaledSessionDown|forwardingPlaneReset|pathDown|concatenatedPathDown|administrativelyDown|reverseConcatenatedPathDown|reserved)): Diagnostic Code

			Returns:
				list(str): ID to associate each async action invocation

		setDiagnosticState(Arg2:enum, Arg3:enum)list
			Args:
				args[0] is Arg2 (str(ospf|ospfv3|bgp|ldp|rsvp|isis|pim|bfd)): Session used by Protocol
				args[1] is Arg3 (str(controlDetectionTimeExpired|echoFunctionFailed|neighbourSignaledSessionDown|forwardingPlaneReset|pathDown|concatenatedPathDown|administrativelyDown|reverseConcatenatedPathDown|reserved)): Diagnostic Code

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('setDiagnosticState', payload=payload, response_object=None)

	def Start(self, *args, **kwargs):
		"""Executes the start operation on the server.

		Activate Interface

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

		Deactivate Interface

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

		Stop PDU

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		stopPDU(Arg2:list, Arg3:enum)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
				args[1] is Arg3 (str(ospf|ospfv3|bgp|ldp|rsvp|isis|pim|bfd)): Session used by Protocol

			Returns:
				list(str): ID to associate each async action invocation

		stopPDU(Arg2:enum)list
			Args:
				args[0] is Arg2 (str(ospf|ospfv3|bgp|ldp|rsvp|isis|pim|bfd)): Session used by Protocol

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
