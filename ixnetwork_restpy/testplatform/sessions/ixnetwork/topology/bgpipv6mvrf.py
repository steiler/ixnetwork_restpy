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


class BgpIpv6MVrf(Base):
	"""BGP IPv6 Peer mVRF Configuration
	The BgpIpv6MVrf class encapsulates a list of bgpIpv6MVrf resources that is be managed by the user.
	A list of resources can be retrieved from the server using the BgpIpv6MVrf.find() method.
	The list can be managed by the user by using the BgpIpv6MVrf.add() and BgpIpv6MVrf.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'bgpIpv6MVrf'

	def __init__(self, parent):
		super(BgpIpv6MVrf, self).__init__(parent)

	@property
	def BgpExportRouteTargetList(self):
		"""An instance of the BgpExportRouteTargetList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpexportroutetargetlist.BgpExportRouteTargetList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpexportroutetargetlist import BgpExportRouteTargetList
		return BgpExportRouteTargetList(self)

	@property
	def BgpImportRouteTargetList(self):
		"""An instance of the BgpImportRouteTargetList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpimportroutetargetlist.BgpImportRouteTargetList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpimportroutetargetlist import BgpImportRouteTargetList
		return BgpImportRouteTargetList(self)

	@property
	def BgpUmhExportRouteTargetList(self):
		"""An instance of the BgpUmhExportRouteTargetList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpumhexportroutetargetlist.BgpUmhExportRouteTargetList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpumhexportroutetargetlist import BgpUmhExportRouteTargetList
		return BgpUmhExportRouteTargetList(self)

	@property
	def BgpUmhImportRouteTargetList(self):
		"""An instance of the BgpUmhImportRouteTargetList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpumhimportroutetargetlist.BgpUmhImportRouteTargetList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpumhimportroutetargetlist import BgpUmhImportRouteTargetList
		return BgpUmhImportRouteTargetList(self)

	@property
	def Connector(self):
		"""An instance of the Connector class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector.Connector)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector import Connector
		return Connector(self)

	@property
	def PnTLVList(self):
		"""An instance of the PnTLVList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pntlvlist.PnTLVList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pntlvlist import PnTLVList
		return PnTLVList(self)

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
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

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
	def DutIpv6(self):
		"""DUT IP

		Returns:
			list(str)
		"""
		return self._get_attribute('dutIpv6')

	@property
	def Errors(self):
		"""A list of errors that have occurred

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
		"""
		return self._get_attribute('errors')

	@property
	def ImportRtListSameAsExportRtList(self):
		"""Import RT List Same As Export RT List

		Returns:
			bool
		"""
		return self._get_attribute('importRtListSameAsExportRtList')
	@ImportRtListSameAsExportRtList.setter
	def ImportRtListSameAsExportRtList(self, value):
		self._set_attribute('importRtListSameAsExportRtList', value)

	@property
	def IncludePmsiTunnelAttribute(self):
		"""Include PMSI Tunnel Attribute

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includePmsiTunnelAttribute')

	@property
	def LocalIpv6(self):
		"""Local IP

		Returns:
			list(str)
		"""
		return self._get_attribute('localIpv6')

	@property
	def LocalRouterID(self):
		"""Router ID

		Returns:
			list(str)
		"""
		return self._get_attribute('localRouterID')

	@property
	def MulticastDistinguisherAs4Number(self):
		"""VMulticast Distinguisher AS4 Number

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('multicastDistinguisherAs4Number')

	@property
	def MulticastDistinguisherAsNumber(self):
		"""VMulticast Distinguisher AS Number

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('multicastDistinguisherAsNumber')

	@property
	def MulticastDistinguisherAssignedNumber(self):
		"""Multicast Distinguisher Assigned Number

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('multicastDistinguisherAssignedNumber')

	@property
	def MulticastDistinguisherIpAddress(self):
		"""Multicast Distinguisher IP Address

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('multicastDistinguisherIpAddress')

	@property
	def MulticastDistinguisherType(self):
		"""Multicast Distinguisher Type

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('multicastDistinguisherType')

	@property
	def MulticastTunnelType(self):
		"""Multicast Tunnel Type

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('multicastTunnelType')

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
	def NumRtInExportRouteTargetList(self):
		"""Number of RTs in Export Route Target List(multiplier)

		Returns:
			number
		"""
		return self._get_attribute('numRtInExportRouteTargetList')
	@NumRtInExportRouteTargetList.setter
	def NumRtInExportRouteTargetList(self, value):
		self._set_attribute('numRtInExportRouteTargetList', value)

	@property
	def NumRtInImportRouteTargetList(self):
		"""Number of RTs in Import Route Target List(multiplier)

		Returns:
			number
		"""
		return self._get_attribute('numRtInImportRouteTargetList')
	@NumRtInImportRouteTargetList.setter
	def NumRtInImportRouteTargetList(self, value):
		self._set_attribute('numRtInImportRouteTargetList', value)

	@property
	def NumRtInUmhExportRouteTargetList(self):
		"""Number of RTs in Export Route Target List(multiplier)

		Returns:
			number
		"""
		return self._get_attribute('numRtInUmhExportRouteTargetList')
	@NumRtInUmhExportRouteTargetList.setter
	def NumRtInUmhExportRouteTargetList(self, value):
		self._set_attribute('numRtInUmhExportRouteTargetList', value)

	@property
	def NumRtInUmhImportRouteTargetList(self):
		"""Number of RTs in Import Route Target List(multiplier)

		Returns:
			number
		"""
		return self._get_attribute('numRtInUmhImportRouteTargetList')
	@NumRtInUmhImportRouteTargetList.setter
	def NumRtInUmhImportRouteTargetList(self, value):
		self._set_attribute('numRtInUmhImportRouteTargetList', value)

	@property
	def RootAddress(self):
		"""Root Address

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('rootAddress')

	@property
	def RsvpP2mpId(self):
		"""RSVP P2MP ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('rsvpP2mpId')

	@property
	def RsvpP2mpIdAsNumber(self):
		"""RSVP P2MP ID as Number

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('rsvpP2mpIdAsNumber')

	@property
	def RsvpTunnelId(self):
		"""RSVP Tunnel ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('rsvpTunnelId')

	@property
	def SameAsExportRT(self):
		"""Same As Export RT Attribute

		Returns:
			bool
		"""
		return self._get_attribute('sameAsExportRT')
	@SameAsExportRT.setter
	def SameAsExportRT(self, value):
		self._set_attribute('sameAsExportRT', value)

	@property
	def SameAsImportRT(self):
		"""Same As Import RT Attribute

		Returns:
			bool
		"""
		return self._get_attribute('sameAsImportRT')
	@SameAsImportRT.setter
	def SameAsImportRT(self, value):
		self._set_attribute('sameAsImportRT', value)

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

	@property
	def UpOrDownStreamAssignedLabel(self):
		"""Upstream/Downstream Assigned Label

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('upOrDownStreamAssignedLabel')

	@property
	def UseUpOrDownStreamAssigneLabel(self):
		"""Use Upstream/Downstream Assigned Label

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('useUpOrDownStreamAssigneLabel')

	def update(self, ConnectedVia=None, ImportRtListSameAsExportRtList=None, Multiplier=None, Name=None, NumRtInExportRouteTargetList=None, NumRtInImportRouteTargetList=None, NumRtInUmhExportRouteTargetList=None, NumRtInUmhImportRouteTargetList=None, SameAsExportRT=None, SameAsImportRT=None, StackedLayers=None):
		"""Updates a child instance of bgpIpv6MVrf on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			NumRtInUmhExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInUmhImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			SameAsExportRT (bool): Same As Export RT Attribute
			SameAsImportRT (bool): Same As Import RT Attribute
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, ConnectedVia=None, ImportRtListSameAsExportRtList=None, Multiplier=None, Name=None, NumRtInExportRouteTargetList=None, NumRtInImportRouteTargetList=None, NumRtInUmhExportRouteTargetList=None, NumRtInUmhImportRouteTargetList=None, SameAsExportRT=None, SameAsImportRT=None, StackedLayers=None):
		"""Adds a new bgpIpv6MVrf node on the server and retrieves it in this instance.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			NumRtInUmhExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInUmhImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			SameAsExportRT (bool): Same As Export RT Attribute
			SameAsImportRT (bool): Same As Import RT Attribute
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

		Returns:
			self: This instance with all currently retrieved bgpIpv6MVrf data using find and the newly added bgpIpv6MVrf data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the bgpIpv6MVrf data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, DutIpv6=None, Errors=None, ImportRtListSameAsExportRtList=None, LocalIpv6=None, LocalRouterID=None, Multiplier=None, Name=None, NumRtInExportRouteTargetList=None, NumRtInImportRouteTargetList=None, NumRtInUmhExportRouteTargetList=None, NumRtInUmhImportRouteTargetList=None, SameAsExportRT=None, SameAsImportRT=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
		"""Finds and retrieves bgpIpv6MVrf data from the server.

		All named parameters support regex and can be used to selectively retrieve bgpIpv6MVrf data from the server.
		By default the find method takes no parameters and will retrieve all bgpIpv6MVrf data from the server.

		Args:
			ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
			DutIpv6 (list(str)): DUT IP
			Errors (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))): A list of errors that have occurred
			ImportRtListSameAsExportRtList (bool): Import RT List Same As Export RT List
			LocalIpv6 (list(str)): Local IP
			LocalRouterID (list(str)): Router ID
			Multiplier (number): Number of layer instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumRtInExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			NumRtInUmhExportRouteTargetList (number): Number of RTs in Export Route Target List(multiplier)
			NumRtInUmhImportRouteTargetList (number): Number of RTs in Import Route Target List(multiplier)
			SameAsExportRT (bool): Same As Export RT Attribute
			SameAsImportRT (bool): Same As Import RT Attribute
			SessionStatus (list(str[down|notStarted|up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
			StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
			StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			self: This instance with matching bgpIpv6MVrf data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of bgpIpv6MVrf data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the bgpIpv6MVrf data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, Active=None, IncludePmsiTunnelAttribute=None, MulticastDistinguisherAs4Number=None, MulticastDistinguisherAsNumber=None, MulticastDistinguisherAssignedNumber=None, MulticastDistinguisherIpAddress=None, MulticastDistinguisherType=None, MulticastTunnelType=None, RootAddress=None, RsvpP2mpId=None, RsvpP2mpIdAsNumber=None, RsvpTunnelId=None, UpOrDownStreamAssignedLabel=None, UseUpOrDownStreamAssigneLabel=None):
		"""Base class infrastructure that gets a list of bgpIpv6MVrf device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			Active (str): optional regex of active
			IncludePmsiTunnelAttribute (str): optional regex of includePmsiTunnelAttribute
			MulticastDistinguisherAs4Number (str): optional regex of multicastDistinguisherAs4Number
			MulticastDistinguisherAsNumber (str): optional regex of multicastDistinguisherAsNumber
			MulticastDistinguisherAssignedNumber (str): optional regex of multicastDistinguisherAssignedNumber
			MulticastDistinguisherIpAddress (str): optional regex of multicastDistinguisherIpAddress
			MulticastDistinguisherType (str): optional regex of multicastDistinguisherType
			MulticastTunnelType (str): optional regex of multicastTunnelType
			RootAddress (str): optional regex of rootAddress
			RsvpP2mpId (str): optional regex of rsvpP2mpId
			RsvpP2mpIdAsNumber (str): optional regex of rsvpP2mpIdAsNumber
			RsvpTunnelId (str): optional regex of rsvpTunnelId
			UpOrDownStreamAssignedLabel (str): optional regex of upOrDownStreamAssignedLabel
			UseUpOrDownStreamAssigneLabel (str): optional regex of useUpOrDownStreamAssigneLabel

		Returns:
			list(int): A list of device ids that meets the regex criteria provided in the method parameters

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._get_ngpf_device_ids(locals())

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

		Start BGP VRF

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

		Stop BGP VRF

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
