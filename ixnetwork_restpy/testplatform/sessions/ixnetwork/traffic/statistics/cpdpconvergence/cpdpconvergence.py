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


class CpdpConvergence(Base):
	"""This object fetches the control plane and data plane statistics.
	The CpdpConvergence class encapsulates a required cpdpConvergence resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'cpdpConvergence'

	def __init__(self, parent):
		super(CpdpConvergence, self).__init__(parent)

	@property
	def DataPlaneJitterWindow(self):
		"""Indicates the number of packets received during a time interval. This is used forcalculating the rate on the recieve side.

		Returns:
			str(0|10485760|1310720|167772160|20971520|2621440|335544320|41943040|5242880|671088640|83886080)
		"""
		return self._get_attribute('dataPlaneJitterWindow')
	@DataPlaneJitterWindow.setter
	def DataPlaneJitterWindow(self, value):
		self._set_attribute('dataPlaneJitterWindow', value)

	@property
	def DataPlaneThreshold(self):
		"""The data loss threshold percentage for CP/DP events at the prompt.

		Returns:
			number
		"""
		return self._get_attribute('dataPlaneThreshold')
	@DataPlaneThreshold.setter
	def DataPlaneThreshold(self, value):
		self._set_attribute('dataPlaneThreshold', value)

	@property
	def EnableControlPlaneEvents(self):
		"""If enabled, fetches control plane event statistics of event name, event start timestamp, and event end timestamp.

		Returns:
			bool
		"""
		return self._get_attribute('enableControlPlaneEvents')
	@EnableControlPlaneEvents.setter
	def EnableControlPlaneEvents(self, value):
		self._set_attribute('enableControlPlaneEvents', value)

	@property
	def EnableDataPlaneEventsRateMonitor(self):
		"""If enabled, fetches data plane event rate statistics of DP above Threshold Timestamp, DP below Threshold Timestamp, Ramp Up Convergence, Ramp Down Convergence, CP/DP Convergence, and DP/DP Convergence.

		Returns:
			bool
		"""
		return self._get_attribute('enableDataPlaneEventsRateMonitor')
	@EnableDataPlaneEventsRateMonitor.setter
	def EnableDataPlaneEventsRateMonitor(self, value):
		self._set_attribute('enableDataPlaneEventsRateMonitor', value)

	@property
	def Enabled(self):
		"""If enabled, fetches control plane/data plane statistics.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	def update(self, DataPlaneJitterWindow=None, DataPlaneThreshold=None, EnableControlPlaneEvents=None, EnableDataPlaneEventsRateMonitor=None, Enabled=None):
		"""Updates a child instance of cpdpConvergence on the server.

		Args:
			DataPlaneJitterWindow (str(0|10485760|1310720|167772160|20971520|2621440|335544320|41943040|5242880|671088640|83886080)): Indicates the number of packets received during a time interval. This is used forcalculating the rate on the recieve side.
			DataPlaneThreshold (number): The data loss threshold percentage for CP/DP events at the prompt.
			EnableControlPlaneEvents (bool): If enabled, fetches control plane event statistics of event name, event start timestamp, and event end timestamp.
			EnableDataPlaneEventsRateMonitor (bool): If enabled, fetches data plane event rate statistics of DP above Threshold Timestamp, DP below Threshold Timestamp, Ramp Up Convergence, Ramp Down Convergence, CP/DP Convergence, and DP/DP Convergence.
			Enabled (bool): If enabled, fetches control plane/data plane statistics.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
