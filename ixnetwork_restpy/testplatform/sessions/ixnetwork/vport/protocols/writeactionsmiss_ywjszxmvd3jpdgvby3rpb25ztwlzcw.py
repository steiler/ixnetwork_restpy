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


class WriteActionsMiss(Base):
	"""Select the type of write action miss capability that the table miss flow entry will support.
	The WriteActionsMiss class encapsulates a required writeActionsMiss resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'writeActionsMiss'

	def __init__(self, parent):
		super(WriteActionsMiss, self).__init__(parent)

	@property
	def CopyTtlIn(self):
		"""If selected, Copy TTL In Write Actions is supported for table miss flow entries.

		Returns:
			bool
		"""
		return self._get_attribute('copyTtlIn')
	@CopyTtlIn.setter
	def CopyTtlIn(self, value):
		self._set_attribute('copyTtlIn', value)

	@property
	def CopyTtlOut(self):
		"""If selected, Copy TTL Out Write Actions is supported for table miss flow entries.

		Returns:
			bool
		"""
		return self._get_attribute('copyTtlOut')
	@CopyTtlOut.setter
	def CopyTtlOut(self, value):
		self._set_attribute('copyTtlOut', value)

	@property
	def DecrementMplsTtl(self):
		"""If selected, Decrement MPLS TTL Write Actions is supported for table miss flow entries.

		Returns:
			bool
		"""
		return self._get_attribute('decrementMplsTtl')
	@DecrementMplsTtl.setter
	def DecrementMplsTtl(self, value):
		self._set_attribute('decrementMplsTtl', value)

	@property
	def DecrementNetworkTtl(self):
		"""If selected, Decrement Network TTL Write Actions is supported for table miss flow entries.

		Returns:
			bool
		"""
		return self._get_attribute('decrementNetworkTtl')
	@DecrementNetworkTtl.setter
	def DecrementNetworkTtl(self, value):
		self._set_attribute('decrementNetworkTtl', value)

	@property
	def Group(self):
		"""If selected, Group Write Actions is supported for table miss flow entries.

		Returns:
			bool
		"""
		return self._get_attribute('group')
	@Group.setter
	def Group(self, value):
		self._set_attribute('group', value)

	@property
	def Output(self):
		"""If selected, Output Write Actions is supported for table miss flow entries.

		Returns:
			bool
		"""
		return self._get_attribute('output')
	@Output.setter
	def Output(self, value):
		self._set_attribute('output', value)

	@property
	def PopMpls(self):
		"""If selected, Pop MPLS Write Actions is supported for table miss flow entries.

		Returns:
			bool
		"""
		return self._get_attribute('popMpls')
	@PopMpls.setter
	def PopMpls(self, value):
		self._set_attribute('popMpls', value)

	@property
	def PopPbb(self):
		"""If selected, Pop PBB Write Actions is supported for table miss flow entries.

		Returns:
			bool
		"""
		return self._get_attribute('popPbb')
	@PopPbb.setter
	def PopPbb(self, value):
		self._set_attribute('popPbb', value)

	@property
	def PopVlan(self):
		"""If selected, Pop VLAN Write Actions is supported for table miss flow entries.

		Returns:
			bool
		"""
		return self._get_attribute('popVlan')
	@PopVlan.setter
	def PopVlan(self, value):
		self._set_attribute('popVlan', value)

	@property
	def PushMpls(self):
		"""If selected, Push MPLS Write Actions is supported for table miss flow entries.

		Returns:
			bool
		"""
		return self._get_attribute('pushMpls')
	@PushMpls.setter
	def PushMpls(self, value):
		self._set_attribute('pushMpls', value)

	@property
	def PushPbb(self):
		"""If selected, Push PBB Write Actions is supported for table miss flow entries.

		Returns:
			bool
		"""
		return self._get_attribute('pushPbb')
	@PushPbb.setter
	def PushPbb(self, value):
		self._set_attribute('pushPbb', value)

	@property
	def PushVlan(self):
		"""If selected, Push VLAN Write Actions is supported for table miss flow entries.

		Returns:
			bool
		"""
		return self._get_attribute('pushVlan')
	@PushVlan.setter
	def PushVlan(self, value):
		self._set_attribute('pushVlan', value)

	@property
	def SetField(self):
		"""If selected, Set Field Write Actions is supported for table miss flow entries.

		Returns:
			bool
		"""
		return self._get_attribute('setField')
	@SetField.setter
	def SetField(self, value):
		self._set_attribute('setField', value)

	@property
	def SetMplsTtl(self):
		"""If selected, Set MPLS TTL Write Actions is supported for table miss flow entries.

		Returns:
			bool
		"""
		return self._get_attribute('setMplsTtl')
	@SetMplsTtl.setter
	def SetMplsTtl(self, value):
		self._set_attribute('setMplsTtl', value)

	@property
	def SetNetworkTtl(self):
		"""If selected, Set Network TTL Write Actions is supported for table miss flow entries.

		Returns:
			bool
		"""
		return self._get_attribute('setNetworkTtl')
	@SetNetworkTtl.setter
	def SetNetworkTtl(self, value):
		self._set_attribute('setNetworkTtl', value)

	@property
	def SetQueue(self):
		"""If selected, Set Queue Write Actions is supported for table miss flow entries.

		Returns:
			bool
		"""
		return self._get_attribute('setQueue')
	@SetQueue.setter
	def SetQueue(self, value):
		self._set_attribute('setQueue', value)

	def update(self, CopyTtlIn=None, CopyTtlOut=None, DecrementMplsTtl=None, DecrementNetworkTtl=None, Group=None, Output=None, PopMpls=None, PopPbb=None, PopVlan=None, PushMpls=None, PushPbb=None, PushVlan=None, SetField=None, SetMplsTtl=None, SetNetworkTtl=None, SetQueue=None):
		"""Updates a child instance of writeActionsMiss on the server.

		Args:
			CopyTtlIn (bool): If selected, Copy TTL In Write Actions is supported for table miss flow entries.
			CopyTtlOut (bool): If selected, Copy TTL Out Write Actions is supported for table miss flow entries.
			DecrementMplsTtl (bool): If selected, Decrement MPLS TTL Write Actions is supported for table miss flow entries.
			DecrementNetworkTtl (bool): If selected, Decrement Network TTL Write Actions is supported for table miss flow entries.
			Group (bool): If selected, Group Write Actions is supported for table miss flow entries.
			Output (bool): If selected, Output Write Actions is supported for table miss flow entries.
			PopMpls (bool): If selected, Pop MPLS Write Actions is supported for table miss flow entries.
			PopPbb (bool): If selected, Pop PBB Write Actions is supported for table miss flow entries.
			PopVlan (bool): If selected, Pop VLAN Write Actions is supported for table miss flow entries.
			PushMpls (bool): If selected, Push MPLS Write Actions is supported for table miss flow entries.
			PushPbb (bool): If selected, Push PBB Write Actions is supported for table miss flow entries.
			PushVlan (bool): If selected, Push VLAN Write Actions is supported for table miss flow entries.
			SetField (bool): If selected, Set Field Write Actions is supported for table miss flow entries.
			SetMplsTtl (bool): If selected, Set MPLS TTL Write Actions is supported for table miss flow entries.
			SetNetworkTtl (bool): If selected, Set Network TTL Write Actions is supported for table miss flow entries.
			SetQueue (bool): If selected, Set Queue Write Actions is supported for table miss flow entries.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
