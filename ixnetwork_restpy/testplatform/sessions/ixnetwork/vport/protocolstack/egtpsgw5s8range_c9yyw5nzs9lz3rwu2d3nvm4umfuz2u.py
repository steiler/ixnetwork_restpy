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


class EgtpSgw5S8Range(Base):
	"""SGW Range
	The EgtpSgw5S8Range class encapsulates a required egtpSgw5S8Range resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'egtpSgw5S8Range'

	def __init__(self, parent):
		super(EgtpSgw5S8Range, self).__init__(parent)

	@property
	def BearerResourceCommandN3(self):
		"""Maximum number of retransmissions that will be permitted for a Bearer Resource Cmd message

		Returns:
			number
		"""
		return self._get_attribute('bearerResourceCommandN3')
	@BearerResourceCommandN3.setter
	def BearerResourceCommandN3(self, value):
		self._set_attribute('bearerResourceCommandN3', value)

	@property
	def BearerResourceCommandT3(self):
		"""Number of seconds to wait for a Bearer Resource Command message. Bearer Resource Command is a tunnel management message that is sent from an MME to an SGW and forwarded to PGW as a part of the UE requested bearer resource modification procedure. The message is also sent on the S4 interface by a SGSN to a SGW and on the S5/S8 interface by a SGW to a PGW as part of the MS-initiated modification procedure, or secondary PDP context activation procedure.

		Returns:
			number
		"""
		return self._get_attribute('bearerResourceCommandT3')
	@BearerResourceCommandT3.setter
	def BearerResourceCommandT3(self, value):
		self._set_attribute('bearerResourceCommandT3', value)

	@property
	def CreateSessionN3(self):
		"""Maximum number of retransmissions that will be permitted for a Create Session Response message.

		Returns:
			number
		"""
		return self._get_attribute('createSessionN3')
	@CreateSessionN3.setter
	def CreateSessionN3(self, value):
		self._set_attribute('createSessionN3', value)

	@property
	def CreateSessiontT3(self):
		"""Number of seconds to wait for a Create Session Response message. Create Session Response is a tunnel management message that is sent on the S11 interface by the SGW to the MME, and on the S5/S8 interface by the PGW to the SGW as part of several procedures, including the E-UTRAN Initial Attach and UE Requested PDN Connectivity procedures.

		Returns:
			number
		"""
		return self._get_attribute('createSessiontT3')
	@CreateSessiontT3.setter
	def CreateSessiontT3(self, value):
		self._set_attribute('createSessiontT3', value)

	@property
	def DeleteBearerCommandN3(self):
		"""Maximum number of retransmissions that will be permitted for a Delete Bearer Command message.

		Returns:
			number
		"""
		return self._get_attribute('deleteBearerCommandN3')
	@DeleteBearerCommandN3.setter
	def DeleteBearerCommandN3(self, value):
		self._set_attribute('deleteBearerCommandN3', value)

	@property
	def DeleteBearerCommandT3(self):
		"""Number of seconds to wait for a Delete Bearer Command message. Delete Bearer Command is a tunnel management message that is sent on the S11 interface by the MME to the SGW and on the S5/S8 interface by the SGW to the PGW as a part of the eNodeB-requested bearer release or MME-Initiated Dedicated Bearer Deactivation procedure. The message is also sent on the S4 interface by the SGSN to the SGW and on the S5/S8 interface by the SGW to the PGW as part of the MS and SGSN Initiated non Default Bearer Deactivation procedure using S4.

		Returns:
			number
		"""
		return self._get_attribute('deleteBearerCommandT3')
	@DeleteBearerCommandT3.setter
	def DeleteBearerCommandT3(self, value):
		self._set_attribute('deleteBearerCommandT3', value)

	@property
	def DeleteSessionN3(self):
		"""Maximum number of retransmissions that will be permitted for a Delete Session Response message

		Returns:
			number
		"""
		return self._get_attribute('deleteSessionN3')
	@DeleteSessionN3.setter
	def DeleteSessionN3(self, value):
		self._set_attribute('deleteSessionN3', value)

	@property
	def DeleteSessionT3(self):
		"""Number of seconds to wait for a Delete Session Response message. Delete Session Response is a tunnel management message that is sent on the S11 interface by the SGW to the MME and on the S5/S8 interface by the PGW to the SGW as part of several procedures, including the EUTRAN Initial Attach procedure; the UE, HSS or MME Initiated Detach procedure; and the UE or MME Requested PDN Disconnection procedure.

		Returns:
			number
		"""
		return self._get_attribute('deleteSessionT3')
	@DeleteSessionT3.setter
	def DeleteSessionT3(self, value):
		self._set_attribute('deleteSessionT3', value)

	@property
	def EchoRequestN3(self):
		"""Maximum number of Echo Request retransmissions that will be permitted when no Echo Response has been received.

		Returns:
			number
		"""
		return self._get_attribute('echoRequestN3')
	@EchoRequestN3.setter
	def EchoRequestN3(self, value):
		self._set_attribute('echoRequestN3', value)

	@property
	def EchoRequestT3(self):
		"""Number of seconds to wait for an Echo Response message from the remote end point, in response to an Echo Request.

		Returns:
			number
		"""
		return self._get_attribute('echoRequestT3')
	@EchoRequestT3.setter
	def EchoRequestT3(self, value):
		self._set_attribute('echoRequestT3', value)

	@property
	def EnableEchoRequest(self):
		"""Set to true to send echo request

		Returns:
			bool
		"""
		return self._get_attribute('enableEchoRequest')
	@EnableEchoRequest.setter
	def EnableEchoRequest(self, value):
		self._set_attribute('enableEchoRequest', value)

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
	def ModifyBearerCommandN3(self):
		"""Maximum number of retransmissions that will be permitted for a Modify Bearer Command message

		Returns:
			number
		"""
		return self._get_attribute('modifyBearerCommandN3')
	@ModifyBearerCommandN3.setter
	def ModifyBearerCommandN3(self, value):
		self._set_attribute('modifyBearerCommandN3', value)

	@property
	def ModifyBearerCommandT3(self):
		"""Number of seconds to wait for a Modify Bearer Command message. Modify Bearer Command is a tunnel management message that is sent on the S11 interface by the MME to the SGW and on the S5/S8 interface by the SGW to the PGW as part of the HSS Initiated Subscribed QoS Modification procedure. The message is also sent on the S4 interface by the SGSN to the SGW and on the S5/S8 interface by the SGW to the PGW as part of the HSS Initiated Subscribed QoS modification

		Returns:
			number
		"""
		return self._get_attribute('modifyBearerCommandT3')
	@ModifyBearerCommandT3.setter
	def ModifyBearerCommandT3(self, value):
		self._set_attribute('modifyBearerCommandT3', value)

	@property
	def ModifyBearerN3(self):
		"""Maximum number of retransmissions that will be permitted for a Modify Bearer Request message.

		Returns:
			number
		"""
		return self._get_attribute('modifyBearerN3')
	@ModifyBearerN3.setter
	def ModifyBearerN3(self, value):
		self._set_attribute('modifyBearerN3', value)

	@property
	def ModifyBearerT3(self):
		"""Number of seconds to wait for a Modify Bearer Response message. Modify Bearer Response is a tunnel management message that is sent on the S11 interface by the SGW to the MME, and on the S5/S8 interfaces by the PGW to the SGW, as part of several procedures.

		Returns:
			number
		"""
		return self._get_attribute('modifyBearerT3')
	@ModifyBearerT3.setter
	def ModifyBearerT3(self, value):
		self._set_attribute('modifyBearerT3', value)

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
	def ObjectId(self):
		"""Unique identifier for this object

		Returns:
			str
		"""
		return self._get_attribute('objectId')

	@property
	def RatType(self):
		"""The Radio Access Technology Type that the MME will include, whenever necessary, in its messages towards the SGW

		Returns:
			str
		"""
		return self._get_attribute('ratType')
	@RatType.setter
	def RatType(self, value):
		self._set_attribute('ratType', value)

	@property
	def SrcUdpPort(self):
		"""Source UDP port for control plane messages (0 for random)

		Returns:
			number
		"""
		return self._get_attribute('srcUdpPort')
	@SrcUdpPort.setter
	def SrcUdpPort(self, value):
		self._set_attribute('srcUdpPort', value)

	def update(self, BearerResourceCommandN3=None, BearerResourceCommandT3=None, CreateSessionN3=None, CreateSessiontT3=None, DeleteBearerCommandN3=None, DeleteBearerCommandT3=None, DeleteSessionN3=None, DeleteSessionT3=None, EchoRequestN3=None, EchoRequestT3=None, EnableEchoRequest=None, Enabled=None, ModifyBearerCommandN3=None, ModifyBearerCommandT3=None, ModifyBearerN3=None, ModifyBearerT3=None, Name=None, RatType=None, SrcUdpPort=None):
		"""Updates a child instance of egtpSgw5S8Range on the server.

		Args:
			BearerResourceCommandN3 (number): Maximum number of retransmissions that will be permitted for a Bearer Resource Cmd message
			BearerResourceCommandT3 (number): Number of seconds to wait for a Bearer Resource Command message. Bearer Resource Command is a tunnel management message that is sent from an MME to an SGW and forwarded to PGW as a part of the UE requested bearer resource modification procedure. The message is also sent on the S4 interface by a SGSN to a SGW and on the S5/S8 interface by a SGW to a PGW as part of the MS-initiated modification procedure, or secondary PDP context activation procedure.
			CreateSessionN3 (number): Maximum number of retransmissions that will be permitted for a Create Session Response message.
			CreateSessiontT3 (number): Number of seconds to wait for a Create Session Response message. Create Session Response is a tunnel management message that is sent on the S11 interface by the SGW to the MME, and on the S5/S8 interface by the PGW to the SGW as part of several procedures, including the E-UTRAN Initial Attach and UE Requested PDN Connectivity procedures.
			DeleteBearerCommandN3 (number): Maximum number of retransmissions that will be permitted for a Delete Bearer Command message.
			DeleteBearerCommandT3 (number): Number of seconds to wait for a Delete Bearer Command message. Delete Bearer Command is a tunnel management message that is sent on the S11 interface by the MME to the SGW and on the S5/S8 interface by the SGW to the PGW as a part of the eNodeB-requested bearer release or MME-Initiated Dedicated Bearer Deactivation procedure. The message is also sent on the S4 interface by the SGSN to the SGW and on the S5/S8 interface by the SGW to the PGW as part of the MS and SGSN Initiated non Default Bearer Deactivation procedure using S4.
			DeleteSessionN3 (number): Maximum number of retransmissions that will be permitted for a Delete Session Response message
			DeleteSessionT3 (number): Number of seconds to wait for a Delete Session Response message. Delete Session Response is a tunnel management message that is sent on the S11 interface by the SGW to the MME and on the S5/S8 interface by the PGW to the SGW as part of several procedures, including the EUTRAN Initial Attach procedure; the UE, HSS or MME Initiated Detach procedure; and the UE or MME Requested PDN Disconnection procedure.
			EchoRequestN3 (number): Maximum number of Echo Request retransmissions that will be permitted when no Echo Response has been received.
			EchoRequestT3 (number): Number of seconds to wait for an Echo Response message from the remote end point, in response to an Echo Request.
			EnableEchoRequest (bool): Set to true to send echo request
			Enabled (bool): Disabled ranges won't be configured nor validated.
			ModifyBearerCommandN3 (number): Maximum number of retransmissions that will be permitted for a Modify Bearer Command message
			ModifyBearerCommandT3 (number): Number of seconds to wait for a Modify Bearer Command message. Modify Bearer Command is a tunnel management message that is sent on the S11 interface by the MME to the SGW and on the S5/S8 interface by the SGW to the PGW as part of the HSS Initiated Subscribed QoS Modification procedure. The message is also sent on the S4 interface by the SGSN to the SGW and on the S5/S8 interface by the SGW to the PGW as part of the HSS Initiated Subscribed QoS modification
			ModifyBearerN3 (number): Maximum number of retransmissions that will be permitted for a Modify Bearer Request message.
			ModifyBearerT3 (number): Number of seconds to wait for a Modify Bearer Response message. Modify Bearer Response is a tunnel management message that is sent on the S11 interface by the SGW to the MME, and on the S5/S8 interfaces by the PGW to the SGW, as part of several procedures.
			Name (str): Name of range
			RatType (str): The Radio Access Technology Type that the MME will include, whenever necessary, in its messages towards the SGW
			SrcUdpPort (number): Source UDP port for control plane messages (0 for random)

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

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
