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


class Dcc(Base):
	"""The Layer 1 Configuration is being configured for a POS port and DCC is selected as the Payload Type.
	The Dcc class encapsulates a required dcc resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'dcc'

	def __init__(self, parent):
		super(Dcc, self).__init__(parent)

	@property
	def Crc(self):
		"""Choose the type of Cyclic Redundancy Check to be used.

		Returns:
			str(crc16|crc32)
		"""
		return self._get_attribute('crc')
	@Crc.setter
	def Crc(self, value):
		self._set_attribute('crc', value)

	@property
	def OverheadByte(self):
		"""Choose the type of Overhead bytes to be used for transmitting the DCC packet streams.

		Returns:
			str(loh|soh)
		"""
		return self._get_attribute('overheadByte')
	@OverheadByte.setter
	def OverheadByte(self, value):
		self._set_attribute('overheadByte', value)

	@property
	def TimeFill(self):
		"""Choose the type of bytes used to fill the gaps between DCC frames.

		Returns:
			str(flag7E|markIdle)
		"""
		return self._get_attribute('timeFill')
	@TimeFill.setter
	def TimeFill(self, value):
		self._set_attribute('timeFill', value)

	def update(self, Crc=None, OverheadByte=None, TimeFill=None):
		"""Updates a child instance of dcc on the server.

		Args:
			Crc (str(crc16|crc32)): Choose the type of Cyclic Redundancy Check to be used.
			OverheadByte (str(loh|soh)): Choose the type of Overhead bytes to be used for transmitting the DCC packet streams.
			TimeFill (str(flag7E|markIdle)): Choose the type of bytes used to fill the gaps between DCC frames.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
