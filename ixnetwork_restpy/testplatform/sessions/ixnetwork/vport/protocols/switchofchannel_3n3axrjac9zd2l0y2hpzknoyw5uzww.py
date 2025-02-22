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


class SwitchOfChannel(Base):
	"""A high level object that allows to define the OpenFlow Channel configurations for the switch.
	The SwitchOfChannel class encapsulates a list of switchOfChannel resources that is be managed by the user.
	A list of resources can be retrieved from the server using the SwitchOfChannel.find() method.
	The list can be managed by the user by using the SwitchOfChannel.add() and SwitchOfChannel.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'switchOfChannel'

	def __init__(self, parent):
		super(SwitchOfChannel, self).__init__(parent)

	@property
	def AuxiliaryConnection(self):
		"""An instance of the AuxiliaryConnection class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.auxiliaryconnection_zwwvyxv4awxpyxj5q29ubmvjdglvbg.AuxiliaryConnection)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.auxiliaryconnection_zwwvyxv4awxpyxj5q29ubmvjdglvbg import AuxiliaryConnection
		return AuxiliaryConnection(self)

	@property
	def Description(self):
		"""A description of the object

		Returns:
			str
		"""
		return self._get_attribute('description')
	@Description.setter
	def Description(self, value):
		self._set_attribute('description', value)

	@property
	def Enabled(self):
		"""If true, the object is enabled.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def RemoteIp(self):
		"""Signifies the Remote IP address of the selected interface.

		Returns:
			str
		"""
		return self._get_attribute('remoteIp')
	@RemoteIp.setter
	def RemoteIp(self, value):
		self._set_attribute('remoteIp', value)

	def update(self, Description=None, Enabled=None, RemoteIp=None):
		"""Updates a child instance of switchOfChannel on the server.

		Args:
			Description (str): A description of the object
			Enabled (bool): If true, the object is enabled.
			RemoteIp (str): Signifies the Remote IP address of the selected interface.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Description=None, Enabled=None, RemoteIp=None):
		"""Adds a new switchOfChannel node on the server and retrieves it in this instance.

		Args:
			Description (str): A description of the object
			Enabled (bool): If true, the object is enabled.
			RemoteIp (str): Signifies the Remote IP address of the selected interface.

		Returns:
			self: This instance with all currently retrieved switchOfChannel data using find and the newly added switchOfChannel data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the switchOfChannel data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Description=None, Enabled=None, RemoteIp=None):
		"""Finds and retrieves switchOfChannel data from the server.

		All named parameters support regex and can be used to selectively retrieve switchOfChannel data from the server.
		By default the find method takes no parameters and will retrieve all switchOfChannel data from the server.

		Args:
			Description (str): A description of the object
			Enabled (bool): If true, the object is enabled.
			RemoteIp (str): Signifies the Remote IP address of the selected interface.

		Returns:
			self: This instance with matching switchOfChannel data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of switchOfChannel data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the switchOfChannel data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
