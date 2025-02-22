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


class SiteEidRange(Base):
	"""It gives details about the site eid range
	The SiteEidRange class encapsulates a list of siteEidRange resources that is be managed by the user.
	A list of resources can be retrieved from the server using the SiteEidRange.find() method.
	The list can be managed by the user by using the SiteEidRange.add() and SiteEidRange.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'siteEidRange'

	def __init__(self, parent):
		super(SiteEidRange, self).__init__(parent)

	@property
	def Address(self):
		"""It gives details about the Ip address

		Returns:
			str
		"""
		return self._get_attribute('address')
	@Address.setter
	def Address(self, value):
		self._set_attribute('address', value)

	@property
	def Count(self):
		"""It details about the count

		Returns:
			number
		"""
		return self._get_attribute('count')
	@Count.setter
	def Count(self, value):
		self._set_attribute('count', value)

	@property
	def Enabled(self):
		"""It true, it enables the protocol

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def Family(self):
		"""It describes which family it belongs to

		Returns:
			str(ipv4|ipv6)
		"""
		return self._get_attribute('family')
	@Family.setter
	def Family(self, value):
		self._set_attribute('family', value)

	@property
	def IncludeOrExclude(self):
		"""It decides whether to include or exclude

		Returns:
			str(include|exclude)
		"""
		return self._get_attribute('includeOrExclude')
	@IncludeOrExclude.setter
	def IncludeOrExclude(self, value):
		self._set_attribute('includeOrExclude', value)

	@property
	def InstanceId(self):
		"""It gives the instance id

		Returns:
			number
		"""
		return self._get_attribute('instanceId')
	@InstanceId.setter
	def InstanceId(self, value):
		self._set_attribute('instanceId', value)

	@property
	def PrefixLength(self):
		"""It gives details about the prefix length

		Returns:
			number
		"""
		return self._get_attribute('prefixLength')
	@PrefixLength.setter
	def PrefixLength(self, value):
		self._set_attribute('prefixLength', value)

	def update(self, Address=None, Count=None, Enabled=None, Family=None, IncludeOrExclude=None, InstanceId=None, PrefixLength=None):
		"""Updates a child instance of siteEidRange on the server.

		Args:
			Address (str): It gives details about the Ip address
			Count (number): It details about the count
			Enabled (bool): It true, it enables the protocol
			Family (str(ipv4|ipv6)): It describes which family it belongs to
			IncludeOrExclude (str(include|exclude)): It decides whether to include or exclude
			InstanceId (number): It gives the instance id
			PrefixLength (number): It gives details about the prefix length

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Address=None, Count=None, Enabled=None, Family=None, IncludeOrExclude=None, InstanceId=None, PrefixLength=None):
		"""Adds a new siteEidRange node on the server and retrieves it in this instance.

		Args:
			Address (str): It gives details about the Ip address
			Count (number): It details about the count
			Enabled (bool): It true, it enables the protocol
			Family (str(ipv4|ipv6)): It describes which family it belongs to
			IncludeOrExclude (str(include|exclude)): It decides whether to include or exclude
			InstanceId (number): It gives the instance id
			PrefixLength (number): It gives details about the prefix length

		Returns:
			self: This instance with all currently retrieved siteEidRange data using find and the newly added siteEidRange data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the siteEidRange data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Address=None, Count=None, Enabled=None, Family=None, IncludeOrExclude=None, InstanceId=None, PrefixLength=None):
		"""Finds and retrieves siteEidRange data from the server.

		All named parameters support regex and can be used to selectively retrieve siteEidRange data from the server.
		By default the find method takes no parameters and will retrieve all siteEidRange data from the server.

		Args:
			Address (str): It gives details about the Ip address
			Count (number): It details about the count
			Enabled (bool): It true, it enables the protocol
			Family (str(ipv4|ipv6)): It describes which family it belongs to
			IncludeOrExclude (str(include|exclude)): It decides whether to include or exclude
			InstanceId (number): It gives the instance id
			PrefixLength (number): It gives details about the prefix length

		Returns:
			self: This instance with matching siteEidRange data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of siteEidRange data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the siteEidRange data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
