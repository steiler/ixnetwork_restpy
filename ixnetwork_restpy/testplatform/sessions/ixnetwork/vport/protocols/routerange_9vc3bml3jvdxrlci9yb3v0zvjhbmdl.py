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


class RouteRange(Base):
	"""If true enables the route range.
	The RouteRange class encapsulates a list of routeRange resources that is be managed by the user.
	A list of resources can be retrieved from the server using the RouteRange.find() method.
	The list can be managed by the user by using the RouteRange.add() and RouteRange.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'routeRange'

	def __init__(self, parent):
		super(RouteRange, self).__init__(parent)

	@property
	def Enabled(self):
		"""Enables the router range.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def Mask(self):
		"""The number of bits in the network mask.

		Returns:
			number
		"""
		return self._get_attribute('mask')
	@Mask.setter
	def Mask(self, value):
		self._set_attribute('mask', value)

	@property
	def Metric(self):
		"""The user-assigned routing metric associated with the route range.

		Returns:
			number
		"""
		return self._get_attribute('metric')
	@Metric.setter
	def Metric(self, value):
		self._set_attribute('metric', value)

	@property
	def NetworkNumber(self):
		"""The number of prefixes to be advertised.

		Returns:
			str
		"""
		return self._get_attribute('networkNumber')
	@NetworkNumber.setter
	def NetworkNumber(self, value):
		self._set_attribute('networkNumber', value)

	@property
	def NumberOfRoutes(self):
		"""The number of routes/network addresses to be created, based on the first route plus the mask.

		Returns:
			number
		"""
		return self._get_attribute('numberOfRoutes')
	@NumberOfRoutes.setter
	def NumberOfRoutes(self, value):
		self._set_attribute('numberOfRoutes', value)

	@property
	def Origin(self):
		"""The origin of the advertised route.

		Returns:
			str(area|externalType1|externalType2|nssa|sameArea)
		"""
		return self._get_attribute('origin')
	@Origin.setter
	def Origin(self, value):
		self._set_attribute('origin', value)

	@property
	def Propagate(self):
		"""Enables emulation of NSSA-LSA propagation.

		Returns:
			bool
		"""
		return self._get_attribute('propagate')
	@Propagate.setter
	def Propagate(self, value):
		self._set_attribute('propagate', value)

	def update(self, Enabled=None, Mask=None, Metric=None, NetworkNumber=None, NumberOfRoutes=None, Origin=None, Propagate=None):
		"""Updates a child instance of routeRange on the server.

		Args:
			Enabled (bool): Enables the router range.
			Mask (number): The number of bits in the network mask.
			Metric (number): The user-assigned routing metric associated with the route range.
			NetworkNumber (str): The number of prefixes to be advertised.
			NumberOfRoutes (number): The number of routes/network addresses to be created, based on the first route plus the mask.
			Origin (str(area|externalType1|externalType2|nssa|sameArea)): The origin of the advertised route.
			Propagate (bool): Enables emulation of NSSA-LSA propagation.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Enabled=None, Mask=None, Metric=None, NetworkNumber=None, NumberOfRoutes=None, Origin=None, Propagate=None):
		"""Adds a new routeRange node on the server and retrieves it in this instance.

		Args:
			Enabled (bool): Enables the router range.
			Mask (number): The number of bits in the network mask.
			Metric (number): The user-assigned routing metric associated with the route range.
			NetworkNumber (str): The number of prefixes to be advertised.
			NumberOfRoutes (number): The number of routes/network addresses to be created, based on the first route plus the mask.
			Origin (str(area|externalType1|externalType2|nssa|sameArea)): The origin of the advertised route.
			Propagate (bool): Enables emulation of NSSA-LSA propagation.

		Returns:
			self: This instance with all currently retrieved routeRange data using find and the newly added routeRange data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the routeRange data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Enabled=None, Mask=None, Metric=None, NetworkNumber=None, NumberOfRoutes=None, Origin=None, Propagate=None):
		"""Finds and retrieves routeRange data from the server.

		All named parameters support regex and can be used to selectively retrieve routeRange data from the server.
		By default the find method takes no parameters and will retrieve all routeRange data from the server.

		Args:
			Enabled (bool): Enables the router range.
			Mask (number): The number of bits in the network mask.
			Metric (number): The user-assigned routing metric associated with the route range.
			NetworkNumber (str): The number of prefixes to be advertised.
			NumberOfRoutes (number): The number of routes/network addresses to be created, based on the first route plus the mask.
			Origin (str(area|externalType1|externalType2|nssa|sameArea)): The origin of the advertised route.
			Propagate (bool): Enables emulation of NSSA-LSA propagation.

		Returns:
			self: This instance with matching routeRange data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of routeRange data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the routeRange data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
