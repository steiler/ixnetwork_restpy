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


class FormulaColumn(Base):
	"""The formula is filtered and maintained in columns.
	The FormulaColumn class encapsulates a list of formulaColumn resources that is be managed by the user.
	A list of resources can be retrieved from the server using the FormulaColumn.find() method.
	The list can be managed by the user by using the FormulaColumn.add() and FormulaColumn.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'formulaColumn'

	def __init__(self, parent):
		super(FormulaColumn, self).__init__(parent)

	@property
	def Caption(self):
		"""The name of the formula.

		Returns:
			str
		"""
		return self._get_attribute('caption')
	@Caption.setter
	def Caption(self, value):
		self._set_attribute('caption', value)

	@property
	def Formula(self):
		"""The formula that is filtered.

		Returns:
			str
		"""
		return self._get_attribute('formula')
	@Formula.setter
	def Formula(self, value):
		self._set_attribute('formula', value)

	def update(self, Caption=None, Formula=None):
		"""Updates a child instance of formulaColumn on the server.

		Args:
			Caption (str): The name of the formula.
			Formula (str): The formula that is filtered.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Caption=None, Formula=None):
		"""Adds a new formulaColumn node on the server and retrieves it in this instance.

		Args:
			Caption (str): The name of the formula.
			Formula (str): The formula that is filtered.

		Returns:
			self: This instance with all currently retrieved formulaColumn data using find and the newly added formulaColumn data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the formulaColumn data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Caption=None, Formula=None):
		"""Finds and retrieves formulaColumn data from the server.

		All named parameters support regex and can be used to selectively retrieve formulaColumn data from the server.
		By default the find method takes no parameters and will retrieve all formulaColumn data from the server.

		Args:
			Caption (str): The name of the formula.
			Formula (str): The formula that is filtered.

		Returns:
			self: This instance with matching formulaColumn data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of formulaColumn data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the formulaColumn data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
