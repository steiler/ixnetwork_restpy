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


class HundredGigLan(Base):
	"""100GE LAN port.
	The HundredGigLan class encapsulates a required hundredGigLan resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'hundredGigLan'

	def __init__(self, parent):
		super(HundredGigLan, self).__init__(parent)

	@property
	def Fcoe(self):
		"""An instance of the Fcoe class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.hundredgiglan.fcoe.fcoe.Fcoe)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.hundredgiglan.fcoe.fcoe import Fcoe
		return Fcoe(self)._select()

	@property
	def TxLane(self):
		"""An instance of the TxLane class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.hundredgiglan.txlane.txlane.TxLane)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.hundredgiglan.txlane.txlane import TxLane
		return TxLane(self)._select()

	@property
	def AutoInstrumentation(self):
		"""The auto instrumentation mode.

		Returns:
			str(endOfFrame|floating)
		"""
		return self._get_attribute('autoInstrumentation')
	@AutoInstrumentation.setter
	def AutoInstrumentation(self, value):
		self._set_attribute('autoInstrumentation', value)

	@property
	def EnablePPM(self):
		"""If true, enables the portsppm.

		Returns:
			bool
		"""
		return self._get_attribute('enablePPM')
	@EnablePPM.setter
	def EnablePPM(self, value):
		self._set_attribute('enablePPM', value)

	@property
	def EnabledFlowControl(self):
		"""If true, enables the ports's MAC flow control and mechanisms to listen for a directed address pause message

		Returns:
			bool
		"""
		return self._get_attribute('enabledFlowControl')
	@EnabledFlowControl.setter
	def EnabledFlowControl(self, value):
		self._set_attribute('enabledFlowControl', value)

	@property
	def FlowControlDirectedAddress(self):
		"""the 48 bit MAC address that the port listens on for a directed pause

		Returns:
			str
		"""
		return self._get_attribute('flowControlDirectedAddress')
	@FlowControlDirectedAddress.setter
	def FlowControlDirectedAddress(self, value):
		self._set_attribute('flowControlDirectedAddress', value)

	@property
	def Loopback(self):
		"""The loopback address.

		Returns:
			bool
		"""
		return self._get_attribute('loopback')
	@Loopback.setter
	def Loopback(self, value):
		self._set_attribute('loopback', value)

	@property
	def Ppm(self):
		"""Indicates the value that needs to be adjusted for the line transmit frequency.

		Returns:
			number
		"""
		return self._get_attribute('ppm')
	@Ppm.setter
	def Ppm(self, value):
		self._set_attribute('ppm', value)

	@property
	def Speed(self):
		"""The speed of the lan

		Returns:
			str(speed100g|speed40g)
		"""
		return self._get_attribute('speed')
	@Speed.setter
	def Speed(self, value):
		self._set_attribute('speed', value)

	@property
	def TxIgnoreRxLinkFaults(self):
		"""If enabled, will allow transmission of packets even if the receive link is down.

		Returns:
			bool
		"""
		return self._get_attribute('txIgnoreRxLinkFaults')
	@TxIgnoreRxLinkFaults.setter
	def TxIgnoreRxLinkFaults(self, value):
		self._set_attribute('txIgnoreRxLinkFaults', value)

	def update(self, AutoInstrumentation=None, EnablePPM=None, EnabledFlowControl=None, FlowControlDirectedAddress=None, Loopback=None, Ppm=None, Speed=None, TxIgnoreRxLinkFaults=None):
		"""Updates a child instance of hundredGigLan on the server.

		Args:
			AutoInstrumentation (str(endOfFrame|floating)): The auto instrumentation mode.
			EnablePPM (bool): If true, enables the portsppm.
			EnabledFlowControl (bool): If true, enables the ports's MAC flow control and mechanisms to listen for a directed address pause message
			FlowControlDirectedAddress (str): the 48 bit MAC address that the port listens on for a directed pause
			Loopback (bool): The loopback address.
			Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency.
			Speed (str(speed100g|speed40g)): The speed of the lan
			TxIgnoreRxLinkFaults (bool): If enabled, will allow transmission of packets even if the receive link is down.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
