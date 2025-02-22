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


class WebAuthRange(Base):
	"""Web Authentication Range Options
	The WebAuthRange class encapsulates a list of webAuthRange resources that is be managed by the user.
	A list of resources can be retrieved from the server using the WebAuthRange.find() method.
	The list can be managed by the user by using the WebAuthRange.add() and WebAuthRange.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'webAuthRange'

	def __init__(self, parent):
		super(WebAuthRange, self).__init__(parent)

	@property
	def Enabled(self):
		"""Disabled ranges won't be configured nor validated.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def Expect(self):
		"""Statistics will be maintained for expected/actual success/failure

		Returns:
			str
		"""
		return self._get_attribute('expect')
	@Expect.setter
	def Expect(self, value):
		self._set_attribute('expect', value)

	@property
	def InputValue1(self):
		"""The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 1 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported

		Returns:
			str
		"""
		return self._get_attribute('inputValue1')
	@InputValue1.setter
	def InputValue1(self, value):
		self._set_attribute('inputValue1', value)

	@property
	def InputValue2(self):
		"""The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 2 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported

		Returns:
			str
		"""
		return self._get_attribute('inputValue2')
	@InputValue2.setter
	def InputValue2(self, value):
		self._set_attribute('inputValue2', value)

	@property
	def InputValue3(self):
		"""The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 3 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported

		Returns:
			str
		"""
		return self._get_attribute('inputValue3')
	@InputValue3.setter
	def InputValue3(self, value):
		self._set_attribute('inputValue3', value)

	@property
	def Name(self):
		"""Name of range

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	@property
	def ObjectId(self):
		"""Unique identifier for this object

		Returns:
			str
		"""
		return self._get_attribute('objectId')

	def update(self, Enabled=None, Expect=None, InputValue1=None, InputValue2=None, InputValue3=None, Name=None):
		"""Updates a child instance of webAuthRange on the server.

		Args:
			Enabled (bool): Disabled ranges won't be configured nor validated.
			Expect (str): Statistics will be maintained for expected/actual success/failure
			InputValue1 (str): The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 1 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported
			InputValue2 (str): The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 2 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported
			InputValue3 (str): The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 3 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported
			Name (str): Name of range

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Enabled=None, Expect=None, InputValue1=None, InputValue2=None, InputValue3=None, Name=None):
		"""Adds a new webAuthRange node on the server and retrieves it in this instance.

		Args:
			Enabled (bool): Disabled ranges won't be configured nor validated.
			Expect (str): Statistics will be maintained for expected/actual success/failure
			InputValue1 (str): The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 1 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported
			InputValue2 (str): The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 2 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported
			InputValue3 (str): The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 3 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported
			Name (str): Name of range

		Returns:
			self: This instance with all currently retrieved webAuthRange data using find and the newly added webAuthRange data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the webAuthRange data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Enabled=None, Expect=None, InputValue1=None, InputValue2=None, InputValue3=None, Name=None, ObjectId=None):
		"""Finds and retrieves webAuthRange data from the server.

		All named parameters support regex and can be used to selectively retrieve webAuthRange data from the server.
		By default the find method takes no parameters and will retrieve all webAuthRange data from the server.

		Args:
			Enabled (bool): Disabled ranges won't be configured nor validated.
			Expect (str): Statistics will be maintained for expected/actual success/failure
			InputValue1 (str): The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 1 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported
			InputValue2 (str): The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 2 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported
			InputValue3 (str): The value to be returned for the input field in the HTTP POST message sent back to the DUT. If the Input field 3 is a radio type, then this value must match one of the choices present on the form. Standard text increment options are supported
			Name (str): Name of range
			ObjectId (str): Unique identifier for this object

		Returns:
			self: This instance with matching webAuthRange data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of webAuthRange data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the webAuthRange data from the server available through an iterator or index

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
