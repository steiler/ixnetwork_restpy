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


class Uds(Base):
	"""A counter that increments each time the capture filter conditions are met, as defined in the Capture Filter window.
	The Uds class encapsulates a list of uds resources that is managed by the system.
	A list of resources can be retrieved from the server using the Uds.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'uds'

	def __init__(self, parent):
		super(Uds, self).__init__(parent)

	@property
	def CustomFrameSizeFrom(self):
		"""Frame size customized from.

		Returns:
			number
		"""
		return self._get_attribute('customFrameSizeFrom')
	@CustomFrameSizeFrom.setter
	def CustomFrameSizeFrom(self, value):
		self._set_attribute('customFrameSizeFrom', value)

	@property
	def CustomFrameSizeTo(self):
		"""Customized frame size.

		Returns:
			number
		"""
		return self._get_attribute('customFrameSizeTo')
	@CustomFrameSizeTo.setter
	def CustomFrameSizeTo(self, value):
		self._set_attribute('customFrameSizeTo', value)

	@property
	def DestinationAddressSelector(self):
		"""Destination address selector.

		Returns:
			str(addr1|addr2|anyAddr|notAddr1|notAddr2)
		"""
		return self._get_attribute('destinationAddressSelector')
	@DestinationAddressSelector.setter
	def DestinationAddressSelector(self, value):
		self._set_attribute('destinationAddressSelector', value)

	@property
	def Error(self):
		"""Indicates error.

		Returns:
			str(errAnyFrame|errBadCRC|errBadFrame|errGoodFrame)
		"""
		return self._get_attribute('error')
	@Error.setter
	def Error(self, value):
		self._set_attribute('error', value)

	@property
	def FrameSizeType(self):
		"""The type of frame size.

		Returns:
			str(any|custom|jumbo|oversized|undersized)
		"""
		return self._get_attribute('frameSizeType')
	@FrameSizeType.setter
	def FrameSizeType(self, value):
		self._set_attribute('frameSizeType', value)

	@property
	def IsEnabled(self):
		"""If true, UDS is enabled.

		Returns:
			bool
		"""
		return self._get_attribute('isEnabled')
	@IsEnabled.setter
	def IsEnabled(self, value):
		self._set_attribute('isEnabled', value)

	@property
	def PatternSelector(self):
		"""Pattern selector.

		Returns:
			str(anyPattern|notPattern1|notPattern2|pattern1|pattern2)
		"""
		return self._get_attribute('patternSelector')
	@PatternSelector.setter
	def PatternSelector(self, value):
		self._set_attribute('patternSelector', value)

	@property
	def SourceAddressSelector(self):
		"""Source address selector.

		Returns:
			str(addr1|addr2|anyAddr|notAddr1|notAddr2)
		"""
		return self._get_attribute('sourceAddressSelector')
	@SourceAddressSelector.setter
	def SourceAddressSelector(self, value):
		self._set_attribute('sourceAddressSelector', value)

	def update(self, CustomFrameSizeFrom=None, CustomFrameSizeTo=None, DestinationAddressSelector=None, Error=None, FrameSizeType=None, IsEnabled=None, PatternSelector=None, SourceAddressSelector=None):
		"""Updates a child instance of uds on the server.

		Args:
			CustomFrameSizeFrom (number): Frame size customized from.
			CustomFrameSizeTo (number): Customized frame size.
			DestinationAddressSelector (str(addr1|addr2|anyAddr|notAddr1|notAddr2)): Destination address selector.
			Error (str(errAnyFrame|errBadCRC|errBadFrame|errGoodFrame)): Indicates error.
			FrameSizeType (str(any|custom|jumbo|oversized|undersized)): The type of frame size.
			IsEnabled (bool): If true, UDS is enabled.
			PatternSelector (str(anyPattern|notPattern1|notPattern2|pattern1|pattern2)): Pattern selector.
			SourceAddressSelector (str(addr1|addr2|anyAddr|notAddr1|notAddr2)): Source address selector.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def find(self, CustomFrameSizeFrom=None, CustomFrameSizeTo=None, DestinationAddressSelector=None, Error=None, FrameSizeType=None, IsEnabled=None, PatternSelector=None, SourceAddressSelector=None):
		"""Finds and retrieves uds data from the server.

		All named parameters support regex and can be used to selectively retrieve uds data from the server.
		By default the find method takes no parameters and will retrieve all uds data from the server.

		Args:
			CustomFrameSizeFrom (number): Frame size customized from.
			CustomFrameSizeTo (number): Customized frame size.
			DestinationAddressSelector (str(addr1|addr2|anyAddr|notAddr1|notAddr2)): Destination address selector.
			Error (str(errAnyFrame|errBadCRC|errBadFrame|errGoodFrame)): Indicates error.
			FrameSizeType (str(any|custom|jumbo|oversized|undersized)): The type of frame size.
			IsEnabled (bool): If true, UDS is enabled.
			PatternSelector (str(anyPattern|notPattern1|notPattern2|pattern1|pattern2)): Pattern selector.
			SourceAddressSelector (str(addr1|addr2|anyAddr|notAddr1|notAddr2)): Source address selector.

		Returns:
			self: This instance with matching uds data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of uds data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the uds data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
