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


class Layer47AppLibraryTrafficFilter(Base):
	"""Describes the filter for a layer 4-7 AppLibrary Traffic view.
	The Layer47AppLibraryTrafficFilter class encapsulates a list of layer47AppLibraryTrafficFilter resources that is be managed by the user.
	A list of resources can be retrieved from the server using the Layer47AppLibraryTrafficFilter.find() method.
	The list can be managed by the user by using the Layer47AppLibraryTrafficFilter.add() and Layer47AppLibraryTrafficFilter.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'layer47AppLibraryTrafficFilter'

	def __init__(self, parent):
		super(Layer47AppLibraryTrafficFilter, self).__init__(parent)

	@property
	def AdvancedFilter(self):
		"""An instance of the AdvancedFilter class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer47applibrarytrafficfilter.advancedfilter.advancedfilter.AdvancedFilter)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer47applibrarytrafficfilter.advancedfilter.advancedfilter import AdvancedFilter
		return AdvancedFilter(self)

	@property
	def AdvancedFilterName(self):
		"""Specifies an advanced filter from the ones available in the selected drill down view.

		Returns:
			str
		"""
		return self._get_attribute('advancedFilterName')
	@AdvancedFilterName.setter
	def AdvancedFilterName(self, value):
		self._set_attribute('advancedFilterName', value)

	@property
	def AllAdvancedFilters(self):
		"""Returns a list with all the filters that are present in the selected drill down views. This includes filters that cannot be applied for the current drill down view.

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableAdvancedFilters)
		"""
		return self._get_attribute('allAdvancedFilters')

	@property
	def MatchingAdvancedFilters(self):
		"""Specifies a list that contains only the filters which can be applied on the current drill down view.

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableAdvancedFilters)
		"""
		return self._get_attribute('matchingAdvancedFilters')

	@property
	def TopxEnabled(self):
		"""The view only shows the number of rows specified by TopXValue. If the view is OnDemand, it will become RealTime.

		Returns:
			bool
		"""
		return self._get_attribute('topxEnabled')
	@TopxEnabled.setter
	def TopxEnabled(self, value):
		self._set_attribute('topxEnabled', value)

	@property
	def TopxValue(self):
		"""The number of rows to be shown when TopXEnabled is set to true.

		Returns:
			number
		"""
		return self._get_attribute('topxValue')
	@TopxValue.setter
	def TopxValue(self, value):
		self._set_attribute('topxValue', value)

	def update(self, AdvancedFilterName=None, TopxEnabled=None, TopxValue=None):
		"""Updates a child instance of layer47AppLibraryTrafficFilter on the server.

		Args:
			AdvancedFilterName (str): Specifies an advanced filter from the ones available in the selected drill down view.
			TopxEnabled (bool): The view only shows the number of rows specified by TopXValue. If the view is OnDemand, it will become RealTime.
			TopxValue (number): The number of rows to be shown when TopXEnabled is set to true.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, AdvancedFilterName=None, TopxEnabled=None, TopxValue=None):
		"""Adds a new layer47AppLibraryTrafficFilter node on the server and retrieves it in this instance.

		Args:
			AdvancedFilterName (str): Specifies an advanced filter from the ones available in the selected drill down view.
			TopxEnabled (bool): The view only shows the number of rows specified by TopXValue. If the view is OnDemand, it will become RealTime.
			TopxValue (number): The number of rows to be shown when TopXEnabled is set to true.

		Returns:
			self: This instance with all currently retrieved layer47AppLibraryTrafficFilter data using find and the newly added layer47AppLibraryTrafficFilter data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the layer47AppLibraryTrafficFilter data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, AdvancedFilterName=None, AllAdvancedFilters=None, MatchingAdvancedFilters=None, TopxEnabled=None, TopxValue=None):
		"""Finds and retrieves layer47AppLibraryTrafficFilter data from the server.

		All named parameters support regex and can be used to selectively retrieve layer47AppLibraryTrafficFilter data from the server.
		By default the find method takes no parameters and will retrieve all layer47AppLibraryTrafficFilter data from the server.

		Args:
			AdvancedFilterName (str): Specifies an advanced filter from the ones available in the selected drill down view.
			AllAdvancedFilters (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableAdvancedFilters)): Returns a list with all the filters that are present in the selected drill down views. This includes filters that cannot be applied for the current drill down view.
			MatchingAdvancedFilters (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableAdvancedFilters)): Specifies a list that contains only the filters which can be applied on the current drill down view.
			TopxEnabled (bool): The view only shows the number of rows specified by TopXValue. If the view is OnDemand, it will become RealTime.
			TopxValue (number): The number of rows to be shown when TopXEnabled is set to true.

		Returns:
			self: This instance with matching layer47AppLibraryTrafficFilter data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of layer47AppLibraryTrafficFilter data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the layer47AppLibraryTrafficFilter data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def AddAdvancedFilter(self, *args, **kwargs):
		"""Executes the addAdvancedFilter operation on the server.

		NOT DEFINED

		addAdvancedFilter(Arg2:href)
			Args:
				args[0] is Arg2 (str(None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availableAdvancedFilters)): NOT DEFINED

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('addAdvancedFilter', payload=payload, response_object=None)

	def RemoveAdvancedFilter(self, *args, **kwargs):
		"""Executes the removeAdvancedFilter operation on the server.

		NOT DEFINED

		removeAdvancedFilter(Arg2:string)
			Args:
				args[0] is Arg2 (str): NOT DEFINED

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('removeAdvancedFilter', payload=payload, response_object=None)

	def RemoveAllAdvancedFilters(self):
		"""Executes the removeAllAdvancedFilters operation on the server.

		NOT DEFINED

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('removeAllAdvancedFilters', payload=payload, response_object=None)
