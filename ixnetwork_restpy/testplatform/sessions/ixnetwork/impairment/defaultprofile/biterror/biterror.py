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


class BitError(Base):
	"""Introduce bit errors.
	The BitError class encapsulates a required bitError resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'bitError'

	def __init__(self, parent):
		super(BitError, self).__init__(parent)

	@property
	def Enabled(self):
		"""If true, periodically introduce bit errors.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def LogRate(self):
		"""If logRate is n, error one out of 10^n bits.

		Returns:
			number
		"""
		return self._get_attribute('logRate')
	@LogRate.setter
	def LogRate(self, value):
		self._set_attribute('logRate', value)

	@property
	def SkipEndOctets(self):
		"""Number of octets to skip at the end of each packet when erroring bits.

		Returns:
			number
		"""
		return self._get_attribute('skipEndOctets')
	@SkipEndOctets.setter
	def SkipEndOctets(self, value):
		self._set_attribute('skipEndOctets', value)

	@property
	def SkipStartOctets(self):
		"""Number of octets to skip at the start of each packet when erroring bits.

		Returns:
			number
		"""
		return self._get_attribute('skipStartOctets')
	@SkipStartOctets.setter
	def SkipStartOctets(self, value):
		self._set_attribute('skipStartOctets', value)

	def update(self, Enabled=None, LogRate=None, SkipEndOctets=None, SkipStartOctets=None):
		"""Updates a child instance of bitError on the server.

		Args:
			Enabled (bool): If true, periodically introduce bit errors.
			LogRate (number): If logRate is n, error one out of 10^n bits.
			SkipEndOctets (number): Number of octets to skip at the end of each packet when erroring bits.
			SkipStartOctets (number): Number of octets to skip at the start of each packet when erroring bits.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
