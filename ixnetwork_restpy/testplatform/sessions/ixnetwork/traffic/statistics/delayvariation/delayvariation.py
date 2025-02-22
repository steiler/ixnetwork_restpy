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


class DelayVariation(Base):
	"""This object fetches delay variation statistics.
	The DelayVariation class encapsulates a required delayVariation resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'delayVariation'

	def __init__(self, parent):
		super(DelayVariation, self).__init__(parent)

	@property
	def Enabled(self):
		"""If enabled, fetches latency delay variation statistics with average, minimum, and maximum measurements.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def LargeSequenceNumberErrorThreshold(self):
		"""The value for the large sequence number error.

		Returns:
			number
		"""
		return self._get_attribute('largeSequenceNumberErrorThreshold')
	@LargeSequenceNumberErrorThreshold.setter
	def LargeSequenceNumberErrorThreshold(self, value):
		self._set_attribute('largeSequenceNumberErrorThreshold', value)

	@property
	def LatencyMode(self):
		"""If enabled, allows to use Cut Through, Forwarding Delay, MEF, and Store and Forward Delay variation statictics measurements.

		Returns:
			str(cutThrough|forwardingDelay|mef|storeForward)
		"""
		return self._get_attribute('latencyMode')
	@LatencyMode.setter
	def LatencyMode(self, value):
		self._set_attribute('latencyMode', value)

	@property
	def StatisticsMode(self):
		"""If enabled, allows to receive delay variation statistics with sequence error measurements.

		Returns:
			str(rxDelayVariationAverage|rxDelayVariationErrorsAndRate|rxDelayVariationMinMaxAndRate)
		"""
		return self._get_attribute('statisticsMode')
	@StatisticsMode.setter
	def StatisticsMode(self, value):
		self._set_attribute('statisticsMode', value)

	def update(self, Enabled=None, LargeSequenceNumberErrorThreshold=None, LatencyMode=None, StatisticsMode=None):
		"""Updates a child instance of delayVariation on the server.

		Args:
			Enabled (bool): If enabled, fetches latency delay variation statistics with average, minimum, and maximum measurements.
			LargeSequenceNumberErrorThreshold (number): The value for the large sequence number error.
			LatencyMode (str(cutThrough|forwardingDelay|mef|storeForward)): If enabled, allows to use Cut Through, Forwarding Delay, MEF, and Store and Forward Delay variation statictics measurements.
			StatisticsMode (str(rxDelayVariationAverage|rxDelayVariationErrorsAndRate|rxDelayVariationMinMaxAndRate)): If enabled, allows to receive delay variation statistics with sequence error measurements.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
