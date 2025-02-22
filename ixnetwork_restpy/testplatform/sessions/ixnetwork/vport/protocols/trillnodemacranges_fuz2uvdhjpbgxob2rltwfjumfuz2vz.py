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


class TrillNodeMacRanges(Base):
	"""NOT DEFINED
	The TrillNodeMacRanges class encapsulates a list of trillNodeMacRanges resources that is be managed by the user.
	A list of resources can be retrieved from the server using the TrillNodeMacRanges.find() method.
	The list can be managed by the user by using the TrillNodeMacRanges.add() and TrillNodeMacRanges.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'trillNodeMacRanges'

	def __init__(self, parent):
		super(TrillNodeMacRanges, self).__init__(parent)

	@property
	def Count(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('count')
	@Count.setter
	def Count(self, value):
		self._set_attribute('count', value)

	@property
	def EnableMacRanges(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('enableMacRanges')
	@EnableMacRanges.setter
	def EnableMacRanges(self, value):
		self._set_attribute('enableMacRanges', value)

	@property
	def InterNodeMacStep(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('interNodeMacStep')
	@InterNodeMacStep.setter
	def InterNodeMacStep(self, value):
		self._set_attribute('interNodeMacStep', value)

	@property
	def StartUnicastMac(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('startUnicastMac')
	@StartUnicastMac.setter
	def StartUnicastMac(self, value):
		self._set_attribute('startUnicastMac', value)

	@property
	def TopologyId(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('topologyId')

	@property
	def UnicastMacStep(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('unicastMacStep')
	@UnicastMacStep.setter
	def UnicastMacStep(self, value):
		self._set_attribute('unicastMacStep', value)

	@property
	def VlanId(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('vlanId')
	@VlanId.setter
	def VlanId(self, value):
		self._set_attribute('vlanId', value)

	def update(self, Count=None, EnableMacRanges=None, InterNodeMacStep=None, StartUnicastMac=None, UnicastMacStep=None, VlanId=None):
		"""Updates a child instance of trillNodeMacRanges on the server.

		Args:
			Count (number): NOT DEFINED
			EnableMacRanges (bool): NOT DEFINED
			InterNodeMacStep (str): NOT DEFINED
			StartUnicastMac (str): NOT DEFINED
			UnicastMacStep (str): NOT DEFINED
			VlanId (number): NOT DEFINED

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Count=None, EnableMacRanges=None, InterNodeMacStep=None, StartUnicastMac=None, UnicastMacStep=None, VlanId=None):
		"""Adds a new trillNodeMacRanges node on the server and retrieves it in this instance.

		Args:
			Count (number): NOT DEFINED
			EnableMacRanges (bool): NOT DEFINED
			InterNodeMacStep (str): NOT DEFINED
			StartUnicastMac (str): NOT DEFINED
			UnicastMacStep (str): NOT DEFINED
			VlanId (number): NOT DEFINED

		Returns:
			self: This instance with all currently retrieved trillNodeMacRanges data using find and the newly added trillNodeMacRanges data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the trillNodeMacRanges data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Count=None, EnableMacRanges=None, InterNodeMacStep=None, StartUnicastMac=None, TopologyId=None, UnicastMacStep=None, VlanId=None):
		"""Finds and retrieves trillNodeMacRanges data from the server.

		All named parameters support regex and can be used to selectively retrieve trillNodeMacRanges data from the server.
		By default the find method takes no parameters and will retrieve all trillNodeMacRanges data from the server.

		Args:
			Count (number): NOT DEFINED
			EnableMacRanges (bool): NOT DEFINED
			InterNodeMacStep (str): NOT DEFINED
			StartUnicastMac (str): NOT DEFINED
			TopologyId (number): NOT DEFINED
			UnicastMacStep (str): NOT DEFINED
			VlanId (number): NOT DEFINED

		Returns:
			self: This instance with matching trillNodeMacRanges data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of trillNodeMacRanges data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the trillNodeMacRanges data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
