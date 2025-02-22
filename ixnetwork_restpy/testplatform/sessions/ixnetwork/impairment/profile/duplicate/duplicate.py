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


class Duplicate(Base):
	"""Duplicate packets.
	The Duplicate class encapsulates a required duplicate resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'duplicate'

	def __init__(self, parent):
		super(Duplicate, self).__init__(parent)

	@property
	def ClusterSize(self):
		"""Number of packets to duplicate on each occurrence.

		Returns:
			number
		"""
		return self._get_attribute('clusterSize')
	@ClusterSize.setter
	def ClusterSize(self, value):
		self._set_attribute('clusterSize', value)

	@property
	def DuplicateCount(self):
		"""Number of times to duplicate each packet.

		Returns:
			number
		"""
		return self._get_attribute('duplicateCount')
	@DuplicateCount.setter
	def DuplicateCount(self, value):
		self._set_attribute('duplicateCount', value)

	@property
	def Enabled(self):
		"""If true, periodically duplicate received packets.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def PercentRate(self):
		"""How often to duplicate packets.

		Returns:
			number
		"""
		return self._get_attribute('percentRate')
	@PercentRate.setter
	def PercentRate(self, value):
		self._set_attribute('percentRate', value)

	def update(self, ClusterSize=None, DuplicateCount=None, Enabled=None, PercentRate=None):
		"""Updates a child instance of duplicate on the server.

		Args:
			ClusterSize (number): Number of packets to duplicate on each occurrence.
			DuplicateCount (number): Number of times to duplicate each packet.
			Enabled (bool): If true, periodically duplicate received packets.
			PercentRate (number): How often to duplicate packets.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
