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


class OpaqueValueElement(Base):
	"""Configures the value for the opaque element.
	The OpaqueValueElement class encapsulates a list of opaqueValueElement resources that is be managed by the user.
	A list of resources can be retrieved from the server using the OpaqueValueElement.find() method.
	The list can be managed by the user by using the OpaqueValueElement.add() and OpaqueValueElement.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'opaqueValueElement'

	def __init__(self, parent):
		super(OpaqueValueElement, self).__init__(parent)

	@property
	def Increment(self):
		"""It signifies the incremented value.

		Returns:
			str
		"""
		return self._get_attribute('increment')
	@Increment.setter
	def Increment(self, value):
		self._set_attribute('increment', value)

	@property
	def Length(self):
		"""It signifies the length.

		Returns:
			number
		"""
		return self._get_attribute('length')
	@Length.setter
	def Length(self, value):
		self._set_attribute('length', value)

	@property
	def Type(self):
		"""It signifies the type.

		Returns:
			number
		"""
		return self._get_attribute('type')
	@Type.setter
	def Type(self, value):
		self._set_attribute('type', value)

	@property
	def Value(self):
		"""It signifies the value.

		Returns:
			str
		"""
		return self._get_attribute('value')
	@Value.setter
	def Value(self, value):
		self._set_attribute('value', value)

	def update(self, Increment=None, Length=None, Type=None, Value=None):
		"""Updates a child instance of opaqueValueElement on the server.

		Args:
			Increment (str): It signifies the incremented value.
			Length (number): It signifies the length.
			Type (number): It signifies the type.
			Value (str): It signifies the value.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Increment=None, Length=None, Type=None, Value=None):
		"""Adds a new opaqueValueElement node on the server and retrieves it in this instance.

		Args:
			Increment (str): It signifies the incremented value.
			Length (number): It signifies the length.
			Type (number): It signifies the type.
			Value (str): It signifies the value.

		Returns:
			self: This instance with all currently retrieved opaqueValueElement data using find and the newly added opaqueValueElement data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the opaqueValueElement data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Increment=None, Length=None, Type=None, Value=None):
		"""Finds and retrieves opaqueValueElement data from the server.

		All named parameters support regex and can be used to selectively retrieve opaqueValueElement data from the server.
		By default the find method takes no parameters and will retrieve all opaqueValueElement data from the server.

		Args:
			Increment (str): It signifies the incremented value.
			Length (number): It signifies the length.
			Type (number): It signifies the type.
			Value (str): It signifies the value.

		Returns:
			self: This instance with matching opaqueValueElement data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of opaqueValueElement data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the opaqueValueElement data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
