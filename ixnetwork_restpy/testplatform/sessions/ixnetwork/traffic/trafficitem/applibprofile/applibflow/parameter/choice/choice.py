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


class Choice(Base):
	"""This specifies the particular choice related properties for the parameter.
	The Choice class encapsulates a list of choice resources that is managed by the system.
	A list of resources can be retrieved from the server using the Choice.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'choice'

	def __init__(self, parent):
		super(Choice, self).__init__(parent)

	@property
	def Default(self):
		"""(Read only) Parameter choice default value.

		Returns:
			str
		"""
		return self._get_attribute('default')

	@property
	def SupportedValues(self):
		"""(Read only) Parameter supported choice values.

		Returns:
			list(str)
		"""
		return self._get_attribute('supportedValues')

	@property
	def Value(self):
		"""Parameter choice selected value.

		Returns:
			str
		"""
		return self._get_attribute('value')
	@Value.setter
	def Value(self, value):
		self._set_attribute('value', value)

	def update(self, Value=None):
		"""Updates a child instance of choice on the server.

		Args:
			Value (str): Parameter choice selected value.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def find(self, Default=None, SupportedValues=None, Value=None):
		"""Finds and retrieves choice data from the server.

		All named parameters support regex and can be used to selectively retrieve choice data from the server.
		By default the find method takes no parameters and will retrieve all choice data from the server.

		Args:
			Default (str): (Read only) Parameter choice default value.
			SupportedValues (list(str)): (Read only) Parameter supported choice values.
			Value (str): Parameter choice selected value.

		Returns:
			self: This instance with matching choice data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of choice data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the choice data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
