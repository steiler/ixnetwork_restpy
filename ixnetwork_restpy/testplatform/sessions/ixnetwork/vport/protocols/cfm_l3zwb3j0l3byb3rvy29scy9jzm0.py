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


class Cfm(Base):
	"""This object contains the configuration of the CFM protocol.
	The Cfm class encapsulates a required cfm resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'cfm'

	def __init__(self, parent):
		super(Cfm, self).__init__(parent)

	@property
	def Bridge(self):
		"""An instance of the Bridge class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bridge_j0l3byb3rvy29scy9jzm0vynjpzgdl.Bridge)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bridge_j0l3byb3rvy29scy9jzm0vynjpzgdl import Bridge
		return Bridge(self)

	@property
	def EnableOptionalLmFunctionality(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('enableOptionalLmFunctionality')
	@EnableOptionalLmFunctionality.setter
	def EnableOptionalLmFunctionality(self, value):
		self._set_attribute('enableOptionalLmFunctionality', value)

	@property
	def EnableOptionalTlvValidation(self):
		"""If true, the CFM protocol will validate optional TLVs present in CFM packets.

		Returns:
			bool
		"""
		return self._get_attribute('enableOptionalTlvValidation')
	@EnableOptionalTlvValidation.setter
	def EnableOptionalTlvValidation(self, value):
		self._set_attribute('enableOptionalTlvValidation', value)

	@property
	def Enabled(self):
		"""If true, the CFM protcol is enabled.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def ReceiveCcm(self):
		"""If true, the CFM protocol can receive CFM CCMs on this port.

		Returns:
			bool
		"""
		return self._get_attribute('receiveCcm')
	@ReceiveCcm.setter
	def ReceiveCcm(self, value):
		self._set_attribute('receiveCcm', value)

	@property
	def RunningState(self):
		"""The current running state of the CFM protocol.

		Returns:
			str(unknown|stopped|stopping|starting|started)
		"""
		return self._get_attribute('runningState')

	@property
	def SendCcm(self):
		"""If true, the CFM protocol can send CFM CCMs from this port.

		Returns:
			bool
		"""
		return self._get_attribute('sendCcm')
	@SendCcm.setter
	def SendCcm(self, value):
		self._set_attribute('sendCcm', value)

	@property
	def SuppressErrorsOnAis(self):
		"""If true, the errors on AIS are suopressed.

		Returns:
			bool
		"""
		return self._get_attribute('suppressErrorsOnAis')
	@SuppressErrorsOnAis.setter
	def SuppressErrorsOnAis(self, value):
		self._set_attribute('suppressErrorsOnAis', value)

	def update(self, EnableOptionalLmFunctionality=None, EnableOptionalTlvValidation=None, Enabled=None, ReceiveCcm=None, SendCcm=None, SuppressErrorsOnAis=None):
		"""Updates a child instance of cfm on the server.

		Args:
			EnableOptionalLmFunctionality (bool): NOT DEFINED
			EnableOptionalTlvValidation (bool): If true, the CFM protocol will validate optional TLVs present in CFM packets.
			Enabled (bool): If true, the CFM protcol is enabled.
			ReceiveCcm (bool): If true, the CFM protocol can receive CFM CCMs on this port.
			SendCcm (bool): If true, the CFM protocol can send CFM CCMs from this port.
			SuppressErrorsOnAis (bool): If true, the errors on AIS are suopressed.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def Start(self):
		"""Executes the start operation on the server.

		Starts the CFM protocol on a port or group of ports.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('start', payload=payload, response_object=None)

	def Stop(self):
		"""Executes the stop operation on the server.

		Stops the CFM protocol on a port or group of ports.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('stop', payload=payload, response_object=None)
