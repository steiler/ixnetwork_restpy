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


class AdvancedSequenceChecking(Base):
	"""Checks advanced sequence.
	The AdvancedSequenceChecking class encapsulates a required advancedSequenceChecking resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'advancedSequenceChecking'

	def __init__(self, parent):
		super(AdvancedSequenceChecking, self).__init__(parent)

	@property
	def AdvancedSequenceThreshold(self):
		"""Signifies the threshold of advanced sequence

		Returns:
			number
		"""
		return self._get_attribute('advancedSequenceThreshold')
	@AdvancedSequenceThreshold.setter
	def AdvancedSequenceThreshold(self, value):
		self._set_attribute('advancedSequenceThreshold', value)

	@property
	def Enabled(self):
		"""If true, enables advanced sequence checking

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	def update(self, AdvancedSequenceThreshold=None, Enabled=None):
		"""Updates a child instance of advancedSequenceChecking on the server.

		Args:
			AdvancedSequenceThreshold (number): Signifies the threshold of advanced sequence
			Enabled (bool): If true, enables advanced sequence checking

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
