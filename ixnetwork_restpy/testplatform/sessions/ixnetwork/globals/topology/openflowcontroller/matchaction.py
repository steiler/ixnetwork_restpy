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


class MatchAction(Base):
	"""Match Criteria and Instruction-Action prototype.
	The MatchAction class encapsulates a list of matchAction resources that is be managed by the user.
	A list of resources can be retrieved from the server using the MatchAction.find() method.
	The list can be managed by the user by using the MatchAction.add() and MatchAction.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'matchAction'

	def __init__(self, parent):
		super(MatchAction, self).__init__(parent)

	@property
	def Instructions(self):
		"""An instance of the Instructions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowcontroller.instructions.Instructions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowcontroller.instructions import Instructions
		return Instructions(self)._select()

	@property
	def MatchCriteria(self):
		"""An instance of the MatchCriteria class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowcontroller.matchcriteria.MatchCriteria)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.openflowcontroller.matchcriteria import MatchCriteria
		return MatchCriteria(self)._select()

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def Description(self):
		"""Description of the TLV prototype.

		Returns:
			str
		"""
		return self._get_attribute('description')
	@Description.setter
	def Description(self, value):
		self._set_attribute('description', value)

	@property
	def IsEditable(self):
		"""Information on the requirement of the field.

		Returns:
			bool
		"""
		return self._get_attribute('isEditable')
	@IsEditable.setter
	def IsEditable(self, value):
		self._set_attribute('isEditable', value)

	@property
	def IsRepeatable(self):
		"""Information if the field can be multiplied in the tlv definition.

		Returns:
			bool
		"""
		return self._get_attribute('isRepeatable')
	@IsRepeatable.setter
	def IsRepeatable(self, value):
		self._set_attribute('isRepeatable', value)

	@property
	def IsRequired(self):
		"""Information on the requirement of the field.

		Returns:
			bool
		"""
		return self._get_attribute('isRequired')
	@IsRequired.setter
	def IsRequired(self, value):
		self._set_attribute('isRequired', value)

	@property
	def Name(self):
		"""Name of the TLV field.

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	def update(self, Description=None, IsEditable=None, IsRepeatable=None, IsRequired=None, Name=None):
		"""Updates a child instance of matchAction on the server.

		Args:
			Description (str): Description of the TLV prototype.
			IsEditable (bool): Information on the requirement of the field.
			IsRepeatable (bool): Information if the field can be multiplied in the tlv definition.
			IsRequired (bool): Information on the requirement of the field.
			Name (str): Name of the TLV field.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Description=None, IsEditable=None, IsRepeatable=None, IsRequired=None, Name=None):
		"""Adds a new matchAction node on the server and retrieves it in this instance.

		Args:
			Description (str): Description of the TLV prototype.
			IsEditable (bool): Information on the requirement of the field.
			IsRepeatable (bool): Information if the field can be multiplied in the tlv definition.
			IsRequired (bool): Information on the requirement of the field.
			Name (str): Name of the TLV field.

		Returns:
			self: This instance with all currently retrieved matchAction data using find and the newly added matchAction data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the matchAction data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Count=None, Description=None, IsEditable=None, IsRepeatable=None, IsRequired=None, Name=None):
		"""Finds and retrieves matchAction data from the server.

		All named parameters support regex and can be used to selectively retrieve matchAction data from the server.
		By default the find method takes no parameters and will retrieve all matchAction data from the server.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
			Description (str): Description of the TLV prototype.
			IsEditable (bool): Information on the requirement of the field.
			IsRepeatable (bool): Information if the field can be multiplied in the tlv definition.
			IsRequired (bool): Information on the requirement of the field.
			Name (str): Name of the TLV field.

		Returns:
			self: This instance with matching matchAction data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of matchAction data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the matchAction data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
