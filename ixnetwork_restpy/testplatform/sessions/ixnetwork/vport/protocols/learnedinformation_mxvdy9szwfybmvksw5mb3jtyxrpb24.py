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


class LearnedInformation(Base):
	"""Indicates the port level aggregated view of Learned Information for per Interface.
	The LearnedInformation class encapsulates a required learnedInformation resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'learnedInformation'

	def __init__(self, parent):
		super(LearnedInformation, self).__init__(parent)

	@property
	def AsyncConfStatLearnedInformation(self):
		"""An instance of the AsyncConfStatLearnedInformation class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.asyncconfstatlearnedinformation_u3rhdexlyxjuzwrjbmzvcm1hdglvbg.AsyncConfStatLearnedInformation)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.asyncconfstatlearnedinformation_u3rhdexlyxjuzwrjbmzvcm1hdglvbg import AsyncConfStatLearnedInformation
		return AsyncConfStatLearnedInformation(self)

	@property
	def Controller131TriggerAttributes(self):
		"""An instance of the Controller131TriggerAttributes class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.controller131triggerattributes_xlcjezmvryawdnzxjbdhryawj1dgvz.Controller131TriggerAttributes)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.controller131triggerattributes_xlcjezmvryawdnzxjbdhryawj1dgvz import Controller131TriggerAttributes
		return Controller131TriggerAttributes(self)._select()

	@property
	def DescriptionStatLearnedInformation(self):
		"""An instance of the DescriptionStatLearnedInformation class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.descriptionstatlearnedinformation_5tdgf0tgvhcm5lzeluzm9ybwf0aw9u.DescriptionStatLearnedInformation)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.descriptionstatlearnedinformation_5tdgf0tgvhcm5lzeluzm9ybwf0aw9u import DescriptionStatLearnedInformation
		return DescriptionStatLearnedInformation(self)

	@property
	def FlowAggregatedStatLearnedInformation(self):
		"""An instance of the FlowAggregatedStatLearnedInformation class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowaggregatedstatlearnedinformation_rtdgf0tgvhcm5lzeluzm9ybwf0aw9u.FlowAggregatedStatLearnedInformation)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowaggregatedstatlearnedinformation_rtdgf0tgvhcm5lzeluzm9ybwf0aw9u import FlowAggregatedStatLearnedInformation
		return FlowAggregatedStatLearnedInformation(self)

	@property
	def FlowAggregatedStatMatchCriteria131TriggerAttributes(self):
		"""An instance of the FlowAggregatedStatMatchCriteria131TriggerAttributes class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowaggregatedstatmatchcriteria131triggerattributes_jpytezmvryawdnzxjbdhryawj1dgvz.FlowAggregatedStatMatchCriteria131TriggerAttributes)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowaggregatedstatmatchcriteria131triggerattributes_jpytezmvryawdnzxjbdhryawj1dgvz import FlowAggregatedStatMatchCriteria131TriggerAttributes
		return FlowAggregatedStatMatchCriteria131TriggerAttributes(self)._select()

	@property
	def FlowStatLearnedInformation(self):
		"""An instance of the FlowStatLearnedInformation class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowstatlearnedinformation_1n0yxrmzwfybmvksw5mb3jtyxrpb24.FlowStatLearnedInformation)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowstatlearnedinformation_1n0yxrmzwfybmvksw5mb3jtyxrpb24 import FlowStatLearnedInformation
		return FlowStatLearnedInformation(self)

	@property
	def FlowStatMatchCriteria131TriggerAttributes(self):
		"""An instance of the FlowStatMatchCriteria131TriggerAttributes class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowstatmatchcriteria131triggerattributes_mlhmtmxvhjpz2dlckf0dhjpynv0zxm.FlowStatMatchCriteria131TriggerAttributes)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowstatmatchcriteria131triggerattributes_mlhmtmxvhjpz2dlckf0dhjpynv0zxm import FlowStatMatchCriteria131TriggerAttributes
		return FlowStatMatchCriteria131TriggerAttributes(self)._select()

	@property
	def GroupDescriptionStatLearnedInformation(self):
		"""An instance of the GroupDescriptionStatLearnedInformation class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupdescriptionstatlearnedinformation_ln0yxrmzwfybmvksw5mb3jtyxrpb24.GroupDescriptionStatLearnedInformation)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupdescriptionstatlearnedinformation_ln0yxrmzwfybmvksw5mb3jtyxrpb24 import GroupDescriptionStatLearnedInformation
		return GroupDescriptionStatLearnedInformation(self)

	@property
	def GroupFeatureStatLearnedInformation(self):
		"""An instance of the GroupFeatureStatLearnedInformation class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupfeaturestatlearnedinformation_u3rhdexlyxjuzwrjbmzvcm1hdglvbg.GroupFeatureStatLearnedInformation)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupfeaturestatlearnedinformation_u3rhdexlyxjuzwrjbmzvcm1hdglvbg import GroupFeatureStatLearnedInformation
		return GroupFeatureStatLearnedInformation(self)

	@property
	def GroupStatLearnedInformation(self):
		"""An instance of the GroupStatLearnedInformation class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupstatlearnedinformation_btdgf0tgvhcm5lzeluzm9ybwf0aw9u.GroupStatLearnedInformation)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupstatlearnedinformation_btdgf0tgvhcm5lzeluzm9ybwf0aw9u import GroupStatLearnedInformation
		return GroupStatLearnedInformation(self)

	@property
	def MeterConfigStatsLearnedInformation(self):
		"""An instance of the MeterConfigStatsLearnedInformation class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterconfigstatslearnedinformation_dgf0c0xlyxjuzwrjbmzvcm1hdglvbg.MeterConfigStatsLearnedInformation)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterconfigstatslearnedinformation_dgf0c0xlyxjuzwrjbmzvcm1hdglvbg import MeterConfigStatsLearnedInformation
		return MeterConfigStatsLearnedInformation(self)

	@property
	def MeterFeatureStatsLearnedInformation(self):
		"""An instance of the MeterFeatureStatsLearnedInformation class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterfeaturestatslearnedinformation_3rhdhnmzwfybmvksw5mb3jtyxrpb24.MeterFeatureStatsLearnedInformation)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterfeaturestatslearnedinformation_3rhdhnmzwfybmvksw5mb3jtyxrpb24 import MeterFeatureStatsLearnedInformation
		return MeterFeatureStatsLearnedInformation(self)

	@property
	def MeterStatsLearnedInformation(self):
		"""An instance of the MeterStatsLearnedInformation class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterstatslearnedinformation_dgf0c0xlyxjuzwrjbmzvcm1hdglvbg.MeterStatsLearnedInformation)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meterstatslearnedinformation_dgf0c0xlyxjuzwrjbmzvcm1hdglvbg import MeterStatsLearnedInformation
		return MeterStatsLearnedInformation(self)

	@property
	def OfChannelLearnedInformation(self):
		"""An instance of the OfChannelLearnedInformation class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannellearnedinformation_fubmvstgvhcm5lzeluzm9ybwf0aw9u.OfChannelLearnedInformation)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ofchannellearnedinformation_fubmvstgvhcm5lzeluzm9ybwf0aw9u import OfChannelLearnedInformation
		return OfChannelLearnedInformation(self)

	@property
	def PacketOutTriggerActions(self):
		"""An instance of the PacketOutTriggerActions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.packetouttriggeractions_gfja2v0t3v0vhjpz2dlckfjdglvbnm.PacketOutTriggerActions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.packetouttriggeractions_gfja2v0t3v0vhjpz2dlckfjdglvbnm import PacketOutTriggerActions
		return PacketOutTriggerActions(self)

	@property
	def PortFeaturesLearnedInformation(self):
		"""An instance of the PortFeaturesLearnedInformation class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portfeatureslearnedinformation_r1cmvztgvhcm5lzeluzm9ybwf0aw9u.PortFeaturesLearnedInformation)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portfeatureslearnedinformation_r1cmvztgvhcm5lzeluzm9ybwf0aw9u import PortFeaturesLearnedInformation
		return PortFeaturesLearnedInformation(self)

	@property
	def PortModificationTriggerAttributes(self):
		"""An instance of the PortModificationTriggerAttributes class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portmodificationtriggerattributes_nhdglvblryawdnzxjbdhryawj1dgvz.PortModificationTriggerAttributes)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portmodificationtriggerattributes_nhdglvblryawdnzxjbdhryawj1dgvz import PortModificationTriggerAttributes
		return PortModificationTriggerAttributes(self)._select()

	@property
	def PortStatLearnedInformation(self):
		"""An instance of the PortStatLearnedInformation class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portstatlearnedinformation_fn0yxrmzwfybmvksw5mb3jtyxrpb24.PortStatLearnedInformation)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portstatlearnedinformation_fn0yxrmzwfybmvksw5mb3jtyxrpb24 import PortStatLearnedInformation
		return PortStatLearnedInformation(self)

	@property
	def QueueConfigLearnedInformation(self):
		"""An instance of the QueueConfigLearnedInformation class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.queueconfiglearnedinformation_25mawdmzwfybmvksw5mb3jtyxrpb24.QueueConfigLearnedInformation)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.queueconfiglearnedinformation_25mawdmzwfybmvksw5mb3jtyxrpb24 import QueueConfigLearnedInformation
		return QueueConfigLearnedInformation(self)

	@property
	def QueueStatLearnedInformation(self):
		"""An instance of the QueueStatLearnedInformation class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.queuestatlearnedinformation_vtdgf0tgvhcm5lzeluzm9ybwf0aw9u.QueueStatLearnedInformation)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.queuestatlearnedinformation_vtdgf0tgvhcm5lzeluzm9ybwf0aw9u import QueueStatLearnedInformation
		return QueueStatLearnedInformation(self)

	@property
	def SwitchConfigLearnedInformation(self):
		"""An instance of the SwitchConfigLearnedInformation class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchconfiglearnedinformation_9uzmlntgvhcm5lzeluzm9ybwf0aw9u.SwitchConfigLearnedInformation)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchconfiglearnedinformation_9uzmlntgvhcm5lzeluzm9ybwf0aw9u import SwitchConfigLearnedInformation
		return SwitchConfigLearnedInformation(self)

	@property
	def TableFeaturePropertiesTrigger(self):
		"""An instance of the TableFeaturePropertiesTrigger class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablefeaturepropertiestrigger_wf0dxjluhjvcgvydgllc1ryawdnzxi.TableFeaturePropertiesTrigger)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablefeaturepropertiestrigger_wf0dxjluhjvcgvydgllc1ryawdnzxi import TableFeaturePropertiesTrigger
		return TableFeaturePropertiesTrigger(self)

	@property
	def TableFeaturesLearnedInformation(self):
		"""An instance of the TableFeaturesLearnedInformation class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablefeatureslearnedinformation_dxjlc0xlyxjuzwrjbmzvcm1hdglvbg.TableFeaturesLearnedInformation)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablefeatureslearnedinformation_dxjlc0xlyxjuzwrjbmzvcm1hdglvbg import TableFeaturesLearnedInformation
		return TableFeaturesLearnedInformation(self)

	@property
	def TableStatLearnedInformation(self):
		"""An instance of the TableStatLearnedInformation class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablestatlearnedinformation_vtdgf0tgvhcm5lzeluzm9ybwf0aw9u.TableStatLearnedInformation)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.tablestatlearnedinformation_vtdgf0tgvhcm5lzeluzm9ybwf0aw9u import TableStatLearnedInformation
		return TableStatLearnedInformation(self)

	@property
	def VendorStatLearnedInformation(self):
		"""An instance of the VendorStatLearnedInformation class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vendorstatlearnedinformation_u3rhdexlyxjuzwrjbmzvcm1hdglvbg.VendorStatLearnedInformation)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.vendorstatlearnedinformation_u3rhdexlyxjuzwrjbmzvcm1hdglvbg import VendorStatLearnedInformation
		return VendorStatLearnedInformation(self)

	@property
	def AsyncConfStatResponseTimeOut(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('asyncConfStatResponseTimeOut')
	@AsyncConfStatResponseTimeOut.setter
	def AsyncConfStatResponseTimeOut(self, value):
		self._set_attribute('asyncConfStatResponseTimeOut', value)

	@property
	def DescriptionStatResponseTimeOut(self):
		"""Indicates the duration in milliseconds after which the trigger request times out if no description statistics response is received.

		Returns:
			number
		"""
		return self._get_attribute('descriptionStatResponseTimeOut')
	@DescriptionStatResponseTimeOut.setter
	def DescriptionStatResponseTimeOut(self, value):
		self._set_attribute('descriptionStatResponseTimeOut', value)

	@property
	def EnableAsyncConfMasterFlowRemovedFlowDelete(self):
		"""If enabled,it denotes that the enable Asynchronous Configuration Master Flow Removed Flow Delete is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableAsyncConfMasterFlowRemovedFlowDelete')
	@EnableAsyncConfMasterFlowRemovedFlowDelete.setter
	def EnableAsyncConfMasterFlowRemovedFlowDelete(self, value):
		self._set_attribute('enableAsyncConfMasterFlowRemovedFlowDelete', value)

	@property
	def EnableAsyncConfMasterFlowRemovedGroupDelete(self):
		"""If enabled,it denotes that the enable Asynchronous Configuration Master Flow Removed Group Delete is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableAsyncConfMasterFlowRemovedGroupDelete')
	@EnableAsyncConfMasterFlowRemovedGroupDelete.setter
	def EnableAsyncConfMasterFlowRemovedGroupDelete(self, value):
		self._set_attribute('enableAsyncConfMasterFlowRemovedGroupDelete', value)

	@property
	def EnableAsyncConfMasterFlowRemovedHardTimeOut(self):
		"""If enabled,it denotes that the enable Asynchronous Configuration Master Flow Removed Hard Time Out is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableAsyncConfMasterFlowRemovedHardTimeOut')
	@EnableAsyncConfMasterFlowRemovedHardTimeOut.setter
	def EnableAsyncConfMasterFlowRemovedHardTimeOut(self, value):
		self._set_attribute('enableAsyncConfMasterFlowRemovedHardTimeOut', value)

	@property
	def EnableAsyncConfMasterFlowRemovedIdleTimeOut(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('enableAsyncConfMasterFlowRemovedIdleTimeOut')
	@EnableAsyncConfMasterFlowRemovedIdleTimeOut.setter
	def EnableAsyncConfMasterFlowRemovedIdleTimeOut(self, value):
		self._set_attribute('enableAsyncConfMasterFlowRemovedIdleTimeOut', value)

	@property
	def EnableAsyncConfMasterPacketInActionOutputToController(self):
		"""If enabled,it denotes that the enable Asynchronous Configuration Master Packet In Action Output To Controller is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableAsyncConfMasterPacketInActionOutputToController')
	@EnableAsyncConfMasterPacketInActionOutputToController.setter
	def EnableAsyncConfMasterPacketInActionOutputToController(self, value):
		self._set_attribute('enableAsyncConfMasterPacketInActionOutputToController', value)

	@property
	def EnableAsyncConfMasterPacketInInvalidTtl(self):
		"""If enabled,it denotes that the enable Asynchronous Configuration Master Packet In Invalid Ttl is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableAsyncConfMasterPacketInInvalidTtl')
	@EnableAsyncConfMasterPacketInInvalidTtl.setter
	def EnableAsyncConfMasterPacketInInvalidTtl(self, value):
		self._set_attribute('enableAsyncConfMasterPacketInInvalidTtl', value)

	@property
	def EnableAsyncConfMasterPacketInNoMatching(self):
		"""If enabled,it denotes that the enable Asynchronous Configuration Master Packet In No Matching is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableAsyncConfMasterPacketInNoMatching')
	@EnableAsyncConfMasterPacketInNoMatching.setter
	def EnableAsyncConfMasterPacketInNoMatching(self, value):
		self._set_attribute('enableAsyncConfMasterPacketInNoMatching', value)

	@property
	def EnableAsyncConfMasterPortStatusAdd(self):
		"""If enabled,it denotes that the enable Asynchronous Configuration Master Port Status Add is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableAsyncConfMasterPortStatusAdd')
	@EnableAsyncConfMasterPortStatusAdd.setter
	def EnableAsyncConfMasterPortStatusAdd(self, value):
		self._set_attribute('enableAsyncConfMasterPortStatusAdd', value)

	@property
	def EnableAsyncConfMasterPortStatusDelete(self):
		"""If enabled,it denotes that the enable Asynchronous Configuration Master Port Status Delete is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableAsyncConfMasterPortStatusDelete')
	@EnableAsyncConfMasterPortStatusDelete.setter
	def EnableAsyncConfMasterPortStatusDelete(self, value):
		self._set_attribute('enableAsyncConfMasterPortStatusDelete', value)

	@property
	def EnableAsyncConfMasterPortStatusModify(self):
		"""If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Delete is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableAsyncConfMasterPortStatusModify')
	@EnableAsyncConfMasterPortStatusModify.setter
	def EnableAsyncConfMasterPortStatusModify(self, value):
		self._set_attribute('enableAsyncConfMasterPortStatusModify', value)

	@property
	def EnableAsyncConfSlaveFlowRemovedFlowDelete(self):
		"""If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Flow Delete is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableAsyncConfSlaveFlowRemovedFlowDelete')
	@EnableAsyncConfSlaveFlowRemovedFlowDelete.setter
	def EnableAsyncConfSlaveFlowRemovedFlowDelete(self, value):
		self._set_attribute('enableAsyncConfSlaveFlowRemovedFlowDelete', value)

	@property
	def EnableAsyncConfSlaveFlowRemovedGroupDelete(self):
		"""If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Group Delete is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableAsyncConfSlaveFlowRemovedGroupDelete')
	@EnableAsyncConfSlaveFlowRemovedGroupDelete.setter
	def EnableAsyncConfSlaveFlowRemovedGroupDelete(self, value):
		self._set_attribute('enableAsyncConfSlaveFlowRemovedGroupDelete', value)

	@property
	def EnableAsyncConfSlaveFlowRemovedHardTimeOut(self):
		"""If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Hard Time Out is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableAsyncConfSlaveFlowRemovedHardTimeOut')
	@EnableAsyncConfSlaveFlowRemovedHardTimeOut.setter
	def EnableAsyncConfSlaveFlowRemovedHardTimeOut(self, value):
		self._set_attribute('enableAsyncConfSlaveFlowRemovedHardTimeOut', value)

	@property
	def EnableAsyncConfSlaveFlowRemovedIdleTimeOut(self):
		"""If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Idle Time Out is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableAsyncConfSlaveFlowRemovedIdleTimeOut')
	@EnableAsyncConfSlaveFlowRemovedIdleTimeOut.setter
	def EnableAsyncConfSlaveFlowRemovedIdleTimeOut(self, value):
		self._set_attribute('enableAsyncConfSlaveFlowRemovedIdleTimeOut', value)

	@property
	def EnableAsyncConfSlavePacketInActionOutputToController(self):
		"""If enabled,it denotes that the enable Asynchronous Configuration Slave Packet In Action Output To Controller is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableAsyncConfSlavePacketInActionOutputToController')
	@EnableAsyncConfSlavePacketInActionOutputToController.setter
	def EnableAsyncConfSlavePacketInActionOutputToController(self, value):
		self._set_attribute('enableAsyncConfSlavePacketInActionOutputToController', value)

	@property
	def EnableAsyncConfSlavePacketInInvalidTtl(self):
		"""If enabled,it denotes that the enable Asynchronous Configuration Slave Packet In Invalid Ttl is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableAsyncConfSlavePacketInInvalidTtl')
	@EnableAsyncConfSlavePacketInInvalidTtl.setter
	def EnableAsyncConfSlavePacketInInvalidTtl(self, value):
		self._set_attribute('enableAsyncConfSlavePacketInInvalidTtl', value)

	@property
	def EnableAsyncConfSlavePacketInNoMatching(self):
		"""If enabled,it denotes that the enable Asynchronous Configuration Slave Packet In No Matching is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableAsyncConfSlavePacketInNoMatching')
	@EnableAsyncConfSlavePacketInNoMatching.setter
	def EnableAsyncConfSlavePacketInNoMatching(self, value):
		self._set_attribute('enableAsyncConfSlavePacketInNoMatching', value)

	@property
	def EnableAsyncConfSlavePortStatusAdd(self):
		"""If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Add is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableAsyncConfSlavePortStatusAdd')
	@EnableAsyncConfSlavePortStatusAdd.setter
	def EnableAsyncConfSlavePortStatusAdd(self, value):
		self._set_attribute('enableAsyncConfSlavePortStatusAdd', value)

	@property
	def EnableAsyncConfSlavePortStatusDelete(self):
		"""If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Delete is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableAsyncConfSlavePortStatusDelete')
	@EnableAsyncConfSlavePortStatusDelete.setter
	def EnableAsyncConfSlavePortStatusDelete(self, value):
		self._set_attribute('enableAsyncConfSlavePortStatusDelete', value)

	@property
	def EnableAsyncConfSlavePortStatusModify(self):
		"""If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Modify is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableAsyncConfSlavePortStatusModify')
	@EnableAsyncConfSlavePortStatusModify.setter
	def EnableAsyncConfSlavePortStatusModify(self, value):
		self._set_attribute('enableAsyncConfSlavePortStatusModify', value)

	@property
	def EnableFlowAggregatedStatMatchCapability(self):
		"""Checks to see if the switch has the capability to publish Flow Aggregated Statistics

		Returns:
			bool
		"""
		return self._get_attribute('enableFlowAggregatedStatMatchCapability')
	@EnableFlowAggregatedStatMatchCapability.setter
	def EnableFlowAggregatedStatMatchCapability(self, value):
		self._set_attribute('enableFlowAggregatedStatMatchCapability', value)

	@property
	def EnableFlowStatMatchCapability(self):
		"""Checks to see if the switch has the capability to publish Flow Statistics

		Returns:
			bool
		"""
		return self._get_attribute('enableFlowStatMatchCapability')
	@EnableFlowStatMatchCapability.setter
	def EnableFlowStatMatchCapability(self, value):
		self._set_attribute('enableFlowStatMatchCapability', value)

	@property
	def EnableGroupStatMatchCapability(self):
		"""If enabled,it denotes that the enable Group Statistics Match Capability is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableGroupStatMatchCapability')
	@EnableGroupStatMatchCapability.setter
	def EnableGroupStatMatchCapability(self, value):
		self._set_attribute('enableGroupStatMatchCapability', value)

	@property
	def EnablePortStatMatchCapability(self):
		"""Checks to see if the switch has the capability to publish Port Statistics

		Returns:
			bool
		"""
		return self._get_attribute('enablePortStatMatchCapability')
	@EnablePortStatMatchCapability.setter
	def EnablePortStatMatchCapability(self, value):
		self._set_attribute('enablePortStatMatchCapability', value)

	@property
	def EnableQueueStatMatchCapability(self):
		"""If true, the switch has the capability to publish Queue Statistics.

		Returns:
			bool
		"""
		return self._get_attribute('enableQueueStatMatchCapability')
	@EnableQueueStatMatchCapability.setter
	def EnableQueueStatMatchCapability(self, value):
		self._set_attribute('enableQueueStatMatchCapability', value)

	@property
	def EnableSendTableFeaturesTrigger(self):
		"""If enabled,it denotes that the enable Send Table Features Trigger is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableSendTableFeaturesTrigger')
	@EnableSendTableFeaturesTrigger.setter
	def EnableSendTableFeaturesTrigger(self, value):
		self._set_attribute('enableSendTableFeaturesTrigger', value)

	@property
	def EnableSendTriggerPortFeaturesLearnedInformation(self):
		"""Enables Trigger for port features learned information.

		Returns:
			bool
		"""
		return self._get_attribute('enableSendTriggerPortFeaturesLearnedInformation')
	@EnableSendTriggerPortFeaturesLearnedInformation.setter
	def EnableSendTriggerPortFeaturesLearnedInformation(self, value):
		self._set_attribute('enableSendTriggerPortFeaturesLearnedInformation', value)

	@property
	def EnableSendTriggeredAsyncConfStatLearnedInformation(self):
		"""If enabled,it denotes that the Triggered Asynchronous Configuration Statistics Learned Information is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableSendTriggeredAsyncConfStatLearnedInformation')
	@EnableSendTriggeredAsyncConfStatLearnedInformation.setter
	def EnableSendTriggeredAsyncConfStatLearnedInformation(self, value):
		self._set_attribute('enableSendTriggeredAsyncConfStatLearnedInformation', value)

	@property
	def EnableSendTriggeredBarrierRequestMessage(self):
		"""If true, enables trigger for barrier request message

		Returns:
			bool
		"""
		return self._get_attribute('enableSendTriggeredBarrierRequestMessage')
	@EnableSendTriggeredBarrierRequestMessage.setter
	def EnableSendTriggeredBarrierRequestMessage(self, value):
		self._set_attribute('enableSendTriggeredBarrierRequestMessage', value)

	@property
	def EnableSendTriggeredDescriptionStatLearnedInformation(self):
		"""If true, the description statistic trigger configuration parameters are available.

		Returns:
			bool
		"""
		return self._get_attribute('enableSendTriggeredDescriptionStatLearnedInformation')
	@EnableSendTriggeredDescriptionStatLearnedInformation.setter
	def EnableSendTriggeredDescriptionStatLearnedInformation(self, value):
		self._set_attribute('enableSendTriggeredDescriptionStatLearnedInformation', value)

	@property
	def EnableSendTriggeredFlowAggregatedStatLearnedInformation(self):
		"""If true, the flow aggregated statistic trigger configuration parameters are available.

		Returns:
			bool
		"""
		return self._get_attribute('enableSendTriggeredFlowAggregatedStatLearnedInformation')
	@EnableSendTriggeredFlowAggregatedStatLearnedInformation.setter
	def EnableSendTriggeredFlowAggregatedStatLearnedInformation(self, value):
		self._set_attribute('enableSendTriggeredFlowAggregatedStatLearnedInformation', value)

	@property
	def EnableSendTriggeredFlowStatLearnedInformation(self):
		"""If true, the flow statistic trigger configuration parameters are available.

		Returns:
			bool
		"""
		return self._get_attribute('enableSendTriggeredFlowStatLearnedInformation')
	@EnableSendTriggeredFlowStatLearnedInformation.setter
	def EnableSendTriggeredFlowStatLearnedInformation(self, value):
		self._set_attribute('enableSendTriggeredFlowStatLearnedInformation', value)

	@property
	def EnableSendTriggeredGroupDescriptionStatLearnedInformation(self):
		"""If enabled,it denotes that the enable Send Triggered Group Description Statistics Learned Information is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableSendTriggeredGroupDescriptionStatLearnedInformation')
	@EnableSendTriggeredGroupDescriptionStatLearnedInformation.setter
	def EnableSendTriggeredGroupDescriptionStatLearnedInformation(self, value):
		self._set_attribute('enableSendTriggeredGroupDescriptionStatLearnedInformation', value)

	@property
	def EnableSendTriggeredGroupFeatureStatLearnedInformation(self):
		"""If enabled,it denotes that the enable Send Triggered Group Feature Statistics Learned Information is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableSendTriggeredGroupFeatureStatLearnedInformation')
	@EnableSendTriggeredGroupFeatureStatLearnedInformation.setter
	def EnableSendTriggeredGroupFeatureStatLearnedInformation(self, value):
		self._set_attribute('enableSendTriggeredGroupFeatureStatLearnedInformation', value)

	@property
	def EnableSendTriggeredGroupStatLearnedInformation(self):
		"""If enabled,it denotes that the Send Triggered Group Statistics Learned Information is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableSendTriggeredGroupStatLearnedInformation')
	@EnableSendTriggeredGroupStatLearnedInformation.setter
	def EnableSendTriggeredGroupStatLearnedInformation(self, value):
		self._set_attribute('enableSendTriggeredGroupStatLearnedInformation', value)

	@property
	def EnableSendTriggeredPacketOutMessage(self):
		"""If enabled,it denotes that the enable Send Triggered Packet Out Message is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableSendTriggeredPacketOutMessage')
	@EnableSendTriggeredPacketOutMessage.setter
	def EnableSendTriggeredPacketOutMessage(self, value):
		self._set_attribute('enableSendTriggeredPacketOutMessage', value)

	@property
	def EnableSendTriggeredPortModificationMessage(self):
		"""If enabled,it denotes that the enable Send Triggered Port Modification Message is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableSendTriggeredPortModificationMessage')
	@EnableSendTriggeredPortModificationMessage.setter
	def EnableSendTriggeredPortModificationMessage(self, value):
		self._set_attribute('enableSendTriggeredPortModificationMessage', value)

	@property
	def EnableSendTriggeredPortStatLearnedInformation(self):
		"""If true, the port statistic trigger configuration parameters are available.

		Returns:
			bool
		"""
		return self._get_attribute('enableSendTriggeredPortStatLearnedInformation')
	@EnableSendTriggeredPortStatLearnedInformation.setter
	def EnableSendTriggeredPortStatLearnedInformation(self, value):
		self._set_attribute('enableSendTriggeredPortStatLearnedInformation', value)

	@property
	def EnableSendTriggeredQueueConfigLearnedInformation(self):
		"""If true, the queue config trigger configuration parameters are available.

		Returns:
			bool
		"""
		return self._get_attribute('enableSendTriggeredQueueConfigLearnedInformation')
	@EnableSendTriggeredQueueConfigLearnedInformation.setter
	def EnableSendTriggeredQueueConfigLearnedInformation(self, value):
		self._set_attribute('enableSendTriggeredQueueConfigLearnedInformation', value)

	@property
	def EnableSendTriggeredQueueStatLearnedInformation(self):
		"""If true, the queue statistic trigger configuration parameters are available.

		Returns:
			bool
		"""
		return self._get_attribute('enableSendTriggeredQueueStatLearnedInformation')
	@EnableSendTriggeredQueueStatLearnedInformation.setter
	def EnableSendTriggeredQueueStatLearnedInformation(self, value):
		self._set_attribute('enableSendTriggeredQueueStatLearnedInformation', value)

	@property
	def EnableSendTriggeredRoleRequestMessage(self):
		"""If enabled,it denotes that the Triggered Role Request Message is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableSendTriggeredRoleRequestMessage')
	@EnableSendTriggeredRoleRequestMessage.setter
	def EnableSendTriggeredRoleRequestMessage(self, value):
		self._set_attribute('enableSendTriggeredRoleRequestMessage', value)

	@property
	def EnableSendTriggeredSwitchConfigLearnedInformation(self):
		"""If enabled,it denotes that the enable Switch Configuration Learned Information is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableSendTriggeredSwitchConfigLearnedInformation')
	@EnableSendTriggeredSwitchConfigLearnedInformation.setter
	def EnableSendTriggeredSwitchConfigLearnedInformation(self, value):
		self._set_attribute('enableSendTriggeredSwitchConfigLearnedInformation', value)

	@property
	def EnableSendTriggeredTableStatLearnedInformation(self):
		"""If true, the table statistic trigger configuration parameters are available.

		Returns:
			bool
		"""
		return self._get_attribute('enableSendTriggeredTableStatLearnedInformation')
	@EnableSendTriggeredTableStatLearnedInformation.setter
	def EnableSendTriggeredTableStatLearnedInformation(self, value):
		self._set_attribute('enableSendTriggeredTableStatLearnedInformation', value)

	@property
	def EnableSendTriggeredVendorStatLearnedInformation(self):
		"""If true, the vendor statistic trigger configuration parameters are available.

		Returns:
			bool
		"""
		return self._get_attribute('enableSendTriggeredVendorStatLearnedInformation')
	@EnableSendTriggeredVendorStatLearnedInformation.setter
	def EnableSendTriggeredVendorStatLearnedInformation(self, value):
		self._set_attribute('enableSendTriggeredVendorStatLearnedInformation', value)

	@property
	def EnableSetAsyncConfig(self):
		"""If enabled,it denotes that the Set Asynchronous Configuration is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableSetAsyncConfig')
	@EnableSetAsyncConfig.setter
	def EnableSetAsyncConfig(self, value):
		self._set_attribute('enableSetAsyncConfig', value)

	@property
	def EnableSetSwitchConfig(self):
		"""If enabled,it denotes that the enable Set Switch Configuration is received.

		Returns:
			bool
		"""
		return self._get_attribute('enableSetSwitchConfig')
	@EnableSetSwitchConfig.setter
	def EnableSetSwitchConfig(self, value):
		self._set_attribute('enableSetSwitchConfig', value)

	@property
	def EnableSetTableFeatures(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('enableSetTableFeatures')
	@EnableSetTableFeatures.setter
	def EnableSetTableFeatures(self, value):
		self._set_attribute('enableSetTableFeatures', value)

	@property
	def EnableTableStatMatchCapability(self):
		"""If true, the switch has the capability to publish Table Statistics.

		Returns:
			bool
		"""
		return self._get_attribute('enableTableStatMatchCapability')
	@EnableTableStatMatchCapability.setter
	def EnableTableStatMatchCapability(self, value):
		self._set_attribute('enableTableStatMatchCapability', value)

	@property
	def EnableTriggeredVendorMessage(self):
		"""If true, the vendor message trigger configuration parameters are available.

		Returns:
			bool
		"""
		return self._get_attribute('enableTriggeredVendorMessage')
	@EnableTriggeredVendorMessage.setter
	def EnableTriggeredVendorMessage(self, value):
		self._set_attribute('enableTriggeredVendorMessage', value)

	@property
	def FlowAggregatedStatEthernetDestination(self):
		"""Signifies the ethernet destination address.

		Returns:
			str
		"""
		return self._get_attribute('flowAggregatedStatEthernetDestination')
	@FlowAggregatedStatEthernetDestination.setter
	def FlowAggregatedStatEthernetDestination(self, value):
		self._set_attribute('flowAggregatedStatEthernetDestination', value)

	@property
	def FlowAggregatedStatEthernetSource(self):
		"""Signifies the ethernet source address.

		Returns:
			str
		"""
		return self._get_attribute('flowAggregatedStatEthernetSource')
	@FlowAggregatedStatEthernetSource.setter
	def FlowAggregatedStatEthernetSource(self, value):
		self._set_attribute('flowAggregatedStatEthernetSource', value)

	@property
	def FlowAggregatedStatEthernetType(self):
		"""Signifies the type of Ethernet used.

		Returns:
			str
		"""
		return self._get_attribute('flowAggregatedStatEthernetType')
	@FlowAggregatedStatEthernetType.setter
	def FlowAggregatedStatEthernetType(self, value):
		self._set_attribute('flowAggregatedStatEthernetType', value)

	@property
	def FlowAggregatedStatInPort(self):
		"""Signifies the input port used.

		Returns:
			str
		"""
		return self._get_attribute('flowAggregatedStatInPort')
	@FlowAggregatedStatInPort.setter
	def FlowAggregatedStatInPort(self, value):
		self._set_attribute('flowAggregatedStatInPort', value)

	@property
	def FlowAggregatedStatIpDscp(self):
		"""Signifies the IP DSCP value for advertising.

		Returns:
			str
		"""
		return self._get_attribute('flowAggregatedStatIpDscp')
	@FlowAggregatedStatIpDscp.setter
	def FlowAggregatedStatIpDscp(self, value):
		self._set_attribute('flowAggregatedStatIpDscp', value)

	@property
	def FlowAggregatedStatIpProtocol(self):
		"""Signifies the IP protocol used.

		Returns:
			str
		"""
		return self._get_attribute('flowAggregatedStatIpProtocol')
	@FlowAggregatedStatIpProtocol.setter
	def FlowAggregatedStatIpProtocol(self, value):
		self._set_attribute('flowAggregatedStatIpProtocol', value)

	@property
	def FlowAggregatedStatIpv4Destination(self):
		"""Signifies the IPv4 destination address.

		Returns:
			str
		"""
		return self._get_attribute('flowAggregatedStatIpv4Destination')
	@FlowAggregatedStatIpv4Destination.setter
	def FlowAggregatedStatIpv4Destination(self, value):
		self._set_attribute('flowAggregatedStatIpv4Destination', value)

	@property
	def FlowAggregatedStatIpv4Source(self):
		"""Signifies the IPv4 source address.

		Returns:
			str
		"""
		return self._get_attribute('flowAggregatedStatIpv4Source')
	@FlowAggregatedStatIpv4Source.setter
	def FlowAggregatedStatIpv4Source(self, value):
		self._set_attribute('flowAggregatedStatIpv4Source', value)

	@property
	def FlowAggregatedStatOutPortInputMode(self):
		"""Signifies the identifier output mode of the aggregated flow statistics table.

		Returns:
			str(ofppInPort|ofppNormal|ofppFlood|ofppAll|ofppController|ofppLocal|ofppNone|custom)
		"""
		return self._get_attribute('flowAggregatedStatOutPortInputMode')
	@FlowAggregatedStatOutPortInputMode.setter
	def FlowAggregatedStatOutPortInputMode(self, value):
		self._set_attribute('flowAggregatedStatOutPortInputMode', value)

	@property
	def FlowAggregatedStatResponseTimeOut(self):
		"""Indicates the duration in milliseconds after which the trigger request times out if no flow aggregated statistics response is received.

		Returns:
			number
		"""
		return self._get_attribute('flowAggregatedStatResponseTimeOut')
	@FlowAggregatedStatResponseTimeOut.setter
	def FlowAggregatedStatResponseTimeOut(self, value):
		self._set_attribute('flowAggregatedStatResponseTimeOut', value)

	@property
	def FlowAggregatedStatTableIdInputMode(self):
		"""Signifies the identifier input mode of the flow aggregated statistics table.

		Returns:
			str(allTables|emergency|custom)
		"""
		return self._get_attribute('flowAggregatedStatTableIdInputMode')
	@FlowAggregatedStatTableIdInputMode.setter
	def FlowAggregatedStatTableIdInputMode(self, value):
		self._set_attribute('flowAggregatedStatTableIdInputMode', value)

	@property
	def FlowAggregatedStatTableIdInputModeNumber(self):
		"""Signifies the identifier input mode of the flow aggregated statistics table.

		Returns:
			number
		"""
		return self._get_attribute('flowAggregatedStatTableIdInputModeNumber')
	@FlowAggregatedStatTableIdInputModeNumber.setter
	def FlowAggregatedStatTableIdInputModeNumber(self, value):
		self._set_attribute('flowAggregatedStatTableIdInputModeNumber', value)

	@property
	def FlowAggregatedStatTransportDestination(self):
		"""Signifies the Transport destination address.

		Returns:
			str
		"""
		return self._get_attribute('flowAggregatedStatTransportDestination')
	@FlowAggregatedStatTransportDestination.setter
	def FlowAggregatedStatTransportDestination(self, value):
		self._set_attribute('flowAggregatedStatTransportDestination', value)

	@property
	def FlowAggregatedStatTransportSource(self):
		"""Signifies the Transport source address.

		Returns:
			str
		"""
		return self._get_attribute('flowAggregatedStatTransportSource')
	@FlowAggregatedStatTransportSource.setter
	def FlowAggregatedStatTransportSource(self, value):
		self._set_attribute('flowAggregatedStatTransportSource', value)

	@property
	def FlowAggregatedStatVlanId(self):
		"""Signifies the unique VLAN Identifier.

		Returns:
			str
		"""
		return self._get_attribute('flowAggregatedStatVlanId')
	@FlowAggregatedStatVlanId.setter
	def FlowAggregatedStatVlanId(self, value):
		self._set_attribute('flowAggregatedStatVlanId', value)

	@property
	def FlowAggregatedStatVlanPriority(self):
		"""Signifies the User Priority for this VLAN.

		Returns:
			str
		"""
		return self._get_attribute('flowAggregatedStatVlanPriority')
	@FlowAggregatedStatVlanPriority.setter
	def FlowAggregatedStatVlanPriority(self, value):
		self._set_attribute('flowAggregatedStatVlanPriority', value)

	@property
	def FlowStatEthernetDestination(self):
		"""Specifies the Ethernet destination address.

		Returns:
			str
		"""
		return self._get_attribute('flowStatEthernetDestination')
	@FlowStatEthernetDestination.setter
	def FlowStatEthernetDestination(self, value):
		self._set_attribute('flowStatEthernetDestination', value)

	@property
	def FlowStatEthernetSource(self):
		"""Specifies the Ethernet source address.

		Returns:
			str
		"""
		return self._get_attribute('flowStatEthernetSource')
	@FlowStatEthernetSource.setter
	def FlowStatEthernetSource(self, value):
		self._set_attribute('flowStatEthernetSource', value)

	@property
	def FlowStatEthernetType(self):
		"""Specifies the type of Ethernet used.

		Returns:
			str
		"""
		return self._get_attribute('flowStatEthernetType')
	@FlowStatEthernetType.setter
	def FlowStatEthernetType(self, value):
		self._set_attribute('flowStatEthernetType', value)

	@property
	def FlowStatInPort(self):
		"""Specifies the input port used.

		Returns:
			str
		"""
		return self._get_attribute('flowStatInPort')
	@FlowStatInPort.setter
	def FlowStatInPort(self, value):
		self._set_attribute('flowStatInPort', value)

	@property
	def FlowStatIpDscp(self):
		"""Specifies the IP DSCP value for advertising.

		Returns:
			str
		"""
		return self._get_attribute('flowStatIpDscp')
	@FlowStatIpDscp.setter
	def FlowStatIpDscp(self, value):
		self._set_attribute('flowStatIpDscp', value)

	@property
	def FlowStatIpProtocol(self):
		"""Specifies the IP protocol used.

		Returns:
			str
		"""
		return self._get_attribute('flowStatIpProtocol')
	@FlowStatIpProtocol.setter
	def FlowStatIpProtocol(self, value):
		self._set_attribute('flowStatIpProtocol', value)

	@property
	def FlowStatIpv4Destination(self):
		"""Specifies the The IPv4 destination address.

		Returns:
			str
		"""
		return self._get_attribute('flowStatIpv4Destination')
	@FlowStatIpv4Destination.setter
	def FlowStatIpv4Destination(self, value):
		self._set_attribute('flowStatIpv4Destination', value)

	@property
	def FlowStatIpv4Source(self):
		"""Specifies the The IPv4 source address.

		Returns:
			str
		"""
		return self._get_attribute('flowStatIpv4Source')
	@FlowStatIpv4Source.setter
	def FlowStatIpv4Source(self, value):
		self._set_attribute('flowStatIpv4Source', value)

	@property
	def FlowStatOutPortInputMode(self):
		"""Specifies the output mode of the Table identifier.

		Returns:
			str(ofppInPort|ofppNormal|ofppFlood|ofppAll|ofppController|ofppLocal|ofppNone|custom)
		"""
		return self._get_attribute('flowStatOutPortInputMode')
	@FlowStatOutPortInputMode.setter
	def FlowStatOutPortInputMode(self, value):
		self._set_attribute('flowStatOutPortInputMode', value)

	@property
	def FlowStatResponseTimeOut(self):
		"""Indicates the duration in milliseconds after which the trigger request times out if no response is received.

		Returns:
			number
		"""
		return self._get_attribute('flowStatResponseTimeOut')
	@FlowStatResponseTimeOut.setter
	def FlowStatResponseTimeOut(self, value):
		self._set_attribute('flowStatResponseTimeOut', value)

	@property
	def FlowStatTableIdInputMode(self):
		"""Specifies the input mode of the Table identifier.

		Returns:
			str(allTables|emergency|custom)
		"""
		return self._get_attribute('flowStatTableIdInputMode')
	@FlowStatTableIdInputMode.setter
	def FlowStatTableIdInputMode(self, value):
		self._set_attribute('flowStatTableIdInputMode', value)

	@property
	def FlowStatTableIdInputModeNumber(self):
		"""Signifies the identifier input mode of the flow statistics table.

		Returns:
			number
		"""
		return self._get_attribute('flowStatTableIdInputModeNumber')
	@FlowStatTableIdInputModeNumber.setter
	def FlowStatTableIdInputModeNumber(self, value):
		self._set_attribute('flowStatTableIdInputModeNumber', value)

	@property
	def FlowStatTransportDestination(self):
		"""Specifies the Transport destination address.

		Returns:
			str
		"""
		return self._get_attribute('flowStatTransportDestination')
	@FlowStatTransportDestination.setter
	def FlowStatTransportDestination(self, value):
		self._set_attribute('flowStatTransportDestination', value)

	@property
	def FlowStatTransportSource(self):
		"""Specifies the Transport source address.

		Returns:
			str
		"""
		return self._get_attribute('flowStatTransportSource')
	@FlowStatTransportSource.setter
	def FlowStatTransportSource(self, value):
		self._set_attribute('flowStatTransportSource', value)

	@property
	def FlowStatVlanId(self):
		"""Specifies the unique VLAN Identifier.

		Returns:
			str
		"""
		return self._get_attribute('flowStatVlanId')
	@FlowStatVlanId.setter
	def FlowStatVlanId(self, value):
		self._set_attribute('flowStatVlanId', value)

	@property
	def FlowStatVlanPriority(self):
		"""Specifies the User Priority for this VLAN.

		Returns:
			str
		"""
		return self._get_attribute('flowStatVlanPriority')
	@FlowStatVlanPriority.setter
	def FlowStatVlanPriority(self, value):
		self._set_attribute('flowStatVlanPriority', value)

	@property
	def GroupDescriptionStatResponseTimeOut(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('groupDescriptionStatResponseTimeOut')
	@GroupDescriptionStatResponseTimeOut.setter
	def GroupDescriptionStatResponseTimeOut(self, value):
		self._set_attribute('groupDescriptionStatResponseTimeOut', value)

	@property
	def GroupFeatureStatResponseTimeOut(self):
		"""The time in milliseconds after which the trigger request times out if no response is received.

		Returns:
			number
		"""
		return self._get_attribute('groupFeatureStatResponseTimeOut')
	@GroupFeatureStatResponseTimeOut.setter
	def GroupFeatureStatResponseTimeOut(self, value):
		self._set_attribute('groupFeatureStatResponseTimeOut', value)

	@property
	def GroupId(self):
		"""The ID of the group used. .

		Returns:
			number
		"""
		return self._get_attribute('groupId')
	@GroupId.setter
	def GroupId(self, value):
		self._set_attribute('groupId', value)

	@property
	def GroupIdType(self):
		"""NOT DEFINED

		Returns:
			str(ofpgAll|ofpgAny|manual)
		"""
		return self._get_attribute('groupIdType')
	@GroupIdType.setter
	def GroupIdType(self, value):
		self._set_attribute('groupIdType', value)

	@property
	def GroupStatResponseTimeOut(self):
		"""The time in milliseconds after which the trigger request times out if no response is received.

		Returns:
			number
		"""
		return self._get_attribute('groupStatResponseTimeOut')
	@GroupStatResponseTimeOut.setter
	def GroupStatResponseTimeOut(self, value):
		self._set_attribute('groupStatResponseTimeOut', value)

	@property
	def IsAsyncConfStatLearnedInformationRefreshed(self):
		"""If true, it denotes that the Learned Info for the Queue Statistics is received.

		Returns:
			bool
		"""
		return self._get_attribute('isAsyncConfStatLearnedInformationRefreshed')

	@property
	def IsDescriptionStatLearnedInformationRefreshed(self):
		"""If true, it denotes that the Learned Info for the Description Statistics is received.

		Returns:
			bool
		"""
		return self._get_attribute('isDescriptionStatLearnedInformationRefreshed')

	@property
	def IsFlowAggregatedStatLearnedInformationRefreshed(self):
		"""If true, it denotes that the Learned Info for the Flow Aggregated Statistics is received.

		Returns:
			bool
		"""
		return self._get_attribute('isFlowAggregatedStatLearnedInformationRefreshed')

	@property
	def IsFlowStatLearnedInformationRefreshed(self):
		"""If true, it denotes that the Learned Info for the Flow Statistics is received.

		Returns:
			bool
		"""
		return self._get_attribute('isFlowStatLearnedInformationRefreshed')

	@property
	def IsGroupDescriptionStatLearnedInformationRefreshed(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('isGroupDescriptionStatLearnedInformationRefreshed')

	@property
	def IsGroupFeatureStatLearnedInformationRefreshed(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('isGroupFeatureStatLearnedInformationRefreshed')

	@property
	def IsGroupStatLearnedInformationRefreshed(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('isGroupStatLearnedInformationRefreshed')

	@property
	def IsOfChannelLearnedInformationRefreshed(self):
		"""If true, it denotes that the Learned Info for the OF Channels is received.

		Returns:
			bool
		"""
		return self._get_attribute('isOfChannelLearnedInformationRefreshed')

	@property
	def IsPortFeaturesLearnedInformationRefreshed(self):
		"""Checks if the learned information for the port feature Learned Information is refreshed.

		Returns:
			bool
		"""
		return self._get_attribute('isPortFeaturesLearnedInformationRefreshed')

	@property
	def IsPortStatLearnedInformationRefreshed(self):
		"""If true, it denotes that the Learned Info for the Port Statistics is received.

		Returns:
			bool
		"""
		return self._get_attribute('isPortStatLearnedInformationRefreshed')

	@property
	def IsQueueConfigLearnedInformationRefreshed(self):
		"""If true, it denotes that the reply for the queue config request is received.

		Returns:
			bool
		"""
		return self._get_attribute('isQueueConfigLearnedInformationRefreshed')

	@property
	def IsQueueStatLearnedInformationRefreshed(self):
		"""If true, it denotes that the Learned Info for the Queue Statistics is received.

		Returns:
			bool
		"""
		return self._get_attribute('isQueueStatLearnedInformationRefreshed')

	@property
	def IsTableStatLearnedInformationRefreshed(self):
		"""If true, it denotes that the Learned Info for the Table Statistics is received.

		Returns:
			bool
		"""
		return self._get_attribute('isTableStatLearnedInformationRefreshed')

	@property
	def IsVendorStatLearnedInformationRefreshed(self):
		"""If true, it denotes that the Learned Info for the Vendor Statistics is received

		Returns:
			bool
		"""
		return self._get_attribute('isVendorStatLearnedInformationRefreshed')

	@property
	def PacketOutAuxiliaryId(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('packetOutAuxiliaryId')
	@PacketOutAuxiliaryId.setter
	def PacketOutAuxiliaryId(self, value):
		self._set_attribute('packetOutAuxiliaryId', value)

	@property
	def PacketOutBufferId(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('packetOutBufferId')
	@PacketOutBufferId.setter
	def PacketOutBufferId(self, value):
		self._set_attribute('packetOutBufferId', value)

	@property
	def PacketOutBufferIdInputMode(self):
		"""NOT DEFINED

		Returns:
			str(opfNoBuffer|manual)
		"""
		return self._get_attribute('packetOutBufferIdInputMode')
	@PacketOutBufferIdInputMode.setter
	def PacketOutBufferIdInputMode(self, value):
		self._set_attribute('packetOutBufferIdInputMode', value)

	@property
	def PacketOutData(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('packetOutData')
	@PacketOutData.setter
	def PacketOutData(self, value):
		self._set_attribute('packetOutData', value)

	@property
	def PacketOutDataLength(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('packetOutDataLength')
	@PacketOutDataLength.setter
	def PacketOutDataLength(self, value):
		self._set_attribute('packetOutDataLength', value)

	@property
	def PacketOutInPortInputMode(self):
		"""NOT DEFINED

		Returns:
			str(ofppController|ofppLocal|manual)
		"""
		return self._get_attribute('packetOutInPortInputMode')
	@PacketOutInPortInputMode.setter
	def PacketOutInPortInputMode(self, value):
		self._set_attribute('packetOutInPortInputMode', value)

	@property
	def PacketOutInPortNumber(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('packetOutInPortNumber')
	@PacketOutInPortNumber.setter
	def PacketOutInPortNumber(self, value):
		self._set_attribute('packetOutInPortNumber', value)

	@property
	def PortFeaturesResponseTimeOut(self):
		"""The time in milliseconds after which the trigger request times out if no response is received.

		Returns:
			number
		"""
		return self._get_attribute('portFeaturesResponseTimeOut')
	@PortFeaturesResponseTimeOut.setter
	def PortFeaturesResponseTimeOut(self, value):
		self._set_attribute('portFeaturesResponseTimeOut', value)

	@property
	def PortNumber(self):
		"""Specifies the port number.

		Returns:
			number
		"""
		return self._get_attribute('portNumber')
	@PortNumber.setter
	def PortNumber(self, value):
		self._set_attribute('portNumber', value)

	@property
	def PortNumberInputMode(self):
		"""Specifies the input mode for the Port number.

		Returns:
			str(ofppNone|custom)
		"""
		return self._get_attribute('portNumberInputMode')
	@PortNumberInputMode.setter
	def PortNumberInputMode(self, value):
		self._set_attribute('portNumberInputMode', value)

	@property
	def PortStatResponseTimeOut(self):
		"""Indicates the duration in milliseconds after which the trigger request times out if no port statistics response is received.

		Returns:
			number
		"""
		return self._get_attribute('portStatResponseTimeOut')
	@PortStatResponseTimeOut.setter
	def PortStatResponseTimeOut(self, value):
		self._set_attribute('portStatResponseTimeOut', value)

	@property
	def QueueConfigPortNumber(self):
		"""Indicates the Port for which the queue config request is sought.

		Returns:
			number
		"""
		return self._get_attribute('queueConfigPortNumber')
	@QueueConfigPortNumber.setter
	def QueueConfigPortNumber(self, value):
		self._set_attribute('queueConfigPortNumber', value)

	@property
	def QueueConfigResponseTimeOut(self):
		"""Indicates the duration in milliseconds after which the trigger request times out if no queue config response is received.

		Returns:
			number
		"""
		return self._get_attribute('queueConfigResponseTimeOut')
	@QueueConfigResponseTimeOut.setter
	def QueueConfigResponseTimeOut(self, value):
		self._set_attribute('queueConfigResponseTimeOut', value)

	@property
	def QueueId(self):
		"""Indicates the queue ID for which queue statistics is being sought.

		Returns:
			number
		"""
		return self._get_attribute('queueId')
	@QueueId.setter
	def QueueId(self, value):
		self._set_attribute('queueId', value)

	@property
	def QueueIdInputMode(self):
		"""Request queue statistics for the queues belonging to the specified ports.

		Returns:
			str(ofpqAll|custom)
		"""
		return self._get_attribute('queueIdInputMode')
	@QueueIdInputMode.setter
	def QueueIdInputMode(self, value):
		self._set_attribute('queueIdInputMode', value)

	@property
	def QueueStatPortNumber(self):
		"""Specifies the port number for which queue statistics is sought.

		Returns:
			number
		"""
		return self._get_attribute('queueStatPortNumber')
	@QueueStatPortNumber.setter
	def QueueStatPortNumber(self, value):
		self._set_attribute('queueStatPortNumber', value)

	@property
	def QueueStatPortNumberInputMode(self):
		"""Indicates the ports for which queue statistics is sought.

		Returns:
			str(ofppAll|custom)
		"""
		return self._get_attribute('queueStatPortNumberInputMode')
	@QueueStatPortNumberInputMode.setter
	def QueueStatPortNumberInputMode(self, value):
		self._set_attribute('queueStatPortNumberInputMode', value)

	@property
	def QueueStatResponseTimeOut(self):
		"""Indicates the duration in milliseconds after which the trigger request times out if no queue statistics response is received.

		Returns:
			number
		"""
		return self._get_attribute('queueStatResponseTimeOut')
	@QueueStatResponseTimeOut.setter
	def QueueStatResponseTimeOut(self, value):
		self._set_attribute('queueStatResponseTimeOut', value)

	@property
	def RoleRequestGenerationId(self):
		"""The generation ID number.

		Returns:
			str
		"""
		return self._get_attribute('roleRequestGenerationId')
	@RoleRequestGenerationId.setter
	def RoleRequestGenerationId(self, value):
		self._set_attribute('roleRequestGenerationId', value)

	@property
	def RoleRequestType(self):
		"""Select the type of role for the controller.

		Returns:
			str(equal|master|slave|noChange)
		"""
		return self._get_attribute('roleRequestType')
	@RoleRequestType.setter
	def RoleRequestType(self, value):
		self._set_attribute('roleRequestType', value)

	@property
	def SwitchConfigDropFragments(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('switchConfigDropFragments')
	@SwitchConfigDropFragments.setter
	def SwitchConfigDropFragments(self, value):
		self._set_attribute('switchConfigDropFragments', value)

	@property
	def SwitchConfigMissSendLength(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('switchConfigMissSendLength')
	@SwitchConfigMissSendLength.setter
	def SwitchConfigMissSendLength(self, value):
		self._set_attribute('switchConfigMissSendLength', value)

	@property
	def SwitchConfigReassembleFragments(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('switchConfigReassembleFragments')
	@SwitchConfigReassembleFragments.setter
	def SwitchConfigReassembleFragments(self, value):
		self._set_attribute('switchConfigReassembleFragments', value)

	@property
	def SwitchConfigResponseTimeOut(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('switchConfigResponseTimeOut')
	@SwitchConfigResponseTimeOut.setter
	def SwitchConfigResponseTimeOut(self, value):
		self._set_attribute('switchConfigResponseTimeOut', value)

	@property
	def TableFeatureConfig(self):
		"""The bitmap of OFPTC_* values.

		Returns:
			number
		"""
		return self._get_attribute('tableFeatureConfig')
	@TableFeatureConfig.setter
	def TableFeatureConfig(self, value):
		self._set_attribute('tableFeatureConfig', value)

	@property
	def TableFeatureMaxEntries(self):
		"""The maximum number of entries supported.

		Returns:
			number
		"""
		return self._get_attribute('tableFeatureMaxEntries')
	@TableFeatureMaxEntries.setter
	def TableFeatureMaxEntries(self, value):
		self._set_attribute('tableFeatureMaxEntries', value)

	@property
	def TableFeatureMetadataMatch(self):
		"""The bits of metadata which the table can match.

		Returns:
			str
		"""
		return self._get_attribute('tableFeatureMetadataMatch')
	@TableFeatureMetadataMatch.setter
	def TableFeatureMetadataMatch(self, value):
		self._set_attribute('tableFeatureMetadataMatch', value)

	@property
	def TableFeatureMetadataWrite(self):
		"""MetaData Write The bits of metadata which the table can write.

		Returns:
			str
		"""
		return self._get_attribute('tableFeatureMetadataWrite')
	@TableFeatureMetadataWrite.setter
	def TableFeatureMetadataWrite(self, value):
		self._set_attribute('tableFeatureMetadataWrite', value)

	@property
	def TableFeatureName(self):
		"""The table name.

		Returns:
			str
		"""
		return self._get_attribute('tableFeatureName')
	@TableFeatureName.setter
	def TableFeatureName(self, value):
		self._set_attribute('tableFeatureName', value)

	@property
	def TableFeatureResponseTimeOut(self):
		"""The time in milliseconds after which the trigger request times out if no response is received.

		Returns:
			number
		"""
		return self._get_attribute('tableFeatureResponseTimeOut')
	@TableFeatureResponseTimeOut.setter
	def TableFeatureResponseTimeOut(self, value):
		self._set_attribute('tableFeatureResponseTimeOut', value)

	@property
	def TableFeatureTableId(self):
		"""The table identifier.

		Returns:
			number
		"""
		return self._get_attribute('tableFeatureTableId')
	@TableFeatureTableId.setter
	def TableFeatureTableId(self, value):
		self._set_attribute('tableFeatureTableId', value)

	@property
	def TableStatResponseTimeOut(self):
		"""Indicates the duration in milliseconds after which the trigger request times out if no table statistics response is received.

		Returns:
			number
		"""
		return self._get_attribute('tableStatResponseTimeOut')
	@TableStatResponseTimeOut.setter
	def TableStatResponseTimeOut(self, value):
		self._set_attribute('tableStatResponseTimeOut', value)

	@property
	def TriggeredVendorMessage(self):
		"""Indicates the vendor data of the vendor message trigger.

		Returns:
			str
		"""
		return self._get_attribute('triggeredVendorMessage')
	@TriggeredVendorMessage.setter
	def TriggeredVendorMessage(self, value):
		self._set_attribute('triggeredVendorMessage', value)

	@property
	def TriggeredVendorMessageId(self):
		"""Indicates the ID of the vendor for which vendor message is triggered.

		Returns:
			number
		"""
		return self._get_attribute('triggeredVendorMessageId')
	@TriggeredVendorMessageId.setter
	def TriggeredVendorMessageId(self, value):
		self._set_attribute('triggeredVendorMessageId', value)

	@property
	def TriggeredVendorMessageLength(self):
		"""Indicates the length of vendor data of the vendor message trigger.

		Returns:
			number
		"""
		return self._get_attribute('triggeredVendorMessageLength')
	@TriggeredVendorMessageLength.setter
	def TriggeredVendorMessageLength(self, value):
		self._set_attribute('triggeredVendorMessageLength', value)

	@property
	def VendorId(self):
		"""Specifies the unique Vendor identifier.

		Returns:
			number
		"""
		return self._get_attribute('vendorId')
	@VendorId.setter
	def VendorId(self, value):
		self._set_attribute('vendorId', value)

	@property
	def VendorMessage(self):
		"""Speciifes the vendor message value.

		Returns:
			str
		"""
		return self._get_attribute('vendorMessage')
	@VendorMessage.setter
	def VendorMessage(self, value):
		self._set_attribute('vendorMessage', value)

	@property
	def VendorMessageLength(self):
		"""Specifies the length of the message being transmitted.

		Returns:
			number
		"""
		return self._get_attribute('vendorMessageLength')
	@VendorMessageLength.setter
	def VendorMessageLength(self, value):
		self._set_attribute('vendorMessageLength', value)

	@property
	def VendorStateResponseTimeOut(self):
		"""Indicates the duration in milliseconds after which the trigger request times out if no vendor statistics response is received.

		Returns:
			number
		"""
		return self._get_attribute('vendorStateResponseTimeOut')
	@VendorStateResponseTimeOut.setter
	def VendorStateResponseTimeOut(self, value):
		self._set_attribute('vendorStateResponseTimeOut', value)

	def update(self, AsyncConfStatResponseTimeOut=None, DescriptionStatResponseTimeOut=None, EnableAsyncConfMasterFlowRemovedFlowDelete=None, EnableAsyncConfMasterFlowRemovedGroupDelete=None, EnableAsyncConfMasterFlowRemovedHardTimeOut=None, EnableAsyncConfMasterFlowRemovedIdleTimeOut=None, EnableAsyncConfMasterPacketInActionOutputToController=None, EnableAsyncConfMasterPacketInInvalidTtl=None, EnableAsyncConfMasterPacketInNoMatching=None, EnableAsyncConfMasterPortStatusAdd=None, EnableAsyncConfMasterPortStatusDelete=None, EnableAsyncConfMasterPortStatusModify=None, EnableAsyncConfSlaveFlowRemovedFlowDelete=None, EnableAsyncConfSlaveFlowRemovedGroupDelete=None, EnableAsyncConfSlaveFlowRemovedHardTimeOut=None, EnableAsyncConfSlaveFlowRemovedIdleTimeOut=None, EnableAsyncConfSlavePacketInActionOutputToController=None, EnableAsyncConfSlavePacketInInvalidTtl=None, EnableAsyncConfSlavePacketInNoMatching=None, EnableAsyncConfSlavePortStatusAdd=None, EnableAsyncConfSlavePortStatusDelete=None, EnableAsyncConfSlavePortStatusModify=None, EnableFlowAggregatedStatMatchCapability=None, EnableFlowStatMatchCapability=None, EnableGroupStatMatchCapability=None, EnablePortStatMatchCapability=None, EnableQueueStatMatchCapability=None, EnableSendTableFeaturesTrigger=None, EnableSendTriggerPortFeaturesLearnedInformation=None, EnableSendTriggeredAsyncConfStatLearnedInformation=None, EnableSendTriggeredBarrierRequestMessage=None, EnableSendTriggeredDescriptionStatLearnedInformation=None, EnableSendTriggeredFlowAggregatedStatLearnedInformation=None, EnableSendTriggeredFlowStatLearnedInformation=None, EnableSendTriggeredGroupDescriptionStatLearnedInformation=None, EnableSendTriggeredGroupFeatureStatLearnedInformation=None, EnableSendTriggeredGroupStatLearnedInformation=None, EnableSendTriggeredPacketOutMessage=None, EnableSendTriggeredPortModificationMessage=None, EnableSendTriggeredPortStatLearnedInformation=None, EnableSendTriggeredQueueConfigLearnedInformation=None, EnableSendTriggeredQueueStatLearnedInformation=None, EnableSendTriggeredRoleRequestMessage=None, EnableSendTriggeredSwitchConfigLearnedInformation=None, EnableSendTriggeredTableStatLearnedInformation=None, EnableSendTriggeredVendorStatLearnedInformation=None, EnableSetAsyncConfig=None, EnableSetSwitchConfig=None, EnableSetTableFeatures=None, EnableTableStatMatchCapability=None, EnableTriggeredVendorMessage=None, FlowAggregatedStatEthernetDestination=None, FlowAggregatedStatEthernetSource=None, FlowAggregatedStatEthernetType=None, FlowAggregatedStatInPort=None, FlowAggregatedStatIpDscp=None, FlowAggregatedStatIpProtocol=None, FlowAggregatedStatIpv4Destination=None, FlowAggregatedStatIpv4Source=None, FlowAggregatedStatOutPortInputMode=None, FlowAggregatedStatResponseTimeOut=None, FlowAggregatedStatTableIdInputMode=None, FlowAggregatedStatTableIdInputModeNumber=None, FlowAggregatedStatTransportDestination=None, FlowAggregatedStatTransportSource=None, FlowAggregatedStatVlanId=None, FlowAggregatedStatVlanPriority=None, FlowStatEthernetDestination=None, FlowStatEthernetSource=None, FlowStatEthernetType=None, FlowStatInPort=None, FlowStatIpDscp=None, FlowStatIpProtocol=None, FlowStatIpv4Destination=None, FlowStatIpv4Source=None, FlowStatOutPortInputMode=None, FlowStatResponseTimeOut=None, FlowStatTableIdInputMode=None, FlowStatTableIdInputModeNumber=None, FlowStatTransportDestination=None, FlowStatTransportSource=None, FlowStatVlanId=None, FlowStatVlanPriority=None, GroupDescriptionStatResponseTimeOut=None, GroupFeatureStatResponseTimeOut=None, GroupId=None, GroupIdType=None, GroupStatResponseTimeOut=None, PacketOutAuxiliaryId=None, PacketOutBufferId=None, PacketOutBufferIdInputMode=None, PacketOutData=None, PacketOutDataLength=None, PacketOutInPortInputMode=None, PacketOutInPortNumber=None, PortFeaturesResponseTimeOut=None, PortNumber=None, PortNumberInputMode=None, PortStatResponseTimeOut=None, QueueConfigPortNumber=None, QueueConfigResponseTimeOut=None, QueueId=None, QueueIdInputMode=None, QueueStatPortNumber=None, QueueStatPortNumberInputMode=None, QueueStatResponseTimeOut=None, RoleRequestGenerationId=None, RoleRequestType=None, SwitchConfigDropFragments=None, SwitchConfigMissSendLength=None, SwitchConfigReassembleFragments=None, SwitchConfigResponseTimeOut=None, TableFeatureConfig=None, TableFeatureMaxEntries=None, TableFeatureMetadataMatch=None, TableFeatureMetadataWrite=None, TableFeatureName=None, TableFeatureResponseTimeOut=None, TableFeatureTableId=None, TableStatResponseTimeOut=None, TriggeredVendorMessage=None, TriggeredVendorMessageId=None, TriggeredVendorMessageLength=None, VendorId=None, VendorMessage=None, VendorMessageLength=None, VendorStateResponseTimeOut=None):
		"""Updates a child instance of learnedInformation on the server.

		Args:
			AsyncConfStatResponseTimeOut (number): NOT DEFINED
			DescriptionStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no description statistics response is received.
			EnableAsyncConfMasterFlowRemovedFlowDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Flow Removed Flow Delete is received.
			EnableAsyncConfMasterFlowRemovedGroupDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Flow Removed Group Delete is received.
			EnableAsyncConfMasterFlowRemovedHardTimeOut (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Flow Removed Hard Time Out is received.
			EnableAsyncConfMasterFlowRemovedIdleTimeOut (bool): NOT DEFINED
			EnableAsyncConfMasterPacketInActionOutputToController (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Packet In Action Output To Controller is received.
			EnableAsyncConfMasterPacketInInvalidTtl (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Packet In Invalid Ttl is received.
			EnableAsyncConfMasterPacketInNoMatching (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Packet In No Matching is received.
			EnableAsyncConfMasterPortStatusAdd (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Port Status Add is received.
			EnableAsyncConfMasterPortStatusDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Master Port Status Delete is received.
			EnableAsyncConfMasterPortStatusModify (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Delete is received.
			EnableAsyncConfSlaveFlowRemovedFlowDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Flow Delete is received.
			EnableAsyncConfSlaveFlowRemovedGroupDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Group Delete is received.
			EnableAsyncConfSlaveFlowRemovedHardTimeOut (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Hard Time Out is received.
			EnableAsyncConfSlaveFlowRemovedIdleTimeOut (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Flow Removed Idle Time Out is received.
			EnableAsyncConfSlavePacketInActionOutputToController (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Packet In Action Output To Controller is received.
			EnableAsyncConfSlavePacketInInvalidTtl (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Packet In Invalid Ttl is received.
			EnableAsyncConfSlavePacketInNoMatching (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Packet In No Matching is received.
			EnableAsyncConfSlavePortStatusAdd (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Add is received.
			EnableAsyncConfSlavePortStatusDelete (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Delete is received.
			EnableAsyncConfSlavePortStatusModify (bool): If enabled,it denotes that the enable Asynchronous Configuration Slave Port Status Modify is received.
			EnableFlowAggregatedStatMatchCapability (bool): Checks to see if the switch has the capability to publish Flow Aggregated Statistics
			EnableFlowStatMatchCapability (bool): Checks to see if the switch has the capability to publish Flow Statistics
			EnableGroupStatMatchCapability (bool): If enabled,it denotes that the enable Group Statistics Match Capability is received.
			EnablePortStatMatchCapability (bool): Checks to see if the switch has the capability to publish Port Statistics
			EnableQueueStatMatchCapability (bool): If true, the switch has the capability to publish Queue Statistics.
			EnableSendTableFeaturesTrigger (bool): If enabled,it denotes that the enable Send Table Features Trigger is received.
			EnableSendTriggerPortFeaturesLearnedInformation (bool): Enables Trigger for port features learned information.
			EnableSendTriggeredAsyncConfStatLearnedInformation (bool): If enabled,it denotes that the Triggered Asynchronous Configuration Statistics Learned Information is received.
			EnableSendTriggeredBarrierRequestMessage (bool): If true, enables trigger for barrier request message
			EnableSendTriggeredDescriptionStatLearnedInformation (bool): If true, the description statistic trigger configuration parameters are available.
			EnableSendTriggeredFlowAggregatedStatLearnedInformation (bool): If true, the flow aggregated statistic trigger configuration parameters are available.
			EnableSendTriggeredFlowStatLearnedInformation (bool): If true, the flow statistic trigger configuration parameters are available.
			EnableSendTriggeredGroupDescriptionStatLearnedInformation (bool): If enabled,it denotes that the enable Send Triggered Group Description Statistics Learned Information is received.
			EnableSendTriggeredGroupFeatureStatLearnedInformation (bool): If enabled,it denotes that the enable Send Triggered Group Feature Statistics Learned Information is received.
			EnableSendTriggeredGroupStatLearnedInformation (bool): If enabled,it denotes that the Send Triggered Group Statistics Learned Information is received.
			EnableSendTriggeredPacketOutMessage (bool): If enabled,it denotes that the enable Send Triggered Packet Out Message is received.
			EnableSendTriggeredPortModificationMessage (bool): If enabled,it denotes that the enable Send Triggered Port Modification Message is received.
			EnableSendTriggeredPortStatLearnedInformation (bool): If true, the port statistic trigger configuration parameters are available.
			EnableSendTriggeredQueueConfigLearnedInformation (bool): If true, the queue config trigger configuration parameters are available.
			EnableSendTriggeredQueueStatLearnedInformation (bool): If true, the queue statistic trigger configuration parameters are available.
			EnableSendTriggeredRoleRequestMessage (bool): If enabled,it denotes that the Triggered Role Request Message is received.
			EnableSendTriggeredSwitchConfigLearnedInformation (bool): If enabled,it denotes that the enable Switch Configuration Learned Information is received.
			EnableSendTriggeredTableStatLearnedInformation (bool): If true, the table statistic trigger configuration parameters are available.
			EnableSendTriggeredVendorStatLearnedInformation (bool): If true, the vendor statistic trigger configuration parameters are available.
			EnableSetAsyncConfig (bool): If enabled,it denotes that the Set Asynchronous Configuration is received.
			EnableSetSwitchConfig (bool): If enabled,it denotes that the enable Set Switch Configuration is received.
			EnableSetTableFeatures (bool): NOT DEFINED
			EnableTableStatMatchCapability (bool): If true, the switch has the capability to publish Table Statistics.
			EnableTriggeredVendorMessage (bool): If true, the vendor message trigger configuration parameters are available.
			FlowAggregatedStatEthernetDestination (str): Signifies the ethernet destination address.
			FlowAggregatedStatEthernetSource (str): Signifies the ethernet source address.
			FlowAggregatedStatEthernetType (str): Signifies the type of Ethernet used.
			FlowAggregatedStatInPort (str): Signifies the input port used.
			FlowAggregatedStatIpDscp (str): Signifies the IP DSCP value for advertising.
			FlowAggregatedStatIpProtocol (str): Signifies the IP protocol used.
			FlowAggregatedStatIpv4Destination (str): Signifies the IPv4 destination address.
			FlowAggregatedStatIpv4Source (str): Signifies the IPv4 source address.
			FlowAggregatedStatOutPortInputMode (str(ofppInPort|ofppNormal|ofppFlood|ofppAll|ofppController|ofppLocal|ofppNone|custom)): Signifies the identifier output mode of the aggregated flow statistics table.
			FlowAggregatedStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no flow aggregated statistics response is received.
			FlowAggregatedStatTableIdInputMode (str(allTables|emergency|custom)): Signifies the identifier input mode of the flow aggregated statistics table.
			FlowAggregatedStatTableIdInputModeNumber (number): Signifies the identifier input mode of the flow aggregated statistics table.
			FlowAggregatedStatTransportDestination (str): Signifies the Transport destination address.
			FlowAggregatedStatTransportSource (str): Signifies the Transport source address.
			FlowAggregatedStatVlanId (str): Signifies the unique VLAN Identifier.
			FlowAggregatedStatVlanPriority (str): Signifies the User Priority for this VLAN.
			FlowStatEthernetDestination (str): Specifies the Ethernet destination address.
			FlowStatEthernetSource (str): Specifies the Ethernet source address.
			FlowStatEthernetType (str): Specifies the type of Ethernet used.
			FlowStatInPort (str): Specifies the input port used.
			FlowStatIpDscp (str): Specifies the IP DSCP value for advertising.
			FlowStatIpProtocol (str): Specifies the IP protocol used.
			FlowStatIpv4Destination (str): Specifies the The IPv4 destination address.
			FlowStatIpv4Source (str): Specifies the The IPv4 source address.
			FlowStatOutPortInputMode (str(ofppInPort|ofppNormal|ofppFlood|ofppAll|ofppController|ofppLocal|ofppNone|custom)): Specifies the output mode of the Table identifier.
			FlowStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no response is received.
			FlowStatTableIdInputMode (str(allTables|emergency|custom)): Specifies the input mode of the Table identifier.
			FlowStatTableIdInputModeNumber (number): Signifies the identifier input mode of the flow statistics table.
			FlowStatTransportDestination (str): Specifies the Transport destination address.
			FlowStatTransportSource (str): Specifies the Transport source address.
			FlowStatVlanId (str): Specifies the unique VLAN Identifier.
			FlowStatVlanPriority (str): Specifies the User Priority for this VLAN.
			GroupDescriptionStatResponseTimeOut (number): NOT DEFINED
			GroupFeatureStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out if no response is received.
			GroupId (number): The ID of the group used. .
			GroupIdType (str(ofpgAll|ofpgAny|manual)): NOT DEFINED
			GroupStatResponseTimeOut (number): The time in milliseconds after which the trigger request times out if no response is received.
			PacketOutAuxiliaryId (number): NOT DEFINED
			PacketOutBufferId (number): NOT DEFINED
			PacketOutBufferIdInputMode (str(opfNoBuffer|manual)): NOT DEFINED
			PacketOutData (str): NOT DEFINED
			PacketOutDataLength (number): NOT DEFINED
			PacketOutInPortInputMode (str(ofppController|ofppLocal|manual)): NOT DEFINED
			PacketOutInPortNumber (number): NOT DEFINED
			PortFeaturesResponseTimeOut (number): The time in milliseconds after which the trigger request times out if no response is received.
			PortNumber (number): Specifies the port number.
			PortNumberInputMode (str(ofppNone|custom)): Specifies the input mode for the Port number.
			PortStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no port statistics response is received.
			QueueConfigPortNumber (number): Indicates the Port for which the queue config request is sought.
			QueueConfigResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no queue config response is received.
			QueueId (number): Indicates the queue ID for which queue statistics is being sought.
			QueueIdInputMode (str(ofpqAll|custom)): Request queue statistics for the queues belonging to the specified ports.
			QueueStatPortNumber (number): Specifies the port number for which queue statistics is sought.
			QueueStatPortNumberInputMode (str(ofppAll|custom)): Indicates the ports for which queue statistics is sought.
			QueueStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no queue statistics response is received.
			RoleRequestGenerationId (str): The generation ID number.
			RoleRequestType (str(equal|master|slave|noChange)): Select the type of role for the controller.
			SwitchConfigDropFragments (bool): NOT DEFINED
			SwitchConfigMissSendLength (number): NOT DEFINED
			SwitchConfigReassembleFragments (bool): NOT DEFINED
			SwitchConfigResponseTimeOut (number): NOT DEFINED
			TableFeatureConfig (number): The bitmap of OFPTC_* values.
			TableFeatureMaxEntries (number): The maximum number of entries supported.
			TableFeatureMetadataMatch (str): The bits of metadata which the table can match.
			TableFeatureMetadataWrite (str): MetaData Write The bits of metadata which the table can write.
			TableFeatureName (str): The table name.
			TableFeatureResponseTimeOut (number): The time in milliseconds after which the trigger request times out if no response is received.
			TableFeatureTableId (number): The table identifier.
			TableStatResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no table statistics response is received.
			TriggeredVendorMessage (str): Indicates the vendor data of the vendor message trigger.
			TriggeredVendorMessageId (number): Indicates the ID of the vendor for which vendor message is triggered.
			TriggeredVendorMessageLength (number): Indicates the length of vendor data of the vendor message trigger.
			VendorId (number): Specifies the unique Vendor identifier.
			VendorMessage (str): Speciifes the vendor message value.
			VendorMessageLength (number): Specifies the length of the message being transmitted.
			VendorStateResponseTimeOut (number): Indicates the duration in milliseconds after which the trigger request times out if no vendor statistics response is received.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def ClearRecordsForTrigger(self):
		"""Executes the clearRecordsForTrigger operation on the server.

		This describes the record cleared for trigger settings.

			Returns:
				bool: NOT DEFINED

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('clearRecordsForTrigger', payload=payload, response_object=None)

	def RefreshLearnedInformation(self):
		"""Executes the refreshLearnedInformation operation on the server.

		This describes the learned information is refreshed.

			Returns:
				bool: NOT DEFINED

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('refreshLearnedInformation', payload=payload, response_object=None)

	def Trigger(self):
		"""Executes the trigger operation on the server.

		This describes the learned info trigger settings.

			Returns:
				number: NOT DEFINED

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('trigger', payload=payload, response_object=None)
