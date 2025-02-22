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
	"""This object displays the information learned from each router.
	The LearnedInformation class encapsulates a list of learnedInformation resources that is managed by the system.
	A list of resources can be retrieved from the server using the LearnedInformation.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'learnedInformation'

	def __init__(self, parent):
		super(LearnedInformation, self).__init__(parent)

	@property
	def GeneralLearnedInfo(self):
		"""An instance of the GeneralLearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.generallearnedinfo_glvbi9nzw5lcmfstgvhcm5lzeluzm8.GeneralLearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.generallearnedinfo_glvbi9nzw5lcmfstgvhcm5lzeluzm8 import GeneralLearnedInfo
		return GeneralLearnedInfo(self)

	@property
	def TriggeredPingLearnedInfo(self):
		"""An instance of the TriggeredPingLearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.triggeredpinglearnedinfo_mlnz2vyzwrqaw5ntgvhcm5lzeluzm8.TriggeredPingLearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.triggeredpinglearnedinfo_mlnz2vyzwrqaw5ntgvhcm5lzeluzm8 import TriggeredPingLearnedInfo
		return TriggeredPingLearnedInfo(self)

	@property
	def TriggeredTracerouteLearnedInfo(self):
		"""An instance of the TriggeredTracerouteLearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.triggeredtraceroutelearnedinfo_wrucmfjzxjvdxrltgvhcm5lzeluzm8.TriggeredTracerouteLearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.triggeredtraceroutelearnedinfo_wrucmfjzxjvdxrltgvhcm5lzeluzm8 import TriggeredTracerouteLearnedInfo
		return TriggeredTracerouteLearnedInfo(self)

	@property
	def DestinationAddressIpv4(self):
		"""This signifies the destination IPv4 address.

		Returns:
			str
		"""
		return self._get_attribute('destinationAddressIpv4')
	@DestinationAddressIpv4.setter
	def DestinationAddressIpv4(self, value):
		self._set_attribute('destinationAddressIpv4', value)

	@property
	def DownstreamAddressType(self):
		"""This signifies the address type of the downstream traffic. Possible values include Ipv4Numbered and Ipv4UnNumbered.

		Returns:
			str(ipv4Numbered|ipv4UnNumbered)
		"""
		return self._get_attribute('downstreamAddressType')
	@DownstreamAddressType.setter
	def DownstreamAddressType(self, value):
		self._set_attribute('downstreamAddressType', value)

	@property
	def DownstreamInterfaceAddress(self):
		"""This signifies the interface address of the downstream LSR.

		Returns:
			str
		"""
		return self._get_attribute('downstreamInterfaceAddress')
	@DownstreamInterfaceAddress.setter
	def DownstreamInterfaceAddress(self, value):
		self._set_attribute('downstreamInterfaceAddress', value)

	@property
	def DownstreamIpAddress(self):
		"""This signifies the IPv4/IPv6 address of the downstream LSR.

		Returns:
			str
		"""
		return self._get_attribute('downstreamIpAddress')
	@DownstreamIpAddress.setter
	def DownstreamIpAddress(self, value):
		self._set_attribute('downstreamIpAddress', value)

	@property
	def EchoResponseTimeoutMs(self):
		"""This signifies the minimum tiomeout interval, in milliseconds, between received Echo packets that this interface is capable of supporting.

		Returns:
			number
		"""
		return self._get_attribute('echoResponseTimeoutMs')
	@EchoResponseTimeoutMs.setter
	def EchoResponseTimeoutMs(self, value):
		self._set_attribute('echoResponseTimeoutMs', value)

	@property
	def EnableAdvance(self):
		"""This signifies the enablement of advance.

		Returns:
			bool
		"""
		return self._get_attribute('enableAdvance')
	@EnableAdvance.setter
	def EnableAdvance(self, value):
		self._set_attribute('enableAdvance', value)

	@property
	def EnableDsiFlag(self):
		"""This signifies the activation of the DS I Flag.

		Returns:
			bool
		"""
		return self._get_attribute('enableDsiFlag')
	@EnableDsiFlag.setter
	def EnableDsiFlag(self, value):
		self._set_attribute('enableDsiFlag', value)

	@property
	def EnableDsnFlag(self):
		"""This signifies the activation of the DN S Flag.

		Returns:
			bool
		"""
		return self._get_attribute('enableDsnFlag')
	@EnableDsnFlag.setter
	def EnableDsnFlag(self, value):
		self._set_attribute('enableDsnFlag', value)

	@property
	def EnableFecValidation(self):
		"""This signifies the selection of the check box to enable FEC validation.

		Returns:
			bool
		"""
		return self._get_attribute('enableFecValidation')
	@EnableFecValidation.setter
	def EnableFecValidation(self, value):
		self._set_attribute('enableFecValidation', value)

	@property
	def EnableIncludeDownstreamMappingTlv(self):
		"""This signifies the inclusion of the downstream mapping TLV in triggered Trace Route.

		Returns:
			bool
		"""
		return self._get_attribute('enableIncludeDownstreamMappingTlv')
	@EnableIncludeDownstreamMappingTlv.setter
	def EnableIncludeDownstreamMappingTlv(self, value):
		self._set_attribute('enableIncludeDownstreamMappingTlv', value)

	@property
	def EnableIncludePadTlv(self):
		"""This signifies the selection of the check box to include Pad TLV.

		Returns:
			bool
		"""
		return self._get_attribute('enableIncludePadTlv')
	@EnableIncludePadTlv.setter
	def EnableIncludePadTlv(self, value):
		self._set_attribute('enableIncludePadTlv', value)

	@property
	def EnableIncludeVendorEnterpriseNumberTlv(self):
		"""This signifies the selection of the checkbox to include the the TLV number of the vendor organization.

		Returns:
			bool
		"""
		return self._get_attribute('enableIncludeVendorEnterpriseNumberTlv')
	@EnableIncludeVendorEnterpriseNumberTlv.setter
	def EnableIncludeVendorEnterpriseNumberTlv(self, value):
		self._set_attribute('enableIncludeVendorEnterpriseNumberTlv', value)

	@property
	def EnablePauseResumeBfdPduTrigger(self):
		"""This signifies the pausing of the BFD PDU trigger.

		Returns:
			bool
		"""
		return self._get_attribute('enablePauseResumeBfdPduTrigger')
	@EnablePauseResumeBfdPduTrigger.setter
	def EnablePauseResumeBfdPduTrigger(self, value):
		self._set_attribute('enablePauseResumeBfdPduTrigger', value)

	@property
	def EnablePauseResumeReplyTrigger(self):
		"""This signifies the pausing of the reply trigger.

		Returns:
			bool
		"""
		return self._get_attribute('enablePauseResumeReplyTrigger')
	@EnablePauseResumeReplyTrigger.setter
	def EnablePauseResumeReplyTrigger(self, value):
		self._set_attribute('enablePauseResumeReplyTrigger', value)

	@property
	def EnableSendTriggeredPing(self):
		"""This signifies the sending of the triggered ping.

		Returns:
			bool
		"""
		return self._get_attribute('enableSendTriggeredPing')
	@EnableSendTriggeredPing.setter
	def EnableSendTriggeredPing(self, value):
		self._set_attribute('enableSendTriggeredPing', value)

	@property
	def EnableSendTriggeredTraceroute(self):
		"""This signifies the enablement of the sending of triggered trace route.

		Returns:
			bool
		"""
		return self._get_attribute('enableSendTriggeredTraceroute')
	@EnableSendTriggeredTraceroute.setter
	def EnableSendTriggeredTraceroute(self, value):
		self._set_attribute('enableSendTriggeredTraceroute', value)

	@property
	def EnableSetResetEchoReplyCodeTrigger(self):
		"""This signifies the setting of the echo reply code trigger.

		Returns:
			bool
		"""
		return self._get_attribute('enableSetResetEchoReplyCodeTrigger')
	@EnableSetResetEchoReplyCodeTrigger.setter
	def EnableSetResetEchoReplyCodeTrigger(self, value):
		self._set_attribute('enableSetResetEchoReplyCodeTrigger', value)

	@property
	def IsGeneralLearnedInformationRefreshed(self):
		"""This signifies the refreshing of the general learned information.

		Returns:
			bool
		"""
		return self._get_attribute('isGeneralLearnedInformationRefreshed')

	@property
	def IsTriggeredPingLearnedInformationRefreshed(self):
		"""This signifies the checking of if the Triggered ping learned information is refreshed.

		Returns:
			bool
		"""
		return self._get_attribute('isTriggeredPingLearnedInformationRefreshed')

	@property
	def IsTriggeredTraceRouteLearnedInformationRefreshed(self):
		"""This signifies the checking of if the Triggered Trace route information is refreshed.

		Returns:
			bool
		"""
		return self._get_attribute('isTriggeredTraceRouteLearnedInformationRefreshed')

	@property
	def PadTlvFirstOctetOptions(self):
		"""This signifies the first octate of Pad TLV in triggered ping. Possible values include CopyPadTlvToReply and DropPadTlvFromReply.

		Returns:
			str(dropPadTlvFromReply|copyPadTlvToReply)
		"""
		return self._get_attribute('padTlvFirstOctetOptions')
	@PadTlvFirstOctetOptions.setter
	def PadTlvFirstOctetOptions(self, value):
		self._set_attribute('padTlvFirstOctetOptions', value)

	@property
	def PadTlvLength(self):
		"""This signifies the specification of the length of the Pad TLV.

		Returns:
			number
		"""
		return self._get_attribute('padTlvLength')
	@PadTlvLength.setter
	def PadTlvLength(self, value):
		self._set_attribute('padTlvLength', value)

	@property
	def PauseResumeBfdPduTriggerOption(self):
		"""This signifies the pausing of the BFD PDU trigger option.Possible values include Pause and Resume.

		Returns:
			str(pause|resume)
		"""
		return self._get_attribute('pauseResumeBfdPduTriggerOption')
	@PauseResumeBfdPduTriggerOption.setter
	def PauseResumeBfdPduTriggerOption(self, value):
		self._set_attribute('pauseResumeBfdPduTriggerOption', value)

	@property
	def PauseResumeReplyTriggerOption(self):
		"""This signifies the pausing of the reply trigger option. Possible values include Pause and Resume.

		Returns:
			str(pause|resume)
		"""
		return self._get_attribute('pauseResumeReplyTriggerOption')
	@PauseResumeReplyTriggerOption.setter
	def PauseResumeReplyTriggerOption(self, value):
		self._set_attribute('pauseResumeReplyTriggerOption', value)

	@property
	def ReplyMode(self):
		"""This signifies the selection of the mode of reply. Possible values include:

		Returns:
			str(doNotReply|replyViaIpv4Ipv6UdpPacket|replyViaIpv4Ipv6UdpPacketWithRouterAlert|replyViaApplicationLevelControlChannel)
		"""
		return self._get_attribute('replyMode')
	@ReplyMode.setter
	def ReplyMode(self, value):
		self._set_attribute('replyMode', value)

	@property
	def ReturnCodeOption(self):
		"""This signifies the return code option value. Possible values include:

		Returns:
			str(noReturnCode|malformedEchoRequestReceived|oneOrMoreOfTheTlvsWasNotUnderstood|replyingRouterIsAnEgressForTheFecAtStackDepthRsc|replyingRouterHasNoMappingForTheFecAtStackDepthRsc|downstreamMappingMismatch|upstreamInterfaceIndexUnknown|lspPingReserved|labelSwitchedAtStackDepthRsc|labelSwitchedButNoMplsForwardingAtStackDepthRsc|mappingForThisFecIsNotTheGivenLabelAtStackDepthRsc|noLabelEntryAtStackDepthRsc|protocolNotAssociatedWithInterfaceatFecStackDepthRsc|prematureTerminationOfPingDueToLabelStackShrinkingToSingleLabel)
		"""
		return self._get_attribute('returnCodeOption')
	@ReturnCodeOption.setter
	def ReturnCodeOption(self, value):
		self._set_attribute('returnCodeOption', value)

	@property
	def ReturnSubCode(self):
		"""This signifies the return subcode value.

		Returns:
			number
		"""
		return self._get_attribute('returnSubCode')
	@ReturnSubCode.setter
	def ReturnSubCode(self, value):
		self._set_attribute('returnSubCode', value)

	@property
	def TriggerOptions(self):
		"""This signifies the trigger option value. Possible values include:

		Returns:
			str(tx|rx|txRx)
		"""
		return self._get_attribute('triggerOptions')
	@TriggerOptions.setter
	def TriggerOptions(self, value):
		self._set_attribute('triggerOptions', value)

	@property
	def TriggerType(self):
		"""This signifies the type of the trigger. Possible values include:

		Returns:
			str(resetToNormalReply|forceReplyCode)
		"""
		return self._get_attribute('triggerType')
	@TriggerType.setter
	def TriggerType(self, value):
		self._set_attribute('triggerType', value)

	@property
	def TtlLimit(self):
		"""This signifies the maximum value of TTL up to which the TTL will be incremented while sending echo request packets.

		Returns:
			number
		"""
		return self._get_attribute('ttlLimit')
	@TtlLimit.setter
	def TtlLimit(self, value):
		self._set_attribute('ttlLimit', value)

	@property
	def VendorEnterpriseNumber(self):
		"""This signifies the specification of the enterprise number of the vendor.

		Returns:
			number
		"""
		return self._get_attribute('vendorEnterpriseNumber')
	@VendorEnterpriseNumber.setter
	def VendorEnterpriseNumber(self, value):
		self._set_attribute('vendorEnterpriseNumber', value)

	def update(self, DestinationAddressIpv4=None, DownstreamAddressType=None, DownstreamInterfaceAddress=None, DownstreamIpAddress=None, EchoResponseTimeoutMs=None, EnableAdvance=None, EnableDsiFlag=None, EnableDsnFlag=None, EnableFecValidation=None, EnableIncludeDownstreamMappingTlv=None, EnableIncludePadTlv=None, EnableIncludeVendorEnterpriseNumberTlv=None, EnablePauseResumeBfdPduTrigger=None, EnablePauseResumeReplyTrigger=None, EnableSendTriggeredPing=None, EnableSendTriggeredTraceroute=None, EnableSetResetEchoReplyCodeTrigger=None, PadTlvFirstOctetOptions=None, PadTlvLength=None, PauseResumeBfdPduTriggerOption=None, PauseResumeReplyTriggerOption=None, ReplyMode=None, ReturnCodeOption=None, ReturnSubCode=None, TriggerOptions=None, TriggerType=None, TtlLimit=None, VendorEnterpriseNumber=None):
		"""Updates a child instance of learnedInformation on the server.

		Args:
			DestinationAddressIpv4 (str): This signifies the destination IPv4 address.
			DownstreamAddressType (str(ipv4Numbered|ipv4UnNumbered)): This signifies the address type of the downstream traffic. Possible values include Ipv4Numbered and Ipv4UnNumbered.
			DownstreamInterfaceAddress (str): This signifies the interface address of the downstream LSR.
			DownstreamIpAddress (str): This signifies the IPv4/IPv6 address of the downstream LSR.
			EchoResponseTimeoutMs (number): This signifies the minimum tiomeout interval, in milliseconds, between received Echo packets that this interface is capable of supporting.
			EnableAdvance (bool): This signifies the enablement of advance.
			EnableDsiFlag (bool): This signifies the activation of the DS I Flag.
			EnableDsnFlag (bool): This signifies the activation of the DN S Flag.
			EnableFecValidation (bool): This signifies the selection of the check box to enable FEC validation.
			EnableIncludeDownstreamMappingTlv (bool): This signifies the inclusion of the downstream mapping TLV in triggered Trace Route.
			EnableIncludePadTlv (bool): This signifies the selection of the check box to include Pad TLV.
			EnableIncludeVendorEnterpriseNumberTlv (bool): This signifies the selection of the checkbox to include the the TLV number of the vendor organization.
			EnablePauseResumeBfdPduTrigger (bool): This signifies the pausing of the BFD PDU trigger.
			EnablePauseResumeReplyTrigger (bool): This signifies the pausing of the reply trigger.
			EnableSendTriggeredPing (bool): This signifies the sending of the triggered ping.
			EnableSendTriggeredTraceroute (bool): This signifies the enablement of the sending of triggered trace route.
			EnableSetResetEchoReplyCodeTrigger (bool): This signifies the setting of the echo reply code trigger.
			PadTlvFirstOctetOptions (str(dropPadTlvFromReply|copyPadTlvToReply)): This signifies the first octate of Pad TLV in triggered ping. Possible values include CopyPadTlvToReply and DropPadTlvFromReply.
			PadTlvLength (number): This signifies the specification of the length of the Pad TLV.
			PauseResumeBfdPduTriggerOption (str(pause|resume)): This signifies the pausing of the BFD PDU trigger option.Possible values include Pause and Resume.
			PauseResumeReplyTriggerOption (str(pause|resume)): This signifies the pausing of the reply trigger option. Possible values include Pause and Resume.
			ReplyMode (str(doNotReply|replyViaIpv4Ipv6UdpPacket|replyViaIpv4Ipv6UdpPacketWithRouterAlert|replyViaApplicationLevelControlChannel)): This signifies the selection of the mode of reply. Possible values include:
			ReturnCodeOption (str(noReturnCode|malformedEchoRequestReceived|oneOrMoreOfTheTlvsWasNotUnderstood|replyingRouterIsAnEgressForTheFecAtStackDepthRsc|replyingRouterHasNoMappingForTheFecAtStackDepthRsc|downstreamMappingMismatch|upstreamInterfaceIndexUnknown|lspPingReserved|labelSwitchedAtStackDepthRsc|labelSwitchedButNoMplsForwardingAtStackDepthRsc|mappingForThisFecIsNotTheGivenLabelAtStackDepthRsc|noLabelEntryAtStackDepthRsc|protocolNotAssociatedWithInterfaceatFecStackDepthRsc|prematureTerminationOfPingDueToLabelStackShrinkingToSingleLabel)): This signifies the return code option value. Possible values include:
			ReturnSubCode (number): This signifies the return subcode value.
			TriggerOptions (str(tx|rx|txRx)): This signifies the trigger option value. Possible values include:
			TriggerType (str(resetToNormalReply|forceReplyCode)): This signifies the type of the trigger. Possible values include:
			TtlLimit (number): This signifies the maximum value of TTL up to which the TTL will be incremented while sending echo request packets.
			VendorEnterpriseNumber (number): This signifies the specification of the enterprise number of the vendor.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def find(self, DestinationAddressIpv4=None, DownstreamAddressType=None, DownstreamInterfaceAddress=None, DownstreamIpAddress=None, EchoResponseTimeoutMs=None, EnableAdvance=None, EnableDsiFlag=None, EnableDsnFlag=None, EnableFecValidation=None, EnableIncludeDownstreamMappingTlv=None, EnableIncludePadTlv=None, EnableIncludeVendorEnterpriseNumberTlv=None, EnablePauseResumeBfdPduTrigger=None, EnablePauseResumeReplyTrigger=None, EnableSendTriggeredPing=None, EnableSendTriggeredTraceroute=None, EnableSetResetEchoReplyCodeTrigger=None, IsGeneralLearnedInformationRefreshed=None, IsTriggeredPingLearnedInformationRefreshed=None, IsTriggeredTraceRouteLearnedInformationRefreshed=None, PadTlvFirstOctetOptions=None, PadTlvLength=None, PauseResumeBfdPduTriggerOption=None, PauseResumeReplyTriggerOption=None, ReplyMode=None, ReturnCodeOption=None, ReturnSubCode=None, TriggerOptions=None, TriggerType=None, TtlLimit=None, VendorEnterpriseNumber=None):
		"""Finds and retrieves learnedInformation data from the server.

		All named parameters support regex and can be used to selectively retrieve learnedInformation data from the server.
		By default the find method takes no parameters and will retrieve all learnedInformation data from the server.

		Args:
			DestinationAddressIpv4 (str): This signifies the destination IPv4 address.
			DownstreamAddressType (str(ipv4Numbered|ipv4UnNumbered)): This signifies the address type of the downstream traffic. Possible values include Ipv4Numbered and Ipv4UnNumbered.
			DownstreamInterfaceAddress (str): This signifies the interface address of the downstream LSR.
			DownstreamIpAddress (str): This signifies the IPv4/IPv6 address of the downstream LSR.
			EchoResponseTimeoutMs (number): This signifies the minimum tiomeout interval, in milliseconds, between received Echo packets that this interface is capable of supporting.
			EnableAdvance (bool): This signifies the enablement of advance.
			EnableDsiFlag (bool): This signifies the activation of the DS I Flag.
			EnableDsnFlag (bool): This signifies the activation of the DN S Flag.
			EnableFecValidation (bool): This signifies the selection of the check box to enable FEC validation.
			EnableIncludeDownstreamMappingTlv (bool): This signifies the inclusion of the downstream mapping TLV in triggered Trace Route.
			EnableIncludePadTlv (bool): This signifies the selection of the check box to include Pad TLV.
			EnableIncludeVendorEnterpriseNumberTlv (bool): This signifies the selection of the checkbox to include the the TLV number of the vendor organization.
			EnablePauseResumeBfdPduTrigger (bool): This signifies the pausing of the BFD PDU trigger.
			EnablePauseResumeReplyTrigger (bool): This signifies the pausing of the reply trigger.
			EnableSendTriggeredPing (bool): This signifies the sending of the triggered ping.
			EnableSendTriggeredTraceroute (bool): This signifies the enablement of the sending of triggered trace route.
			EnableSetResetEchoReplyCodeTrigger (bool): This signifies the setting of the echo reply code trigger.
			IsGeneralLearnedInformationRefreshed (bool): This signifies the refreshing of the general learned information.
			IsTriggeredPingLearnedInformationRefreshed (bool): This signifies the checking of if the Triggered ping learned information is refreshed.
			IsTriggeredTraceRouteLearnedInformationRefreshed (bool): This signifies the checking of if the Triggered Trace route information is refreshed.
			PadTlvFirstOctetOptions (str(dropPadTlvFromReply|copyPadTlvToReply)): This signifies the first octate of Pad TLV in triggered ping. Possible values include CopyPadTlvToReply and DropPadTlvFromReply.
			PadTlvLength (number): This signifies the specification of the length of the Pad TLV.
			PauseResumeBfdPduTriggerOption (str(pause|resume)): This signifies the pausing of the BFD PDU trigger option.Possible values include Pause and Resume.
			PauseResumeReplyTriggerOption (str(pause|resume)): This signifies the pausing of the reply trigger option. Possible values include Pause and Resume.
			ReplyMode (str(doNotReply|replyViaIpv4Ipv6UdpPacket|replyViaIpv4Ipv6UdpPacketWithRouterAlert|replyViaApplicationLevelControlChannel)): This signifies the selection of the mode of reply. Possible values include:
			ReturnCodeOption (str(noReturnCode|malformedEchoRequestReceived|oneOrMoreOfTheTlvsWasNotUnderstood|replyingRouterIsAnEgressForTheFecAtStackDepthRsc|replyingRouterHasNoMappingForTheFecAtStackDepthRsc|downstreamMappingMismatch|upstreamInterfaceIndexUnknown|lspPingReserved|labelSwitchedAtStackDepthRsc|labelSwitchedButNoMplsForwardingAtStackDepthRsc|mappingForThisFecIsNotTheGivenLabelAtStackDepthRsc|noLabelEntryAtStackDepthRsc|protocolNotAssociatedWithInterfaceatFecStackDepthRsc|prematureTerminationOfPingDueToLabelStackShrinkingToSingleLabel)): This signifies the return code option value. Possible values include:
			ReturnSubCode (number): This signifies the return subcode value.
			TriggerOptions (str(tx|rx|txRx)): This signifies the trigger option value. Possible values include:
			TriggerType (str(resetToNormalReply|forceReplyCode)): This signifies the type of the trigger. Possible values include:
			TtlLimit (number): This signifies the maximum value of TTL up to which the TTL will be incremented while sending echo request packets.
			VendorEnterpriseNumber (number): This signifies the specification of the enterprise number of the vendor.

		Returns:
			self: This instance with matching learnedInformation data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of learnedInformation data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the learnedInformation data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def ClearRecordsForTrigger(self):
		"""Executes the clearRecordsForTrigger operation on the server.

		This signifies the record cleared for trigger settings.

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

		This signifies that the learned information is refreshed.

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

		This signifies the learned info trigger settings.

			Returns:
				number: NOT DEFINED

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('trigger', payload=payload, response_object=None)
