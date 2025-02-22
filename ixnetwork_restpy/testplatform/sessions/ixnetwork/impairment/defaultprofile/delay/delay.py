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


class Delay(Base):
	"""Delay each packet.
	The Delay class encapsulates a required delay resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'delay'

	def __init__(self, parent):
		super(Delay, self).__init__(parent)

	@property
	def Enabled(self):
		"""If true, delay packets.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def Units(self):
		"""Specify the units for the delay value.

		Returns:
			str(kilometers|kKilometers|kMicroseconds|kMilliseconds|kSeconds|microseconds|milliseconds|seconds)
		"""
		return self._get_attribute('units')
	@Units.setter
	def Units(self, value):
		self._set_attribute('units', value)

	@property
	def Value(self):
		"""Time to delay each packet.

		Returns:
			number
		"""
		return self._get_attribute('value')
	@Value.setter
	def Value(self, value):
		self._set_attribute('value', value)

	def update(self, Enabled=None, Units=None, Value=None):
		"""Updates a child instance of delay on the server.

		Args:
			Enabled (bool): If true, delay packets.
			Units (str(kilometers|kKilometers|kMicroseconds|kMilliseconds|kSeconds|microseconds|milliseconds|seconds)): Specify the units for the delay value.
			Value (number): Time to delay each packet.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
