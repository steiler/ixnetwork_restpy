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


class AccumulateAndBurst(Base):
	"""Accumulates packets in a queue and transmit groups of packets as a burst. It can only be used on a profile if delayVariation and customDelayVariation are disabled.
	The AccumulateAndBurst class encapsulates a required accumulateAndBurst resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'accumulateAndBurst'

	def __init__(self, parent):
		super(AccumulateAndBurst, self).__init__(parent)

	@property
	def BurstSize(self):
		"""Represents the burst octet size. The default value is 1014.

		Returns:
			number
		"""
		return self._get_attribute('burstSize')
	@BurstSize.setter
	def BurstSize(self, value):
		self._set_attribute('burstSize', value)

	@property
	def BurstSizeUnit(self):
		"""The burst size unit is either megabytes or kilobytes. The default unit is kilobytes.

		Returns:
			str(kilobytes|kKilobytes|kMegabytes|megabytes)
		"""
		return self._get_attribute('burstSizeUnit')
	@BurstSizeUnit.setter
	def BurstSizeUnit(self, value):
		self._set_attribute('burstSizeUnit', value)

	@property
	def BurstTimeout(self):
		"""The burst timeout.The default value is 5 seconds.

		Returns:
			str
		"""
		return self._get_attribute('burstTimeout')
	@BurstTimeout.setter
	def BurstTimeout(self, value):
		self._set_attribute('burstTimeout', value)

	@property
	def BurstTimeoutUnit(self):
		"""Seconds(default) / milliseconds / mm:ss.fff time format.

		Returns:
			str(kMilliseconds|kSeconds|kTimeFormat|milliseconds|seconds|timeFormat)
		"""
		return self._get_attribute('burstTimeoutUnit')
	@BurstTimeoutUnit.setter
	def BurstTimeoutUnit(self, value):
		self._set_attribute('burstTimeoutUnit', value)

	@property
	def Enabled(self):
		"""If true, received packets are queued and transmitted in bursts.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def InterBurstGap(self):
		"""Tail to head (default) / Head to head.

		Returns:
			str(headToHead|kHeadToHead|kTailToHead|tailToHead)
		"""
		return self._get_attribute('interBurstGap')
	@InterBurstGap.setter
	def InterBurstGap(self, value):
		self._set_attribute('interBurstGap', value)

	@property
	def InterBurstGapValue(self):
		"""The InterBurst gap value. The default value is 20 ms.

		Returns:
			number
		"""
		return self._get_attribute('interBurstGapValue')
	@InterBurstGapValue.setter
	def InterBurstGapValue(self, value):
		self._set_attribute('interBurstGapValue', value)

	@property
	def InterBurstGapValueUnit(self):
		"""Seconds / milliseconds (default).

		Returns:
			str(kMilliseconds|kSeconds|milliseconds|seconds)
		"""
		return self._get_attribute('interBurstGapValueUnit')
	@InterBurstGapValueUnit.setter
	def InterBurstGapValueUnit(self, value):
		self._set_attribute('interBurstGapValueUnit', value)

	@property
	def PacketCount(self):
		"""Represents the burst packet count. The default value is 1000 packets.

		Returns:
			number
		"""
		return self._get_attribute('packetCount')
	@PacketCount.setter
	def PacketCount(self, value):
		self._set_attribute('packetCount', value)

	@property
	def QueueAutoSize(self):
		"""Gets the automatically calculated queue size when queueAutoSizeEnable is true or zero when queueAutoSizeEnable is false.

		Returns:
			number
		"""
		return self._get_attribute('queueAutoSize')

	@property
	def QueueAutoSizeEnabled(self):
		"""Automatically calculate queue size. The default value is true.

		Returns:
			bool
		"""
		return self._get_attribute('queueAutoSizeEnabled')
	@QueueAutoSizeEnabled.setter
	def QueueAutoSizeEnabled(self, value):
		self._set_attribute('queueAutoSizeEnabled', value)

	@property
	def QueueSize(self):
		"""The accumulate-and-burst queue size expressed in MB. The default value is 1.

		Returns:
			number
		"""
		return self._get_attribute('queueSize')
	@QueueSize.setter
	def QueueSize(self, value):
		self._set_attribute('queueSize', value)

	def update(self, BurstSize=None, BurstSizeUnit=None, BurstTimeout=None, BurstTimeoutUnit=None, Enabled=None, InterBurstGap=None, InterBurstGapValue=None, InterBurstGapValueUnit=None, PacketCount=None, QueueAutoSizeEnabled=None, QueueSize=None):
		"""Updates a child instance of accumulateAndBurst on the server.

		Args:
			BurstSize (number): Represents the burst octet size. The default value is 1014.
			BurstSizeUnit (str(kilobytes|kKilobytes|kMegabytes|megabytes)): The burst size unit is either megabytes or kilobytes. The default unit is kilobytes.
			BurstTimeout (str): The burst timeout.The default value is 5 seconds.
			BurstTimeoutUnit (str(kMilliseconds|kSeconds|kTimeFormat|milliseconds|seconds|timeFormat)): Seconds(default) / milliseconds / mm:ss.fff time format.
			Enabled (bool): If true, received packets are queued and transmitted in bursts.
			InterBurstGap (str(headToHead|kHeadToHead|kTailToHead|tailToHead)): Tail to head (default) / Head to head.
			InterBurstGapValue (number): The InterBurst gap value. The default value is 20 ms.
			InterBurstGapValueUnit (str(kMilliseconds|kSeconds|milliseconds|seconds)): Seconds / milliseconds (default).
			PacketCount (number): Represents the burst packet count. The default value is 1000 packets.
			QueueAutoSizeEnabled (bool): Automatically calculate queue size. The default value is true.
			QueueSize (number): The accumulate-and-burst queue size expressed in MB. The default value is 1.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
