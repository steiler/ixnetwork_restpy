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


class ApplyActionType(Base):
	"""NOT DEFINED
	The ApplyActionType class encapsulates a required applyActionType resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'applyActionType'

	def __init__(self, parent):
		super(ApplyActionType, self).__init__(parent)

	@property
	def CopyTtlIn(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('copyTtlIn')
	@CopyTtlIn.setter
	def CopyTtlIn(self, value):
		self._set_attribute('copyTtlIn', value)

	@property
	def CopyTtlOut(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('copyTtlOut')
	@CopyTtlOut.setter
	def CopyTtlOut(self, value):
		self._set_attribute('copyTtlOut', value)

	@property
	def DecrementMplsTtl(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('decrementMplsTtl')
	@DecrementMplsTtl.setter
	def DecrementMplsTtl(self, value):
		self._set_attribute('decrementMplsTtl', value)

	@property
	def DecrementNetworkTtl(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('decrementNetworkTtl')
	@DecrementNetworkTtl.setter
	def DecrementNetworkTtl(self, value):
		self._set_attribute('decrementNetworkTtl', value)

	@property
	def Experimenter(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('experimenter')
	@Experimenter.setter
	def Experimenter(self, value):
		self._set_attribute('experimenter', value)

	@property
	def Group(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('group')
	@Group.setter
	def Group(self, value):
		self._set_attribute('group', value)

	@property
	def Output(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('output')
	@Output.setter
	def Output(self, value):
		self._set_attribute('output', value)

	@property
	def PopMpls(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('popMpls')
	@PopMpls.setter
	def PopMpls(self, value):
		self._set_attribute('popMpls', value)

	@property
	def PopPbb(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('popPbb')
	@PopPbb.setter
	def PopPbb(self, value):
		self._set_attribute('popPbb', value)

	@property
	def PopVlan(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('popVlan')
	@PopVlan.setter
	def PopVlan(self, value):
		self._set_attribute('popVlan', value)

	@property
	def PushMpls(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('pushMpls')
	@PushMpls.setter
	def PushMpls(self, value):
		self._set_attribute('pushMpls', value)

	@property
	def PushPbb(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('pushPbb')
	@PushPbb.setter
	def PushPbb(self, value):
		self._set_attribute('pushPbb', value)

	@property
	def PushVlan(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('pushVlan')
	@PushVlan.setter
	def PushVlan(self, value):
		self._set_attribute('pushVlan', value)

	@property
	def SetField(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('setField')
	@SetField.setter
	def SetField(self, value):
		self._set_attribute('setField', value)

	@property
	def SetMplsTtl(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('setMplsTtl')
	@SetMplsTtl.setter
	def SetMplsTtl(self, value):
		self._set_attribute('setMplsTtl', value)

	@property
	def SetNetworkTtl(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('setNetworkTtl')
	@SetNetworkTtl.setter
	def SetNetworkTtl(self, value):
		self._set_attribute('setNetworkTtl', value)

	@property
	def SetQueue(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('setQueue')
	@SetQueue.setter
	def SetQueue(self, value):
		self._set_attribute('setQueue', value)

	def update(self, CopyTtlIn=None, CopyTtlOut=None, DecrementMplsTtl=None, DecrementNetworkTtl=None, Experimenter=None, Group=None, Output=None, PopMpls=None, PopPbb=None, PopVlan=None, PushMpls=None, PushPbb=None, PushVlan=None, SetField=None, SetMplsTtl=None, SetNetworkTtl=None, SetQueue=None):
		"""Updates a child instance of applyActionType on the server.

		Args:
			CopyTtlIn (bool): NOT DEFINED
			CopyTtlOut (bool): NOT DEFINED
			DecrementMplsTtl (bool): NOT DEFINED
			DecrementNetworkTtl (bool): NOT DEFINED
			Experimenter (bool): NOT DEFINED
			Group (bool): NOT DEFINED
			Output (bool): NOT DEFINED
			PopMpls (bool): NOT DEFINED
			PopPbb (bool): NOT DEFINED
			PopVlan (bool): NOT DEFINED
			PushMpls (bool): NOT DEFINED
			PushPbb (bool): NOT DEFINED
			PushVlan (bool): NOT DEFINED
			SetField (bool): NOT DEFINED
			SetMplsTtl (bool): NOT DEFINED
			SetNetworkTtl (bool): NOT DEFINED
			SetQueue (bool): NOT DEFINED

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
