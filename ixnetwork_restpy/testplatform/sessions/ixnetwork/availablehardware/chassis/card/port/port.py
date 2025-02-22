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


class Port(Base):
	"""The physical port assigned to this port configuration.
	The Port class encapsulates a list of port resources that is managed by the system.
	A list of resources can be retrieved from the server using the Port.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'port'

	def __init__(self, parent):
		super(Port, self).__init__(parent)

	@property
	def TapSettings(self):
		"""An instance of the TapSettings class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.card.port.tapsettings.tapsettings.TapSettings)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.card.port.tapsettings.tapsettings import TapSettings
		return TapSettings(self)

	@property
	def Description(self):
		"""The port description/mode.

		Returns:
			str
		"""
		return self._get_attribute('description')

	@property
	def IsAvailable(self):
		"""The link is available on the port.

		Returns:
			bool
		"""
		return self._get_attribute('isAvailable')

	@property
	def IsBusy(self):
		"""The link is unavailable on the port.

		Returns:
			bool
		"""
		return self._get_attribute('isBusy')

	@property
	def IsLinkUp(self):
		"""The link is up on the port.

		Returns:
			bool
		"""
		return self._get_attribute('isLinkUp')

	@property
	def IsUsable(self):
		"""(read only) Returns true of false depending on whether the port can be used, based on the value of parent card aggregationMode. If card aggregationMode is notSupported and normal it always returns true. If card aggregationMode is tenGigAggregation, only the ports with index 1, 5, 9, and 13 returns true.

		Returns:
			bool
		"""
		return self._get_attribute('isUsable')

	@property
	def Owner(self):
		"""The current owner of the port.

		Returns:
			str
		"""
		return self._get_attribute('owner')

	@property
	def PortId(self):
		"""The physical port ID.

		Returns:
			number
		"""
		return self._get_attribute('portId')

	def find(self, Description=None, IsAvailable=None, IsBusy=None, IsLinkUp=None, IsUsable=None, Owner=None, PortId=None):
		"""Finds and retrieves port data from the server.

		All named parameters support regex and can be used to selectively retrieve port data from the server.
		By default the find method takes no parameters and will retrieve all port data from the server.

		Args:
			Description (str): The port description/mode.
			IsAvailable (bool): The link is available on the port.
			IsBusy (bool): The link is unavailable on the port.
			IsLinkUp (bool): The link is up on the port.
			IsUsable (bool): (read only) Returns true of false depending on whether the port can be used, based on the value of parent card aggregationMode. If card aggregationMode is notSupported and normal it always returns true. If card aggregationMode is tenGigAggregation, only the ports with index 1, 5, 9, and 13 returns true.
			Owner (str): The current owner of the port.
			PortId (number): The physical port ID.

		Returns:
			self: This instance with matching port data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of port data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the port data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def ClearOwnership(self):
		"""Executes the clearOwnership operation on the server.

		Clears ownership on a list of hardware ports.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		return self._execute('clearOwnership', payload=payload, response_object=None)

	def CopyTapSettings(self, *args, **kwargs):
		"""Executes the copyTapSettings operation on the server.

		It will copy the values from a port to the given ports.

		copyTapSettings(Arg2:list)
			Args:
				args[0] is Arg2 (list(str[None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=port])): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('copyTapSettings', payload=payload, response_object=None)

	def DeleteCustomDefaults(self):
		"""Executes the deleteCustomDefaults operation on the server.

		It will delete custom defaults for the given ports.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		return self._execute('deleteCustomDefaults', payload=payload, response_object=None)

	def GetTapSettings(self):
		"""Executes the getTapSettings operation on the server.

		Get TAP Settings for the given ports.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		return self._execute('getTapSettings', payload=payload, response_object=None)

	def RestoreCustomDefaults(self):
		"""Executes the restoreCustomDefaults operation on the server.

		It will restore custom defaults for the given ports.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		return self._execute('restoreCustomDefaults', payload=payload, response_object=None)

	def RestoreDefaults(self):
		"""Executes the restoreDefaults operation on the server.

		Restore de default values for the given ports.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		return self._execute('restoreDefaults', payload=payload, response_object=None)

	def SaveCustomDefaults(self):
		"""Executes the saveCustomDefaults operation on the server.

		It will save custom defaults for the given ports.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		return self._execute('saveCustomDefaults', payload=payload, response_object=None)

	def SetTapSettings(self):
		"""Executes the setTapSettings operation on the server.

		Send TAP Settings to IxServer for the given ports.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		return self._execute('setTapSettings', payload=payload, response_object=None)
