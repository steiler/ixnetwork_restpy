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


class LabelSpace(Base):
	"""This object configures the labels for the route range.
	The LabelSpace class encapsulates a required labelSpace resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'labelSpace'

	def __init__(self, parent):
		super(LabelSpace, self).__init__(parent)

	@property
	def End(self):
		"""The last label value available in the label space (range).

		Returns:
			number
		"""
		return self._get_attribute('end')
	@End.setter
	def End(self, value):
		self._set_attribute('end', value)

	@property
	def LabelId(self):
		"""The identifier for the label space.

		Returns:
			number
		"""
		return self._get_attribute('labelId')
	@LabelId.setter
	def LabelId(self, value):
		self._set_attribute('labelId', value)

	@property
	def Mode(self):
		"""Sets the Label mode.

		Returns:
			str(fixedLabel|incrementLabel)
		"""
		return self._get_attribute('mode')
	@Mode.setter
	def Mode(self, value):
		self._set_attribute('mode', value)

	@property
	def Start(self):
		"""The first label value available in the label space (range). The default is 16.

		Returns:
			number
		"""
		return self._get_attribute('start')
	@Start.setter
	def Start(self, value):
		self._set_attribute('start', value)

	@property
	def Step(self):
		"""The value to add for creating each additional label value.

		Returns:
			number
		"""
		return self._get_attribute('step')
	@Step.setter
	def Step(self, value):
		self._set_attribute('step', value)

	def update(self, End=None, LabelId=None, Mode=None, Start=None, Step=None):
		"""Updates a child instance of labelSpace on the server.

		Args:
			End (number): The last label value available in the label space (range).
			LabelId (number): The identifier for the label space.
			Mode (str(fixedLabel|incrementLabel)): Sets the Label mode.
			Start (number): The first label value available in the label space (range). The default is 16.
			Step (number): The value to add for creating each additional label value.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
