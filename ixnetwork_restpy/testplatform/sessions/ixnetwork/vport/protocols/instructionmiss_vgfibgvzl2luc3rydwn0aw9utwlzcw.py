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


class InstructionMiss(Base):
	"""Select the type of instruction miss capabilities that the table miss flow entry will support.
	The InstructionMiss class encapsulates a required instructionMiss resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'instructionMiss'

	def __init__(self, parent):
		super(InstructionMiss, self).__init__(parent)

	@property
	def ApplyActions(self):
		"""If selected, applies the actions associated with a flow immediately.

		Returns:
			bool
		"""
		return self._get_attribute('applyActions')
	@ApplyActions.setter
	def ApplyActions(self, value):
		self._set_attribute('applyActions', value)

	@property
	def ClearActions(self):
		"""If selected, clears the actions attached with the flow.

		Returns:
			bool
		"""
		return self._get_attribute('clearActions')
	@ClearActions.setter
	def ClearActions(self, value):
		self._set_attribute('clearActions', value)

	@property
	def Experimenter(self):
		"""If selected, gives experimenter instruction.

		Returns:
			bool
		"""
		return self._get_attribute('experimenter')
	@Experimenter.setter
	def Experimenter(self, value):
		self._set_attribute('experimenter', value)

	@property
	def GoToTable(self):
		"""If selected, forwards the packet to the next table in the pipeline.

		Returns:
			bool
		"""
		return self._get_attribute('goToTable')
	@GoToTable.setter
	def GoToTable(self, value):
		self._set_attribute('goToTable', value)

	@property
	def Meter(self):
		"""If selected, directs a flow to a particular meter.

		Returns:
			bool
		"""
		return self._get_attribute('meter')
	@Meter.setter
	def Meter(self, value):
		self._set_attribute('meter', value)

	@property
	def WriteActions(self):
		"""If selected, appends actions to the existing action set of the packet.

		Returns:
			bool
		"""
		return self._get_attribute('writeActions')
	@WriteActions.setter
	def WriteActions(self, value):
		self._set_attribute('writeActions', value)

	@property
	def WriteMetadata(self):
		"""If selected, writes the masked metadata field to the match.

		Returns:
			bool
		"""
		return self._get_attribute('writeMetadata')
	@WriteMetadata.setter
	def WriteMetadata(self, value):
		self._set_attribute('writeMetadata', value)

	def update(self, ApplyActions=None, ClearActions=None, Experimenter=None, GoToTable=None, Meter=None, WriteActions=None, WriteMetadata=None):
		"""Updates a child instance of instructionMiss on the server.

		Args:
			ApplyActions (bool): If selected, applies the actions associated with a flow immediately.
			ClearActions (bool): If selected, clears the actions attached with the flow.
			Experimenter (bool): If selected, gives experimenter instruction.
			GoToTable (bool): If selected, forwards the packet to the next table in the pipeline.
			Meter (bool): If selected, directs a flow to a particular meter.
			WriteActions (bool): If selected, appends actions to the existing action set of the packet.
			WriteMetadata (bool): If selected, writes the masked metadata field to the match.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
