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


class AvailableAdvancedFilterOptions(Base):
	"""Provides a list of all the statistics and the filtering options for the current view.
	The AvailableAdvancedFilterOptions class encapsulates a list of availableAdvancedFilterOptions resources that is managed by the system.
	A list of resources can be retrieved from the server using the AvailableAdvancedFilterOptions.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'availableAdvancedFilterOptions'

	def __init__(self, parent):
		super(AvailableAdvancedFilterOptions, self).__init__(parent)

	@property
	def Operators(self):
		"""Returns the operators list for a filter option.

		Returns:
			str
		"""
		return self._get_attribute('operators')

	@property
	def Stat(self):
		"""Returns the statistic name for a filter option.

		Returns:
			str
		"""
		return self._get_attribute('stat')

	def find(self, Operators=None, Stat=None):
		"""Finds and retrieves availableAdvancedFilterOptions data from the server.

		All named parameters support regex and can be used to selectively retrieve availableAdvancedFilterOptions data from the server.
		By default the find method takes no parameters and will retrieve all availableAdvancedFilterOptions data from the server.

		Args:
			Operators (str): Returns the operators list for a filter option.
			Stat (str): Returns the statistic name for a filter option.

		Returns:
			self: This instance with matching availableAdvancedFilterOptions data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of availableAdvancedFilterOptions data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the availableAdvancedFilterOptions data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
