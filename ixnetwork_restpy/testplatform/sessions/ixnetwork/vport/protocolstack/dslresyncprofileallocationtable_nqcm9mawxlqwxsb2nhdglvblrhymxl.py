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


class DslResyncProfileAllocationTable(Base):
	"""Percentage of how much this DSL Profile will be used
	The DslResyncProfileAllocationTable class encapsulates a list of dslResyncProfileAllocationTable resources that is be managed by the user.
	A list of resources can be retrieved from the server using the DslResyncProfileAllocationTable.find() method.
	The list can be managed by the user by using the DslResyncProfileAllocationTable.add() and DslResyncProfileAllocationTable.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'dslResyncProfileAllocationTable'

	def __init__(self, parent):
		super(DslResyncProfileAllocationTable, self).__init__(parent)

	@property
	def DslProfile(self):
		"""The DSL profile.

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=ancpDslResyncProfile)
		"""
		return self._get_attribute('dslProfile')
	@DslProfile.setter
	def DslProfile(self, value):
		self._set_attribute('dslProfile', value)

	@property
	def ObjectId(self):
		"""Unique identifier for this object

		Returns:
			str
		"""
		return self._get_attribute('objectId')

	@property
	def Percentage(self):
		"""Percentage of this profile.

		Returns:
			number
		"""
		return self._get_attribute('percentage')
	@Percentage.setter
	def Percentage(self, value):
		self._set_attribute('percentage', value)

	def update(self, DslProfile=None, Percentage=None):
		"""Updates a child instance of dslResyncProfileAllocationTable on the server.

		Args:
			DslProfile (str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=ancpDslResyncProfile)): The DSL profile.
			Percentage (number): Percentage of this profile.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, DslProfile=None, Percentage=None):
		"""Adds a new dslResyncProfileAllocationTable node on the server and retrieves it in this instance.

		Args:
			DslProfile (str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=ancpDslResyncProfile)): The DSL profile.
			Percentage (number): Percentage of this profile.

		Returns:
			self: This instance with all currently retrieved dslResyncProfileAllocationTable data using find and the newly added dslResyncProfileAllocationTable data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the dslResyncProfileAllocationTable data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, DslProfile=None, ObjectId=None, Percentage=None):
		"""Finds and retrieves dslResyncProfileAllocationTable data from the server.

		All named parameters support regex and can be used to selectively retrieve dslResyncProfileAllocationTable data from the server.
		By default the find method takes no parameters and will retrieve all dslResyncProfileAllocationTable data from the server.

		Args:
			DslProfile (str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=ancpDslResyncProfile)): The DSL profile.
			ObjectId (str): Unique identifier for this object
			Percentage (number): Percentage of this profile.

		Returns:
			self: This instance with matching dslResyncProfileAllocationTable data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of dslResyncProfileAllocationTable data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the dslResyncProfileAllocationTable data from the server available through an iterator or index

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
