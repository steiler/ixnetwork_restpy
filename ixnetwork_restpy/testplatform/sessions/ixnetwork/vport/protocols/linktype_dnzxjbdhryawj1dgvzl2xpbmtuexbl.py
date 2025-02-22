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


class LinkType(Base):
	"""NOT DEFINED
	The LinkType class encapsulates a required linkType resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'linkType'

	def __init__(self, parent):
		super(LinkType, self).__init__(parent)

	@property
	def OfppfCopper(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('ofppfCopper')
	@OfppfCopper.setter
	def OfppfCopper(self, value):
		self._set_attribute('ofppfCopper', value)

	@property
	def OfppfFiber(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('ofppfFiber')
	@OfppfFiber.setter
	def OfppfFiber(self, value):
		self._set_attribute('ofppfFiber', value)

	def update(self, OfppfCopper=None, OfppfFiber=None):
		"""Updates a child instance of linkType on the server.

		Args:
			OfppfCopper (bool): NOT DEFINED
			OfppfFiber (bool): NOT DEFINED

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
