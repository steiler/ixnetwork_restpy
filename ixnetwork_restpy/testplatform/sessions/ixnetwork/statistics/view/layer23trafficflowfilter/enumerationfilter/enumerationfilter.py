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


class EnumerationFilter(Base):
	"""Enumeration filter specification.
	The EnumerationFilter class encapsulates a list of enumerationFilter resources that is be managed by the user.
	A list of resources can be retrieved from the server using the EnumerationFilter.find() method.
	The list can be managed by the user by using the EnumerationFilter.add() and EnumerationFilter.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'enumerationFilter'

	def __init__(self, parent):
		super(EnumerationFilter, self).__init__(parent)

	@property
	def SortDirection(self):
		"""Sets the display order of the view.

		Returns:
			str(ascending|descending)
		"""
		return self._get_attribute('sortDirection')
	@SortDirection.setter
	def SortDirection(self, value):
		self._set_attribute('sortDirection', value)

	@property
	def TrackingFilterId(self):
		"""Selected tracking filters from the availableTrackingFilter list.

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrackingFilter)
		"""
		return self._get_attribute('trackingFilterId')
	@TrackingFilterId.setter
	def TrackingFilterId(self, value):
		self._set_attribute('trackingFilterId', value)

	def update(self, SortDirection=None, TrackingFilterId=None):
		"""Updates a child instance of enumerationFilter on the server.

		Args:
			SortDirection (str(ascending|descending)): Sets the display order of the view.
			TrackingFilterId (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrackingFilter)): Selected tracking filters from the availableTrackingFilter list.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, SortDirection=None, TrackingFilterId=None):
		"""Adds a new enumerationFilter node on the server and retrieves it in this instance.

		Args:
			SortDirection (str(ascending|descending)): Sets the display order of the view.
			TrackingFilterId (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrackingFilter)): Selected tracking filters from the availableTrackingFilter list.

		Returns:
			self: This instance with all currently retrieved enumerationFilter data using find and the newly added enumerationFilter data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the enumerationFilter data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, SortDirection=None, TrackingFilterId=None):
		"""Finds and retrieves enumerationFilter data from the server.

		All named parameters support regex and can be used to selectively retrieve enumerationFilter data from the server.
		By default the find method takes no parameters and will retrieve all enumerationFilter data from the server.

		Args:
			SortDirection (str(ascending|descending)): Sets the display order of the view.
			TrackingFilterId (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableTrackingFilter)): Selected tracking filters from the availableTrackingFilter list.

		Returns:
			self: This instance with matching enumerationFilter data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of enumerationFilter data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the enumerationFilter data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
