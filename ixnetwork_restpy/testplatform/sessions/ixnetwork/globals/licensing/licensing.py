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


class Licensing(Base):
	"""Container for licensing options
	The Licensing class encapsulates a required licensing resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'licensing'

	def __init__(self, parent):
		super(Licensing, self).__init__(parent)

	@property
	def LicensingServers(self):
		"""List of license servers to use

		Returns:
			list(str)
		"""
		return self._get_attribute('licensingServers')
	@LicensingServers.setter
	def LicensingServers(self, value):
		self._set_attribute('licensingServers', value)

	@property
	def Mode(self):
		"""Set license mode to either perpetual or subscription

		Returns:
			str(mixed|perpetual|subscription)
		"""
		return self._get_attribute('mode')
	@Mode.setter
	def Mode(self, value):
		self._set_attribute('mode', value)

	@property
	def Tier(self):
		"""set or get the tier level, using the tier ID. Available IDs are: tier3-10g, tier3, tier2, tier1

		Returns:
			str
		"""
		return self._get_attribute('tier')
	@Tier.setter
	def Tier(self, value):
		self._set_attribute('tier', value)

	def update(self, LicensingServers=None, Mode=None, Tier=None):
		"""Updates a child instance of licensing on the server.

		Args:
			LicensingServers (list(str)): List of license servers to use
			Mode (str(mixed|perpetual|subscription)): Set license mode to either perpetual or subscription
			Tier (str): set or get the tier level, using the tier ID. Available IDs are: tier3-10g, tier3, tier2, tier1

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
