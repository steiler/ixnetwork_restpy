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


class LosLof(Base):
	"""Emulates loss of signal or loss of framing on the link.
	The LosLof class encapsulates a required losLof resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'losLof'

	def __init__(self, parent):
		super(LosLof, self).__init__(parent)

	@property
	def Duration(self):
		"""The burst duration.

		Returns:
			number
		"""
		return self._get_attribute('duration')
	@Duration.setter
	def Duration(self, value):
		self._set_attribute('duration', value)

	@property
	def IsBurst(self):
		"""If true, loss of signal or loss of frame will be enabled for the specified duration.

		Returns:
			bool
		"""
		return self._get_attribute('isBurst')
	@IsBurst.setter
	def IsBurst(self, value):
		self._set_attribute('isBurst', value)

	@property
	def State(self):
		"""Gets the loss of signal or loss of framing state.

		Returns:
			str(started|stopped)
		"""
		return self._get_attribute('state')

	@property
	def Type(self):
		"""Selects loss of signal or loss of framing.

		Returns:
			str(lof|los)
		"""
		return self._get_attribute('type')
	@Type.setter
	def Type(self, value):
		self._set_attribute('type', value)

	@property
	def Units(self):
		"""Burst duration units.

		Returns:
			str(kMicroseconds|kMilliseconds|kSeconds|microseconds|milliseconds|seconds)
		"""
		return self._get_attribute('units')
	@Units.setter
	def Units(self, value):
		self._set_attribute('units', value)

	def update(self, Duration=None, IsBurst=None, Type=None, Units=None):
		"""Updates a child instance of losLof on the server.

		Args:
			Duration (number): The burst duration.
			IsBurst (bool): If true, loss of signal or loss of frame will be enabled for the specified duration.
			Type (str(lof|los)): Selects loss of signal or loss of framing.
			Units (str(kMicroseconds|kMilliseconds|kSeconds|microseconds|milliseconds|seconds)): Burst duration units.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def Start(self):
		"""Executes the start operation on the server.

		Starts the impairments defined by user (traffic will be impaired).

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('start', payload=payload, response_object=None)

	def Stop(self):
		"""Executes the stop operation on the server.

		Stops the impairments defined by user (traffic will pass unimpaired).

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('stop', payload=payload, response_object=None)
