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


class Config(Base):
	"""This object allow to define the settings for the current configuration of the physical port.
	The Config class encapsulates a required config resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'config'

	def __init__(self, parent):
		super(Config, self).__init__(parent)

	@property
	def NoFlood(self):
		"""Indicates that the port is not included when flooding.

		Returns:
			bool
		"""
		return self._get_attribute('noFlood')
	@NoFlood.setter
	def NoFlood(self, value):
		self._set_attribute('noFlood', value)

	@property
	def NoForward(self):
		"""Indicates that the port drop all packets forwarded to it.

		Returns:
			bool
		"""
		return self._get_attribute('noForward')
	@NoForward.setter
	def NoForward(self, value):
		self._set_attribute('noForward', value)

	@property
	def NoPacketIn(self):
		"""Indicates that the port does not send packet-in messages.

		Returns:
			bool
		"""
		return self._get_attribute('noPacketIn')
	@NoPacketIn.setter
	def NoPacketIn(self, value):
		self._set_attribute('noPacketIn', value)

	@property
	def NoReceive(self):
		"""Indicates that the port drops all packets except 802.1D spanning tree packets.

		Returns:
			bool
		"""
		return self._get_attribute('noReceive')
	@NoReceive.setter
	def NoReceive(self, value):
		self._set_attribute('noReceive', value)

	@property
	def NoReceiveStp(self):
		"""Indicates that the port drops received 802.1D STP packets.

		Returns:
			bool
		"""
		return self._get_attribute('noReceiveStp')
	@NoReceiveStp.setter
	def NoReceiveStp(self, value):
		self._set_attribute('noReceiveStp', value)

	@property
	def NoStp(self):
		"""Indicates that 802.1D spanning tree on port is disable.

		Returns:
			bool
		"""
		return self._get_attribute('noStp')
	@NoStp.setter
	def NoStp(self, value):
		self._set_attribute('noStp', value)

	@property
	def PortDown(self):
		"""Indicates that the port is administratively down.

		Returns:
			bool
		"""
		return self._get_attribute('portDown')
	@PortDown.setter
	def PortDown(self, value):
		self._set_attribute('portDown', value)

	def update(self, NoFlood=None, NoForward=None, NoPacketIn=None, NoReceive=None, NoReceiveStp=None, NoStp=None, PortDown=None):
		"""Updates a child instance of config on the server.

		Args:
			NoFlood (bool): Indicates that the port is not included when flooding.
			NoForward (bool): Indicates that the port drop all packets forwarded to it.
			NoPacketIn (bool): Indicates that the port does not send packet-in messages.
			NoReceive (bool): Indicates that the port drops all packets except 802.1D spanning tree packets.
			NoReceiveStp (bool): Indicates that the port drops received 802.1D STP packets.
			NoStp (bool): Indicates that 802.1D spanning tree on port is disable.
			PortDown (bool): Indicates that the port is administratively down.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
