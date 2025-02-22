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


class PacketInMaskSlave(Base):
	"""When packets are received by the datapath and sent to the Controller, it may get no response from the Controller based on what the asynchronous message contains.
	The PacketInMaskSlave class encapsulates a required packetInMaskSlave resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'packetInMaskSlave'

	def __init__(self, parent):
		super(PacketInMaskSlave, self).__init__(parent)

	@property
	def Action(self):
		"""Action explicitly output to controller.

		Returns:
			bool
		"""
		return self._get_attribute('action')
	@Action.setter
	def Action(self, value):
		self._set_attribute('action', value)

	@property
	def InvalidTtl(self):
		"""This indicates that a packet with an invalid IP TTL or MPLS TTL was rejected by the OpenFlow pipeline and passed to the controller.

		Returns:
			bool
		"""
		return self._get_attribute('invalidTtl')
	@InvalidTtl.setter
	def InvalidTtl(self, value):
		self._set_attribute('invalidTtl', value)

	@property
	def NoMatch(self):
		"""This indicates that a packet with no matching flow (table-miss flow entry) is passed to the controller.

		Returns:
			bool
		"""
		return self._get_attribute('noMatch')
	@NoMatch.setter
	def NoMatch(self, value):
		self._set_attribute('noMatch', value)

	def update(self, Action=None, InvalidTtl=None, NoMatch=None):
		"""Updates a child instance of packetInMaskSlave on the server.

		Args:
			Action (bool): Action explicitly output to controller.
			InvalidTtl (bool): This indicates that a packet with an invalid IP TTL or MPLS TTL was rejected by the OpenFlow pipeline and passed to the controller.
			NoMatch (bool): This indicates that a packet with no matching flow (table-miss flow entry) is passed to the controller.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
