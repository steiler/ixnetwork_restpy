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


class Ethernetvm(Base):
	"""Layer 1 Configuration for Ethernet VM
	The Ethernetvm class encapsulates a required ethernetvm resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'ethernetvm'

	def __init__(self, parent):
		super(Ethernetvm, self).__init__(parent)

	@property
	def AutoInstrumentation(self):
		"""NOT DEFINED

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

	@property
	def Loopback(self):
		"""If true, enables the ports ppm

		Returns:
			bool
		"""
		return self._get_attribute('loopback')
	@Loopback.setter
	def Loopback(self, value):
		self._set_attribute('loopback', value)

	@property
	def Mtu(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('mtu')
	@Mtu.setter
	def Mtu(self, value):
		self._set_attribute('mtu', value)

	@property
	def Ppm(self):
		"""Indicates the value that needs to be adjusted for the line transmit frequency

		Returns:
			number
		"""
		return self._get_attribute('ppm')

	@property
	def PromiscuousMode(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('promiscuousMode')
	@PromiscuousMode.setter
	def PromiscuousMode(self, value):
		self._set_attribute('promiscuousMode', value)

	@property
	def Speed(self):
		"""Select one of the enums to set the speed of the ethernet vm

		Returns:
			str(speed100|speed1000|speed10g|speed2000|speed20g|speed25g|speed3000|speed30g|speed4000|speed40g|speed5000|speed50g|speed6000|speed7000|speed8000|speed9000)
		"""
		return self._get_attribute('speed')
	@Speed.setter
	def Speed(self, value):
		self._set_attribute('speed', value)

	def update(self, AutoInstrumentation=None, Loopback=None, Mtu=None, PromiscuousMode=None, Speed=None):
		"""Updates a child instance of ethernetvm on the server.

		Args:
			AutoInstrumentation (str(endOfFrame|floating)): NOT DEFINED
			Loopback (bool): If true, enables the ports ppm
			Mtu (number): 
			PromiscuousMode (bool): 
			Speed (str(speed100|speed1000|speed10g|speed2000|speed20g|speed25g|speed3000|speed30g|speed4000|speed40g|speed5000|speed50g|speed6000|speed7000|speed8000|speed9000)): Select one of the enums to set the speed of the ethernet vm

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
