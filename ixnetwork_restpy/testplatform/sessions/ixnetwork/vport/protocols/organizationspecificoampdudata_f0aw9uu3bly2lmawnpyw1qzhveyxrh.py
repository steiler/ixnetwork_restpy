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


class OrganizationSpecificOamPduData(Base):
	"""
	The OrganizationSpecificOamPduData class encapsulates a list of organizationSpecificOamPduData resources that is be managed by the user.
	A list of resources can be retrieved from the server using the OrganizationSpecificOamPduData.find() method.
	The list can be managed by the user by using the OrganizationSpecificOamPduData.add() and OrganizationSpecificOamPduData.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'organizationSpecificOamPduData'

	def __init__(self, parent):
		super(OrganizationSpecificOamPduData, self).__init__(parent)

	@property
	def Oui(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('oui')
	@Oui.setter
	def Oui(self, value):
		self._set_attribute('oui', value)

	@property
	def Value(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('value')
	@Value.setter
	def Value(self, value):
		self._set_attribute('value', value)

	def update(self, Oui=None, Value=None):
		"""Updates a child instance of organizationSpecificOamPduData on the server.

		Args:
			Oui (str): 
			Value (str): 

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Oui=None, Value=None):
		"""Adds a new organizationSpecificOamPduData node on the server and retrieves it in this instance.

		Args:
			Oui (str): 
			Value (str): 

		Returns:
			self: This instance with all currently retrieved organizationSpecificOamPduData data using find and the newly added organizationSpecificOamPduData data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the organizationSpecificOamPduData data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Oui=None, Value=None):
		"""Finds and retrieves organizationSpecificOamPduData data from the server.

		All named parameters support regex and can be used to selectively retrieve organizationSpecificOamPduData data from the server.
		By default the find method takes no parameters and will retrieve all organizationSpecificOamPduData data from the server.

		Args:
			Oui (str): 
			Value (str): 

		Returns:
			self: This instance with matching organizationSpecificOamPduData data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of organizationSpecificOamPduData data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the organizationSpecificOamPduData data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
