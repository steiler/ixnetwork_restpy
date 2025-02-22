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


class Instructions(Base):
	"""This object allows to configure the instructions in Controller Table Flow Ranges.
	The Instructions class encapsulates a list of instructions resources that is be managed by the user.
	A list of resources can be retrieved from the server using the Instructions.find() method.
	The list can be managed by the user by using the Instructions.add() and Instructions.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'instructions'

	def __init__(self, parent):
		super(Instructions, self).__init__(parent)

	@property
	def InstructionActions(self):
		"""An instance of the InstructionActions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionactions_b25zl2luc3rydwn0aw9uqwn0aw9ucw.InstructionActions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructionactions_b25zl2luc3rydwn0aw9uqwn0aw9ucw import InstructionActions
		return InstructionActions(self)

	@property
	def Experimenter(self):
		"""The unique identifier for the Experimenter.

		Returns:
			number
		"""
		return self._get_attribute('experimenter')
	@Experimenter.setter
	def Experimenter(self, value):
		self._set_attribute('experimenter', value)

	@property
	def ExperimenterData(self):
		"""The experimenter data field value.

		Returns:
			str
		"""
		return self._get_attribute('experimenterData')
	@ExperimenterData.setter
	def ExperimenterData(self, value):
		self._set_attribute('experimenterData', value)

	@property
	def ExperimenterDataLength(self):
		"""The Value of the data length of the Experimenter. The default value is 1.

		Returns:
			number
		"""
		return self._get_attribute('experimenterDataLength')
	@ExperimenterDataLength.setter
	def ExperimenterDataLength(self, value):
		self._set_attribute('experimenterDataLength', value)

	@property
	def InstructionType(self):
		"""The instruction type associated with this Flow Range.

		Returns:
			str(meter|applyActions|clearActions|experimenter|goToTable|writeActions|writeMetadata)
		"""
		return self._get_attribute('instructionType')
	@InstructionType.setter
	def InstructionType(self, value):
		self._set_attribute('instructionType', value)

	@property
	def Metadata(self):
		"""Value of the metadata field.

		Returns:
			str
		"""
		return self._get_attribute('metadata')
	@Metadata.setter
	def Metadata(self, value):
		self._set_attribute('metadata', value)

	@property
	def MetadataInHex(self):
		"""Specify the table metadata value in hexadecimal format.

		Returns:
			str
		"""
		return self._get_attribute('metadataInHex')
	@MetadataInHex.setter
	def MetadataInHex(self, value):
		self._set_attribute('metadataInHex', value)

	@property
	def MetadataMask(self):
		"""Specify the metadata bitmask value.

		Returns:
			str
		"""
		return self._get_attribute('metadataMask')
	@MetadataMask.setter
	def MetadataMask(self, value):
		self._set_attribute('metadataMask', value)

	@property
	def MeterId(self):
		"""The value by which a meter is uniquely identified within a switch. The default value is 1.

		Returns:
			number
		"""
		return self._get_attribute('meterId')
	@MeterId.setter
	def MeterId(self, value):
		self._set_attribute('meterId', value)

	@property
	def TableId(self):
		"""The ID of the table to go to.

		Returns:
			number
		"""
		return self._get_attribute('tableId')
	@TableId.setter
	def TableId(self, value):
		self._set_attribute('tableId', value)

	def update(self, Experimenter=None, ExperimenterData=None, ExperimenterDataLength=None, InstructionType=None, Metadata=None, MetadataInHex=None, MetadataMask=None, MeterId=None, TableId=None):
		"""Updates a child instance of instructions on the server.

		Args:
			Experimenter (number): The unique identifier for the Experimenter.
			ExperimenterData (str): The experimenter data field value.
			ExperimenterDataLength (number): The Value of the data length of the Experimenter. The default value is 1.
			InstructionType (str(meter|applyActions|clearActions|experimenter|goToTable|writeActions|writeMetadata)): The instruction type associated with this Flow Range.
			Metadata (str): Value of the metadata field.
			MetadataInHex (str): Specify the table metadata value in hexadecimal format.
			MetadataMask (str): Specify the metadata bitmask value.
			MeterId (number): The value by which a meter is uniquely identified within a switch. The default value is 1.
			TableId (number): The ID of the table to go to.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Experimenter=None, ExperimenterData=None, ExperimenterDataLength=None, InstructionType=None, Metadata=None, MetadataInHex=None, MetadataMask=None, MeterId=None, TableId=None):
		"""Adds a new instructions node on the server and retrieves it in this instance.

		Args:
			Experimenter (number): The unique identifier for the Experimenter.
			ExperimenterData (str): The experimenter data field value.
			ExperimenterDataLength (number): The Value of the data length of the Experimenter. The default value is 1.
			InstructionType (str(meter|applyActions|clearActions|experimenter|goToTable|writeActions|writeMetadata)): The instruction type associated with this Flow Range.
			Metadata (str): Value of the metadata field.
			MetadataInHex (str): Specify the table metadata value in hexadecimal format.
			MetadataMask (str): Specify the metadata bitmask value.
			MeterId (number): The value by which a meter is uniquely identified within a switch. The default value is 1.
			TableId (number): The ID of the table to go to.

		Returns:
			self: This instance with all currently retrieved instructions data using find and the newly added instructions data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the instructions data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Experimenter=None, ExperimenterData=None, ExperimenterDataLength=None, InstructionType=None, Metadata=None, MetadataInHex=None, MetadataMask=None, MeterId=None, TableId=None):
		"""Finds and retrieves instructions data from the server.

		All named parameters support regex and can be used to selectively retrieve instructions data from the server.
		By default the find method takes no parameters and will retrieve all instructions data from the server.

		Args:
			Experimenter (number): The unique identifier for the Experimenter.
			ExperimenterData (str): The experimenter data field value.
			ExperimenterDataLength (number): The Value of the data length of the Experimenter. The default value is 1.
			InstructionType (str(meter|applyActions|clearActions|experimenter|goToTable|writeActions|writeMetadata)): The instruction type associated with this Flow Range.
			Metadata (str): Value of the metadata field.
			MetadataInHex (str): Specify the table metadata value in hexadecimal format.
			MetadataMask (str): Specify the metadata bitmask value.
			MeterId (number): The value by which a meter is uniquely identified within a switch. The default value is 1.
			TableId (number): The ID of the table to go to.

		Returns:
			self: This instance with matching instructions data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of instructions data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the instructions data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
