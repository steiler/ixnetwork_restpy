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


class Ospfv2Router(Base):
	"""Ospf Device level Configuration
	The Ospfv2Router class encapsulates a list of ospfv2Router resources that is managed by the system.
	A list of resources can be retrieved from the server using the Ospfv2Router.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'ospfv2Router'

	def __init__(self, parent):
		super(Ospfv2Router, self).__init__(parent)

	@property
	def OspfBierSubDomainList(self):
		"""An instance of the OspfBierSubDomainList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfbiersubdomainlist.OspfBierSubDomainList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfbiersubdomainlist import OspfBierSubDomainList
		return OspfBierSubDomainList(self)._select()

	@property
	def OspfSRAlgorithmList(self):
		"""An instance of the OspfSRAlgorithmList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfsralgorithmlist.OspfSRAlgorithmList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfsralgorithmlist import OspfSRAlgorithmList
		return OspfSRAlgorithmList(self)

	@property
	def OspfSRGBRangeSubObjectsList(self):
		"""An instance of the OspfSRGBRangeSubObjectsList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfsrgbrangesubobjectslist.OspfSRGBRangeSubObjectsList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfsrgbrangesubobjectslist import OspfSRGBRangeSubObjectsList
		return OspfSRGBRangeSubObjectsList(self)

	@property
	def BIERPrefix(self):
		"""A BFR's BFR-Prefix is an IP address (either IPv4 or IPv6) of the BFR, and MUST be unique and routable within the BIER domain.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('BIERPrefix')

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def Algorithm(self):
		"""Algorithm for the Node SID/Label

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('algorithm')

	@property
	def BBit(self):
		"""Router-LSA B-Bit

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bBit')

	@property
	def BierAFlag(self):
		"""Attach Flag: If set an Area Border Router (ABR) will generate an Extended Prefix TLV for inter-area prefix that is locally connected or attached in other connected area

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bierAFlag')

	@property
	def BierNFlag(self):
		"""Node Flag: Set when the prefix identifies the advertising router i.e., the prefix is a host prefix advertising a globally reachable address typically associated with a loopback address

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bierNFlag')

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
	def DiscardLearnedLsa(self):
		"""Discard Learned LSAs

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('discardLearnedLsa')

	@property
	def DoNotGenerateRouterLsa(self):
		"""Generate Router LSA.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('doNotGenerateRouterLsa')

	@property
	def EBit(self):
		"""Router-LSA E-Bit

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('eBit')

	@property
	def EFlag(self):
		"""Explicit-Null Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('eFlag')

	@property
	def EnableBIER(self):
		"""Enable BIER

		Returns:
			bool
		"""
		return self._get_attribute('enableBIER')
	@EnableBIER.setter
	def EnableBIER(self, value):
		self._set_attribute('enableBIER', value)

	@property
	def EnableMappingServer(self):
		"""Enable Mapping Server of Segment Routing

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableMappingServer')

	@property
	def EnableSegmentRouting(self):
		"""Enable Segment Routing

		Returns:
			bool
		"""
		return self._get_attribute('enableSegmentRouting')
	@EnableSegmentRouting.setter
	def EnableSegmentRouting(self, value):
		self._set_attribute('enableSegmentRouting', value)

	@property
	def Errors(self):
		"""A list of errors that have occurred

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
		"""
		return self._get_attribute('errors')

	@property
	def GracefulRestart(self):
		"""Enable Graceful Restart,if enabled Discard Learned LSAs should be disabled in order to learn the LSAs

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('gracefulRestart')

	@property
	def HighPerfLearningModeForSR(self):
		"""This option can be used to increase scale. When enabled then the minimum information required to generate traffic is stored instead of the entire LSA. For example, for SR traffic generation, sid, vflag, SRGB details are stored and label is calculated accordingly. Please note when this flag is enabled, we will not store any LSAs so Learned Info will not display any details. Currently this is supported for only SR opaque LSAs, other Opaque LSAs like BIER, Graceful Restart is not supported, also not supported for BGP-LS scenarios.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('highPerfLearningModeForSR')

	@property
	def InterFloodLsUpdateBurstGap(self):
		"""Inter Flood LSUpdate burst gap (ms)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('interFloodLsUpdateBurstGap')

	@property
	def LFlag(self):
		"""Local or Global Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lFlag')

	@property
	def LocalRouterID(self):
		"""Router ID

		Returns:
			list(str)
		"""
		return self._get_attribute('localRouterID')

	@property
	def LoopBackAddress(self):
		"""Router ID

		Returns:
			list(str)
		"""
		return self._get_attribute('loopBackAddress')

	@property
	def LsaRefreshTime(self):
		"""LSA Refresh time (s)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lsaRefreshTime')

	@property
	def LsaRetransmitTime(self):
		"""LSA Retransmit time(s)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lsaRetransmitTime')

	@property
	def MFlag(self):
		"""Mapping Server Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('mFlag')

	@property
	def MaxLsUpdatesPerBurst(self):
		"""Max Flood LSUpdates Per Burst

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('maxLsUpdatesPerBurst')

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
	def NoOfAddressPrefix(self):
		"""Number Of Address Prefix Range

		Returns:
			number
		"""
		return self._get_attribute('noOfAddressPrefix')
	@NoOfAddressPrefix.setter
	def NoOfAddressPrefix(self, value):
		self._set_attribute('noOfAddressPrefix', value)

	@property
	def NoOfBIERSubDomains(self):
		"""Number of BIER Sub Domains

		Returns:
			number
		"""
		return self._get_attribute('noOfBIERSubDomains')
	@NoOfBIERSubDomains.setter
	def NoOfBIERSubDomains(self, value):
		self._set_attribute('noOfBIERSubDomains', value)

	@property
	def NpFlag(self):
		"""No-PHP Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('npFlag')

	@property
	def OobResyncBreakout(self):
		"""Enable out-of-band resynchronization breakout

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('oobResyncBreakout')

	@property
	def SRAlgorithmCount(self):
		"""SR Algorithm Count

		Returns:
			number
		"""
		return self._get_attribute('sRAlgorithmCount')
	@SRAlgorithmCount.setter
	def SRAlgorithmCount(self, value):
		self._set_attribute('sRAlgorithmCount', value)

	@property
	def SessionInfo(self):
		"""Logs additional information about the session Information

		Returns:
			list(str[noIfaceUp|sameNbrRouterId|up])
		"""
		return self._get_attribute('sessionInfo')

	@property
	def SessionStatus(self):
		"""Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.

		Returns:
			list(str[down|notStarted|up])
		"""
		return self._get_attribute('sessionStatus')

	@property
	def SidIndexLabel(self):
		"""SID/Index/Label

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sidIndexLabel')

	@property
	def SrgbRangeCount(self):
		"""SRGB Range Count

		Returns:
			number
		"""
		return self._get_attribute('srgbRangeCount')
	@SrgbRangeCount.setter
	def SrgbRangeCount(self, value):
		self._set_attribute('srgbRangeCount', value)

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
	def StrictLsaChecking(self):
		"""Terminate graceful restart when an LSA has changed

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('strictLsaChecking')

	@property
	def SupportForRfc3623(self):
		"""Support RFC 3623 features,if enabled Discard Learned LSAs should be disabled in order to learn the LSAs

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('supportForRfc3623')

	@property
	def SupportReasonSoftReloadUpgrade(self):
		"""Support graceful restart helper mode when restart reason is Software Reload or Upgrade.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('supportReasonSoftReloadUpgrade')

	@property
	def SupportReasonSoftRestart(self):
		"""Support graceful restart helper mode when restart reason is OSPFv2 software restart.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('supportReasonSoftRestart')

	@property
	def SupportReasonSwitchRedundantCntrlProcessor(self):
		"""Support graceful restart helper mode when restart reason is unplanned switchover.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('supportReasonSwitchRedundantCntrlProcessor')

	@property
	def SupportReasonUnknown(self):
		"""Support graceful restart helper mode when restart reason is unknown and unplanned.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('supportReasonUnknown')

	@property
	def VFlag(self):
		"""Value or Index Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('vFlag')

	def update(self, EnableBIER=None, EnableSegmentRouting=None, Name=None, NoOfAddressPrefix=None, NoOfBIERSubDomains=None, SRAlgorithmCount=None, SrgbRangeCount=None):
		"""Updates a child instance of ospfv2Router on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			EnableBIER (bool): Enable BIER
			EnableSegmentRouting (bool): Enable Segment Routing
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfAddressPrefix (number): Number Of Address Prefix Range
			NoOfBIERSubDomains (number): Number of BIER Sub Domains
			SRAlgorithmCount (number): SR Algorithm Count
			SrgbRangeCount (number): SRGB Range Count

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def find(self, Count=None, DescriptiveName=None, EnableBIER=None, EnableSegmentRouting=None, Errors=None, LocalRouterID=None, LoopBackAddress=None, Name=None, NoOfAddressPrefix=None, NoOfBIERSubDomains=None, SRAlgorithmCount=None, SessionInfo=None, SessionStatus=None, SrgbRangeCount=None, StateCounts=None, Status=None):
		"""Finds and retrieves ospfv2Router data from the server.

		All named parameters support regex and can be used to selectively retrieve ospfv2Router data from the server.
		By default the find method takes no parameters and will retrieve all ospfv2Router data from the server.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
			EnableBIER (bool): Enable BIER
			EnableSegmentRouting (bool): Enable Segment Routing
			Errors (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))): A list of errors that have occurred
			LocalRouterID (list(str)): Router ID
			LoopBackAddress (list(str)): Router ID
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NoOfAddressPrefix (number): Number Of Address Prefix Range
			NoOfBIERSubDomains (number): Number of BIER Sub Domains
			SRAlgorithmCount (number): SR Algorithm Count
			SessionInfo (list(str[noIfaceUp|sameNbrRouterId|up])): Logs additional information about the session Information
			SessionStatus (list(str[down|notStarted|up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
			SrgbRangeCount (number): SRGB Range Count
			StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			self: This instance with matching ospfv2Router data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of ospfv2Router data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the ospfv2Router data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, BIERPrefix=None, Active=None, Algorithm=None, BBit=None, BierAFlag=None, BierNFlag=None, ConfigureSIDIndexLabel=None, DiscardLearnedLsa=None, DoNotGenerateRouterLsa=None, EBit=None, EFlag=None, EnableMappingServer=None, GracefulRestart=None, HighPerfLearningModeForSR=None, InterFloodLsUpdateBurstGap=None, LFlag=None, LsaRefreshTime=None, LsaRetransmitTime=None, MFlag=None, MaxLsUpdatesPerBurst=None, NpFlag=None, OobResyncBreakout=None, SidIndexLabel=None, StrictLsaChecking=None, SupportForRfc3623=None, SupportReasonSoftReloadUpgrade=None, SupportReasonSoftRestart=None, SupportReasonSwitchRedundantCntrlProcessor=None, SupportReasonUnknown=None, VFlag=None):
		"""Base class infrastructure that gets a list of ospfv2Router device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			BIERPrefix (str): optional regex of BIERPrefix
			Active (str): optional regex of active
			Algorithm (str): optional regex of algorithm
			BBit (str): optional regex of bBit
			BierAFlag (str): optional regex of bierAFlag
			BierNFlag (str): optional regex of bierNFlag
			ConfigureSIDIndexLabel (str): optional regex of configureSIDIndexLabel
			DiscardLearnedLsa (str): optional regex of discardLearnedLsa
			DoNotGenerateRouterLsa (str): optional regex of doNotGenerateRouterLsa
			EBit (str): optional regex of eBit
			EFlag (str): optional regex of eFlag
			EnableMappingServer (str): optional regex of enableMappingServer
			GracefulRestart (str): optional regex of gracefulRestart
			HighPerfLearningModeForSR (str): optional regex of highPerfLearningModeForSR
			InterFloodLsUpdateBurstGap (str): optional regex of interFloodLsUpdateBurstGap
			LFlag (str): optional regex of lFlag
			LsaRefreshTime (str): optional regex of lsaRefreshTime
			LsaRetransmitTime (str): optional regex of lsaRetransmitTime
			MFlag (str): optional regex of mFlag
			MaxLsUpdatesPerBurst (str): optional regex of maxLsUpdatesPerBurst
			NpFlag (str): optional regex of npFlag
			OobResyncBreakout (str): optional regex of oobResyncBreakout
			SidIndexLabel (str): optional regex of sidIndexLabel
			StrictLsaChecking (str): optional regex of strictLsaChecking
			SupportForRfc3623 (str): optional regex of supportForRfc3623
			SupportReasonSoftReloadUpgrade (str): optional regex of supportReasonSoftReloadUpgrade
			SupportReasonSoftRestart (str): optional regex of supportReasonSoftRestart
			SupportReasonSwitchRedundantCntrlProcessor (str): optional regex of supportReasonSwitchRedundantCntrlProcessor
			SupportReasonUnknown (str): optional regex of supportReasonUnknown
			VFlag (str): optional regex of vFlag

		Returns:
			list(int): A list of device ids that meets the regex criteria provided in the method parameters

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._get_ngpf_device_ids(locals())

	def OspfStartRouter(self, *args, **kwargs):
		"""Executes the ospfStartRouter operation on the server.

		Start OSPF Router

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		ospfStartRouter()

		ospfStartRouter(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		ospfStartRouter(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('ospfStartRouter', payload=payload, response_object=None)

	def OspfStopRouter(self, *args, **kwargs):
		"""Executes the ospfStopRouter operation on the server.

		Stop OSPF Router

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		ospfStopRouter()

		ospfStopRouter(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		ospfStopRouter(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('ospfStopRouter', payload=payload, response_object=None)

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
