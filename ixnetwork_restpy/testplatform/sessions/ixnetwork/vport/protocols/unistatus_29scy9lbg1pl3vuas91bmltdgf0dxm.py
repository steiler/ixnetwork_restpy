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


class UniStatus(Base):
	"""It signifies the status of the user network interface in case of UNI-N.
	The UniStatus class encapsulates a list of uniStatus resources that is be managed by the user.
	A list of resources can be retrieved from the server using the UniStatus.find() method.
	The list can be managed by the user by using the UniStatus.add() and UniStatus.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'uniStatus'

	def __init__(self, parent):
		super(UniStatus, self).__init__(parent)

	@property
	def BwProfile(self):
		"""An instance of the BwProfile class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bwprofile_vuas91bmltdgf0dxmvyndqcm9mawxl.BwProfile)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bwprofile_vuas91bmltdgf0dxmvyndqcm9mawxl import BwProfile
		return BwProfile(self)

	@property
	def CeVlanIdEvcMapType(self):
		"""Possible values include:allToOneBundling 1, noBundling 2, bundling 3

		Returns:
			str(allToOneBundling|noBundling|bundling)
		"""
		return self._get_attribute('ceVlanIdEvcMapType')
	@CeVlanIdEvcMapType.setter
	def CeVlanIdEvcMapType(self, value):
		self._set_attribute('ceVlanIdEvcMapType', value)

	@property
	def Enabled(self):
		"""If enabled, it shows the UNI status. Not more than one UNI Status can be enabled per UNI-N per port.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def UniIdentifier(self):
		"""It signifies the content of the UNI identifier. The length is determined by UNI Identifier Length field. Default is 0.

		Returns:
			str
		"""
		return self._get_attribute('uniIdentifier')
	@UniIdentifier.setter
	def UniIdentifier(self, value):
		self._set_attribute('uniIdentifier', value)

	@property
	def UniIdentifierLength(self):
		"""It is a 1 octet field. It indicates the length of UNI Identifier content. Default is 1. Min is 1 and Max is 64.

		Returns:
			number
		"""
		return self._get_attribute('uniIdentifierLength')
	@UniIdentifierLength.setter
	def UniIdentifierLength(self, value):
		self._set_attribute('uniIdentifierLength', value)

	def update(self, CeVlanIdEvcMapType=None, Enabled=None, UniIdentifier=None, UniIdentifierLength=None):
		"""Updates a child instance of uniStatus on the server.

		Args:
			CeVlanIdEvcMapType (str(allToOneBundling|noBundling|bundling)): Possible values include:allToOneBundling 1, noBundling 2, bundling 3
			Enabled (bool): If enabled, it shows the UNI status. Not more than one UNI Status can be enabled per UNI-N per port.
			UniIdentifier (str): It signifies the content of the UNI identifier. The length is determined by UNI Identifier Length field. Default is 0.
			UniIdentifierLength (number): It is a 1 octet field. It indicates the length of UNI Identifier content. Default is 1. Min is 1 and Max is 64.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, CeVlanIdEvcMapType=None, Enabled=None, UniIdentifier=None, UniIdentifierLength=None):
		"""Adds a new uniStatus node on the server and retrieves it in this instance.

		Args:
			CeVlanIdEvcMapType (str(allToOneBundling|noBundling|bundling)): Possible values include:allToOneBundling 1, noBundling 2, bundling 3
			Enabled (bool): If enabled, it shows the UNI status. Not more than one UNI Status can be enabled per UNI-N per port.
			UniIdentifier (str): It signifies the content of the UNI identifier. The length is determined by UNI Identifier Length field. Default is 0.
			UniIdentifierLength (number): It is a 1 octet field. It indicates the length of UNI Identifier content. Default is 1. Min is 1 and Max is 64.

		Returns:
			self: This instance with all currently retrieved uniStatus data using find and the newly added uniStatus data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the uniStatus data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, CeVlanIdEvcMapType=None, Enabled=None, UniIdentifier=None, UniIdentifierLength=None):
		"""Finds and retrieves uniStatus data from the server.

		All named parameters support regex and can be used to selectively retrieve uniStatus data from the server.
		By default the find method takes no parameters and will retrieve all uniStatus data from the server.

		Args:
			CeVlanIdEvcMapType (str(allToOneBundling|noBundling|bundling)): Possible values include:allToOneBundling 1, noBundling 2, bundling 3
			Enabled (bool): If enabled, it shows the UNI status. Not more than one UNI Status can be enabled per UNI-N per port.
			UniIdentifier (str): It signifies the content of the UNI identifier. The length is determined by UNI Identifier Length field. Default is 0.
			UniIdentifierLength (number): It is a 1 octet field. It indicates the length of UNI Identifier content. Default is 1. Min is 1 and Max is 64.

		Returns:
			self: This instance with matching uniStatus data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of uniStatus data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the uniStatus data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
