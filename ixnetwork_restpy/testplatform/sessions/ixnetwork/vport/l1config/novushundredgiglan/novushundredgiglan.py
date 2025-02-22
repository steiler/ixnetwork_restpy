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


class NovusHundredGigLan(Base):
	"""Novus 100GE LAN port.
	The NovusHundredGigLan class encapsulates a required novusHundredGigLan resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'novusHundredGigLan'

	def __init__(self, parent):
		super(NovusHundredGigLan, self).__init__(parent)

	@property
	def Fcoe(self):
		"""An instance of the Fcoe class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novushundredgiglan.fcoe.fcoe.Fcoe)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novushundredgiglan.fcoe.fcoe import Fcoe
		return Fcoe(self)._select()

	@property
	def TxLane(self):
		"""An instance of the TxLane class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novushundredgiglan.txlane.txlane.TxLane)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novushundredgiglan.txlane.txlane import TxLane
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
	def BadBlocksNumber(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('badBlocksNumber')
	@BadBlocksNumber.setter
	def BadBlocksNumber(self, value):
		self._set_attribute('badBlocksNumber', value)

	@property
	def EnableAutoNegotiation(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('enableAutoNegotiation')
	@EnableAutoNegotiation.setter
	def EnableAutoNegotiation(self, value):
		self._set_attribute('enableAutoNegotiation', value)

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
	def EnableRsFec(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('enableRsFec')
	@EnableRsFec.setter
	def EnableRsFec(self, value):
		self._set_attribute('enableRsFec', value)

	@property
	def EnableRsFecStats(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('enableRsFecStats')
	@EnableRsFecStats.setter
	def EnableRsFecStats(self, value):
		self._set_attribute('enableRsFecStats', value)

	@property
	def EnabledFlowControl(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('enabledFlowControl')
	@EnabledFlowControl.setter
	def EnabledFlowControl(self, value):
		self._set_attribute('enabledFlowControl', value)

	@property
	def FirecodeAdvertise(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('firecodeAdvertise')
	@FirecodeAdvertise.setter
	def FirecodeAdvertise(self, value):
		self._set_attribute('firecodeAdvertise', value)

	@property
	def FirecodeForceOff(self):
		"""DEPRECATED NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('firecodeForceOff')
	@FirecodeForceOff.setter
	def FirecodeForceOff(self, value):
		self._set_attribute('firecodeForceOff', value)

	@property
	def FirecodeForceOn(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('firecodeForceOn')
	@FirecodeForceOn.setter
	def FirecodeForceOn(self, value):
		self._set_attribute('firecodeForceOn', value)

	@property
	def FirecodeRequest(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('firecodeRequest')
	@FirecodeRequest.setter
	def FirecodeRequest(self, value):
		self._set_attribute('firecodeRequest', value)

	@property
	def FlowControlDirectedAddress(self):
		"""The 48-bit MAC address that the port listens on for a directed pause.

		Returns:
			str
		"""
		return self._get_attribute('flowControlDirectedAddress')
	@FlowControlDirectedAddress.setter
	def FlowControlDirectedAddress(self, value):
		self._set_attribute('flowControlDirectedAddress', value)

	@property
	def ForceDisableFEC(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('forceDisableFEC')
	@ForceDisableFEC.setter
	def ForceDisableFEC(self, value):
		self._set_attribute('forceDisableFEC', value)

	@property
	def GoodBlocksNumber(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('goodBlocksNumber')
	@GoodBlocksNumber.setter
	def GoodBlocksNumber(self, value):
		self._set_attribute('goodBlocksNumber', value)

	@property
	def IeeeL1Defaults(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('ieeeL1Defaults')
	@IeeeL1Defaults.setter
	def IeeeL1Defaults(self, value):
		self._set_attribute('ieeeL1Defaults', value)

	@property
	def LaserOn(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('laserOn')
	@LaserOn.setter
	def LaserOn(self, value):
		self._set_attribute('laserOn', value)

	@property
	def LinkTraining(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('linkTraining')

	@property
	def LoopContinuously(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('loopContinuously')
	@LoopContinuously.setter
	def LoopContinuously(self, value):
		self._set_attribute('loopContinuously', value)

	@property
	def LoopCountNumber(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('loopCountNumber')
	@LoopCountNumber.setter
	def LoopCountNumber(self, value):
		self._set_attribute('loopCountNumber', value)

	@property
	def Loopback(self):
		"""If enabled, the port is set to internally loopback from transmit to receive.

		Returns:
			bool
		"""
		return self._get_attribute('loopback')
	@Loopback.setter
	def Loopback(self, value):
		self._set_attribute('loopback', value)

	@property
	def LoopbackMode(self):
		"""NOT DEFINED

		Returns:
			str(internalLoopback|lineLoopback|none)
		"""
		return self._get_attribute('loopbackMode')
	@LoopbackMode.setter
	def LoopbackMode(self, value):
		self._set_attribute('loopbackMode', value)

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
	def RsFecAdvertise(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('rsFecAdvertise')
	@RsFecAdvertise.setter
	def RsFecAdvertise(self, value):
		self._set_attribute('rsFecAdvertise', value)

	@property
	def RsFecForceOn(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('rsFecForceOn')
	@RsFecForceOn.setter
	def RsFecForceOn(self, value):
		self._set_attribute('rsFecForceOn', value)

	@property
	def RsFecRequest(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('rsFecRequest')
	@RsFecRequest.setter
	def RsFecRequest(self, value):
		self._set_attribute('rsFecRequest', value)

	@property
	def SendSetsMode(self):
		"""NOT DEFINED

		Returns:
			str(alternate|typeAOnly|typeBOnly)
		"""
		return self._get_attribute('sendSetsMode')
	@SendSetsMode.setter
	def SendSetsMode(self, value):
		self._set_attribute('sendSetsMode', value)

	@property
	def Speed(self):
		"""NOT DEFINED

		Returns:
			str(speed100g|speed10g|speed25g|speed40g|speed50g)
		"""
		return self._get_attribute('speed')
	@Speed.setter
	def Speed(self, value):
		self._set_attribute('speed', value)

	@property
	def StartErrorInsertion(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('startErrorInsertion')
	@StartErrorInsertion.setter
	def StartErrorInsertion(self, value):
		self._set_attribute('startErrorInsertion', value)

	@property
	def TxIgnoreRxLinkFaults(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('txIgnoreRxLinkFaults')
	@TxIgnoreRxLinkFaults.setter
	def TxIgnoreRxLinkFaults(self, value):
		self._set_attribute('txIgnoreRxLinkFaults', value)

	@property
	def TypeAOrderedSets(self):
		"""NOT DEFINED

		Returns:
			str(localFault|remoteFault)
		"""
		return self._get_attribute('typeAOrderedSets')
	@TypeAOrderedSets.setter
	def TypeAOrderedSets(self, value):
		self._set_attribute('typeAOrderedSets', value)

	@property
	def TypeBOrderedSets(self):
		"""NOT DEFINED

		Returns:
			str(localFault|remoteFault)
		"""
		return self._get_attribute('typeBOrderedSets')
	@TypeBOrderedSets.setter
	def TypeBOrderedSets(self, value):
		self._set_attribute('typeBOrderedSets', value)

	@property
	def UseANResults(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('useANResults')
	@UseANResults.setter
	def UseANResults(self, value):
		self._set_attribute('useANResults', value)

	def update(self, AutoInstrumentation=None, BadBlocksNumber=None, EnableAutoNegotiation=None, EnablePPM=None, EnableRsFec=None, EnableRsFecStats=None, EnabledFlowControl=None, FirecodeAdvertise=None, FirecodeForceOff=None, FirecodeForceOn=None, FirecodeRequest=None, FlowControlDirectedAddress=None, ForceDisableFEC=None, GoodBlocksNumber=None, IeeeL1Defaults=None, LaserOn=None, LoopContinuously=None, LoopCountNumber=None, Loopback=None, LoopbackMode=None, Ppm=None, RsFecAdvertise=None, RsFecForceOn=None, RsFecRequest=None, SendSetsMode=None, Speed=None, StartErrorInsertion=None, TxIgnoreRxLinkFaults=None, TypeAOrderedSets=None, TypeBOrderedSets=None, UseANResults=None):
		"""Updates a child instance of novusHundredGigLan on the server.

		Args:
			AutoInstrumentation (str(endOfFrame|floating)): The auto instrumentation mode.
			BadBlocksNumber (number): NOT DEFINED
			EnableAutoNegotiation (bool): NOT DEFINED
			EnablePPM (bool): If true, enables the portsppm.
			EnableRsFec (bool): NOT DEFINED
			EnableRsFecStats (bool): NOT DEFINED
			EnabledFlowControl (bool): NOT DEFINED
			FirecodeAdvertise (bool): NOT DEFINED
			FirecodeForceOff (bool): NOT DEFINED
			FirecodeForceOn (bool): NOT DEFINED
			FirecodeRequest (bool): NOT DEFINED
			FlowControlDirectedAddress (str): The 48-bit MAC address that the port listens on for a directed pause.
			ForceDisableFEC (bool): NOT DEFINED
			GoodBlocksNumber (number): NOT DEFINED
			IeeeL1Defaults (bool): NOT DEFINED
			LaserOn (bool): NOT DEFINED
			LoopContinuously (bool): NOT DEFINED
			LoopCountNumber (number): NOT DEFINED
			Loopback (bool): If enabled, the port is set to internally loopback from transmit to receive.
			LoopbackMode (str(internalLoopback|lineLoopback|none)): NOT DEFINED
			Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency.
			RsFecAdvertise (bool): NOT DEFINED
			RsFecForceOn (bool): NOT DEFINED
			RsFecRequest (bool): NOT DEFINED
			SendSetsMode (str(alternate|typeAOnly|typeBOnly)): NOT DEFINED
			Speed (str(speed100g|speed10g|speed25g|speed40g|speed50g)): NOT DEFINED
			StartErrorInsertion (bool): NOT DEFINED
			TxIgnoreRxLinkFaults (bool): NOT DEFINED
			TypeAOrderedSets (str(localFault|remoteFault)): NOT DEFINED
			TypeBOrderedSets (str(localFault|remoteFault)): NOT DEFINED
			UseANResults (bool): NOT DEFINED

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
