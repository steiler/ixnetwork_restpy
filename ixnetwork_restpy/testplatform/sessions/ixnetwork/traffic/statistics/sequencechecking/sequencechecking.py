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


class SequenceChecking(Base):
	"""This object fetches sequence checking statistics.
	The SequenceChecking class encapsulates a required sequenceChecking resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'sequenceChecking'

	def __init__(self, parent):
		super(SequenceChecking, self).__init__(parent)

	@property
	def AdvancedSequenceThreshold(self):
		"""DEPRECATED Checks the sequence.

		Returns:
			number
		"""
		return self._get_attribute('advancedSequenceThreshold')
	@AdvancedSequenceThreshold.setter
	def AdvancedSequenceThreshold(self, value):
		self._set_attribute('advancedSequenceThreshold', value)

	@property
	def Enabled(self):
		"""If enabled, fetches sequence checking statistics to measure duplicate packets, sequence gap, and the last sequence number.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def SequenceMode(self):
		"""The mode to conduct sequence checking.

		Returns:
			str(advanced|rxPacketArrival|rxSwitchedPath|rxThreshold)
		"""
		return self._get_attribute('sequenceMode')
	@SequenceMode.setter
	def SequenceMode(self, value):
		self._set_attribute('sequenceMode', value)

	def update(self, AdvancedSequenceThreshold=None, Enabled=None, SequenceMode=None):
		"""Updates a child instance of sequenceChecking on the server.

		Args:
			AdvancedSequenceThreshold (number): Checks the sequence.
			Enabled (bool): If enabled, fetches sequence checking statistics to measure duplicate packets, sequence gap, and the last sequence number.
			SequenceMode (str(advanced|rxPacketArrival|rxSwitchedPath|rxThreshold)): The mode to conduct sequence checking.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
