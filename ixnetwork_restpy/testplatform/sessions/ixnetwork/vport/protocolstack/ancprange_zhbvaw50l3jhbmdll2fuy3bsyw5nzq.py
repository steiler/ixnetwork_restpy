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


class AncpRange(Base):
	"""ANCP Range
	The AncpRange class encapsulates a list of ancpRange resources that is be managed by the user.
	A list of resources can be retrieved from the server using the AncpRange.find() method.
	The list can be managed by the user by using the AncpRange.add() and AncpRange.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'ancpRange'

	def __init__(self, parent):
		super(AncpRange, self).__init__(parent)

	@property
	def AncpAtmRange(self):
		"""An instance of the AncpAtmRange class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancpatmrange_2fuy3bsyw5nzs9hbmnwqxrtumfuz2u.AncpAtmRange)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancpatmrange_2fuy3bsyw5nzs9hbmnwqxrtumfuz2u import AncpAtmRange
		return AncpAtmRange(self)._select()

	@property
	def AncpIpRange(self):
		"""An instance of the AncpIpRange class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancpiprange_l2fuy3bsyw5nzs9hbmnwsxbsyw5nzq.AncpIpRange)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancpiprange_l2fuy3bsyw5nzs9hbmnwsxbsyw5nzq import AncpIpRange
		return AncpIpRange(self)._select()

	@property
	def AncpMacRange(self):
		"""An instance of the AncpMacRange class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancpmacrange_2fuy3bsyw5nzs9hbmnwtwfjumfuz2u.AncpMacRange)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancpmacrange_2fuy3bsyw5nzs9hbmnwtwfjumfuz2u import AncpMacRange
		return AncpMacRange(self)._select()

	@property
	def AncpPvcRange(self):
		"""An instance of the AncpPvcRange class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancppvcrange_2fuy3bsyw5nzs9hbmnwuhzjumfuz2u.AncpPvcRange)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancppvcrange_2fuy3bsyw5nzs9hbmnwuhzjumfuz2u import AncpPvcRange
		return AncpPvcRange(self)._select()

	@property
	def AncpVlanRange(self):
		"""An instance of the AncpVlanRange class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancpvlanrange_fuy3bsyw5nzs9hbmnwvmxhbljhbmdl.AncpVlanRange)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancpvlanrange_fuy3bsyw5nzs9hbmnwvmxhbljhbmdl import AncpVlanRange
		return AncpVlanRange(self)._select()

	@property
	def DslProfileAllocationTable(self):
		"""An instance of the DslProfileAllocationTable class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dslprofileallocationtable_xqcm9mawxlqwxsb2nhdglvblrhymxl.DslProfileAllocationTable)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dslprofileallocationtable_xqcm9mawxlqwxsb2nhdglvblrhymxl import DslProfileAllocationTable
		return DslProfileAllocationTable(self)

	@property
	def DslResyncProfileAllocationTable(self):
		"""An instance of the DslResyncProfileAllocationTable class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dslresyncprofileallocationtable_nqcm9mawxlqwxsb2nhdglvblrhymxl.DslResyncProfileAllocationTable)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dslresyncprofileallocationtable_nqcm9mawxlqwxsb2nhdglvblrhymxl import DslResyncProfileAllocationTable
		return DslResyncProfileAllocationTable(self)

	@property
	def AccessAggregationCbTlv(self):
		"""Enable Access Aggregation Circuit ID Binary TLV

		Returns:
			str
		"""
		return self._get_attribute('accessAggregationCbTlv')
	@AccessAggregationCbTlv.setter
	def AccessAggregationCbTlv(self, value):
		self._set_attribute('accessAggregationCbTlv', value)

	@property
	def AtmVci(self):
		"""Custom VPI.

		Returns:
			number
		"""
		return self._get_attribute('atmVci')
	@AtmVci.setter
	def AtmVci(self, value):
		self._set_attribute('atmVci', value)

	@property
	def AtmVpi(self):
		"""Custom VCI.

		Returns:
			number
		"""
		return self._get_attribute('atmVpi')
	@AtmVpi.setter
	def AtmVpi(self, value):
		self._set_attribute('atmVpi', value)

	@property
	def CircuitId(self):
		"""Circuit ID.

		Returns:
			str
		"""
		return self._get_attribute('circuitId')
	@CircuitId.setter
	def CircuitId(self, value):
		self._set_attribute('circuitId', value)

	@property
	def DistributionAlgorithmPercent(self):
		"""DSL_Subscriber-per-AN distribution scattering model.

		Returns:
			number
		"""
		return self._get_attribute('distributionAlgorithmPercent')
	@DistributionAlgorithmPercent.setter
	def DistributionAlgorithmPercent(self, value):
		self._set_attribute('distributionAlgorithmPercent', value)

	@property
	def EnableAccessAggregation(self):
		"""Enable Access Aggregation Circuit Binary.

		Returns:
			bool
		"""
		return self._get_attribute('enableAccessAggregation')
	@EnableAccessAggregation.setter
	def EnableAccessAggregation(self, value):
		self._set_attribute('enableAccessAggregation', value)

	@property
	def Enabled(self):
		"""Disabled ranges won't be configured nor validated.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def InnerVlanId(self):
		"""Custom inner VLAN ID.

		Returns:
			number
		"""
		return self._get_attribute('innerVlanId')
	@InnerVlanId.setter
	def InnerVlanId(self, value):
		self._set_attribute('innerVlanId', value)

	@property
	def Name(self):
		"""Name of range

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	@property
	def NasAncpServicePort(self):
		"""NAS Ancp Service Port.

		Returns:
			number
		"""
		return self._get_attribute('nasAncpServicePort')
	@NasAncpServicePort.setter
	def NasAncpServicePort(self, value):
		self._set_attribute('nasAncpServicePort', value)

	@property
	def NasIPAddressIncr(self):
		"""DEPRECATED NAS IP Increment.

		Returns:
			str
		"""
		return self._get_attribute('nasIPAddressIncr')
	@NasIPAddressIncr.setter
	def NasIPAddressIncr(self, value):
		self._set_attribute('nasIPAddressIncr', value)

	@property
	def NasIpAddress(self):
		"""NAS IP.

		Returns:
			str
		"""
		return self._get_attribute('nasIpAddress')
	@NasIpAddress.setter
	def NasIpAddress(self, value):
		self._set_attribute('nasIpAddress', value)

	@property
	def NasIpAddressIncr(self):
		"""NAS IP Increment.

		Returns:
			str
		"""
		return self._get_attribute('nasIpAddressIncr')
	@NasIpAddressIncr.setter
	def NasIpAddressIncr(self, value):
		self._set_attribute('nasIpAddressIncr', value)

	@property
	def NasKeepAliveRetries(self):
		"""NAS Keep Alive Retries.

		Returns:
			number
		"""
		return self._get_attribute('nasKeepAliveRetries')
	@NasKeepAliveRetries.setter
	def NasKeepAliveRetries(self, value):
		self._set_attribute('nasKeepAliveRetries', value)

	@property
	def NasKeepAliveTimeout(self):
		"""NAS Keep Alive Timeout, in seconds

		Returns:
			number
		"""
		return self._get_attribute('nasKeepAliveTimeout')
	@NasKeepAliveTimeout.setter
	def NasKeepAliveTimeout(self, value):
		self._set_attribute('nasKeepAliveTimeout', value)

	@property
	def ObjectId(self):
		"""Unique identifier for this object

		Returns:
			str
		"""
		return self._get_attribute('objectId')

	@property
	def OuterVlanId(self):
		"""Custom outer VLAN ID.

		Returns:
			number
		"""
		return self._get_attribute('outerVlanId')
	@OuterVlanId.setter
	def OuterVlanId(self, value):
		self._set_attribute('outerVlanId', value)

	@property
	def UseDslInnerVlan(self):
		"""Use DSL subscriber inner VLAN.

		Returns:
			bool
		"""
		return self._get_attribute('useDslInnerVlan')
	@UseDslInnerVlan.setter
	def UseDslInnerVlan(self, value):
		self._set_attribute('useDslInnerVlan', value)

	@property
	def UseDslOuterVlan(self):
		"""Use actual DSL outer VLAN.

		Returns:
			bool
		"""
		return self._get_attribute('useDslOuterVlan')
	@UseDslOuterVlan.setter
	def UseDslOuterVlan(self, value):
		self._set_attribute('useDslOuterVlan', value)

	def update(self, AccessAggregationCbTlv=None, AtmVci=None, AtmVpi=None, CircuitId=None, DistributionAlgorithmPercent=None, EnableAccessAggregation=None, Enabled=None, InnerVlanId=None, Name=None, NasAncpServicePort=None, NasIPAddressIncr=None, NasIpAddress=None, NasIpAddressIncr=None, NasKeepAliveRetries=None, NasKeepAliveTimeout=None, OuterVlanId=None, UseDslInnerVlan=None, UseDslOuterVlan=None):
		"""Updates a child instance of ancpRange on the server.

		Args:
			AccessAggregationCbTlv (str): Enable Access Aggregation Circuit ID Binary TLV
			AtmVci (number): Custom VPI.
			AtmVpi (number): Custom VCI.
			CircuitId (str): Circuit ID.
			DistributionAlgorithmPercent (number): DSL_Subscriber-per-AN distribution scattering model.
			EnableAccessAggregation (bool): Enable Access Aggregation Circuit Binary.
			Enabled (bool): Disabled ranges won't be configured nor validated.
			InnerVlanId (number): Custom inner VLAN ID.
			Name (str): Name of range
			NasAncpServicePort (number): NAS Ancp Service Port.
			NasIPAddressIncr (str): NAS IP Increment.
			NasIpAddress (str): NAS IP.
			NasIpAddressIncr (str): NAS IP Increment.
			NasKeepAliveRetries (number): NAS Keep Alive Retries.
			NasKeepAliveTimeout (number): NAS Keep Alive Timeout, in seconds
			OuterVlanId (number): Custom outer VLAN ID.
			UseDslInnerVlan (bool): Use DSL subscriber inner VLAN.
			UseDslOuterVlan (bool): Use actual DSL outer VLAN.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, AccessAggregationCbTlv=None, AtmVci=None, AtmVpi=None, CircuitId=None, DistributionAlgorithmPercent=None, EnableAccessAggregation=None, Enabled=None, InnerVlanId=None, Name=None, NasAncpServicePort=None, NasIPAddressIncr=None, NasIpAddress=None, NasIpAddressIncr=None, NasKeepAliveRetries=None, NasKeepAliveTimeout=None, OuterVlanId=None, UseDslInnerVlan=None, UseDslOuterVlan=None):
		"""Adds a new ancpRange node on the server and retrieves it in this instance.

		Args:
			AccessAggregationCbTlv (str): Enable Access Aggregation Circuit ID Binary TLV
			AtmVci (number): Custom VPI.
			AtmVpi (number): Custom VCI.
			CircuitId (str): Circuit ID.
			DistributionAlgorithmPercent (number): DSL_Subscriber-per-AN distribution scattering model.
			EnableAccessAggregation (bool): Enable Access Aggregation Circuit Binary.
			Enabled (bool): Disabled ranges won't be configured nor validated.
			InnerVlanId (number): Custom inner VLAN ID.
			Name (str): Name of range
			NasAncpServicePort (number): NAS Ancp Service Port.
			NasIPAddressIncr (str): NAS IP Increment.
			NasIpAddress (str): NAS IP.
			NasIpAddressIncr (str): NAS IP Increment.
			NasKeepAliveRetries (number): NAS Keep Alive Retries.
			NasKeepAliveTimeout (number): NAS Keep Alive Timeout, in seconds
			OuterVlanId (number): Custom outer VLAN ID.
			UseDslInnerVlan (bool): Use DSL subscriber inner VLAN.
			UseDslOuterVlan (bool): Use actual DSL outer VLAN.

		Returns:
			self: This instance with all currently retrieved ancpRange data using find and the newly added ancpRange data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the ancpRange data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, AccessAggregationCbTlv=None, AtmVci=None, AtmVpi=None, CircuitId=None, DistributionAlgorithmPercent=None, EnableAccessAggregation=None, Enabled=None, InnerVlanId=None, Name=None, NasAncpServicePort=None, NasIPAddressIncr=None, NasIpAddress=None, NasIpAddressIncr=None, NasKeepAliveRetries=None, NasKeepAliveTimeout=None, ObjectId=None, OuterVlanId=None, UseDslInnerVlan=None, UseDslOuterVlan=None):
		"""Finds and retrieves ancpRange data from the server.

		All named parameters support regex and can be used to selectively retrieve ancpRange data from the server.
		By default the find method takes no parameters and will retrieve all ancpRange data from the server.

		Args:
			AccessAggregationCbTlv (str): Enable Access Aggregation Circuit ID Binary TLV
			AtmVci (number): Custom VPI.
			AtmVpi (number): Custom VCI.
			CircuitId (str): Circuit ID.
			DistributionAlgorithmPercent (number): DSL_Subscriber-per-AN distribution scattering model.
			EnableAccessAggregation (bool): Enable Access Aggregation Circuit Binary.
			Enabled (bool): Disabled ranges won't be configured nor validated.
			InnerVlanId (number): Custom inner VLAN ID.
			Name (str): Name of range
			NasAncpServicePort (number): NAS Ancp Service Port.
			NasIPAddressIncr (str): NAS IP Increment.
			NasIpAddress (str): NAS IP.
			NasIpAddressIncr (str): NAS IP Increment.
			NasKeepAliveRetries (number): NAS Keep Alive Retries.
			NasKeepAliveTimeout (number): NAS Keep Alive Timeout, in seconds
			ObjectId (str): Unique identifier for this object
			OuterVlanId (number): Custom outer VLAN ID.
			UseDslInnerVlan (bool): Use DSL subscriber inner VLAN.
			UseDslOuterVlan (bool): Use actual DSL outer VLAN.

		Returns:
			self: This instance with matching ancpRange data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of ancpRange data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the ancpRange data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def AncpBringUpDslSubscribers(self, *args, **kwargs):
		"""Executes the ancpBringUpDslSubscribers operation on the server.

		Bring up DSL subscribers

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		ancpBringUpDslSubscribers()

		ancpBringUpDslSubscribers(Arg2:enum)
			Args:
				args[0] is Arg2 (str(async|sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/ancp,/vport/protocolStack/atm/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/ancp,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/ancp,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ipEndpoint/ancp,/vport/protocolStack/atm/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/ancp,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/atm/pppoxEndpoint/ancp,/vport/protocolStack/atm/pppoxEndpoint/range/ancpRange,/vport/protocolStack/ethernet/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/ancp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/ancp,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ipEndpoint/ancp,/vport/protocolStack/ethernet/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/ancp,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppoxEndpoint/ancp,/vport/protocolStack/ethernet/pppoxEndpoint/range/ancpRange]

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('ancpBringUpDslSubscribers', payload=payload, response_object=None)

	def AncpStart(self, *args, **kwargs):
		"""Executes the ancpStart operation on the server.

		Negotiate ANCP and PPPoE sessions for selected ranges

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		ancpStart()

		ancpStart(Arg2:enum)
			Args:
				args[0] is Arg2 (str(async|sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/ancp,/vport/protocolStack/atm/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/ancp,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/ancp,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ipEndpoint/ancp,/vport/protocolStack/atm/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/ancp,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/atm/pppoxEndpoint/ancp,/vport/protocolStack/atm/pppoxEndpoint/range/ancpRange,/vport/protocolStack/ethernet/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/ancp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/ancp,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ipEndpoint/ancp,/vport/protocolStack/ethernet/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/ancp,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppoxEndpoint/ancp,/vport/protocolStack/ethernet/pppoxEndpoint/range/ancpRange]

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('ancpStart', payload=payload, response_object=None)

	def AncpStartAdjacency(self, *args, **kwargs):
		"""Executes the ancpStartAdjacency operation on the server.

		Start ANCP adjacency

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		ancpStartAdjacency()

		ancpStartAdjacency(Arg2:enum)
			Args:
				args[0] is Arg2 (str(async|sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/ancp,/vport/protocolStack/atm/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/ancp,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/ancp,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ipEndpoint/ancp,/vport/protocolStack/atm/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/ancp,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/atm/pppoxEndpoint/ancp,/vport/protocolStack/atm/pppoxEndpoint/range/ancpRange,/vport/protocolStack/ethernet/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/ancp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/ancp,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ipEndpoint/ancp,/vport/protocolStack/ethernet/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/ancp,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppoxEndpoint/ancp,/vport/protocolStack/ethernet/pppoxEndpoint/range/ancpRange]

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('ancpStartAdjacency', payload=payload, response_object=None)

	def AncpStartResync(self, *args, **kwargs):
		"""Executes the ancpStartResync operation on the server.

		Start resync ANCP DSL line capabilities for selected ranges

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		ancpStartResync(Arg2:number, Arg3:number)
			Args:
				args[0] is Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/ancp,/vport/protocolStack/atm/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/ancp,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/ancp,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ipEndpoint/ancp,/vport/protocolStack/atm/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/ancp,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/atm/pppoxEndpoint/ancp,/vport/protocolStack/atm/pppoxEndpoint/range/ancpRange,/vport/protocolStack/ethernet/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/ancp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/ancp,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ipEndpoint/ancp,/vport/protocolStack/ethernet/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/ancp,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppoxEndpoint/ancp,/vport/protocolStack/ethernet/pppoxEndpoint/range/ancpRange]
				args[1] is Arg3 (number): Number of ReSync iterations performed by DSL Lines in selected ANCP ranges.

		ancpStartResync(Arg2:number, Arg3:number, Arg4:enum)
			Args:
				args[0] is Arg2 (number): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/ancp,/vport/protocolStack/atm/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/ancp,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/ancp,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ipEndpoint/ancp,/vport/protocolStack/atm/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/ancp,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/atm/pppoxEndpoint/ancp,/vport/protocolStack/atm/pppoxEndpoint/range/ancpRange,/vport/protocolStack/ethernet/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/ancp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/ancp,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ipEndpoint/ancp,/vport/protocolStack/ethernet/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/ancp,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppoxEndpoint/ancp,/vport/protocolStack/ethernet/pppoxEndpoint/range/ancpRange]
				args[1] is Arg3 (number): Number of ReSync iterations performed by DSL Lines in selected ANCP ranges.
				args[2] is Arg4 (str(async|sync)): Time gap between ReSync terations performed by DSL Lines in selected ANCP ranges [seconds].

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('ancpStartResync', payload=payload, response_object=None)

	def AncpStop(self, *args, **kwargs):
		"""Executes the ancpStop operation on the server.

		Teardown ANCP and PPPoE sessions for selected ranges

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		ancpStop()

		ancpStop(Arg2:enum)
			Args:
				args[0] is Arg2 (str(async|sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/ancp,/vport/protocolStack/atm/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/ancp,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/ancp,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ipEndpoint/ancp,/vport/protocolStack/atm/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/ancp,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/atm/pppoxEndpoint/ancp,/vport/protocolStack/atm/pppoxEndpoint/range/ancpRange,/vport/protocolStack/ethernet/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/ancp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/ancp,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ipEndpoint/ancp,/vport/protocolStack/ethernet/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/ancp,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppoxEndpoint/ancp,/vport/protocolStack/ethernet/pppoxEndpoint/range/ancpRange]

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('ancpStop', payload=payload, response_object=None)

	def AncpStopAdjacency(self, *args, **kwargs):
		"""Executes the ancpStopAdjacency operation on the server.

		Stop ANCP adjacency

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		ancpStopAdjacency()

		ancpStopAdjacency(Arg2:enum)
			Args:
				args[0] is Arg2 (str(async|sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/ancp,/vport/protocolStack/atm/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/ancp,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/ancp,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ipEndpoint/ancp,/vport/protocolStack/atm/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/ancp,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/atm/pppoxEndpoint/ancp,/vport/protocolStack/atm/pppoxEndpoint/range/ancpRange,/vport/protocolStack/ethernet/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/ancp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/ancp,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ipEndpoint/ancp,/vport/protocolStack/ethernet/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/ancp,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppoxEndpoint/ancp,/vport/protocolStack/ethernet/pppoxEndpoint/range/ancpRange]

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('ancpStopAdjacency', payload=payload, response_object=None)

	def AncpTeardownDslSubscribers(self, *args, **kwargs):
		"""Executes the ancpTeardownDslSubscribers operation on the server.

		Tear down DSL subscribers

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		ancpTeardownDslSubscribers()

		ancpTeardownDslSubscribers(Arg2:enum)
			Args:
				args[0] is Arg2 (str(async|sync)): kArray[kObjref=/vport/protocolStack/atm/dhcpEndpoint/ancp,/vport/protocolStack/atm/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/ancp,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/ancp,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ipEndpoint/ancp,/vport/protocolStack/atm/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/ancp,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/atm/pppoxEndpoint/ancp,/vport/protocolStack/atm/pppoxEndpoint/range/ancpRange,/vport/protocolStack/ethernet/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/ancp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/ancp,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ipEndpoint/ancp,/vport/protocolStack/ethernet/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/ancp,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppoxEndpoint/ancp,/vport/protocolStack/ethernet/pppoxEndpoint/range/ancpRange]

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('ancpTeardownDslSubscribers', payload=payload, response_object=None)

	def CustomProtocolStack(self, *args, **kwargs):
		"""Executes the customProtocolStack operation on the server.

		Create custom protocol stack under /vport/protocolStack

		customProtocolStack(Arg2:list, Arg3:enum)
			Args:
				args[0] is Arg2 (list(str)): List of plugin types to be added in the new custom stack
				args[1] is Arg3 (str(kAppend|kMerge|kOverwrite)): Append, merge or overwrite existing protocol stack

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('customProtocolStack', payload=payload, response_object=None)

	def DisableProtocolStack(self, *args, **kwargs):
		"""Executes the disableProtocolStack operation on the server.

		Disable a protocol under protocolStack using the class name

		disableProtocolStack(Arg2:string)string
			Args:
				args[0] is Arg2 (str): Protocol class name to disable

			Returns:
				str: Status of the exec

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('disableProtocolStack', payload=payload, response_object=None)

	def EnableProtocolStack(self, *args, **kwargs):
		"""Executes the enableProtocolStack operation on the server.

		Enable a protocol under protocolStack using the class name

		enableProtocolStack(Arg2:string)string
			Args:
				args[0] is Arg2 (str): Protocol class name to enable

			Returns:
				str: Status of the exec

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('enableProtocolStack', payload=payload, response_object=None)

	def Start(self, *args, **kwargs):
		"""Executes the start operation on the server.

		Negotiate sessions for all protocols on all ranges belonging to selected plugins

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		start()

		start(Arg2:enum)
			Args:
				args[0] is Arg2 (str(async|sync)): kArray[kObjref=/vport/protocolStack/atm,/vport/protocolStack/atm/dhcpEndpoint,/vport/protocolStack/atm/dhcpEndpoint/ancp,/vport/protocolStack/atm/dhcpEndpoint/range,/vport/protocolStack/atm/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/dhcpServerEndpoint,/vport/protocolStack/atm/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip,/vport/protocolStack/atm/emulatedRouter/ip/ancp,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/ueSecondaryRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/twampClient,/vport/protocolStack/atm/emulatedRouter/ip/twampServer,/vport/protocolStack/atm/emulatedRouter/ipEndpoint,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/twampClient,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/twampServer,/vport/protocolStack/atm/emulatedRouterEndpoint,/vport/protocolStack/atm/emulatedRouterEndpoint/range/amtRange,/vport/protocolStack/atm/ip,/vport/protocolStack/atm/ip/ancp,/vport/protocolStack/atm/ip/egtpEnbEndpoint,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpEnbEndpoint/ueSecondaryRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpUeEndpoint,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tpEndpoint,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/smDnsEndpoint,/vport/protocolStack/atm/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/twampClient,/vport/protocolStack/atm/ip/twampServer,/vport/protocolStack/atm/ipEndpoint,/vport/protocolStack/atm/ipEndpoint/ancp,/vport/protocolStack/atm/ipEndpoint/range/amtRange,/vport/protocolStack/atm/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/ipEndpoint/range/twampControlRange,/vport/protocolStack/atm/ipEndpoint/twampClient,/vport/protocolStack/atm/ipEndpoint/twampServer,/vport/protocolStack/atm/pppox,/vport/protocolStack/atm/pppox/ancp,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/pppoxEndpoint,/vport/protocolStack/atm/pppoxEndpoint/ancp,/vport/protocolStack/atm/pppoxEndpoint/range,/vport/protocolStack/atm/pppoxEndpoint/range/ancpRange,/vport/protocolStack/atm/pppoxEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppoxEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet,/vport/protocolStack/ethernet/dcbxEndpoint,/vport/protocolStack/ethernet/dcbxEndpoint/range,/vport/protocolStack/ethernet/dhcpEndpoint,/vport/protocolStack/ethernet/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/dhcpEndpoint/range,/vport/protocolStack/ethernet/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/dhcpServerEndpoint,/vport/protocolStack/ethernet/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip,/vport/protocolStack/ethernet/emulatedRouter/ip/ancp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/ueSecondaryRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/twampClient,/vport/protocolStack/ethernet/emulatedRouter/ip/twampServer,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/twampClient,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/twampServer,/vport/protocolStack/ethernet/emulatedRouterEndpoint,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/amtRange,/vport/protocolStack/ethernet/esmc,/vport/protocolStack/ethernet/fcoeClientEndpoint,/vport/protocolStack/ethernet/fcoeClientEndpoint/range,/vport/protocolStack/ethernet/fcoeClientEndpoint/range,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/fcoeClientFdiscRange,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/fcoeClientFlogiRange,/vport/protocolStack/ethernet/fcoeFwdEndpoint,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range,/vport/protocolStack/ethernet/fcoeFwdEndpoint/secondaryRange,/vport/protocolStack/ethernet/ip,/vport/protocolStack/ethernet/ip/ancp,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/ueSecondaryRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/twampClient,/vport/protocolStack/ethernet/ip/twampServer,/vport/protocolStack/ethernet/ipEndpoint,/vport/protocolStack/ethernet/ipEndpoint/ancp,/vport/protocolStack/ethernet/ipEndpoint/range/amtRange,/vport/protocolStack/ethernet/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ipEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ipEndpoint/twampClient,/vport/protocolStack/ethernet/ipEndpoint/twampServer,/vport/protocolStack/ethernet/pppox,/vport/protocolStack/ethernet/pppox/ancp,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/pppoxEndpoint,/vport/protocolStack/ethernet/pppoxEndpoint/ancp,/vport/protocolStack/ethernet/pppoxEndpoint/range,/vport/protocolStack/ethernet/pppoxEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/vepaEndpoint,/vport/protocolStack/ethernet/vepaEndpoint/range,/vport/protocolStack/ethernetEndpoint,/vport/protocolStack/ethernetEndpoint/esmc,/vport/protocolStack/fcClientEndpoint,/vport/protocolStack/fcClientEndpoint/range,/vport/protocolStack/fcClientEndpoint/range,/vport/protocolStack/fcClientEndpoint/range/fcClientFdiscRange,/vport/protocolStack/fcClientEndpoint/range/fcClientFlogiRange,/vport/protocolStack/fcFportFwdEndpoint,/vport/protocolStack/fcFportFwdEndpoint/range,/vport/protocolStack/fcFportFwdEndpoint/secondaryRange]

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

		Teardown sessions for all protocols on all ranges belonging to selected plugins

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		stop()

		stop(Arg2:enum)
			Args:
				args[0] is Arg2 (str(async|sync)): kArray[kObjref=/vport/protocolStack/atm,/vport/protocolStack/atm/dhcpEndpoint,/vport/protocolStack/atm/dhcpEndpoint/ancp,/vport/protocolStack/atm/dhcpEndpoint/range,/vport/protocolStack/atm/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/dhcpServerEndpoint,/vport/protocolStack/atm/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/atm/emulatedRouter/dhcpServerEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip,/vport/protocolStack/atm/emulatedRouter/ip/ancp,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpEnbEndpoint/ueSecondaryRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpMmeEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/emulatedRouter/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ip/twampClient,/vport/protocolStack/atm/emulatedRouter/ip/twampServer,/vport/protocolStack/atm/emulatedRouter/ipEndpoint,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/amtRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/range/twampControlRange,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/twampClient,/vport/protocolStack/atm/emulatedRouter/ipEndpoint/twampServer,/vport/protocolStack/atm/emulatedRouterEndpoint,/vport/protocolStack/atm/emulatedRouterEndpoint/range/amtRange,/vport/protocolStack/atm/ip,/vport/protocolStack/atm/ip/ancp,/vport/protocolStack/atm/ip/egtpEnbEndpoint,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpEnbEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpEnbEndpoint/ueSecondaryRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpMmeEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpUeEndpoint,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tp,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/l2tpEndpoint,/vport/protocolStack/atm/ip/l2tpEndpoint/range,/vport/protocolStack/atm/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/smDnsEndpoint,/vport/protocolStack/atm/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/atm/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/atm/ip/twampClient,/vport/protocolStack/atm/ip/twampServer,/vport/protocolStack/atm/ipEndpoint,/vport/protocolStack/atm/ipEndpoint/ancp,/vport/protocolStack/atm/ipEndpoint/range/amtRange,/vport/protocolStack/atm/ipEndpoint/range/ancpRange,/vport/protocolStack/atm/ipEndpoint/range/twampControlRange,/vport/protocolStack/atm/ipEndpoint/twampClient,/vport/protocolStack/atm/ipEndpoint/twampServer,/vport/protocolStack/atm/pppox,/vport/protocolStack/atm/pppox/ancp,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppox/dhcpoPppClientEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppox/dhcpoPppServerEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/atm/pppoxEndpoint,/vport/protocolStack/atm/pppoxEndpoint/ancp,/vport/protocolStack/atm/pppoxEndpoint/range,/vport/protocolStack/atm/pppoxEndpoint/range/ancpRange,/vport/protocolStack/atm/pppoxEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/atm/pppoxEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet,/vport/protocolStack/ethernet/dcbxEndpoint,/vport/protocolStack/ethernet/dcbxEndpoint/range,/vport/protocolStack/ethernet/dhcpEndpoint,/vport/protocolStack/ethernet/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/dhcpEndpoint/range,/vport/protocolStack/ethernet/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/dhcpServerEndpoint,/vport/protocolStack/ethernet/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/dhcpServerEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip,/vport/protocolStack/ethernet/emulatedRouter/ip/ancp,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpEnbEndpoint/ueSecondaryRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpMmeEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/emulatedRouter/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ip/twampClient,/vport/protocolStack/ethernet/emulatedRouter/ip/twampServer,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/ancp,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/amtRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/twampClient,/vport/protocolStack/ethernet/emulatedRouter/ipEndpoint/twampServer,/vport/protocolStack/ethernet/emulatedRouterEndpoint,/vport/protocolStack/ethernet/emulatedRouterEndpoint/range/amtRange,/vport/protocolStack/ethernet/esmc,/vport/protocolStack/ethernet/fcoeClientEndpoint,/vport/protocolStack/ethernet/fcoeClientEndpoint/range,/vport/protocolStack/ethernet/fcoeClientEndpoint/range,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/fcoeClientFdiscRange,/vport/protocolStack/ethernet/fcoeClientEndpoint/range/fcoeClientFlogiRange,/vport/protocolStack/ethernet/fcoeFwdEndpoint,/vport/protocolStack/ethernet/fcoeFwdEndpoint/range,/vport/protocolStack/ethernet/fcoeFwdEndpoint/secondaryRange,/vport/protocolStack/ethernet/ip,/vport/protocolStack/ethernet/ip/ancp,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpEnbEndpoint/ueSecondaryRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpMmeEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpPcrfS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8PgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpSgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/egtpUeS5S8SgwEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tp,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLacEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tp/dhcpoLnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/ip/l2tpEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/amtRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ip/smDnsEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ip/twampClient,/vport/protocolStack/ethernet/ip/twampServer,/vport/protocolStack/ethernet/ipEndpoint,/vport/protocolStack/ethernet/ipEndpoint/ancp,/vport/protocolStack/ethernet/ipEndpoint/range/amtRange,/vport/protocolStack/ethernet/ipEndpoint/range/ancpRange,/vport/protocolStack/ethernet/ipEndpoint/range/twampControlRange,/vport/protocolStack/ethernet/ipEndpoint/twampClient,/vport/protocolStack/ethernet/ipEndpoint/twampServer,/vport/protocolStack/ethernet/pppox,/vport/protocolStack/ethernet/pppox/ancp,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppClientEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppox/dhcpoPppServerEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/pppoxEndpoint,/vport/protocolStack/ethernet/pppoxEndpoint/ancp,/vport/protocolStack/ethernet/pppoxEndpoint/range,/vport/protocolStack/ethernet/pppoxEndpoint/range/ancpRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/dhcpv6PdClientRange,/vport/protocolStack/ethernet/pppoxEndpoint/range/dhcpv6ServerRange,/vport/protocolStack/ethernet/vepaEndpoint,/vport/protocolStack/ethernet/vepaEndpoint/range,/vport/protocolStack/ethernetEndpoint,/vport/protocolStack/ethernetEndpoint/esmc,/vport/protocolStack/fcClientEndpoint,/vport/protocolStack/fcClientEndpoint/range,/vport/protocolStack/fcClientEndpoint/range,/vport/protocolStack/fcClientEndpoint/range/fcClientFdiscRange,/vport/protocolStack/fcClientEndpoint/range/fcClientFlogiRange,/vport/protocolStack/fcFportFwdEndpoint,/vport/protocolStack/fcFportFwdEndpoint/range,/vport/protocolStack/fcFportFwdEndpoint/secondaryRange]

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('stop', payload=payload, response_object=None)
