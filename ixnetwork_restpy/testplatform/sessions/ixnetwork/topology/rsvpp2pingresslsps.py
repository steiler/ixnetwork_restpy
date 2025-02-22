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


class RsvpP2PIngressLsps(Base):
	"""RSVP-TE p2p Head ( Ingress ) LSPs
	The RsvpP2PIngressLsps class encapsulates a required rsvpP2PIngressLsps resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'rsvpP2PIngressLsps'

	def __init__(self, parent):
		super(RsvpP2PIngressLsps, self).__init__(parent)

	@property
	def BackupLspEROSubObjectsList(self):
		"""An instance of the BackupLspEROSubObjectsList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.backuplsperosubobjectslist.BackupLspEROSubObjectsList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.backuplsperosubobjectslist import BackupLspEROSubObjectsList
		return BackupLspEROSubObjectsList(self)

	@property
	def RsvpDetourSubObjectsList(self):
		"""An instance of the RsvpDetourSubObjectsList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpdetoursubobjectslist.RsvpDetourSubObjectsList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpdetoursubobjectslist import RsvpDetourSubObjectsList
		return RsvpDetourSubObjectsList(self)

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
	def RsvpIngressRROSubObjectsList(self):
		"""An instance of the RsvpIngressRROSubObjectsList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpingressrrosubobjectslist.RsvpIngressRROSubObjectsList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpingressrrosubobjectslist import RsvpIngressRROSubObjectsList
		return RsvpIngressRROSubObjectsList(self)

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
	def AssociationId(self):
		"""The Association ID of this LSP.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('associationId')

	@property
	def AutoGenerateSessionName(self):
		"""Auto Generate Session Name

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('autoGenerateSessionName')

	@property
	def AutorouteTraffic(self):
		"""Autoroute Traffic

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('autorouteTraffic')

	@property
	def BackupLspEnableEro(self):
		"""Enable ERO

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('backupLspEnableEro')

	@property
	def BackupLspId(self):
		"""Backup LSP Id Pool Start

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('backupLspId')

	@property
	def BackupLspMaximumPacketSize(self):
		"""Maximum Packet Size

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('backupLspMaximumPacketSize')

	@property
	def BackupLspMinimumPolicedUnit(self):
		"""Minimum Policed Unit

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('backupLspMinimumPolicedUnit')

	@property
	def BackupLspNumberOfEroSubObjects(self):
		"""Number Of ERO Sub-Objects

		Returns:
			number
		"""
		return self._get_attribute('backupLspNumberOfEroSubObjects')
	@BackupLspNumberOfEroSubObjects.setter
	def BackupLspNumberOfEroSubObjects(self, value):
		self._set_attribute('backupLspNumberOfEroSubObjects', value)

	@property
	def BackupLspPeakDataRate(self):
		"""Peak Data Rate

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('backupLspPeakDataRate')

	@property
	def BackupLspPrefixLength(self):
		"""Prefix Length

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('backupLspPrefixLength')

	@property
	def BackupLspPrependDutToEro(self):
		"""Prepend DUT to ERO

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('backupLspPrependDutToEro')

	@property
	def BackupLspSessionId(self):
		"""Backup LSP Session Id

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('backupLspSessionId')

	@property
	def BackupLspTokenBucketRate(self):
		"""Token Bucket Rate

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('backupLspTokenBucketRate')

	@property
	def BackupLspTokenBucketSize(self):
		"""Token Bucket Size

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('backupLspTokenBucketSize')

	@property
	def Bandwidth(self):
		"""DEPRECATED Bandwidth (bps)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bandwidth')

	@property
	def BandwidthProtectionDesired(self):
		"""Bandwidth Protection Desired

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bandwidthProtectionDesired')

	@property
	def ConfigureSyncLspObject(self):
		"""Include Objects

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('configureSyncLspObject')

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def DelayLspSwitchOver(self):
		"""Delay LSP switch over

		Returns:
			bool
		"""
		return self._get_attribute('delayLspSwitchOver')
	@DelayLspSwitchOver.setter
	def DelayLspSwitchOver(self, value):
		self._set_attribute('delayLspSwitchOver', value)

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def DoMBBOnApplyChanges(self):
		"""Do Make Before Break on Apply Changes

		Returns:
			bool
		"""
		return self._get_attribute('doMBBOnApplyChanges')
	@DoMBBOnApplyChanges.setter
	def DoMBBOnApplyChanges(self, value):
		self._set_attribute('doMBBOnApplyChanges', value)

	@property
	def EnableBfdMpls(self):
		"""If selected, BFD MPLS is enabled.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableBfdMpls')

	@property
	def EnableEro(self):
		"""Enable ERO

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableEro')

	@property
	def EnableFastReroute(self):
		"""Enable Fast Reroute

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableFastReroute')

	@property
	def EnableLspPing(self):
		"""If selected, LSP Ping is enabled for learned LSPs.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableLspPing')

	@property
	def EnableLspSelfPing(self):
		"""If enabled, Ingress LSP will use LSP Self Ping procedure to verify that forwarding state has been installed on all downstream nodes.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableLspSelfPing')

	@property
	def EnablePathReOptimization(self):
		"""Enable Path Re-Optimization

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enablePathReOptimization')

	@property
	def EnablePeriodicReEvaluationRequest(self):
		"""Enable Periodic Re-Evaluation Request

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enablePeriodicReEvaluationRequest')

	@property
	def EroSameAsPrimary(self):
		"""ERO Same As Primary

		Returns:
			bool
		"""
		return self._get_attribute('eroSameAsPrimary')
	@EroSameAsPrimary.setter
	def EroSameAsPrimary(self, value):
		self._set_attribute('eroSameAsPrimary', value)

	@property
	def ExcludeAny(self):
		"""Exclude Any

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('excludeAny')

	@property
	def FacilityBackupDesired(self):
		"""Facility Backup Desired

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('facilityBackupDesired')

	@property
	def FastRerouteBandwidth(self):
		"""Bandwidth (bps)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('fastRerouteBandwidth')

	@property
	def FastRerouteExcludeAny(self):
		"""Exclude Any

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('fastRerouteExcludeAny')

	@property
	def FastRerouteHoldingPriority(self):
		"""Holding Priority

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('fastRerouteHoldingPriority')

	@property
	def FastRerouteIncludeAll(self):
		"""Include All

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('fastRerouteIncludeAll')

	@property
	def FastRerouteIncludeAny(self):
		"""Include Any

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('fastRerouteIncludeAny')

	@property
	def FastRerouteSetupPriority(self):
		"""Setup Priority

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('fastRerouteSetupPriority')

	@property
	def HoldingPriority(self):
		"""Holding Priority

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('holdingPriority')

	@property
	def HopLimit(self):
		"""Hop Limit

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('hopLimit')

	@property
	def IncludeAll(self):
		"""Include All

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeAll')

	@property
	def IncludeAny(self):
		"""Include Any

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeAny')

	@property
	def IncludeAssociation(self):
		"""Indicates whether Association will be included in a RSVP Sync LSP. All other attributes in sub-tab-PPAG would be editable only if this checkbox is enabled.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeAssociation')

	@property
	def InitialDelegation(self):
		"""Initial Delegation

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('initialDelegation')

	@property
	def InsertIPv6ExplicitNull(self):
		"""Insert IPv6 explicit NULL

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('insertIPv6ExplicitNull')

	@property
	def IpDSCPofLspSelfPing(self):
		"""IP DSCP of LSP Self Ping. IP DSCP classifies the way an IP packet is routed in a network.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipDSCPofLspSelfPing')

	@property
	def IpTTLofLspSelfPing(self):
		"""IP TTL of LSP Self Ping. IP TTL limits the lifespan or lifetime of IP Packet in a network.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipTTLofLspSelfPing')

	@property
	def LabelRecordingDesired(self):
		"""Label Recording Desired

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('labelRecordingDesired')

	@property
	def LocalIp(self):
		"""Local IP

		Returns:
			list(str)
		"""
		return self._get_attribute('localIp')

	@property
	def LocalProtectionDesired(self):
		"""Local Protection Desired

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('localProtectionDesired')

	@property
	def LspCount(self):
		"""LSP#

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lspCount')

	@property
	def LspDelegationState(self):
		"""LSP Delegation State

		Returns:
			list(str[delegated|delegationConfirmed|delegationRejected|delegationReturned|delegationRevoked|nonDelegated|none])
		"""
		return self._get_attribute('lspDelegationState')

	@property
	def LspId(self):
		"""LSP Id

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lspId')

	@property
	def LspOperativeMode(self):
		"""The mode of LSP in which it is currently behaving.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lspOperativeMode')

	@property
	def LspSelfPingRetryCount(self):
		"""LSP Self Ping Retry Count. Maximum number of times LSP Self Ping Message will be Transmitted.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lspSelfPingRetryCount')

	@property
	def LspSelfPingRetryInterval(self):
		"""LSP Self Ping Retry Interval (ms).

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lspSelfPingRetryInterval')

	@property
	def LspSelfPingSessionId(self):
		"""LSP Self Ping Session Id.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lspSelfPingSessionId')

	@property
	def LspSelfPingStatus(self):
		"""Logs additional information about the LSP Self Ping Status(Success/Timed Out)

		Returns:
			list(str[none|success|timedOut])
		"""
		return self._get_attribute('lspSelfPingStatus')

	@property
	def LspSwitchOverDelayTime(self):
		"""LSP Switch Over Delay timer (sec)

		Returns:
			number
		"""
		return self._get_attribute('lspSwitchOverDelayTime')
	@LspSwitchOverDelayTime.setter
	def LspSwitchOverDelayTime(self, value):
		self._set_attribute('lspSwitchOverDelayTime', value)

	@property
	def MaximumPacketSize(self):
		"""Maximum Packet Size (in Bytes)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('maximumPacketSize')

	@property
	def MinimumPolicedUnit(self):
		"""Minimum Policed Unit (in Bytes)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('minimumPolicedUnit')

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
	def NodeProtectionDesired(self):
		"""Node Protection Desired

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('nodeProtectionDesired')

	@property
	def NumberOfDetourSubObjects(self):
		"""Number Of Detour Sub-Objects

		Returns:
			number
		"""
		return self._get_attribute('numberOfDetourSubObjects')
	@NumberOfDetourSubObjects.setter
	def NumberOfDetourSubObjects(self, value):
		self._set_attribute('numberOfDetourSubObjects', value)

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
	def NumberOfRroSubObjects(self):
		"""Number Of RRO Sub-Objects

		Returns:
			number
		"""
		return self._get_attribute('numberOfRroSubObjects')
	@NumberOfRroSubObjects.setter
	def NumberOfRroSubObjects(self, value):
		self._set_attribute('numberOfRroSubObjects', value)

	@property
	def OneToOneBackupDesired(self):
		"""One To One Backup Desired

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('oneToOneBackupDesired')

	@property
	def PccIp(self):
		"""PCC IP

		Returns:
			list(str)
		"""
		return self._get_attribute('pccIp')

	@property
	def PeakDataRate(self):
		"""Peak Data Rate (in Bytes per seconds)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('peakDataRate')

	@property
	def PpagTLVType(self):
		"""PPAG TLV Type

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ppagTLVType')

	@property
	def PrefixLength(self):
		"""Prefix Length

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('prefixLength')

	@property
	def PrependDutToEro(self):
		"""Prepend DUT to ERO

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('prependDutToEro')

	@property
	def ProtectionLsp(self):
		"""Indicates whether Protection LSP Bit is On.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('protectionLsp')

	@property
	def ReDelegationTimerStatus(self):
		"""Re-Delegation Timer Status

		Returns:
			list(str[expired|none|notStarted|running|stopped])
		"""
		return self._get_attribute('reDelegationTimerStatus')

	@property
	def ReEvaluationRequestInterval(self):
		"""Re-Evaluation Request Interval

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('reEvaluationRequestInterval')

	@property
	def RedelegationTimeoutInterval(self):
		"""The period of time a PCC waits for, when a PCEP session is terminated, before revoking LSP delegation to a PCE and attempting to redelegate LSPs associated with the terminated PCEP session to PCE.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('redelegationTimeoutInterval')

	@property
	def RefreshInterval(self):
		"""Refresh Interval (ms)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('refreshInterval')

	@property
	def RemoteIp(self):
		"""Remote IP Address

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('remoteIp')

	@property
	def ResourceAffinities(self):
		"""Resource Affinities

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('resourceAffinities')

	@property
	def SeStyleDesired(self):
		"""SE Style Desired

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('seStyleDesired')

	@property
	def SendDetour(self):
		"""Send Detour

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sendDetour')

	@property
	def SendRro(self):
		"""Send RRO

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sendRro')

	@property
	def SessionInformation(self):
		"""Logs additional information about the RSVP session state

		Returns:
			list(str[lastErrLSPAdmissionControlFailure|lastErrLSPBadAdSpecValue|lastErrLSPBadExplicitRoute|lastErrLSPBadFlowspecValue|lastErrLSPBadInitialSubobject|lastErrLSPBadLooseNode|lastErrLSPBadStrictNode|lastErrLSPBadTSpecValue|lastErrLSPDelayBoundNotMet|lastErrLSPMPLSAllocationFailure|lastErrLSPMTUTooBig|lastErrLSPNonRSVPRouter|lastErrLSPNoRouteAvailable|lastErrLSPPathErr|lastErrLSPPathTearSent|lastErrLSPRequestedBandwidthUnavailable|lastErrLSPReservationTearReceived|lastErrLSPReservationTearSent|lastErrLSPReservationTimeout|lastErrLSPRoutingLoops|lastErrLSPRoutingProblem|lastErrLSPRSVPSystemError|lastErrLSPServiceConflict|lastErrLSPServiceUnsupported|lastErrLSPTrafficControlError|lastErrLSPTrafficControlSystemError|lastErrLSPTrafficOrganizationError|lastErrLSPTrafficServiceError|lastErrLSPUnknownObjectClass|lastErrLSPUnknownObjectCType|lastErrLSPUnsupportedL3PID|lSPAdmissionControlFailure|lSPBadAdSpecValue|lSPBadExplicitRoute|lSPBadFlowspecValue|lSPBadInitialSubobject|lSPBadLooseNode|lSPBadStrictNode|lSPBadTSpecValue|lSPDelayBoundNotMet|lSPMPLSAllocationFailure|lSPMTUTooBig|lSPNonRSVPRouter|lSPNoRouteAvailable|lSPPathErr|lSPPathTearSent|lSPRequestedBandwidthUnavailable|lSPReservationNotReceived|lSPReservationTearReceived|lSPReservationTearSent|lSPReservationTimeout|lSPRoutingLoops|lSPRoutingProblem|lSPRSVPSystemError|lSPServiceConflict|lSPServiceUnsupported|lSPTrafficControlError|lSPTrafficControlSystemError|lSPTrafficOrganizationError|lSPTrafficServiceError|lSPUnknownObjectClass|lSPUnknownObjectCType|lSPUnsupportedL3PID|mbbCompleted|mbbTriggered|none|noPathReceived|pCRepReceived|pCReqSent])
		"""
		return self._get_attribute('sessionInformation')

	@property
	def SessionName(self):
		"""Session Name

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sessionName')

	@property
	def SetupPriority(self):
		"""Setup Priority

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('setupPriority')

	@property
	def SourceIp(self):
		"""Source IP

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sourceIp')

	@property
	def SourceIpv6(self):
		"""Source IPv6

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sourceIpv6')

	@property
	def StandbyMode(self):
		"""Indicates whether Standby LSP Bit is On.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('standbyMode')

	@property
	def State(self):
		"""State

		Returns:
			list(str[down|none|notStarted|up])
		"""
		return self._get_attribute('state')

	@property
	def TSpecSameAsPrimary(self):
		"""TSpec Same As Primary

		Returns:
			bool
		"""
		return self._get_attribute('tSpecSameAsPrimary')
	@TSpecSameAsPrimary.setter
	def TSpecSameAsPrimary(self, value):
		self._set_attribute('tSpecSameAsPrimary', value)

	@property
	def TimeoutMultiplier(self):
		"""Timeout Multiplier

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('timeoutMultiplier')

	@property
	def TokenBucketRate(self):
		"""Token Bucket Rate (in Bytes per seconds)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('tokenBucketRate')

	@property
	def TokenBucketSize(self):
		"""Token Bucket Size (in Bytes)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('tokenBucketSize')

	@property
	def TunnelId(self):
		"""Tunnel ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('tunnelId')

	@property
	def UsingHeadendIp(self):
		"""Using Headend IP

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('usingHeadendIp')

	def update(self, BackupLspNumberOfEroSubObjects=None, DelayLspSwitchOver=None, DoMBBOnApplyChanges=None, EroSameAsPrimary=None, LspSwitchOverDelayTime=None, Name=None, NumberOfDetourSubObjects=None, NumberOfEroSubObjects=None, NumberOfRroSubObjects=None, TSpecSameAsPrimary=None):
		"""Updates a child instance of rsvpP2PIngressLsps on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			BackupLspNumberOfEroSubObjects (number): Number Of ERO Sub-Objects
			DelayLspSwitchOver (bool): Delay LSP switch over
			DoMBBOnApplyChanges (bool): Do Make Before Break on Apply Changes
			EroSameAsPrimary (bool): ERO Same As Primary
			LspSwitchOverDelayTime (number): LSP Switch Over Delay timer (sec)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfDetourSubObjects (number): Number Of Detour Sub-Objects
			NumberOfEroSubObjects (number): Number Of ERO Sub-Objects
			NumberOfRroSubObjects (number): Number Of RRO Sub-Objects
			TSpecSameAsPrimary (bool): TSpec Same As Primary

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def get_device_ids(self, PortNames=None, Active=None, AssociationId=None, AutoGenerateSessionName=None, AutorouteTraffic=None, BackupLspEnableEro=None, BackupLspId=None, BackupLspMaximumPacketSize=None, BackupLspMinimumPolicedUnit=None, BackupLspPeakDataRate=None, BackupLspPrefixLength=None, BackupLspPrependDutToEro=None, BackupLspSessionId=None, BackupLspTokenBucketRate=None, BackupLspTokenBucketSize=None, Bandwidth=None, BandwidthProtectionDesired=None, ConfigureSyncLspObject=None, EnableBfdMpls=None, EnableEro=None, EnableFastReroute=None, EnableLspPing=None, EnableLspSelfPing=None, EnablePathReOptimization=None, EnablePeriodicReEvaluationRequest=None, ExcludeAny=None, FacilityBackupDesired=None, FastRerouteBandwidth=None, FastRerouteExcludeAny=None, FastRerouteHoldingPriority=None, FastRerouteIncludeAll=None, FastRerouteIncludeAny=None, FastRerouteSetupPriority=None, HoldingPriority=None, HopLimit=None, IncludeAll=None, IncludeAny=None, IncludeAssociation=None, InitialDelegation=None, InsertIPv6ExplicitNull=None, IpDSCPofLspSelfPing=None, IpTTLofLspSelfPing=None, LabelRecordingDesired=None, LocalProtectionDesired=None, LspCount=None, LspId=None, LspOperativeMode=None, LspSelfPingRetryCount=None, LspSelfPingRetryInterval=None, LspSelfPingSessionId=None, MaximumPacketSize=None, MinimumPolicedUnit=None, NodeProtectionDesired=None, OneToOneBackupDesired=None, PeakDataRate=None, PpagTLVType=None, PrefixLength=None, PrependDutToEro=None, ProtectionLsp=None, ReEvaluationRequestInterval=None, RedelegationTimeoutInterval=None, RefreshInterval=None, RemoteIp=None, ResourceAffinities=None, SeStyleDesired=None, SendDetour=None, SendRro=None, SessionName=None, SetupPriority=None, SourceIp=None, SourceIpv6=None, StandbyMode=None, TimeoutMultiplier=None, TokenBucketRate=None, TokenBucketSize=None, TunnelId=None, UsingHeadendIp=None):
		"""Base class infrastructure that gets a list of rsvpP2PIngressLsps device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			Active (str): optional regex of active
			AssociationId (str): optional regex of associationId
			AutoGenerateSessionName (str): optional regex of autoGenerateSessionName
			AutorouteTraffic (str): optional regex of autorouteTraffic
			BackupLspEnableEro (str): optional regex of backupLspEnableEro
			BackupLspId (str): optional regex of backupLspId
			BackupLspMaximumPacketSize (str): optional regex of backupLspMaximumPacketSize
			BackupLspMinimumPolicedUnit (str): optional regex of backupLspMinimumPolicedUnit
			BackupLspPeakDataRate (str): optional regex of backupLspPeakDataRate
			BackupLspPrefixLength (str): optional regex of backupLspPrefixLength
			BackupLspPrependDutToEro (str): optional regex of backupLspPrependDutToEro
			BackupLspSessionId (str): optional regex of backupLspSessionId
			BackupLspTokenBucketRate (str): optional regex of backupLspTokenBucketRate
			BackupLspTokenBucketSize (str): optional regex of backupLspTokenBucketSize
			Bandwidth (str): optional regex of bandwidth
			BandwidthProtectionDesired (str): optional regex of bandwidthProtectionDesired
			ConfigureSyncLspObject (str): optional regex of configureSyncLspObject
			EnableBfdMpls (str): optional regex of enableBfdMpls
			EnableEro (str): optional regex of enableEro
			EnableFastReroute (str): optional regex of enableFastReroute
			EnableLspPing (str): optional regex of enableLspPing
			EnableLspSelfPing (str): optional regex of enableLspSelfPing
			EnablePathReOptimization (str): optional regex of enablePathReOptimization
			EnablePeriodicReEvaluationRequest (str): optional regex of enablePeriodicReEvaluationRequest
			ExcludeAny (str): optional regex of excludeAny
			FacilityBackupDesired (str): optional regex of facilityBackupDesired
			FastRerouteBandwidth (str): optional regex of fastRerouteBandwidth
			FastRerouteExcludeAny (str): optional regex of fastRerouteExcludeAny
			FastRerouteHoldingPriority (str): optional regex of fastRerouteHoldingPriority
			FastRerouteIncludeAll (str): optional regex of fastRerouteIncludeAll
			FastRerouteIncludeAny (str): optional regex of fastRerouteIncludeAny
			FastRerouteSetupPriority (str): optional regex of fastRerouteSetupPriority
			HoldingPriority (str): optional regex of holdingPriority
			HopLimit (str): optional regex of hopLimit
			IncludeAll (str): optional regex of includeAll
			IncludeAny (str): optional regex of includeAny
			IncludeAssociation (str): optional regex of includeAssociation
			InitialDelegation (str): optional regex of initialDelegation
			InsertIPv6ExplicitNull (str): optional regex of insertIPv6ExplicitNull
			IpDSCPofLspSelfPing (str): optional regex of ipDSCPofLspSelfPing
			IpTTLofLspSelfPing (str): optional regex of ipTTLofLspSelfPing
			LabelRecordingDesired (str): optional regex of labelRecordingDesired
			LocalProtectionDesired (str): optional regex of localProtectionDesired
			LspCount (str): optional regex of lspCount
			LspId (str): optional regex of lspId
			LspOperativeMode (str): optional regex of lspOperativeMode
			LspSelfPingRetryCount (str): optional regex of lspSelfPingRetryCount
			LspSelfPingRetryInterval (str): optional regex of lspSelfPingRetryInterval
			LspSelfPingSessionId (str): optional regex of lspSelfPingSessionId
			MaximumPacketSize (str): optional regex of maximumPacketSize
			MinimumPolicedUnit (str): optional regex of minimumPolicedUnit
			NodeProtectionDesired (str): optional regex of nodeProtectionDesired
			OneToOneBackupDesired (str): optional regex of oneToOneBackupDesired
			PeakDataRate (str): optional regex of peakDataRate
			PpagTLVType (str): optional regex of ppagTLVType
			PrefixLength (str): optional regex of prefixLength
			PrependDutToEro (str): optional regex of prependDutToEro
			ProtectionLsp (str): optional regex of protectionLsp
			ReEvaluationRequestInterval (str): optional regex of reEvaluationRequestInterval
			RedelegationTimeoutInterval (str): optional regex of redelegationTimeoutInterval
			RefreshInterval (str): optional regex of refreshInterval
			RemoteIp (str): optional regex of remoteIp
			ResourceAffinities (str): optional regex of resourceAffinities
			SeStyleDesired (str): optional regex of seStyleDesired
			SendDetour (str): optional regex of sendDetour
			SendRro (str): optional regex of sendRro
			SessionName (str): optional regex of sessionName
			SetupPriority (str): optional regex of setupPriority
			SourceIp (str): optional regex of sourceIp
			SourceIpv6 (str): optional regex of sourceIpv6
			StandbyMode (str): optional regex of standbyMode
			TimeoutMultiplier (str): optional regex of timeoutMultiplier
			TokenBucketRate (str): optional regex of tokenBucketRate
			TokenBucketSize (str): optional regex of tokenBucketSize
			TunnelId (str): optional regex of tunnelId
			UsingHeadendIp (str): optional regex of usingHeadendIp

		Returns:
			list(int): A list of device ids that meets the regex criteria provided in the method parameters

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._get_ngpf_device_ids(locals())

	def InitiatePathReoptimization(self, *args, **kwargs):
		"""Executes the initiatePathReoptimization operation on the server.

		Send Path with re-evaluation request bit of SESSION-ATTRIBUTE object set, for selected Head Ranges

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		initiatePathReoptimization()

		initiatePathReoptimization(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		initiatePathReoptimization(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		initiatePathReoptimization(Arg2:list)list
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
		return self._execute('initiatePathReoptimization', payload=payload, response_object=None)

	def MakeBeforeBreak(self, *args, **kwargs):
		"""Executes the makeBeforeBreak operation on the server.

		Initiate Make Before Break for selected Head Ranges

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		makeBeforeBreak()

		makeBeforeBreak(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		makeBeforeBreak(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		makeBeforeBreak(Arg2:list)list
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
		return self._execute('makeBeforeBreak', payload=payload, response_object=None)

	def PcepDelegate(self, *args, **kwargs):
		"""Executes the pcepDelegate operation on the server.

		Delegate the non-delegated LSPs among the selected RSVP-TE LSPs to PCE.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		pcepDelegate()

		pcepDelegate(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		pcepDelegate(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		pcepDelegate(Arg2:list)list
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
		return self._execute('pcepDelegate', payload=payload, response_object=None)

	def PcepRevokeDelegation(self, *args, **kwargs):
		"""Executes the pcepRevokeDelegation operation on the server.

		Revoke Delegation from PCE for delegated LSPs among the selected LSPs.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		pcepRevokeDelegation()

		pcepRevokeDelegation(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		pcepRevokeDelegation(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		pcepRevokeDelegation(Arg2:list)list
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
		return self._execute('pcepRevokeDelegation', payload=payload, response_object=None)

	def Start(self, *args, **kwargs):
		"""Executes the start operation on the server.

		Activate/Enable Tunnel selected Head Ranges

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		start()

		start(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		start(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		start(Arg2:list)list
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
		return self._execute('start', payload=payload, response_object=None)

	def Stop(self, *args, **kwargs):
		"""Executes the stop operation on the server.

		Deactivate/Disable selected Tunnel Head Ranges

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		stop()

		stop(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		stop(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		stop(Arg2:list)list
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
		return self._execute('stop', payload=payload, response_object=None)
