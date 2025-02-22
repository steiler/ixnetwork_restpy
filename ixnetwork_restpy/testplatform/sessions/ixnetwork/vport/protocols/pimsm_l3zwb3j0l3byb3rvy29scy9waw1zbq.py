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


class Pimsm(Base):
	"""This object simulates one or more PIM-SM routers in a network of routers.
	The Pimsm class encapsulates a required pimsm resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'pimsm'

	def __init__(self, parent):
		super(Pimsm, self).__init__(parent)

	@property
	def Router(self):
		"""An instance of the Router class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_3byb3rvy29scy9waw1zbs9yb3v0zxi.Router)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_3byb3rvy29scy9waw1zbs9yb3v0zxi import Router
		return Router(self)

	@property
	def BsmFramePerInterval(self):
		"""Allows to specify the rate of the number of BSM messages to be sent per interval. Note: This field is enabled only after enabling Rate Control interval.

		Returns:
			number
		"""
		return self._get_attribute('bsmFramePerInterval')
	@BsmFramePerInterval.setter
	def BsmFramePerInterval(self, value):
		self._set_attribute('bsmFramePerInterval', value)

	@property
	def CrpFramePerInterval(self):
		"""Allows to specify the rate of the number of CRP Adv messages to be sent per interval. Note: This field is enabled only after enabling Rate Control interval.

		Returns:
			number
		"""
		return self._get_attribute('crpFramePerInterval')
	@CrpFramePerInterval.setter
	def CrpFramePerInterval(self, value):
		self._set_attribute('crpFramePerInterval', value)

	@property
	def DataMdtFramePerInterval(self):
		"""The number of Data MST message to be sent per interval specified in the interval field below. The default value is 0, which means that messages will be sent on a best effort basis.

		Returns:
			number
		"""
		return self._get_attribute('dataMdtFramePerInterval')
	@DataMdtFramePerInterval.setter
	def DataMdtFramePerInterval(self, value):
		self._set_attribute('dataMdtFramePerInterval', value)

	@property
	def DenyGrePimIpPrefix(self):
		"""Ixia will reject all GRE-PIM packets whose outer source IP address falls within this specified network prefix.

		Returns:
			str
		"""
		return self._get_attribute('denyGrePimIpPrefix')
	@DenyGrePimIpPrefix.setter
	def DenyGrePimIpPrefix(self, value):
		self._set_attribute('denyGrePimIpPrefix', value)

	@property
	def EnableDiscardJoinPruneProcessing(self):
		"""If enabled, discards the join/prune messages.

		Returns:
			bool
		"""
		return self._get_attribute('enableDiscardJoinPruneProcessing')
	@EnableDiscardJoinPruneProcessing.setter
	def EnableDiscardJoinPruneProcessing(self, value):
		self._set_attribute('enableDiscardJoinPruneProcessing', value)

	@property
	def EnableRateControl(self):
		"""Rate control (flow control) is enabled on this PIM-SM port.

		Returns:
			bool
		"""
		return self._get_attribute('enableRateControl')
	@EnableRateControl.setter
	def EnableRateControl(self, value):
		self._set_attribute('enableRateControl', value)

	@property
	def Enabled(self):
		"""Enables the emulated PIM-SM router.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def GreFilterType(self):
		"""Specifies type of filter for GRE.

		Returns:
			str(noDataMdt|dataMdtIpv4)
		"""
		return self._get_attribute('greFilterType')
	@GreFilterType.setter
	def GreFilterType(self, value):
		self._set_attribute('greFilterType', value)

	@property
	def HelloMsgsPerInterval(self):
		"""The total hello messages received per interval.

		Returns:
			number
		"""
		return self._get_attribute('helloMsgsPerInterval')
	@HelloMsgsPerInterval.setter
	def HelloMsgsPerInterval(self, value):
		self._set_attribute('helloMsgsPerInterval', value)

	@property
	def Interval(self):
		"""The length of the interval during which a number of messages are sent. The default value is 0, which means that messages will be sent on a best effort basis.

		Returns:
			number
		"""
		return self._get_attribute('interval')
	@Interval.setter
	def Interval(self, value):
		self._set_attribute('interval', value)

	@property
	def JoinPruneMessagesPerInterval(self):
		"""The join/prune interval specifies the length of time between transmissions of join/prune messages.The default is 60 seconds.

		Returns:
			number
		"""
		return self._get_attribute('joinPruneMessagesPerInterval')
	@JoinPruneMessagesPerInterval.setter
	def JoinPruneMessagesPerInterval(self, value):
		self._set_attribute('joinPruneMessagesPerInterval', value)

	@property
	def OverrideSourceIpForSmInterface(self):
		"""If enabled, it will override source ip for SM interfaces.

		Returns:
			bool
		"""
		return self._get_attribute('overrideSourceIpForSmInterface')
	@OverrideSourceIpForSmInterface.setter
	def OverrideSourceIpForSmInterface(self, value):
		self._set_attribute('overrideSourceIpForSmInterface', value)

	@property
	def RegisterMessagesPerInterval(self):
		"""The number of Register messages to be sent per interval specified in the Interval field below. The default value is 0, which means that messages will be sent on a best effort basis.

		Returns:
			number
		"""
		return self._get_attribute('registerMessagesPerInterval')
	@RegisterMessagesPerInterval.setter
	def RegisterMessagesPerInterval(self, value):
		self._set_attribute('registerMessagesPerInterval', value)

	@property
	def RegisterStopMessagesPerInterval(self):
		"""The number of Register messages to be sent per interval specified in the Interval field below. The default value is 0, which means that messages will be sent on a best effort basis.

		Returns:
			number
		"""
		return self._get_attribute('registerStopMessagesPerInterval')
	@RegisterStopMessagesPerInterval.setter
	def RegisterStopMessagesPerInterval(self, value):
		self._set_attribute('registerStopMessagesPerInterval', value)

	@property
	def RunningState(self):
		"""The current running state of the PIM-SM server.

		Returns:
			str(unknown|stopped|stopping|starting|started)
		"""
		return self._get_attribute('runningState')

	def update(self, BsmFramePerInterval=None, CrpFramePerInterval=None, DataMdtFramePerInterval=None, DenyGrePimIpPrefix=None, EnableDiscardJoinPruneProcessing=None, EnableRateControl=None, Enabled=None, GreFilterType=None, HelloMsgsPerInterval=None, Interval=None, JoinPruneMessagesPerInterval=None, OverrideSourceIpForSmInterface=None, RegisterMessagesPerInterval=None, RegisterStopMessagesPerInterval=None):
		"""Updates a child instance of pimsm on the server.

		Args:
			BsmFramePerInterval (number): Allows to specify the rate of the number of BSM messages to be sent per interval. Note: This field is enabled only after enabling Rate Control interval.
			CrpFramePerInterval (number): Allows to specify the rate of the number of CRP Adv messages to be sent per interval. Note: This field is enabled only after enabling Rate Control interval.
			DataMdtFramePerInterval (number): The number of Data MST message to be sent per interval specified in the interval field below. The default value is 0, which means that messages will be sent on a best effort basis.
			DenyGrePimIpPrefix (str): Ixia will reject all GRE-PIM packets whose outer source IP address falls within this specified network prefix.
			EnableDiscardJoinPruneProcessing (bool): If enabled, discards the join/prune messages.
			EnableRateControl (bool): Rate control (flow control) is enabled on this PIM-SM port.
			Enabled (bool): Enables the emulated PIM-SM router.
			GreFilterType (str(noDataMdt|dataMdtIpv4)): Specifies type of filter for GRE.
			HelloMsgsPerInterval (number): The total hello messages received per interval.
			Interval (number): The length of the interval during which a number of messages are sent. The default value is 0, which means that messages will be sent on a best effort basis.
			JoinPruneMessagesPerInterval (number): The join/prune interval specifies the length of time between transmissions of join/prune messages.The default is 60 seconds.
			OverrideSourceIpForSmInterface (bool): If enabled, it will override source ip for SM interfaces.
			RegisterMessagesPerInterval (number): The number of Register messages to be sent per interval specified in the Interval field below. The default value is 0, which means that messages will be sent on a best effort basis.
			RegisterStopMessagesPerInterval (number): The number of Register messages to be sent per interval specified in the Interval field below. The default value is 0, which means that messages will be sent on a best effort basis.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def Start(self):
		"""Executes the start operation on the server.

		Starts the PIMSM protocol on a port or group of ports simultaneously.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('start', payload=payload, response_object=None)

	def Stop(self):
		"""Executes the stop operation on the server.

		Stops the PIMSM protocol on a port or group of ports simultaneously.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('stop', payload=payload, response_object=None)
