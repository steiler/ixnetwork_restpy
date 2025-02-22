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


class IxNetCodeOptions(Base):
	"""Contains the ixNet code generation options
	The IxNetCodeOptions class encapsulates a required ixNetCodeOptions resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'ixNetCodeOptions'

	def __init__(self, parent):
		super(IxNetCodeOptions, self).__init__(parent)

	@property
	def IncludeAvailableHardware(self):
		"""Flag to include available hardware nodes

		Returns:
			bool
		"""
		return self._get_attribute('includeAvailableHardware')
	@IncludeAvailableHardware.setter
	def IncludeAvailableHardware(self, value):
		self._set_attribute('includeAvailableHardware', value)

	@property
	def IncludeConnect(self):
		"""DEPRECATED Flag to include the connect command

		Returns:
			bool
		"""
		return self._get_attribute('includeConnect')
	@IncludeConnect.setter
	def IncludeConnect(self, value):
		self._set_attribute('includeConnect', value)

	@property
	def IncludeDefaultValues(self):
		"""Flag to include attributes that have values which are default

		Returns:
			bool
		"""
		return self._get_attribute('includeDefaultValues')
	@IncludeDefaultValues.setter
	def IncludeDefaultValues(self, value):
		self._set_attribute('includeDefaultValues', value)

	@property
	def IncludeQuickTest(self):
		"""Flag to include quickTest nodes

		Returns:
			bool
		"""
		return self._get_attribute('includeQuickTest')
	@IncludeQuickTest.setter
	def IncludeQuickTest(self, value):
		self._set_attribute('includeQuickTest', value)

	@property
	def IncludeStatistic(self):
		"""Flag to include statistic view nodes

		Returns:
			bool
		"""
		return self._get_attribute('includeStatistic')
	@IncludeStatistic.setter
	def IncludeStatistic(self, value):
		self._set_attribute('includeStatistic', value)

	@property
	def IncludeTAPSettings(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('includeTAPSettings')
	@IncludeTAPSettings.setter
	def IncludeTAPSettings(self, value):
		self._set_attribute('includeTAPSettings', value)

	@property
	def IncludeTestComposer(self):
		"""DEPRECATED Flag to include test composer code

		Returns:
			bool
		"""
		return self._get_attribute('includeTestComposer')
	@IncludeTestComposer.setter
	def IncludeTestComposer(self, value):
		self._set_attribute('includeTestComposer', value)

	@property
	def IncludeTraffic(self):
		"""Flag to include traffic item nodes

		Returns:
			bool
		"""
		return self._get_attribute('includeTraffic')
	@IncludeTraffic.setter
	def IncludeTraffic(self, value):
		self._set_attribute('includeTraffic', value)

	@property
	def IncludeTrafficFlowGroup(self):
		"""Flag to include traffic item high level stream nodes

		Returns:
			bool
		"""
		return self._get_attribute('includeTrafficFlowGroup')
	@IncludeTrafficFlowGroup.setter
	def IncludeTrafficFlowGroup(self, value):
		self._set_attribute('includeTrafficFlowGroup', value)

	@property
	def IncludeTrafficStack(self):
		"""Flag to include high level stream stack nodes

		Returns:
			bool
		"""
		return self._get_attribute('includeTrafficStack')
	@IncludeTrafficStack.setter
	def IncludeTrafficStack(self, value):
		self._set_attribute('includeTrafficStack', value)

	def update(self, IncludeAvailableHardware=None, IncludeConnect=None, IncludeDefaultValues=None, IncludeQuickTest=None, IncludeStatistic=None, IncludeTAPSettings=None, IncludeTestComposer=None, IncludeTraffic=None, IncludeTrafficFlowGroup=None, IncludeTrafficStack=None):
		"""Updates a child instance of ixNetCodeOptions on the server.

		Args:
			IncludeAvailableHardware (bool): Flag to include available hardware nodes
			IncludeConnect (bool): Flag to include the connect command
			IncludeDefaultValues (bool): Flag to include attributes that have values which are default
			IncludeQuickTest (bool): Flag to include quickTest nodes
			IncludeStatistic (bool): Flag to include statistic view nodes
			IncludeTAPSettings (bool): 
			IncludeTestComposer (bool): Flag to include test composer code
			IncludeTraffic (bool): Flag to include traffic item nodes
			IncludeTrafficFlowGroup (bool): Flag to include traffic item high level stream nodes
			IncludeTrafficStack (bool): Flag to include high level stream stack nodes

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
