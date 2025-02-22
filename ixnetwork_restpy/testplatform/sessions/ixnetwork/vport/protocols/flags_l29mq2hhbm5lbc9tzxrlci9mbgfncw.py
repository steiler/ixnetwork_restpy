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


class Flags(Base):
	"""Select the meter configuration flags from the list.
	The Flags class encapsulates a required flags resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'flags'

	def __init__(self, parent):
		super(Flags, self).__init__(parent)

	@property
	def BurstSize(self):
		"""This flag indicate that burst size calculation is to be done while applying the bands.

		Returns:
			bool
		"""
		return self._get_attribute('burstSize')
	@BurstSize.setter
	def BurstSize(self, value):
		self._set_attribute('burstSize', value)

	@property
	def CollectStatistics(self):
		"""This flag enables statistics collection for the meter and each band.

		Returns:
			bool
		"""
		return self._get_attribute('collectStatistics')
	@CollectStatistics.setter
	def CollectStatistics(self, value):
		self._set_attribute('collectStatistics', value)

	@property
	def RateKb(self):
		"""This flag indicates the rate value for bands associated with this meter is considered in kilo-bits per second.

		Returns:
			bool
		"""
		return self._get_attribute('rateKb')
	@RateKb.setter
	def RateKb(self, value):
		self._set_attribute('rateKb', value)

	@property
	def RatePacket(self):
		"""This flag indicates same as Rate (kb/sec)but the rate value is in packet per second.

		Returns:
			bool
		"""
		return self._get_attribute('ratePacket')
	@RatePacket.setter
	def RatePacket(self, value):
		self._set_attribute('ratePacket', value)

	def update(self, BurstSize=None, CollectStatistics=None, RateKb=None, RatePacket=None):
		"""Updates a child instance of flags on the server.

		Args:
			BurstSize (bool): This flag indicate that burst size calculation is to be done while applying the bands.
			CollectStatistics (bool): This flag enables statistics collection for the meter and each band.
			RateKb (bool): This flag indicates the rate value for bands associated with this meter is considered in kilo-bits per second.
			RatePacket (bool): This flag indicates same as Rate (kb/sec)but the rate value is in packet per second.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
