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


class CeVlanIdRange(Base):
	"""It signifies the VLAN ranges configured for a particular EVC.
	The CeVlanIdRange class encapsulates a list of ceVlanIdRange resources that is be managed by the user.
	A list of resources can be retrieved from the server using the CeVlanIdRange.find() method.
	The list can be managed by the user by using the CeVlanIdRange.add() and CeVlanIdRange.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'ceVlanIdRange'

	def __init__(self, parent):
		super(CeVlanIdRange, self).__init__(parent)

	@property
	def Count(self):
		"""It signifies the number of Vlan Ids configured for the EVC.

		Returns:
			number
		"""
		return self._get_attribute('count')
	@Count.setter
	def Count(self, value):
		self._set_attribute('count', value)

	@property
	def Enabled(self):
		"""If enabled, CE VLAN Id range is in effect for the EVC.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def IncrementStep(self):
		"""It shows the Increment Step of Vlan ID. Default is 1.

		Returns:
			number
		"""
		return self._get_attribute('incrementStep')
	@IncrementStep.setter
	def IncrementStep(self, value):
		self._set_attribute('incrementStep', value)

	@property
	def StartVlanId(self):
		"""The VLAN Id of first VLAN. Default is 1.

		Returns:
			number
		"""
		return self._get_attribute('startVlanId')
	@StartVlanId.setter
	def StartVlanId(self, value):
		self._set_attribute('startVlanId', value)

	def update(self, Count=None, Enabled=None, IncrementStep=None, StartVlanId=None):
		"""Updates a child instance of ceVlanIdRange on the server.

		Args:
			Count (number): It signifies the number of Vlan Ids configured for the EVC.
			Enabled (bool): If enabled, CE VLAN Id range is in effect for the EVC.
			IncrementStep (number): It shows the Increment Step of Vlan ID. Default is 1.
			StartVlanId (number): The VLAN Id of first VLAN. Default is 1.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Count=None, Enabled=None, IncrementStep=None, StartVlanId=None):
		"""Adds a new ceVlanIdRange node on the server and retrieves it in this instance.

		Args:
			Count (number): It signifies the number of Vlan Ids configured for the EVC.
			Enabled (bool): If enabled, CE VLAN Id range is in effect for the EVC.
			IncrementStep (number): It shows the Increment Step of Vlan ID. Default is 1.
			StartVlanId (number): The VLAN Id of first VLAN. Default is 1.

		Returns:
			self: This instance with all currently retrieved ceVlanIdRange data using find and the newly added ceVlanIdRange data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the ceVlanIdRange data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Count=None, Enabled=None, IncrementStep=None, StartVlanId=None):
		"""Finds and retrieves ceVlanIdRange data from the server.

		All named parameters support regex and can be used to selectively retrieve ceVlanIdRange data from the server.
		By default the find method takes no parameters and will retrieve all ceVlanIdRange data from the server.

		Args:
			Count (number): It signifies the number of Vlan Ids configured for the EVC.
			Enabled (bool): If enabled, CE VLAN Id range is in effect for the EVC.
			IncrementStep (number): It shows the Increment Step of Vlan ID. Default is 1.
			StartVlanId (number): The VLAN Id of first VLAN. Default is 1.

		Returns:
			self: This instance with matching ceVlanIdRange data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of ceVlanIdRange data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the ceVlanIdRange data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
