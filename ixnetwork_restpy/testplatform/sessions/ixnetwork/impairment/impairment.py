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


class Impairment(Base):
	"""Allows the user to emulate WAN links with impairments such as packet delay and drop.
	The Impairment class encapsulates a required impairment resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'impairment'

	def __init__(self, parent):
		super(Impairment, self).__init__(parent)

	@property
	def DefaultProfile(self):
		"""An instance of the DefaultProfile class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.defaultprofile.DefaultProfile)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.defaultprofile import DefaultProfile
		return DefaultProfile(self)._select()

	@property
	def Link(self):
		"""An instance of the Link class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.link.link.Link)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.link.link import Link
		return Link(self)

	@property
	def Profile(self):
		"""An instance of the Profile class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.profile.profile.Profile)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.profile.profile import Profile
		return Profile(self)

	@property
	def Errors(self):
		"""List of errors which occurred while applying changes to the impairment configuration.

		Returns:
			list(str)
		"""
		return self._get_attribute('errors')

	@property
	def State(self):
		"""Indicates whether changes are being applied to the impairment configuration.

		Returns:
			str(applyingChanges|changesPending|errorOccurred|ready)
		"""
		return self._get_attribute('state')

	@property
	def Warnings(self):
		"""List of warnings which occurred while applying changes to the impairment configuration.

		Returns:
			list(str)
		"""
		return self._get_attribute('warnings')

	def Apply(self):
		"""Executes the apply operation on the server.

		Applies traffic impairments defined by user.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('apply', payload=payload, response_object=None)
