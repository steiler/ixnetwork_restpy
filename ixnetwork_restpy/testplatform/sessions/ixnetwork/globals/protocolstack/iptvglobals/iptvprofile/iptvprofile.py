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


class IptvProfile(Base):
	"""
	The IptvProfile class encapsulates a list of iptvProfile resources that is be managed by the user.
	A list of resources can be retrieved from the server using the IptvProfile.find() method.
	The list can be managed by the user by using the IptvProfile.add() and IptvProfile.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'iptvProfile'

	def __init__(self, parent):
		super(IptvProfile, self).__init__(parent)

	@property
	def ChangesBeforeView(self):
		"""Number of channels to change before stopping on a channel and watching it for View Duration.

		Returns:
			number
		"""
		return self._get_attribute('changesBeforeView')
	@ChangesBeforeView.setter
	def ChangesBeforeView(self, value):
		self._set_attribute('changesBeforeView', value)

	@property
	def Name(self):
		"""The name of the viewing profile.

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

	@property
	def ViewDuration(self):
		"""Specifies the time in milliseconds to view the last channel.

		Returns:
			number
		"""
		return self._get_attribute('viewDuration')
	@ViewDuration.setter
	def ViewDuration(self, value):
		self._set_attribute('viewDuration', value)

	@property
	def ZapBehavior(self):
		"""Use Zap Only to change channels without viewing the channel or Zap and View to change traffic and receive traffic for the last channel.

		Returns:
			str
		"""
		return self._get_attribute('zapBehavior')
	@ZapBehavior.setter
	def ZapBehavior(self, value):
		self._set_attribute('zapBehavior', value)

	@property
	def ZapDirection(self):
		"""Specifies the direction of changing channels.

		Returns:
			str
		"""
		return self._get_attribute('zapDirection')
	@ZapDirection.setter
	def ZapDirection(self, value):
		self._set_attribute('zapDirection', value)

	@property
	def ZapInterval(self):
		"""Interval in milliseconds between channel changes based on the selected type.

		Returns:
			number
		"""
		return self._get_attribute('zapInterval')
	@ZapInterval.setter
	def ZapInterval(self, value):
		self._set_attribute('zapInterval', value)

	@property
	def ZapIntervalType(self):
		"""Specifies the wait interval type before changing the channels.

		Returns:
			str
		"""
		return self._get_attribute('zapIntervalType')
	@ZapIntervalType.setter
	def ZapIntervalType(self, value):
		self._set_attribute('zapIntervalType', value)

	def update(self, ChangesBeforeView=None, Name=None, ViewDuration=None, ZapBehavior=None, ZapDirection=None, ZapInterval=None, ZapIntervalType=None):
		"""Updates a child instance of iptvProfile on the server.

		Args:
			ChangesBeforeView (number): Number of channels to change before stopping on a channel and watching it for View Duration.
			Name (str): The name of the viewing profile.
			ViewDuration (number): Specifies the time in milliseconds to view the last channel.
			ZapBehavior (str): Use Zap Only to change channels without viewing the channel or Zap and View to change traffic and receive traffic for the last channel.
			ZapDirection (str): Specifies the direction of changing channels.
			ZapInterval (number): Interval in milliseconds between channel changes based on the selected type.
			ZapIntervalType (str): Specifies the wait interval type before changing the channels.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, ChangesBeforeView=None, Name=None, ViewDuration=None, ZapBehavior=None, ZapDirection=None, ZapInterval=None, ZapIntervalType=None):
		"""Adds a new iptvProfile node on the server and retrieves it in this instance.

		Args:
			ChangesBeforeView (number): Number of channels to change before stopping on a channel and watching it for View Duration.
			Name (str): The name of the viewing profile.
			ViewDuration (number): Specifies the time in milliseconds to view the last channel.
			ZapBehavior (str): Use Zap Only to change channels without viewing the channel or Zap and View to change traffic and receive traffic for the last channel.
			ZapDirection (str): Specifies the direction of changing channels.
			ZapInterval (number): Interval in milliseconds between channel changes based on the selected type.
			ZapIntervalType (str): Specifies the wait interval type before changing the channels.

		Returns:
			self: This instance with all currently retrieved iptvProfile data using find and the newly added iptvProfile data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the iptvProfile data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, ChangesBeforeView=None, Name=None, ObjectId=None, ViewDuration=None, ZapBehavior=None, ZapDirection=None, ZapInterval=None, ZapIntervalType=None):
		"""Finds and retrieves iptvProfile data from the server.

		All named parameters support regex and can be used to selectively retrieve iptvProfile data from the server.
		By default the find method takes no parameters and will retrieve all iptvProfile data from the server.

		Args:
			ChangesBeforeView (number): Number of channels to change before stopping on a channel and watching it for View Duration.
			Name (str): The name of the viewing profile.
			ObjectId (str): Unique identifier for this object
			ViewDuration (number): Specifies the time in milliseconds to view the last channel.
			ZapBehavior (str): Use Zap Only to change channels without viewing the channel or Zap and View to change traffic and receive traffic for the last channel.
			ZapDirection (str): Specifies the direction of changing channels.
			ZapInterval (number): Interval in milliseconds between channel changes based on the selected type.
			ZapIntervalType (str): Specifies the wait interval type before changing the channels.

		Returns:
			self: This instance with matching iptvProfile data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of iptvProfile data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the iptvProfile data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
