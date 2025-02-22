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


class ProtocolTemplate(Base):
	"""This object provides different options for Protocol Template.
	The ProtocolTemplate class encapsulates a list of protocolTemplate resources that is managed by the system.
	A list of resources can be retrieved from the server using the ProtocolTemplate.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'protocolTemplate'

	def __init__(self, parent):
		super(ProtocolTemplate, self).__init__(parent)

	@property
	def Field(self):
		"""An instance of the Field class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.protocoltemplate.field.field.Field)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.protocoltemplate.field.field import Field
		return Field(self)

	@property
	def DisplayName(self):
		"""The display name of the template.

		Returns:
			str
		"""
		return self._get_attribute('displayName')

	@property
	def StackTypeId(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('stackTypeId')

	@property
	def TemplateName(self):
		"""Indicates the protocol template name that is added to a packet.

		Returns:
			str
		"""
		return self._get_attribute('templateName')

	def find(self, DisplayName=None, StackTypeId=None, TemplateName=None):
		"""Finds and retrieves protocolTemplate data from the server.

		All named parameters support regex and can be used to selectively retrieve protocolTemplate data from the server.
		By default the find method takes no parameters and will retrieve all protocolTemplate data from the server.

		Args:
			DisplayName (str): The display name of the template.
			StackTypeId (str): 
			TemplateName (str): Indicates the protocol template name that is added to a packet.

		Returns:
			self: This instance with matching protocolTemplate data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of protocolTemplate data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the protocolTemplate data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
