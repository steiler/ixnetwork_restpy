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


class Uni(Base):
	"""It signifies the user network interface.
	The Uni class encapsulates a list of uni resources that is be managed by the user.
	A list of resources can be retrieved from the server using the Uni.find() method.
	The list can be managed by the user by using the Uni.add() and Uni.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'uni'

	def __init__(self, parent):
		super(Uni, self).__init__(parent)

	@property
	def Evc(self):
		"""An instance of the Evc class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evc_3byb3rvy29scy9lbg1pl3vuas9ldmm.Evc)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evc_3byb3rvy29scy9lbg1pl3vuas9ldmm import Evc
		return Evc(self)

	@property
	def EvcStatusLearnedInfo(self):
		"""An instance of the EvcStatusLearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evcstatuslearnedinfo_as9ldmntdgf0dxnmzwfybmvksw5mbw.EvcStatusLearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.evcstatuslearnedinfo_as9ldmntdgf0dxnmzwfybmvksw5mbw import EvcStatusLearnedInfo
		return EvcStatusLearnedInfo(self)

	@property
	def LmiStatusLearnedInfo(self):
		"""An instance of the LmiStatusLearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lmistatuslearnedinfo_as9sbwltdgf0dxnmzwfybmvksw5mbw.LmiStatusLearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lmistatuslearnedinfo_as9sbwltdgf0dxnmzwfybmvksw5mbw import LmiStatusLearnedInfo
		return LmiStatusLearnedInfo(self)

	@property
	def UniStatus(self):
		"""An instance of the UniStatus class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.unistatus_29scy9lbg1pl3vuas91bmltdgf0dxm.UniStatus)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.unistatus_29scy9lbg1pl3vuas91bmltdgf0dxm import UniStatus
		return UniStatus(self)

	@property
	def UniStatusLearnedInfo(self):
		"""An instance of the UniStatusLearnedInfo class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.unistatuslearnedinfo_as91bmltdgf0dxnmzwfybmvksw5mbw.UniStatusLearnedInfo)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.unistatuslearnedinfo_as91bmltdgf0dxnmzwfybmvksw5mbw import UniStatusLearnedInfo
		return UniStatusLearnedInfo(self)

	@property
	def DataInstance(self):
		"""This four-octet field indicates the Data Instance value to be sent in transmitted packet. It will be configurable only if Override Data Instance is enabled. By default it is grayed out with default value 0 for UNI-C and 1 for UNI-N. Max 4294967295, Min 0 for UNI-C and 1 for UNI- V. Change of value in this field takes effect when protocol is running.

		Returns:
			number
		"""
		return self._get_attribute('dataInstance')
	@DataInstance.setter
	def DataInstance(self, value):
		self._set_attribute('dataInstance', value)

	@property
	def EnablePollingVerificationTimer(self):
		"""If enabled, it shows the default value.

		Returns:
			bool
		"""
		return self._get_attribute('enablePollingVerificationTimer')
	@EnablePollingVerificationTimer.setter
	def EnablePollingVerificationTimer(self, value):
		self._set_attribute('enablePollingVerificationTimer', value)

	@property
	def Enabled(self):
		"""It signifies whether the protocol is enabled or disabled.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def IsEvcStatusLearnedInfoRefreshed(self):
		"""It checks whether the EVC status learned info is refreshed or not.

		Returns:
			bool
		"""
		return self._get_attribute('isEvcStatusLearnedInfoRefreshed')

	@property
	def IsLmiStatusLearnedInfoRefreshed(self):
		"""It checks whether the LMI status learned info is refreshed or not.

		Returns:
			bool
		"""
		return self._get_attribute('isLmiStatusLearnedInfoRefreshed')

	@property
	def IsUniStatusLearnedInfoRefreshed(self):
		"""It checks whether the UNI status learned info is refreshed or not.

		Returns:
			bool
		"""
		return self._get_attribute('isUniStatusLearnedInfoRefreshed')

	@property
	def Mode(self):
		"""It is a type of UNI end point.

		Returns:
			str(uniC|uniN)
		"""
		return self._get_attribute('mode')
	@Mode.setter
	def Mode(self, value):
		self._set_attribute('mode', value)

	@property
	def OverrideDataInstance(self):
		"""If enabled, it updates the Data Instance field of Data Instance Information Element (IE). Default is false. Change of value in this field takes effect when protocol is running.

		Returns:
			bool
		"""
		return self._get_attribute('overrideDataInstance')
	@OverrideDataInstance.setter
	def OverrideDataInstance(self, value):
		self._set_attribute('overrideDataInstance', value)

	@property
	def OverrideReceiveSequenceNumber(self):
		"""If enabled, it updates the receive sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.

		Returns:
			bool
		"""
		return self._get_attribute('overrideReceiveSequenceNumber')
	@OverrideReceiveSequenceNumber.setter
	def OverrideReceiveSequenceNumber(self, value):
		self._set_attribute('overrideReceiveSequenceNumber', value)

	@property
	def OverrideSendSequenceNumber(self):
		"""If enabled, it updates the send sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.

		Returns:
			bool
		"""
		return self._get_attribute('overrideSendSequenceNumber')
	@OverrideSendSequenceNumber.setter
	def OverrideSendSequenceNumber(self, value):
		self._set_attribute('overrideSendSequenceNumber', value)

	@property
	def PollingCounter(self):
		"""It signifies the full status (status of UNI and all EVCs) polling count. Range is 1- 65k. Default is 360. This is applicable only for UNI-C.

		Returns:
			number
		"""
		return self._get_attribute('pollingCounter')
	@PollingCounter.setter
	def PollingCounter(self, value):
		self._set_attribute('pollingCounter', value)

	@property
	def PollingTimer(self):
		"""The range is 5-30 in seconds. Default is 10 seconds. This is applicable only for UNI-C.

		Returns:
			number
		"""
		return self._get_attribute('pollingTimer')
	@PollingTimer.setter
	def PollingTimer(self, value):
		self._set_attribute('pollingTimer', value)

	@property
	def PollingVerificationTimer(self):
		"""This is applicable only for UNI-N. Range is 5-30 secs. Default is 15 seconds.

		Returns:
			number
		"""
		return self._get_attribute('pollingVerificationTimer')
	@PollingVerificationTimer.setter
	def PollingVerificationTimer(self, value):
		self._set_attribute('pollingVerificationTimer', value)

	@property
	def ProtocolInterface(self):
		"""It signifies the configured protocol interface. User has to select one interface to enable configuring UNI. Until and unless protocol interface is selected user will not be able to configure and enable UNI. Default is unassigned.

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=interface)
		"""
		return self._get_attribute('protocolInterface')
	@ProtocolInterface.setter
	def ProtocolInterface(self, value):
		self._set_attribute('protocolInterface', value)

	@property
	def ProtocolVersion(self):
		"""This one-octet field indicates the version supported by the sending entity (UNI-C or UNI-N). Default value is ox1. Max 255, Min - 1.

		Returns:
			number
		"""
		return self._get_attribute('protocolVersion')
	@ProtocolVersion.setter
	def ProtocolVersion(self, value):
		self._set_attribute('protocolVersion', value)

	@property
	def ReceiveSequenceNumber(self):
		"""This one-octet field indicates the sequence number to be sent in the 'Receive Sequence Number' in transmitted packet. It will be configurable only if Override Receive Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.

		Returns:
			number
		"""
		return self._get_attribute('receiveSequenceNumber')
	@ReceiveSequenceNumber.setter
	def ReceiveSequenceNumber(self, value):
		self._set_attribute('receiveSequenceNumber', value)

	@property
	def SendSequenceNumber(self):
		"""This one-octet field indicates the sequence number to be sent in the 'Send Sequence Number' field in transmitted packet. It will be configurable only if Override Send Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.

		Returns:
			number
		"""
		return self._get_attribute('sendSequenceNumber')
	@SendSequenceNumber.setter
	def SendSequenceNumber(self, value):
		self._set_attribute('sendSequenceNumber', value)

	@property
	def StatusCounter(self):
		"""It signifies the count of consecutive errors. Range is 2 10. Default is 4.

		Returns:
			number
		"""
		return self._get_attribute('statusCounter')
	@StatusCounter.setter
	def StatusCounter(self, value):
		self._set_attribute('statusCounter', value)

	def update(self, DataInstance=None, EnablePollingVerificationTimer=None, Enabled=None, Mode=None, OverrideDataInstance=None, OverrideReceiveSequenceNumber=None, OverrideSendSequenceNumber=None, PollingCounter=None, PollingTimer=None, PollingVerificationTimer=None, ProtocolInterface=None, ProtocolVersion=None, ReceiveSequenceNumber=None, SendSequenceNumber=None, StatusCounter=None):
		"""Updates a child instance of uni on the server.

		Args:
			DataInstance (number): This four-octet field indicates the Data Instance value to be sent in transmitted packet. It will be configurable only if Override Data Instance is enabled. By default it is grayed out with default value 0 for UNI-C and 1 for UNI-N. Max 4294967295, Min 0 for UNI-C and 1 for UNI- V. Change of value in this field takes effect when protocol is running.
			EnablePollingVerificationTimer (bool): If enabled, it shows the default value.
			Enabled (bool): It signifies whether the protocol is enabled or disabled.
			Mode (str(uniC|uniN)): It is a type of UNI end point.
			OverrideDataInstance (bool): If enabled, it updates the Data Instance field of Data Instance Information Element (IE). Default is false. Change of value in this field takes effect when protocol is running.
			OverrideReceiveSequenceNumber (bool): If enabled, it updates the receive sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.
			OverrideSendSequenceNumber (bool): If enabled, it updates the send sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.
			PollingCounter (number): It signifies the full status (status of UNI and all EVCs) polling count. Range is 1- 65k. Default is 360. This is applicable only for UNI-C.
			PollingTimer (number): The range is 5-30 in seconds. Default is 10 seconds. This is applicable only for UNI-C.
			PollingVerificationTimer (number): This is applicable only for UNI-N. Range is 5-30 secs. Default is 15 seconds.
			ProtocolInterface (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=interface)): It signifies the configured protocol interface. User has to select one interface to enable configuring UNI. Until and unless protocol interface is selected user will not be able to configure and enable UNI. Default is unassigned.
			ProtocolVersion (number): This one-octet field indicates the version supported by the sending entity (UNI-C or UNI-N). Default value is ox1. Max 255, Min - 1.
			ReceiveSequenceNumber (number): This one-octet field indicates the sequence number to be sent in the 'Receive Sequence Number' in transmitted packet. It will be configurable only if Override Receive Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.
			SendSequenceNumber (number): This one-octet field indicates the sequence number to be sent in the 'Send Sequence Number' field in transmitted packet. It will be configurable only if Override Send Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.
			StatusCounter (number): It signifies the count of consecutive errors. Range is 2 10. Default is 4.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, DataInstance=None, EnablePollingVerificationTimer=None, Enabled=None, Mode=None, OverrideDataInstance=None, OverrideReceiveSequenceNumber=None, OverrideSendSequenceNumber=None, PollingCounter=None, PollingTimer=None, PollingVerificationTimer=None, ProtocolInterface=None, ProtocolVersion=None, ReceiveSequenceNumber=None, SendSequenceNumber=None, StatusCounter=None):
		"""Adds a new uni node on the server and retrieves it in this instance.

		Args:
			DataInstance (number): This four-octet field indicates the Data Instance value to be sent in transmitted packet. It will be configurable only if Override Data Instance is enabled. By default it is grayed out with default value 0 for UNI-C and 1 for UNI-N. Max 4294967295, Min 0 for UNI-C and 1 for UNI- V. Change of value in this field takes effect when protocol is running.
			EnablePollingVerificationTimer (bool): If enabled, it shows the default value.
			Enabled (bool): It signifies whether the protocol is enabled or disabled.
			Mode (str(uniC|uniN)): It is a type of UNI end point.
			OverrideDataInstance (bool): If enabled, it updates the Data Instance field of Data Instance Information Element (IE). Default is false. Change of value in this field takes effect when protocol is running.
			OverrideReceiveSequenceNumber (bool): If enabled, it updates the receive sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.
			OverrideSendSequenceNumber (bool): If enabled, it updates the send sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.
			PollingCounter (number): It signifies the full status (status of UNI and all EVCs) polling count. Range is 1- 65k. Default is 360. This is applicable only for UNI-C.
			PollingTimer (number): The range is 5-30 in seconds. Default is 10 seconds. This is applicable only for UNI-C.
			PollingVerificationTimer (number): This is applicable only for UNI-N. Range is 5-30 secs. Default is 15 seconds.
			ProtocolInterface (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=interface)): It signifies the configured protocol interface. User has to select one interface to enable configuring UNI. Until and unless protocol interface is selected user will not be able to configure and enable UNI. Default is unassigned.
			ProtocolVersion (number): This one-octet field indicates the version supported by the sending entity (UNI-C or UNI-N). Default value is ox1. Max 255, Min - 1.
			ReceiveSequenceNumber (number): This one-octet field indicates the sequence number to be sent in the 'Receive Sequence Number' in transmitted packet. It will be configurable only if Override Receive Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.
			SendSequenceNumber (number): This one-octet field indicates the sequence number to be sent in the 'Send Sequence Number' field in transmitted packet. It will be configurable only if Override Send Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.
			StatusCounter (number): It signifies the count of consecutive errors. Range is 2 10. Default is 4.

		Returns:
			self: This instance with all currently retrieved uni data using find and the newly added uni data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the uni data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, DataInstance=None, EnablePollingVerificationTimer=None, Enabled=None, IsEvcStatusLearnedInfoRefreshed=None, IsLmiStatusLearnedInfoRefreshed=None, IsUniStatusLearnedInfoRefreshed=None, Mode=None, OverrideDataInstance=None, OverrideReceiveSequenceNumber=None, OverrideSendSequenceNumber=None, PollingCounter=None, PollingTimer=None, PollingVerificationTimer=None, ProtocolInterface=None, ProtocolVersion=None, ReceiveSequenceNumber=None, SendSequenceNumber=None, StatusCounter=None):
		"""Finds and retrieves uni data from the server.

		All named parameters support regex and can be used to selectively retrieve uni data from the server.
		By default the find method takes no parameters and will retrieve all uni data from the server.

		Args:
			DataInstance (number): This four-octet field indicates the Data Instance value to be sent in transmitted packet. It will be configurable only if Override Data Instance is enabled. By default it is grayed out with default value 0 for UNI-C and 1 for UNI-N. Max 4294967295, Min 0 for UNI-C and 1 for UNI- V. Change of value in this field takes effect when protocol is running.
			EnablePollingVerificationTimer (bool): If enabled, it shows the default value.
			Enabled (bool): It signifies whether the protocol is enabled or disabled.
			IsEvcStatusLearnedInfoRefreshed (bool): It checks whether the EVC status learned info is refreshed or not.
			IsLmiStatusLearnedInfoRefreshed (bool): It checks whether the LMI status learned info is refreshed or not.
			IsUniStatusLearnedInfoRefreshed (bool): It checks whether the UNI status learned info is refreshed or not.
			Mode (str(uniC|uniN)): It is a type of UNI end point.
			OverrideDataInstance (bool): If enabled, it updates the Data Instance field of Data Instance Information Element (IE). Default is false. Change of value in this field takes effect when protocol is running.
			OverrideReceiveSequenceNumber (bool): If enabled, it updates the receive sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.
			OverrideSendSequenceNumber (bool): If enabled, it updates the send sequence number. This is used for negative testing. Default is false. Change of value in this field takes effect when protocol is running.
			PollingCounter (number): It signifies the full status (status of UNI and all EVCs) polling count. Range is 1- 65k. Default is 360. This is applicable only for UNI-C.
			PollingTimer (number): The range is 5-30 in seconds. Default is 10 seconds. This is applicable only for UNI-C.
			PollingVerificationTimer (number): This is applicable only for UNI-N. Range is 5-30 secs. Default is 15 seconds.
			ProtocolInterface (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=interface)): It signifies the configured protocol interface. User has to select one interface to enable configuring UNI. Until and unless protocol interface is selected user will not be able to configure and enable UNI. Default is unassigned.
			ProtocolVersion (number): This one-octet field indicates the version supported by the sending entity (UNI-C or UNI-N). Default value is ox1. Max 255, Min - 1.
			ReceiveSequenceNumber (number): This one-octet field indicates the sequence number to be sent in the 'Receive Sequence Number' in transmitted packet. It will be configurable only if Override Receive Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.
			SendSequenceNumber (number): This one-octet field indicates the sequence number to be sent in the 'Send Sequence Number' field in transmitted packet. It will be configurable only if Override Send Sequence Number is enabled. Default value of this field is 0. Max 255, Min - 0 Change of value in this field takes effect when protocol is running.
			StatusCounter (number): It signifies the count of consecutive errors. Range is 2 10. Default is 4.

		Returns:
			self: This instance with matching uni data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of uni data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the uni data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def RefreshEvcStatusLearnedInfo(self):
		"""Executes the refreshEvcStatusLearnedInfo operation on the server.

		NOT DEFINED

			Returns:
				bool: NOT DEFINED

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('refreshEvcStatusLearnedInfo', payload=payload, response_object=None)

	def RefreshLmiStatusLearnedInfo(self):
		"""Executes the refreshLmiStatusLearnedInfo operation on the server.

		NOT DEFINED

			Returns:
				bool: NOT DEFINED

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('refreshLmiStatusLearnedInfo', payload=payload, response_object=None)

	def RefreshUniStatusLearnedInfo(self):
		"""Executes the refreshUniStatusLearnedInfo operation on the server.

		NOT DEFINED

			Returns:
				bool: NOT DEFINED

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('refreshUniStatusLearnedInfo', payload=payload, response_object=None)
