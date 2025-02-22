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


class Rsvp(Base):
	"""Simulates one or more RSVP ingress or egress routers. Concentrates on Traffic Engineering parameters.
	The Rsvp class encapsulates a required rsvp resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'rsvp'

	def __init__(self, parent):
		super(Rsvp, self).__init__(parent)

	@property
	def NeighborPair(self):
		"""An instance of the NeighborPair class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.neighborpair_y29scy9yc3zwl25lawdoym9yugfpcg.NeighborPair)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.neighborpair_y29scy9yc3zwl25lawdoym9yugfpcg import NeighborPair
		return NeighborPair(self)

	@property
	def EnableBgpOverLsp(self):
		"""DEPRECATED Enables the ability to exchange labels over LSP for VPNs.

		Returns:
			bool
		"""
		return self._get_attribute('enableBgpOverLsp')
	@EnableBgpOverLsp.setter
	def EnableBgpOverLsp(self, value):
		self._set_attribute('enableBgpOverLsp', value)

	@property
	def EnableControlLspInitiationRate(self):
		"""Controls the LSP initiation rate.

		Returns:
			bool
		"""
		return self._get_attribute('enableControlLspInitiationRate')
	@EnableControlLspInitiationRate.setter
	def EnableControlLspInitiationRate(self, value):
		self._set_attribute('enableControlLspInitiationRate', value)

	@property
	def EnableShowTimeValue(self):
		"""If true, allows to calculate LSP/sub LSP setup time. When a first path message is sent for an LSP or sub LSP, the state machine takes the time stamp and stores it in the internal structure. It repeats this, when a reserve message is received for that LSP or sub LSP.

		Returns:
			bool
		"""
		return self._get_attribute('enableShowTimeValue')
	@EnableShowTimeValue.setter
	def EnableShowTimeValue(self, value):
		self._set_attribute('enableShowTimeValue', value)

	@property
	def EnableVpnLabelExchangeOverLsp(self):
		"""If true, enables VPN label exchange over LSP

		Returns:
			bool
		"""
		return self._get_attribute('enableVpnLabelExchangeOverLsp')
	@EnableVpnLabelExchangeOverLsp.setter
	def EnableVpnLabelExchangeOverLsp(self, value):
		self._set_attribute('enableVpnLabelExchangeOverLsp', value)

	@property
	def Enabled(self):
		"""Enables or disables the use of this emulated RSVP router in the emulated RSVP network. (default = disabled)

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def MaxLspInitiationsPerSec(self):
		"""The maximum number of LSP Initiations sent per second.

		Returns:
			number
		"""
		return self._get_attribute('maxLspInitiationsPerSec')
	@MaxLspInitiationsPerSec.setter
	def MaxLspInitiationsPerSec(self, value):
		self._set_attribute('maxLspInitiationsPerSec', value)

	@property
	def RunningState(self):
		"""The current running state of the RSVP server.

		Returns:
			str(unknown|stopped|stopping|starting|started)
		"""
		return self._get_attribute('runningState')

	@property
	def UseTransportLabelsForMplsOam(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('useTransportLabelsForMplsOam')
	@UseTransportLabelsForMplsOam.setter
	def UseTransportLabelsForMplsOam(self, value):
		self._set_attribute('useTransportLabelsForMplsOam', value)

	def update(self, EnableBgpOverLsp=None, EnableControlLspInitiationRate=None, EnableShowTimeValue=None, EnableVpnLabelExchangeOverLsp=None, Enabled=None, MaxLspInitiationsPerSec=None, UseTransportLabelsForMplsOam=None):
		"""Updates a child instance of rsvp on the server.

		Args:
			EnableBgpOverLsp (bool): Enables the ability to exchange labels over LSP for VPNs.
			EnableControlLspInitiationRate (bool): Controls the LSP initiation rate.
			EnableShowTimeValue (bool): If true, allows to calculate LSP/sub LSP setup time. When a first path message is sent for an LSP or sub LSP, the state machine takes the time stamp and stores it in the internal structure. It repeats this, when a reserve message is received for that LSP or sub LSP.
			EnableVpnLabelExchangeOverLsp (bool): If true, enables VPN label exchange over LSP
			Enabled (bool): Enables or disables the use of this emulated RSVP router in the emulated RSVP network. (default = disabled)
			MaxLspInitiationsPerSec (number): The maximum number of LSP Initiations sent per second.
			UseTransportLabelsForMplsOam (bool): NOT DEFINED

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def Start(self):
		"""Executes the start operation on the server.

		Starts RSVP on a port or a group of ports.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('start', payload=payload, response_object=None)

	def Stop(self):
		"""Executes the stop operation on the server.

		Stops RSVP on a port or group of ports.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('stop', payload=payload, response_object=None)
