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


class FilterPalette(Base):
	"""Select the filter palette.
	The FilterPalette class encapsulates a required filterPalette resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'filterPalette'

	def __init__(self, parent):
		super(FilterPalette, self).__init__(parent)

	@property
	def DestinationAddress1(self):
		"""Destination address 1.

		Returns:
			str
		"""
		return self._get_attribute('destinationAddress1')
	@DestinationAddress1.setter
	def DestinationAddress1(self, value):
		self._set_attribute('destinationAddress1', value)

	@property
	def DestinationAddress1Mask(self):
		"""The destination address mask.

		Returns:
			str
		"""
		return self._get_attribute('destinationAddress1Mask')
	@DestinationAddress1Mask.setter
	def DestinationAddress1Mask(self, value):
		self._set_attribute('destinationAddress1Mask', value)

	@property
	def DestinationAddress2(self):
		"""Destination address 2.

		Returns:
			str
		"""
		return self._get_attribute('destinationAddress2')
	@DestinationAddress2.setter
	def DestinationAddress2(self, value):
		self._set_attribute('destinationAddress2', value)

	@property
	def DestinationAddress2Mask(self):
		"""Destination address to mask.

		Returns:
			str
		"""
		return self._get_attribute('destinationAddress2Mask')
	@DestinationAddress2Mask.setter
	def DestinationAddress2Mask(self, value):
		self._set_attribute('destinationAddress2Mask', value)

	@property
	def Pattern1(self):
		"""Pattern 1.

		Returns:
			str
		"""
		return self._get_attribute('pattern1')
	@Pattern1.setter
	def Pattern1(self, value):
		self._set_attribute('pattern1', value)

	@property
	def Pattern1Mask(self):
		"""Pattern 1 mask.

		Returns:
			str
		"""
		return self._get_attribute('pattern1Mask')
	@Pattern1Mask.setter
	def Pattern1Mask(self, value):
		self._set_attribute('pattern1Mask', value)

	@property
	def Pattern1Offset(self):
		"""Pattern 1 offset.

		Returns:
			number
		"""
		return self._get_attribute('pattern1Offset')
	@Pattern1Offset.setter
	def Pattern1Offset(self, value):
		self._set_attribute('pattern1Offset', value)

	@property
	def Pattern1OffsetType(self):
		"""The pattern offset type.

		Returns:
			str(fromStartOfFrame|fromStartOfIp|fromStartOfProtocol|fromStartOfSonet)
		"""
		return self._get_attribute('pattern1OffsetType')
	@Pattern1OffsetType.setter
	def Pattern1OffsetType(self, value):
		self._set_attribute('pattern1OffsetType', value)

	@property
	def Pattern2(self):
		"""Patternt 2.

		Returns:
			str
		"""
		return self._get_attribute('pattern2')
	@Pattern2.setter
	def Pattern2(self, value):
		self._set_attribute('pattern2', value)

	@property
	def Pattern2Mask(self):
		"""The pattern mask.

		Returns:
			str
		"""
		return self._get_attribute('pattern2Mask')
	@Pattern2Mask.setter
	def Pattern2Mask(self, value):
		self._set_attribute('pattern2Mask', value)

	@property
	def Pattern2Offset(self):
		"""The offset at which the pattern is located in the packet.

		Returns:
			number
		"""
		return self._get_attribute('pattern2Offset')
	@Pattern2Offset.setter
	def Pattern2Offset(self, value):
		self._set_attribute('pattern2Offset', value)

	@property
	def Pattern2OffsetType(self):
		"""Pattern 2 offset type

		Returns:
			str(fromStartOfFrame|fromStartOfIp|fromStartOfProtocol|fromStartOfSonet)
		"""
		return self._get_attribute('pattern2OffsetType')
	@Pattern2OffsetType.setter
	def Pattern2OffsetType(self, value):
		self._set_attribute('pattern2OffsetType', value)

	@property
	def SourceAddress1(self):
		"""Source address 1.

		Returns:
			str
		"""
		return self._get_attribute('sourceAddress1')
	@SourceAddress1.setter
	def SourceAddress1(self, value):
		self._set_attribute('sourceAddress1', value)

	@property
	def SourceAddress1Mask(self):
		"""Source address 1 mask.

		Returns:
			str
		"""
		return self._get_attribute('sourceAddress1Mask')
	@SourceAddress1Mask.setter
	def SourceAddress1Mask(self, value):
		self._set_attribute('sourceAddress1Mask', value)

	@property
	def SourceAddress2(self):
		"""Source address 2.

		Returns:
			str
		"""
		return self._get_attribute('sourceAddress2')
	@SourceAddress2.setter
	def SourceAddress2(self, value):
		self._set_attribute('sourceAddress2', value)

	@property
	def SourceAddress2Mask(self):
		"""Source address to mask.

		Returns:
			str
		"""
		return self._get_attribute('sourceAddress2Mask')
	@SourceAddress2Mask.setter
	def SourceAddress2Mask(self, value):
		self._set_attribute('sourceAddress2Mask', value)

	def update(self, DestinationAddress1=None, DestinationAddress1Mask=None, DestinationAddress2=None, DestinationAddress2Mask=None, Pattern1=None, Pattern1Mask=None, Pattern1Offset=None, Pattern1OffsetType=None, Pattern2=None, Pattern2Mask=None, Pattern2Offset=None, Pattern2OffsetType=None, SourceAddress1=None, SourceAddress1Mask=None, SourceAddress2=None, SourceAddress2Mask=None):
		"""Updates a child instance of filterPalette on the server.

		Args:
			DestinationAddress1 (str): Destination address 1.
			DestinationAddress1Mask (str): The destination address mask.
			DestinationAddress2 (str): Destination address 2.
			DestinationAddress2Mask (str): Destination address to mask.
			Pattern1 (str): Pattern 1.
			Pattern1Mask (str): Pattern 1 mask.
			Pattern1Offset (number): Pattern 1 offset.
			Pattern1OffsetType (str(fromStartOfFrame|fromStartOfIp|fromStartOfProtocol|fromStartOfSonet)): The pattern offset type.
			Pattern2 (str): Patternt 2.
			Pattern2Mask (str): The pattern mask.
			Pattern2Offset (number): The offset at which the pattern is located in the packet.
			Pattern2OffsetType (str(fromStartOfFrame|fromStartOfIp|fromStartOfProtocol|fromStartOfSonet)): Pattern 2 offset type
			SourceAddress1 (str): Source address 1.
			SourceAddress1Mask (str): Source address 1 mask.
			SourceAddress2 (str): Source address 2.
			SourceAddress2Mask (str): Source address to mask.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
