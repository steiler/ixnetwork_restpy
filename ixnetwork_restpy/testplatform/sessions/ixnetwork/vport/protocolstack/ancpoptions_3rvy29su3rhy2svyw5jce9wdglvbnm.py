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


class AncpOptions(Base):
	"""Portgroup settings placeholder for AncpPlugin.
	The AncpOptions class encapsulates a list of ancpOptions resources that is be managed by the user.
	A list of resources can be retrieved from the server using the AncpOptions.find() method.
	The list can be managed by the user by using the AncpOptions.add() and AncpOptions.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'ancpOptions'

	def __init__(self, parent):
		super(AncpOptions, self).__init__(parent)

	@property
	def ObjectId(self):
		"""Unique identifier for this object

		Returns:
			str
		"""
		return self._get_attribute('objectId')

	@property
	def OverrideGlobalRate(self):
		"""If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.

		Returns:
			bool
		"""
		return self._get_attribute('overrideGlobalRate')
	@OverrideGlobalRate.setter
	def OverrideGlobalRate(self, value):
		self._set_attribute('overrideGlobalRate', value)

	@property
	def PortDownRate(self):
		"""PORT-DOWN rate is the number of clients to stop in each second.

		Returns:
			number
		"""
		return self._get_attribute('portDownRate')
	@PortDownRate.setter
	def PortDownRate(self, value):
		self._set_attribute('portDownRate', value)

	@property
	def PortUpRate(self):
		"""PORT-UP rate is the number of clients to start in each second.

		Returns:
			number
		"""
		return self._get_attribute('portUpRate')
	@PortUpRate.setter
	def PortUpRate(self, value):
		self._set_attribute('portUpRate', value)

	@property
	def ResyncRate(self):
		"""RESYNC rate is the number of clients to stop in each second.

		Returns:
			number
		"""
		return self._get_attribute('resyncRate')
	@ResyncRate.setter
	def ResyncRate(self, value):
		self._set_attribute('resyncRate', value)

	def update(self, OverrideGlobalRate=None, PortDownRate=None, PortUpRate=None, ResyncRate=None):
		"""Updates a child instance of ancpOptions on the server.

		Args:
			OverrideGlobalRate (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
			PortDownRate (number): PORT-DOWN rate is the number of clients to stop in each second.
			PortUpRate (number): PORT-UP rate is the number of clients to start in each second.
			ResyncRate (number): RESYNC rate is the number of clients to stop in each second.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, OverrideGlobalRate=None, PortDownRate=None, PortUpRate=None, ResyncRate=None):
		"""Adds a new ancpOptions node on the server and retrieves it in this instance.

		Args:
			OverrideGlobalRate (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
			PortDownRate (number): PORT-DOWN rate is the number of clients to stop in each second.
			PortUpRate (number): PORT-UP rate is the number of clients to start in each second.
			ResyncRate (number): RESYNC rate is the number of clients to stop in each second.

		Returns:
			self: This instance with all currently retrieved ancpOptions data using find and the newly added ancpOptions data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the ancpOptions data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, ObjectId=None, OverrideGlobalRate=None, PortDownRate=None, PortUpRate=None, ResyncRate=None):
		"""Finds and retrieves ancpOptions data from the server.

		All named parameters support regex and can be used to selectively retrieve ancpOptions data from the server.
		By default the find method takes no parameters and will retrieve all ancpOptions data from the server.

		Args:
			ObjectId (str): Unique identifier for this object
			OverrideGlobalRate (bool): If true then all the rate settings defined at Session level will be overriden by rate settings defined on this PortGroup.
			PortDownRate (number): PORT-DOWN rate is the number of clients to stop in each second.
			PortUpRate (number): PORT-UP rate is the number of clients to start in each second.
			ResyncRate (number): RESYNC rate is the number of clients to stop in each second.

		Returns:
			self: This instance with matching ancpOptions data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of ancpOptions data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the ancpOptions data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def CustomProtocolStack(self, *args, **kwargs):
		"""Executes the customProtocolStack operation on the server.

		Create custom protocol stack under /vport/protocolStack

		customProtocolStack(Arg2:list, Arg3:enum)
			Args:
				args[0] is Arg2 (list(str)): List of plugin types to be added in the new custom stack
				args[1] is Arg3 (str(kAppend|kMerge|kOverwrite)): Append, merge or overwrite existing protocol stack

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('customProtocolStack', payload=payload, response_object=None)

	def DisableProtocolStack(self, *args, **kwargs):
		"""Executes the disableProtocolStack operation on the server.

		Disable a protocol under protocolStack using the class name

		disableProtocolStack(Arg2:string)string
			Args:
				args[0] is Arg2 (str): Protocol class name to disable

			Returns:
				str: Status of the exec

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('disableProtocolStack', payload=payload, response_object=None)

	def EnableProtocolStack(self, *args, **kwargs):
		"""Executes the enableProtocolStack operation on the server.

		Enable a protocol under protocolStack using the class name

		enableProtocolStack(Arg2:string)string
			Args:
				args[0] is Arg2 (str): Protocol class name to enable

			Returns:
				str: Status of the exec

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('enableProtocolStack', payload=payload, response_object=None)
