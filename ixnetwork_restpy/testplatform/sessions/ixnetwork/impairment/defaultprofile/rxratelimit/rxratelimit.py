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


class RxRateLimit(Base):
	"""Limit receive bandwidth, by dropping incoming packets which exceed the limit.
	The RxRateLimit class encapsulates a required rxRateLimit resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'rxRateLimit'

	def __init__(self, parent):
		super(RxRateLimit, self).__init__(parent)

	@property
	def BufferSizeEnabled(self):
		"""Allows user to specify a custom buffer size. Default false

		Returns:
			bool
		"""
		return self._get_attribute('bufferSizeEnabled')
	@BufferSizeEnabled.setter
	def BufferSizeEnabled(self, value):
		self._set_attribute('bufferSizeEnabled', value)

	@property
	def BufferSizeUnits(self):
		"""Units (Kilobytes, Megabytes). Default: Kilobytes

		Returns:
			str(kilobytes|kKilobytes|kMegabytes|megabytes)
		"""
		return self._get_attribute('bufferSizeUnits')
	@BufferSizeUnits.setter
	def BufferSizeUnits(self, value):
		self._set_attribute('bufferSizeUnits', value)

	@property
	def BufferSizeValue(self):
		"""Burst tolerance buffer size. Default value is 32 KB

		Returns:
			number
		"""
		return self._get_attribute('bufferSizeValue')
	@BufferSizeValue.setter
	def BufferSizeValue(self, value):
		self._set_attribute('bufferSizeValue', value)

	@property
	def Enabled(self):
		"""Enable or disable the receive rate limit impairment.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def Units(self):
		"""Specify the units for the receive rate limit value.

		Returns:
			str(kilobitsPerSecond|kKilobitsPerSecond|kMegabitsPerSecond|megabitsPerSecond)
		"""
		return self._get_attribute('units')
	@Units.setter
	def Units(self, value):
		self._set_attribute('units', value)

	@property
	def Value(self):
		"""Specify the value of the receive rate limit.

		Returns:
			number
		"""
		return self._get_attribute('value')
	@Value.setter
	def Value(self, value):
		self._set_attribute('value', value)

	def update(self, BufferSizeEnabled=None, BufferSizeUnits=None, BufferSizeValue=None, Enabled=None, Units=None, Value=None):
		"""Updates a child instance of rxRateLimit on the server.

		Args:
			BufferSizeEnabled (bool): Allows user to specify a custom buffer size. Default false
			BufferSizeUnits (str(kilobytes|kKilobytes|kMegabytes|megabytes)): Units (Kilobytes, Megabytes). Default: Kilobytes
			BufferSizeValue (number): Burst tolerance buffer size. Default value is 32 KB
			Enabled (bool): Enable or disable the receive rate limit impairment.
			Units (str(kilobitsPerSecond|kKilobitsPerSecond|kMegabitsPerSecond|megabitsPerSecond)): Specify the units for the receive rate limit value.
			Value (number): Specify the value of the receive rate limit.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
