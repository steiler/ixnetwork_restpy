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


class Groups(Base):
	"""Openflow Groups Configuration
	The Groups class encapsulates a list of groups resources that is managed by the system.
	A list of resources can be retrieved from the server using the Groups.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'groups'

	def __init__(self, parent):
		super(Groups, self).__init__(parent)

	@property
	def Buckets(self):
		"""An instance of the Buckets class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.buckets.Buckets)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.buckets import Buckets
		return Buckets(self)

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def ChannelName(self):
		"""Parent Channel Name

		Returns:
			str
		"""
		return self._get_attribute('channelName')

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def GroupAdvertise(self):
		"""If selected, group is advertised when the OpenFlow channel comes up.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('groupAdvertise')

	@property
	def GroupDescription(self):
		"""A description of the group.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('groupDescription')

	@property
	def GroupId(self):
		"""A 32-bit integer uniquely identifying the group.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('groupId')

	@property
	def GroupType(self):
		"""Select the type of group to determine the group semantics.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('groupType')

	@property
	def Multiplier(self):
		"""Number of instances per parent instance (multiplier)

		Returns:
			number
		"""
		return self._get_attribute('multiplier')
	@Multiplier.setter
	def Multiplier(self, value):
		self._set_attribute('multiplier', value)

	@property
	def Name(self):
		"""Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	@property
	def NumberOfBuckets(self):
		"""Specify the number of Buckets.

		Returns:
			number
		"""
		return self._get_attribute('numberOfBuckets')
	@NumberOfBuckets.setter
	def NumberOfBuckets(self, value):
		self._set_attribute('numberOfBuckets', value)

	@property
	def OfChannel(self):
		"""The OF Channel to which the group belongs.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ofChannel')

	def update(self, Multiplier=None, Name=None, NumberOfBuckets=None):
		"""Updates a child instance of groups on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			Multiplier (number): Number of instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfBuckets (number): Specify the number of Buckets.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def find(self, ChannelName=None, Count=None, DescriptiveName=None, Multiplier=None, Name=None, NumberOfBuckets=None):
		"""Finds and retrieves groups data from the server.

		All named parameters support regex and can be used to selectively retrieve groups data from the server.
		By default the find method takes no parameters and will retrieve all groups data from the server.

		Args:
			ChannelName (str): Parent Channel Name
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
			Multiplier (number): Number of instances per parent instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfBuckets (number): Specify the number of Buckets.

		Returns:
			self: This instance with matching groups data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of groups data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the groups data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, Active=None, GroupAdvertise=None, GroupDescription=None, GroupId=None, GroupType=None, OfChannel=None):
		"""Base class infrastructure that gets a list of groups device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			Active (str): optional regex of active
			GroupAdvertise (str): optional regex of groupAdvertise
			GroupDescription (str): optional regex of groupDescription
			GroupId (str): optional regex of groupId
			GroupType (str): optional regex of groupType
			OfChannel (str): optional regex of ofChannel

		Returns:
			list(int): A list of device ids that meets the regex criteria provided in the method parameters

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._get_ngpf_device_ids(locals())

	def SendAllGroupAdd(self):
		"""Executes the sendAllGroupAdd operation on the server.

		Sends a Group Add on all groups.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('sendAllGroupAdd', payload=payload, response_object=None)

	def SendAllGroupRemove(self):
		"""Executes the sendAllGroupRemove operation on the server.

		Sends a Group Remove on all groups.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('sendAllGroupRemove', payload=payload, response_object=None)

	def SendGroupAdd(self, *args, **kwargs):
		"""Executes the sendGroupAdd operation on the server.

		Sends a Group Add on selected Group.

		sendGroupAdd(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the group range grid

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendGroupAdd', payload=payload, response_object=None)

	def SendGroupRemove(self, *args, **kwargs):
		"""Executes the sendGroupRemove operation on the server.

		Sends a Group Remove on selected Group.

		sendGroupRemove(Arg2:list)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the group range grid

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendGroupRemove', payload=payload, response_object=None)
