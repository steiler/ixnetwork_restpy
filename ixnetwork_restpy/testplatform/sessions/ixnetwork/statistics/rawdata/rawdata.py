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


class RawData(Base):
	"""NOT DEFINED
	The RawData class encapsulates a required rawData resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'rawData'

	def __init__(self, parent):
		super(RawData, self).__init__(parent)

	@property
	def Statistic(self):
		"""An instance of the Statistic class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.rawdata.statistic.statistic.Statistic)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.rawdata.statistic.statistic import Statistic
		return Statistic(self)

	@property
	def Enabled(self):
		"""NOT DEFINED

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def LastRawDataFolder(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('lastRawDataFolder')

	@property
	def Path(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('path')
	@Path.setter
	def Path(self, value):
		self._set_attribute('path', value)

	def update(self, Enabled=None, Path=None):
		"""Updates a child instance of rawData on the server.

		Args:
			Enabled (bool): NOT DEFINED
			Path (str): NOT DEFINED

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def StopCollection(self):
		"""Executes the stopCollection operation on the server.

		NOT DEFINED

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('stopCollection', payload=payload, response_object=None)
