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


class Instruction(Base):
	"""NOT DEFINED
	The Instruction class encapsulates a required instruction resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'instruction'

	def __init__(self, parent):
		super(Instruction, self).__init__(parent)

	@property
	def InstructionType(self):
		"""An instance of the InstructionType class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructiontype_j1y3rpb24vaw5zdhj1y3rpb25uexbl.InstructionType)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructiontype_j1y3rpb24vaw5zdhj1y3rpb25uexbl import InstructionType
		return InstructionType(self)._select()

	@property
	def InstructionTypeMiss(self):
		"""An instance of the InstructionTypeMiss class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructiontypemiss_b24vaw5zdhj1y3rpb25uexbltwlzcw.InstructionTypeMiss)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructiontypemiss_b24vaw5zdhj1y3rpb25uexbltwlzcw import InstructionTypeMiss
		return InstructionTypeMiss(self)._select()

	@property
	def ExperimenterData(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('experimenterData')
	@ExperimenterData.setter
	def ExperimenterData(self, value):
		self._set_attribute('experimenterData', value)

	@property
	def ExperimenterDataLength(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('experimenterDataLength')
	@ExperimenterDataLength.setter
	def ExperimenterDataLength(self, value):
		self._set_attribute('experimenterDataLength', value)

	@property
	def ExperimenterDataLengthMiss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('experimenterDataLengthMiss')
	@ExperimenterDataLengthMiss.setter
	def ExperimenterDataLengthMiss(self, value):
		self._set_attribute('experimenterDataLengthMiss', value)

	@property
	def ExperimenterDataMiss(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('experimenterDataMiss')
	@ExperimenterDataMiss.setter
	def ExperimenterDataMiss(self, value):
		self._set_attribute('experimenterDataMiss', value)

	@property
	def ExperimenterId(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('experimenterId')
	@ExperimenterId.setter
	def ExperimenterId(self, value):
		self._set_attribute('experimenterId', value)

	@property
	def ExperimenterIdMiss(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('experimenterIdMiss')
	@ExperimenterIdMiss.setter
	def ExperimenterIdMiss(self, value):
		self._set_attribute('experimenterIdMiss', value)

	def update(self, ExperimenterData=None, ExperimenterDataLength=None, ExperimenterDataLengthMiss=None, ExperimenterDataMiss=None, ExperimenterId=None, ExperimenterIdMiss=None):
		"""Updates a child instance of instruction on the server.

		Args:
			ExperimenterData (str): NOT DEFINED
			ExperimenterDataLength (number): NOT DEFINED
			ExperimenterDataLengthMiss (number): NOT DEFINED
			ExperimenterDataMiss (str): NOT DEFINED
			ExperimenterId (number): NOT DEFINED
			ExperimenterIdMiss (number): NOT DEFINED

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
