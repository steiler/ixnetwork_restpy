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


class Bfd(Base):
	"""Simulates one or more BFD routers in a network of routers.
	The Bfd class encapsulates a required bfd resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'bfd'

	def __init__(self, parent):
		super(Bfd, self).__init__(parent)

	@property
	def Router(self):
		"""An instance of the Router class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_j0l3byb3rvy29scy9izmqvcm91dgvy.Router)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_j0l3byb3rvy29scy9izmqvcm91dgvy import Router
		return Router(self)

	@property
	def Enabled(self):
		"""Enables or disables the use of this emulated BFD router in the emulated BFD network. (default = disabled)

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def IntervalValue(self):
		"""Interval Value

		Returns:
			number
		"""
		return self._get_attribute('intervalValue')
	@IntervalValue.setter
	def IntervalValue(self, value):
		self._set_attribute('intervalValue', value)

	@property
	def PacketsPerInterval(self):
		"""Number of BFD control packets per interval.

		Returns:
			number
		"""
		return self._get_attribute('packetsPerInterval')
	@PacketsPerInterval.setter
	def PacketsPerInterval(self, value):
		self._set_attribute('packetsPerInterval', value)

	@property
	def RunningState(self):
		"""The current running state of the BFD protocol.

		Returns:
			str(unknown|stopped|stopping|starting|started)
		"""
		return self._get_attribute('runningState')

	def update(self, Enabled=None, IntervalValue=None, PacketsPerInterval=None):
		"""Updates a child instance of bfd on the server.

		Args:
			Enabled (bool): Enables or disables the use of this emulated BFD router in the emulated BFD network. (default = disabled)
			IntervalValue (number): Interval Value
			PacketsPerInterval (number): Number of BFD control packets per interval.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def Start(self):
		"""Executes the start operation on the server.

		Starts the BFD protocol on a port or group of ports.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('start', payload=payload, response_object=None)

	def Stop(self):
		"""Executes the stop operation on the server.

		Stops the BFD protocol on a port or group of ports.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('stop', payload=payload, response_object=None)
