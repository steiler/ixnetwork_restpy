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


class UserDefinedAfiSafiRoutes(Base):
	"""Configures the user defined afi/safi routes.
	The UserDefinedAfiSafiRoutes class encapsulates a list of userDefinedAfiSafiRoutes resources that is be managed by the user.
	A list of resources can be retrieved from the server using the UserDefinedAfiSafiRoutes.find() method.
	The list can be managed by the user by using the UserDefinedAfiSafiRoutes.add() and UserDefinedAfiSafiRoutes.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'userDefinedAfiSafiRoutes'

	def __init__(self, parent):
		super(UserDefinedAfiSafiRoutes, self).__init__(parent)

	@property
	def Data(self):
		"""Data to be transmitted for AFI/SAFI, and regular enable-disable.

		Returns:
			str
		"""
		return self._get_attribute('data')
	@Data.setter
	def Data(self, value):
		self._set_attribute('data', value)

	@property
	def Enabled(self):
		"""If true, the user-defined afi/safi is enabled.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def Length(self):
		"""The data is padded up to length with left alignment otherwise chopped till length.

		Returns:
			number
		"""
		return self._get_attribute('length')
	@Length.setter
	def Length(self, value):
		self._set_attribute('length', value)

	def update(self, Data=None, Enabled=None, Length=None):
		"""Updates a child instance of userDefinedAfiSafiRoutes on the server.

		Args:
			Data (str): Data to be transmitted for AFI/SAFI, and regular enable-disable.
			Enabled (bool): If true, the user-defined afi/safi is enabled.
			Length (number): The data is padded up to length with left alignment otherwise chopped till length.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Data=None, Enabled=None, Length=None):
		"""Adds a new userDefinedAfiSafiRoutes node on the server and retrieves it in this instance.

		Args:
			Data (str): Data to be transmitted for AFI/SAFI, and regular enable-disable.
			Enabled (bool): If true, the user-defined afi/safi is enabled.
			Length (number): The data is padded up to length with left alignment otherwise chopped till length.

		Returns:
			self: This instance with all currently retrieved userDefinedAfiSafiRoutes data using find and the newly added userDefinedAfiSafiRoutes data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the userDefinedAfiSafiRoutes data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Data=None, Enabled=None, Length=None):
		"""Finds and retrieves userDefinedAfiSafiRoutes data from the server.

		All named parameters support regex and can be used to selectively retrieve userDefinedAfiSafiRoutes data from the server.
		By default the find method takes no parameters and will retrieve all userDefinedAfiSafiRoutes data from the server.

		Args:
			Data (str): Data to be transmitted for AFI/SAFI, and regular enable-disable.
			Enabled (bool): If true, the user-defined afi/safi is enabled.
			Length (number): The data is padded up to length with left alignment otherwise chopped till length.

		Returns:
			self: This instance with matching userDefinedAfiSafiRoutes data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of userDefinedAfiSafiRoutes data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the userDefinedAfiSafiRoutes data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
