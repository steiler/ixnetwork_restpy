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


class Group(Base):
	"""A group is a list of action buckets and some means of choosing one or more of those buckets to apply on a per-packet basis. A group table consists of group entries. The ability for a flow entry to point to a group enables OpenFlow to represent additional methods of forwarding
	The Group class encapsulates a list of group resources that is be managed by the user.
	A list of resources can be retrieved from the server using the Group.find() method.
	The list can be managed by the user by using the Group.add() and Group.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'group'

	def __init__(self, parent):
		super(Group, self).__init__(parent)

	@property
	def Bucket(self):
		"""An instance of the Bucket class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bucket_29mq2hhbm5lbc9ncm91cc9idwnrzxq.Bucket)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bucket_29mq2hhbm5lbc9ncm91cc9idwnrzxq import Bucket
		return Bucket(self)

	@property
	def __id__(self):
		"""A 32-bit integer uniquely identifying the group. The minimum value is 1. the maximum value is 4294967295

		Returns:
			number
		"""
		return self._get_attribute('__id__')
	@__id__.setter
	def __id__(self, value):
		self._set_attribute('__id__', value)

	@property
	def Description(self):
		"""A description of the group is shown

		Returns:
			str
		"""
		return self._get_attribute('description')
	@Description.setter
	def Description(self, value):
		self._set_attribute('description', value)

	@property
	def Enabled(self):
		"""If selected, this group is used in this controller configuration. The default value is False.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def GroupAdvertise(self):
		"""If this check box is selected, Group ADD message is sent automatically after OpenFlow channel comes up. Group ADD or DEL message is sent out when the Enable is checked or cleared respectively. When this check box is not selected, no group is advertised when the OpenFlow channel comes up or when the Enable check box is selected/ cleared. This field is useful to send group ADD/MOD/DEL messages on demand, or doing negative testing. The on-demand ADD/MOD/DEL messages can be sent by choosing the appropriate option from the right-click menu or from the ribbon option of Update Group Mod Status.

		Returns:
			bool
		"""
		return self._get_attribute('groupAdvertise')
	@GroupAdvertise.setter
	def GroupAdvertise(self, value):
		self._set_attribute('groupAdvertise', value)

	@property
	def Type(self):
		"""Select the type to determine the group semantics.The default Value is all.

		Returns:
			str(all|select|indirect|fastFailover)
		"""
		return self._get_attribute('type')
	@Type.setter
	def Type(self, value):
		self._set_attribute('type', value)

	@property
	def UpdateGroupModStatus(self):
		"""It is a read-only field which indicates if any group is changed in the GUI. If any group is changed then this status indicates to the user to send a Group MOD request to the switch so that the changed value is updated in switch.

		Returns:
			str
		"""
		return self._get_attribute('updateGroupModStatus')

	def update(self, __id__=None, Description=None, Enabled=None, GroupAdvertise=None, Type=None):
		"""Updates a child instance of group on the server.

		Args:
			__id__ (number): A 32-bit integer uniquely identifying the group. The minimum value is 1. the maximum value is 4294967295
			Description (str): A description of the group is shown
			Enabled (bool): If selected, this group is used in this controller configuration. The default value is False.
			GroupAdvertise (bool): If this check box is selected, Group ADD message is sent automatically after OpenFlow channel comes up. Group ADD or DEL message is sent out when the Enable is checked or cleared respectively. When this check box is not selected, no group is advertised when the OpenFlow channel comes up or when the Enable check box is selected/ cleared. This field is useful to send group ADD/MOD/DEL messages on demand, or doing negative testing. The on-demand ADD/MOD/DEL messages can be sent by choosing the appropriate option from the right-click menu or from the ribbon option of Update Group Mod Status.
			Type (str(all|select|indirect|fastFailover)): Select the type to determine the group semantics.The default Value is all.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, __id__=None, Description=None, Enabled=None, GroupAdvertise=None, Type=None):
		"""Adds a new group node on the server and retrieves it in this instance.

		Args:
			__id__ (number): A 32-bit integer uniquely identifying the group. The minimum value is 1. the maximum value is 4294967295
			Description (str): A description of the group is shown
			Enabled (bool): If selected, this group is used in this controller configuration. The default value is False.
			GroupAdvertise (bool): If this check box is selected, Group ADD message is sent automatically after OpenFlow channel comes up. Group ADD or DEL message is sent out when the Enable is checked or cleared respectively. When this check box is not selected, no group is advertised when the OpenFlow channel comes up or when the Enable check box is selected/ cleared. This field is useful to send group ADD/MOD/DEL messages on demand, or doing negative testing. The on-demand ADD/MOD/DEL messages can be sent by choosing the appropriate option from the right-click menu or from the ribbon option of Update Group Mod Status.
			Type (str(all|select|indirect|fastFailover)): Select the type to determine the group semantics.The default Value is all.

		Returns:
			self: This instance with all currently retrieved group data using find and the newly added group data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the group data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, __id__=None, Description=None, Enabled=None, GroupAdvertise=None, Type=None, UpdateGroupModStatus=None):
		"""Finds and retrieves group data from the server.

		All named parameters support regex and can be used to selectively retrieve group data from the server.
		By default the find method takes no parameters and will retrieve all group data from the server.

		Args:
			__id__ (number): A 32-bit integer uniquely identifying the group. The minimum value is 1. the maximum value is 4294967295
			Description (str): A description of the group is shown
			Enabled (bool): If selected, this group is used in this controller configuration. The default value is False.
			GroupAdvertise (bool): If this check box is selected, Group ADD message is sent automatically after OpenFlow channel comes up. Group ADD or DEL message is sent out when the Enable is checked or cleared respectively. When this check box is not selected, no group is advertised when the OpenFlow channel comes up or when the Enable check box is selected/ cleared. This field is useful to send group ADD/MOD/DEL messages on demand, or doing negative testing. The on-demand ADD/MOD/DEL messages can be sent by choosing the appropriate option from the right-click menu or from the ribbon option of Update Group Mod Status.
			Type (str(all|select|indirect|fastFailover)): Select the type to determine the group semantics.The default Value is all.
			UpdateGroupModStatus (str): It is a read-only field which indicates if any group is changed in the GUI. If any group is changed then this status indicates to the user to send a Group MOD request to the switch so that the changed value is updated in switch.

		Returns:
			self: This instance with matching group data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of group data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the group data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def UpdateGroupMod(self, *args, **kwargs):
		"""Executes the updateGroupMod operation on the server.

		NOT DEFINED

		updateGroupMod(Arg2:enum)bool
			Args:
				args[0] is Arg2 (str(sendGroupAdd|sendGroupModify|sendGroupRemove)): NOT DEFINED

			Returns:
				bool: NOT DEFINED

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('updateGroupMod', payload=payload, response_object=None)
