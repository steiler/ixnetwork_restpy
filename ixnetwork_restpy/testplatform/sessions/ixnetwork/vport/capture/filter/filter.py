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


class Filter(Base):
	"""This object specifies the field properties.
	The Filter class encapsulates a required filter resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'filter'

	def __init__(self, parent):
		super(Filter, self).__init__(parent)

	@property
	def CaptureFilterDA(self):
		"""One of two available destination MAC addresses to filter on. Applicable only when capturefilternable is set to true.

		Returns:
			str(addr1|addr2|anyAddr|notAddr1|notAddr2)
		"""
		return self._get_attribute('captureFilterDA')
	@CaptureFilterDA.setter
	def CaptureFilterDA(self, value):
		self._set_attribute('captureFilterDA', value)

	@property
	def CaptureFilterEnable(self):
		"""Enables or disables the capture filter.

		Returns:
			bool
		"""
		return self._get_attribute('captureFilterEnable')
	@CaptureFilterEnable.setter
	def CaptureFilterEnable(self, value):
		self._set_attribute('captureFilterEnable', value)

	@property
	def CaptureFilterError(self):
		"""Applicable only when captureFilterEnable is set to true.

		Returns:
			str(errAnyFrame|errAnyIpTcpUdpChecksumError|errAnySequencekError|errBadCRC|errBadFrame|errBigSequenceError|errDataIntegrityError|errGoodFrame|errInvalidFcoeFrame|errReverseSequenceError|errSmallSequenceError)
		"""
		return self._get_attribute('captureFilterError')
	@CaptureFilterError.setter
	def CaptureFilterError(self, value):
		self._set_attribute('captureFilterError', value)

	@property
	def CaptureFilterExpressionString(self):
		"""String composed of SA1, DA1, P1, P2, optionally negated with '!', and connected with operators 'and', 'or', 'xor', 'nand' or 'nor'. (Eg: {DA1 and SA1 or !P1 and P2} ). NOTE: The 'or', 'xor', 'nand' and 'nor' operators are available only on the following load modules: XMVDC, NGY, XMSP12, LAVA(MK), Xcellon AP, Xcellon NP.

		Returns:
			str
		"""
		return self._get_attribute('captureFilterExpressionString')
	@CaptureFilterExpressionString.setter
	def CaptureFilterExpressionString(self, value):
		self._set_attribute('captureFilterExpressionString', value)

	@property
	def CaptureFilterFrameSizeEnable(self):
		"""Enables or disables the frame size constraint which specifies a range of frame.

		Returns:
			bool
		"""
		return self._get_attribute('captureFilterFrameSizeEnable')
	@CaptureFilterFrameSizeEnable.setter
	def CaptureFilterFrameSizeEnable(self, value):
		self._set_attribute('captureFilterFrameSizeEnable', value)

	@property
	def CaptureFilterFrameSizeFrom(self):
		"""Applicable only when captureFilterFrameSizeEnable is enabled. The minimum range of the size of frame to be filtered.

		Returns:
			number
		"""
		return self._get_attribute('captureFilterFrameSizeFrom')
	@CaptureFilterFrameSizeFrom.setter
	def CaptureFilterFrameSizeFrom(self, value):
		self._set_attribute('captureFilterFrameSizeFrom', value)

	@property
	def CaptureFilterFrameSizeTo(self):
		"""Applicable only when captureFilterFrameSizeEnable is enabled. The maximum range of the size of frame to be filtered.

		Returns:
			number
		"""
		return self._get_attribute('captureFilterFrameSizeTo')
	@CaptureFilterFrameSizeTo.setter
	def CaptureFilterFrameSizeTo(self, value):
		self._set_attribute('captureFilterFrameSizeTo', value)

	@property
	def CaptureFilterPattern(self):
		"""Applicable only when captureFilterEnable is set to true.

		Returns:
			str(anyPattern|notPattern1|notPattern2|pattern1|pattern1AndPattern2|pattern2)
		"""
		return self._get_attribute('captureFilterPattern')
	@CaptureFilterPattern.setter
	def CaptureFilterPattern(self, value):
		self._set_attribute('captureFilterPattern', value)

	@property
	def CaptureFilterSA(self):
		"""One of two available destination MAC addresses to filter on. Applicable only when capturefilternable is set to true.

		Returns:
			str(addr1|addr2|anyAddr|notAddr1|notAddr2)
		"""
		return self._get_attribute('captureFilterSA')
	@CaptureFilterSA.setter
	def CaptureFilterSA(self, value):
		self._set_attribute('captureFilterSA', value)

	def update(self, CaptureFilterDA=None, CaptureFilterEnable=None, CaptureFilterError=None, CaptureFilterExpressionString=None, CaptureFilterFrameSizeEnable=None, CaptureFilterFrameSizeFrom=None, CaptureFilterFrameSizeTo=None, CaptureFilterPattern=None, CaptureFilterSA=None):
		"""Updates a child instance of filter on the server.

		Args:
			CaptureFilterDA (str(addr1|addr2|anyAddr|notAddr1|notAddr2)): One of two available destination MAC addresses to filter on. Applicable only when capturefilternable is set to true.
			CaptureFilterEnable (bool): Enables or disables the capture filter.
			CaptureFilterError (str(errAnyFrame|errAnyIpTcpUdpChecksumError|errAnySequencekError|errBadCRC|errBadFrame|errBigSequenceError|errDataIntegrityError|errGoodFrame|errInvalidFcoeFrame|errReverseSequenceError|errSmallSequenceError)): Applicable only when captureFilterEnable is set to true.
			CaptureFilterExpressionString (str): String composed of SA1, DA1, P1, P2, optionally negated with '!', and connected with operators 'and', 'or', 'xor', 'nand' or 'nor'. (Eg: {DA1 and SA1 or !P1 and P2} ). NOTE: The 'or', 'xor', 'nand' and 'nor' operators are available only on the following load modules: XMVDC, NGY, XMSP12, LAVA(MK), Xcellon AP, Xcellon NP.
			CaptureFilterFrameSizeEnable (bool): Enables or disables the frame size constraint which specifies a range of frame.
			CaptureFilterFrameSizeFrom (number): Applicable only when captureFilterFrameSizeEnable is enabled. The minimum range of the size of frame to be filtered.
			CaptureFilterFrameSizeTo (number): Applicable only when captureFilterFrameSizeEnable is enabled. The maximum range of the size of frame to be filtered.
			CaptureFilterPattern (str(anyPattern|notPattern1|notPattern2|pattern1|pattern1AndPattern2|pattern2)): Applicable only when captureFilterEnable is set to true.
			CaptureFilterSA (str(addr1|addr2|anyAddr|notAddr1|notAddr2)): One of two available destination MAC addresses to filter on. Applicable only when capturefilternable is set to true.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
