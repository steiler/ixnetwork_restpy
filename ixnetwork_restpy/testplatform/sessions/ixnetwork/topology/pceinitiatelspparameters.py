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


class PceInitiateLSPParameters(Base):
	"""This tab configures the Initiated LSP Parameters.
	The PceInitiateLSPParameters class encapsulates a required pceInitiateLSPParameters resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'pceInitiateLSPParameters'

	def __init__(self, parent):
		super(PceInitiateLSPParameters, self).__init__(parent)

	@property
	def PceInitiateXROobject(self):
		"""An instance of the PceInitiateXROobject class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pceinitiatexroobject.PceInitiateXROobject)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pceinitiatexroobject import PceInitiateXROobject
		return PceInitiateXROobject(self)

	@property
	def PcepEroSubObjectsList(self):
		"""An instance of the PcepEroSubObjectsList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pceperosubobjectslist.PcepEroSubObjectsList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pceperosubobjectslist import PcepEroSubObjectsList
		return PcepEroSubObjectsList(self)

	@property
	def PcepMetricSubObjectsList(self):
		"""An instance of the PcepMetricSubObjectsList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepmetricsubobjectslist.PcepMetricSubObjectsList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepmetricsubobjectslist import PcepMetricSubObjectsList
		return PcepMetricSubObjectsList(self)

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
	def Bandwidth(self):
		"""Bandwidth (bits/sec)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bandwidth')

	@property
	def BindingType(self):
		"""Indicates the type of binding included in the TLV. Types are as follows: 20bit MPLS Label 32bit MPLS Label. Default value is 20bit MPLS Label.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bindingType')

	@property
	def Bos(self):
		"""This bit is set to True for the last entry in the label stack i.e., for the bottom of the stack, and False for all other label stack entries. This control will be editable only if Binding Type is MPLS Label 32bit.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bos')

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
	def DestEndPointIpv4(self):
		"""Dest IPv4 address of the path for which a path computation is Initiated. Will be greyed out if IP Version is IPv6.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('destEndPointIpv4')

	@property
	def DestEndPointIpv6(self):
		"""Dest IPv6 address of the path for which a path computation is Initiated. Will be greyed out if IP Version is IPv4.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('destEndPointIpv6')

	@property
	def EnableXro(self):
		"""Include XRO

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableXro')

	@property
	def ExcludeAny(self):
		"""This is a type of Resource Affinity Procedure that is used to validate a link. This control accepts a link only if the link carries all of the attributes in the set.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('excludeAny')

	@property
	def FailBit(self):
		"""Fail Bit

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('failBit')

	@property
	def HoldingPriority(self):
		"""The priority of the LSP with respect to holding resources. The value 0 is the highest priority. Holding Priority is used in deciding whether this session can be preempted by another session.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('holdingPriority')

	@property
	def IncludeAll(self):
		"""This is a type of Resource Affinity Procedure that is used to validate a link. This control excludes a link from consideration if the link carries any of the attributes in the set.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeAll')

	@property
	def IncludeAny(self):
		"""This is a type of Resource Affinity Procedure that is used to validate a link. This control accepts a link if the link carries any of the attributes in the set.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeAny')

	@property
	def IncludeAssociation(self):
		"""Indicates whether PPAG will be included in a PCInitiate message. All other attributes in sub-tab-PPAG would be editable only if this checkbox is enabled.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeAssociation')

	@property
	def IncludeBandwidth(self):
		"""Indicates whether Bandwidth will be included in a PCInitiate message. All other attributes in sub-tab-Bandwidth would be editable only if this checkbox is enabled.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeBandwidth')

	@property
	def IncludeEndPoints(self):
		"""Indicates whether END-POINTS object will be included in a PCInitiate message. All other attributes in sub-tab-End Points would be editable only if this checkbox is enabled

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeEndPoints')

	@property
	def IncludeEro(self):
		"""Specifies whether ERO is active or inactive. All subsequent attributes of the sub-tab-ERO would be editable only if this is enabled.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeEro')

	@property
	def IncludeLsp(self):
		"""Indicates whether LSP will be included in a PCInitiate message. All other attributes in sub-tab-LSP would be editable only if this checkbox is enabled.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeLsp')

	@property
	def IncludeLspa(self):
		"""Indicates whether LSPA will be included in a PCInitiate message. All other attributes in sub-tab-LSPA would be editable only if this checkbox is enabled.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeLspa')

	@property
	def IncludeMetric(self):
		"""Indicates whether the PCInitiate message will have the metric list that is configured. All subsequent attributes of the sub-tab-Metric would be editable only if this is enabled.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeMetric')

	@property
	def IncludeSrp(self):
		"""Indicates whether SRP object will be included in a PCInitiate message. All other attributes in sub-tab-SRP would be editable only if this checkbox is enabled.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeSrp')

	@property
	def IncludeSymbolicPathNameTlv(self):
		"""Indicates if Symbolic-Path-Name TLV is to be included in PCInitiate message.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeSymbolicPathNameTlv')

	@property
	def IncludeTEPathBindingTLV(self):
		"""Indicates if TE-PATH-BINDING TLV is to be included in PCInitiate message.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeTEPathBindingTLV')

	@property
	def IpVersion(self):
		"""Drop down to select the IP Version with 2 choices : IPv4 / IPv6

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipVersion')

	@property
	def LocalProtection(self):
		"""When set, this means that the path must include links protected with Fast Reroute

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('localProtection')

	@property
	def MplsLabel(self):
		"""This control will be editable if the Binding Type is set to either 20bit or 32bit MPLS-Label. This field will take the 20bit value of the MPLS-Label

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('mplsLabel')

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
		"""Value that indicates the number of ERO Sub Objects to be configured.

		Returns:
			number
		"""
		return self._get_attribute('numberOfEroSubObjects')
	@NumberOfEroSubObjects.setter
	def NumberOfEroSubObjects(self, value):
		self._set_attribute('numberOfEroSubObjects', value)

	@property
	def NumberOfMetricSubObject(self):
		"""Value that indicates the number of Metric Objects to be configured.

		Returns:
			number
		"""
		return self._get_attribute('numberOfMetricSubObject')
	@NumberOfMetricSubObject.setter
	def NumberOfMetricSubObject(self, value):
		self._set_attribute('numberOfMetricSubObject', value)

	@property
	def NumberOfXroSubObjects(self):
		"""Number of XRO Sub Objects

		Returns:
			number
		"""
		return self._get_attribute('numberOfXroSubObjects')
	@NumberOfXroSubObjects.setter
	def NumberOfXroSubObjects(self, value):
		self._set_attribute('numberOfXroSubObjects', value)

	@property
	def OverridePlspId(self):
		"""Indicates if PLSP-ID will be set by the state machine or user. If disabled user wont have the control and state machine will set it.

		Returns:
			bool
		"""
		return self._get_attribute('overridePlspId')
	@OverridePlspId.setter
	def OverridePlspId(self, value):
		self._set_attribute('overridePlspId', value)

	@property
	def OverrideSrpIdNumber(self):
		"""Indicates whether SRP ID Number is overridable.

		Returns:
			bool
		"""
		return self._get_attribute('overrideSrpIdNumber')
	@OverrideSrpIdNumber.setter
	def OverrideSrpIdNumber(self, value):
		self._set_attribute('overrideSrpIdNumber', value)

	@property
	def PathSetupType(self):
		"""Indicates which type of LSP will be requested in the PCInitiated Request.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('pathSetupType')

	@property
	def PlspId(self):
		"""An identifier for the LSP. A PCC creates a unique PLSP-ID for each LSP that is constant for the lifetime of a PCEP session. The PCC will advertise the same PLSP-ID on all PCEP sessions it maintains at a given time.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('plspId')

	@property
	def ProtectionLsp(self):
		"""Indicates whether Protection LSP Bit is On.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('protectionLsp')

	@property
	def SendEmptyTLV(self):
		"""If enabled all fields after Binding Type will be grayed out.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sendEmptyTLV')

	@property
	def SessionInfo(self):
		"""Logs additional information about the LSP state

		Returns:
			list(str[advertised|delegatedActive|delegatedDown|delegatedGoingUp|delegatedUp|init|none|notDelegatedActive|notDelegatedDown|notDelegatedGoingUp|notDelegatedUp|pcErrorReceived|removedByPCC|removedByPCE|returnDelegation])
		"""
		return self._get_attribute('sessionInfo')

	@property
	def SetupPriority(self):
		"""The priority of the LSP with respect to taking resources.The value 0 is the highest priority.The Setup Priority is used in deciding whether this session can preempt another session.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('setupPriority')

	@property
	def SrcEndPointIpv4(self):
		"""Source IPv4 address of the path for which a path computation is Initiated. Will be greyed out if IP Version is set to IPv6.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srcEndPointIpv4')

	@property
	def SrcEndPointIpv6(self):
		"""Source IPv6 address of the path for which a path computation is Initiated. Will be greyed out if IP version is set to IPv4.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srcEndPointIpv6')

	@property
	def SrpIdNumber(self):
		"""The SRP object is used to correlate between initiation requests sent by the PCE and the error reports and state reports sent by the PCC. This number is unique per PCEP session and is incremented per initiation.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srpIdNumber')

	@property
	def StandbyMode(self):
		"""Indicates whether Standby LSP Bit is On.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('standbyMode')

	@property
	def SymbolicPathName(self):
		"""Each LSP (path) must have a symbolic name that is unique in the PCC. It must remain constant throughout a path's lifetime, which may span across multiple consecutive PCEP sessions and/or PCC restarts.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('symbolicPathName')

	@property
	def Tc(self):
		"""This field is used to carry traffic class information. This control will be editable only if Binding Type is MPLS Label 32bit.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('tc')

	@property
	def Ttl(self):
		"""This field is used to encode a time-to-live value. This control will be editable only if Binding Type is MPLS Label 32bit.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ttl')

	def update(self, Name=None, NumberOfEroSubObjects=None, NumberOfMetricSubObject=None, NumberOfXroSubObjects=None, OverridePlspId=None, OverrideSrpIdNumber=None):
		"""Updates a child instance of pceInitiateLSPParameters on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfEroSubObjects (number): Value that indicates the number of ERO Sub Objects to be configured.
			NumberOfMetricSubObject (number): Value that indicates the number of Metric Objects to be configured.
			NumberOfXroSubObjects (number): Number of XRO Sub Objects
			OverridePlspId (bool): Indicates if PLSP-ID will be set by the state machine or user. If disabled user wont have the control and state machine will set it.
			OverrideSrpIdNumber (bool): Indicates whether SRP ID Number is overridable.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def get_device_ids(self, PortNames=None, Active=None, AssociationId=None, Bandwidth=None, BindingType=None, Bos=None, DestEndPointIpv4=None, DestEndPointIpv6=None, EnableXro=None, ExcludeAny=None, FailBit=None, HoldingPriority=None, IncludeAll=None, IncludeAny=None, IncludeAssociation=None, IncludeBandwidth=None, IncludeEndPoints=None, IncludeEro=None, IncludeLsp=None, IncludeLspa=None, IncludeMetric=None, IncludeSrp=None, IncludeSymbolicPathNameTlv=None, IncludeTEPathBindingTLV=None, IpVersion=None, LocalProtection=None, MplsLabel=None, PathSetupType=None, PlspId=None, ProtectionLsp=None, SendEmptyTLV=None, SetupPriority=None, SrcEndPointIpv4=None, SrcEndPointIpv6=None, SrpIdNumber=None, StandbyMode=None, SymbolicPathName=None, Tc=None, Ttl=None):
		"""Base class infrastructure that gets a list of pceInitiateLSPParameters device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			Active (str): optional regex of active
			AssociationId (str): optional regex of associationId
			Bandwidth (str): optional regex of bandwidth
			BindingType (str): optional regex of bindingType
			Bos (str): optional regex of bos
			DestEndPointIpv4 (str): optional regex of destEndPointIpv4
			DestEndPointIpv6 (str): optional regex of destEndPointIpv6
			EnableXro (str): optional regex of enableXro
			ExcludeAny (str): optional regex of excludeAny
			FailBit (str): optional regex of failBit
			HoldingPriority (str): optional regex of holdingPriority
			IncludeAll (str): optional regex of includeAll
			IncludeAny (str): optional regex of includeAny
			IncludeAssociation (str): optional regex of includeAssociation
			IncludeBandwidth (str): optional regex of includeBandwidth
			IncludeEndPoints (str): optional regex of includeEndPoints
			IncludeEro (str): optional regex of includeEro
			IncludeLsp (str): optional regex of includeLsp
			IncludeLspa (str): optional regex of includeLspa
			IncludeMetric (str): optional regex of includeMetric
			IncludeSrp (str): optional regex of includeSrp
			IncludeSymbolicPathNameTlv (str): optional regex of includeSymbolicPathNameTlv
			IncludeTEPathBindingTLV (str): optional regex of includeTEPathBindingTLV
			IpVersion (str): optional regex of ipVersion
			LocalProtection (str): optional regex of localProtection
			MplsLabel (str): optional regex of mplsLabel
			PathSetupType (str): optional regex of pathSetupType
			PlspId (str): optional regex of plspId
			ProtectionLsp (str): optional regex of protectionLsp
			SendEmptyTLV (str): optional regex of sendEmptyTLV
			SetupPriority (str): optional regex of setupPriority
			SrcEndPointIpv4 (str): optional regex of srcEndPointIpv4
			SrcEndPointIpv6 (str): optional regex of srcEndPointIpv6
			SrpIdNumber (str): optional regex of srpIdNumber
			StandbyMode (str): optional regex of standbyMode
			SymbolicPathName (str): optional regex of symbolicPathName
			Tc (str): optional regex of tc
			Ttl (str): optional regex of ttl

		Returns:
			list(int): A list of device ids that meets the regex criteria provided in the method parameters

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._get_ngpf_device_ids(locals())

	def ReturnDelegation(self, *args, **kwargs):
		"""Executes the returnDelegation operation on the server.

		Return Delegation of PCE-Initiated LSPs

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		returnDelegation()

		returnDelegation(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		returnDelegation(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		returnDelegation(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): Return Delegation.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('returnDelegation', payload=payload, response_object=None)

	def TakeControl(self, *args, **kwargs):
		"""Executes the takeControl operation on the server.

		Take Control of PCE-Initiated LSPs

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		takeControl()

		takeControl(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		takeControl(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		takeControl(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): Take Control.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('takeControl', payload=payload, response_object=None)
