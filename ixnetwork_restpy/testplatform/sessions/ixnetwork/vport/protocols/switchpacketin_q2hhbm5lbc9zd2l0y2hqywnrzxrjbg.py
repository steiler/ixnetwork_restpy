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


class SwitchPacketIn(Base):
	"""This object allows to configure the packet-in message parameters of the switch.
	The SwitchPacketIn class encapsulates a list of switchPacketIn resources that is be managed by the user.
	A list of resources can be retrieved from the server using the SwitchPacketIn.find() method.
	The list can be managed by the user by using the SwitchPacketIn.add() and SwitchPacketIn.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'switchPacketIn'

	def __init__(self, parent):
		super(SwitchPacketIn, self).__init__(parent)

	@property
	def PacketInHeaders(self):
		"""An instance of the PacketInHeaders class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.packetinheaders_wnrzxrjbi9wywnrzxrjbkhlywrlcnm.PacketInHeaders)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.packetinheaders_wnrzxrjbi9wywnrzxrjbkhlywrlcnm import PacketInHeaders
		return PacketInHeaders(self)._select()

	@property
	def ConsultFlowTable(self):
		"""If true, consults Flow Table before sending packet-in messages. If any flow present then do not send packet-in messages.

		Returns:
			bool
		"""
		return self._get_attribute('consultFlowTable')
	@ConsultFlowTable.setter
	def ConsultFlowTable(self, value):
		self._set_attribute('consultFlowTable', value)

	@property
	def Enabled(self):
		"""If true, enables Packet-In Range for the switch.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def InPort(self):
		"""Specifies the number of ports on which the switch receives the new packet.

		Returns:
			str
		"""
		return self._get_attribute('inPort')
	@InPort.setter
	def InPort(self, value):
		self._set_attribute('inPort', value)

	@property
	def PacketIn(self):
		"""Specifies the contents of the new packet that will be sent via the Packet-In message.

		Returns:
			str
		"""
		return self._get_attribute('packetIn')
	@PacketIn.setter
	def PacketIn(self, value):
		self._set_attribute('packetIn', value)

	@property
	def PacketInName(self):
		"""Indicates the packet-in Range identifier name.

		Returns:
			str
		"""
		return self._get_attribute('packetInName')
	@PacketInName.setter
	def PacketInName(self, value):
		self._set_attribute('packetInName', value)

	@property
	def SendPacketIn(self):
		"""If true, packet-in messages will be sent to the controller using this Packet-In range definitions.

		Returns:
			bool
		"""
		return self._get_attribute('sendPacketIn')
	@SendPacketIn.setter
	def SendPacketIn(self, value):
		self._set_attribute('sendPacketIn', value)

	def update(self, ConsultFlowTable=None, Enabled=None, InPort=None, PacketIn=None, PacketInName=None, SendPacketIn=None):
		"""Updates a child instance of switchPacketIn on the server.

		Args:
			ConsultFlowTable (bool): If true, consults Flow Table before sending packet-in messages. If any flow present then do not send packet-in messages.
			Enabled (bool): If true, enables Packet-In Range for the switch.
			InPort (str): Specifies the number of ports on which the switch receives the new packet.
			PacketIn (str): Specifies the contents of the new packet that will be sent via the Packet-In message.
			PacketInName (str): Indicates the packet-in Range identifier name.
			SendPacketIn (bool): If true, packet-in messages will be sent to the controller using this Packet-In range definitions.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, ConsultFlowTable=None, Enabled=None, InPort=None, PacketIn=None, PacketInName=None, SendPacketIn=None):
		"""Adds a new switchPacketIn node on the server and retrieves it in this instance.

		Args:
			ConsultFlowTable (bool): If true, consults Flow Table before sending packet-in messages. If any flow present then do not send packet-in messages.
			Enabled (bool): If true, enables Packet-In Range for the switch.
			InPort (str): Specifies the number of ports on which the switch receives the new packet.
			PacketIn (str): Specifies the contents of the new packet that will be sent via the Packet-In message.
			PacketInName (str): Indicates the packet-in Range identifier name.
			SendPacketIn (bool): If true, packet-in messages will be sent to the controller using this Packet-In range definitions.

		Returns:
			self: This instance with all currently retrieved switchPacketIn data using find and the newly added switchPacketIn data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the switchPacketIn data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, ConsultFlowTable=None, Enabled=None, InPort=None, PacketIn=None, PacketInName=None, SendPacketIn=None):
		"""Finds and retrieves switchPacketIn data from the server.

		All named parameters support regex and can be used to selectively retrieve switchPacketIn data from the server.
		By default the find method takes no parameters and will retrieve all switchPacketIn data from the server.

		Args:
			ConsultFlowTable (bool): If true, consults Flow Table before sending packet-in messages. If any flow present then do not send packet-in messages.
			Enabled (bool): If true, enables Packet-In Range for the switch.
			InPort (str): Specifies the number of ports on which the switch receives the new packet.
			PacketIn (str): Specifies the contents of the new packet that will be sent via the Packet-In message.
			PacketInName (str): Indicates the packet-in Range identifier name.
			SendPacketIn (bool): If true, packet-in messages will be sent to the controller using this Packet-In range definitions.

		Returns:
			self: This instance with matching switchPacketIn data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of switchPacketIn data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the switchPacketIn data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def SendSwitchPacketInOption(self, *args, **kwargs):
		"""Executes the sendSwitchPacketInOption operation on the server.

		NOT DEFINED

		sendSwitchPacketInOption(Arg2:enum)bool
			Args:
				args[0] is Arg2 (str(sendPause|sendStart|sendStop)): NOT DEFINED

			Returns:
				bool: NOT DEFINED

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendSwitchPacketInOption', payload=payload, response_object=None)
