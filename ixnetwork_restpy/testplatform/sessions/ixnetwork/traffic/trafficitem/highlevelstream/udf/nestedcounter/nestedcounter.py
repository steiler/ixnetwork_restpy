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


class NestedCounter(Base):
	"""This object provides different options for UDF in Nested Counter Type.
	The NestedCounter class encapsulates a list of nestedCounter resources that is managed by the system.
	A list of resources can be retrieved from the server using the NestedCounter.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'nestedCounter'

	def __init__(self, parent):
		super(NestedCounter, self).__init__(parent)

	@property
	def AvailableWidths(self):
		"""Species all the possible widths available for a UDF in particular Type.

		Returns:
			list(str)
		"""
		return self._get_attribute('availableWidths')

	@property
	def BitOffset(self):
		"""Specifies additional Offset of the UDF in terms of bits. This Offset will start from where the Offset provided in Byte Offset field ends.

		Returns:
			number
		"""
		return self._get_attribute('bitOffset')
	@BitOffset.setter
	def BitOffset(self, value):
		self._set_attribute('bitOffset', value)

	@property
	def InnerLoopIncrementBy(self):
		"""Specifies the Step Value by which the Inner Loop will be incremented.

		Returns:
			number
		"""
		return self._get_attribute('innerLoopIncrementBy')
	@InnerLoopIncrementBy.setter
	def InnerLoopIncrementBy(self, value):
		self._set_attribute('innerLoopIncrementBy', value)

	@property
	def InnerLoopLoopCount(self):
		"""Specifies the no. of times the inner loop will occur.

		Returns:
			number
		"""
		return self._get_attribute('innerLoopLoopCount')
	@InnerLoopLoopCount.setter
	def InnerLoopLoopCount(self, value):
		self._set_attribute('innerLoopLoopCount', value)

	@property
	def InnerLoopRepeatValue(self):
		"""Specifies the number of times the UDF Value will be repeated in inner loop.

		Returns:
			number
		"""
		return self._get_attribute('innerLoopRepeatValue')
	@InnerLoopRepeatValue.setter
	def InnerLoopRepeatValue(self, value):
		self._set_attribute('innerLoopRepeatValue', value)

	@property
	def OuterLoopIncrementBy(self):
		"""Specifies the Step Value by which the outer loop will be incremented.

		Returns:
			number
		"""
		return self._get_attribute('outerLoopIncrementBy')
	@OuterLoopIncrementBy.setter
	def OuterLoopIncrementBy(self, value):
		self._set_attribute('outerLoopIncrementBy', value)

	@property
	def OuterLoopLoopCount(self):
		"""Specifies the number of times the outer loop will occur.

		Returns:
			number
		"""
		return self._get_attribute('outerLoopLoopCount')
	@OuterLoopLoopCount.setter
	def OuterLoopLoopCount(self, value):
		self._set_attribute('outerLoopLoopCount', value)

	@property
	def StartValue(self):
		"""Specifies the Start Value of the UDF.

		Returns:
			number
		"""
		return self._get_attribute('startValue')
	@StartValue.setter
	def StartValue(self, value):
		self._set_attribute('startValue', value)

	@property
	def Width(self):
		"""Specifies the width of the UDF.

		Returns:
			str(1|10|11|12|13|14|15|16|17|18|19|2|20|21|22|23|24|25|26|27|28|29|3|30|31|32|4|5|6|7|8|9)
		"""
		return self._get_attribute('width')
	@Width.setter
	def Width(self, value):
		self._set_attribute('width', value)

	def update(self, BitOffset=None, InnerLoopIncrementBy=None, InnerLoopLoopCount=None, InnerLoopRepeatValue=None, OuterLoopIncrementBy=None, OuterLoopLoopCount=None, StartValue=None, Width=None):
		"""Updates a child instance of nestedCounter on the server.

		Args:
			BitOffset (number): Specifies additional Offset of the UDF in terms of bits. This Offset will start from where the Offset provided in Byte Offset field ends.
			InnerLoopIncrementBy (number): Specifies the Step Value by which the Inner Loop will be incremented.
			InnerLoopLoopCount (number): Specifies the no. of times the inner loop will occur.
			InnerLoopRepeatValue (number): Specifies the number of times the UDF Value will be repeated in inner loop.
			OuterLoopIncrementBy (number): Specifies the Step Value by which the outer loop will be incremented.
			OuterLoopLoopCount (number): Specifies the number of times the outer loop will occur.
			StartValue (number): Specifies the Start Value of the UDF.
			Width (str(1|10|11|12|13|14|15|16|17|18|19|2|20|21|22|23|24|25|26|27|28|29|3|30|31|32|4|5|6|7|8|9)): Specifies the width of the UDF.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def find(self, AvailableWidths=None, BitOffset=None, InnerLoopIncrementBy=None, InnerLoopLoopCount=None, InnerLoopRepeatValue=None, OuterLoopIncrementBy=None, OuterLoopLoopCount=None, StartValue=None, Width=None):
		"""Finds and retrieves nestedCounter data from the server.

		All named parameters support regex and can be used to selectively retrieve nestedCounter data from the server.
		By default the find method takes no parameters and will retrieve all nestedCounter data from the server.

		Args:
			AvailableWidths (list(str)): Species all the possible widths available for a UDF in particular Type.
			BitOffset (number): Specifies additional Offset of the UDF in terms of bits. This Offset will start from where the Offset provided in Byte Offset field ends.
			InnerLoopIncrementBy (number): Specifies the Step Value by which the Inner Loop will be incremented.
			InnerLoopLoopCount (number): Specifies the no. of times the inner loop will occur.
			InnerLoopRepeatValue (number): Specifies the number of times the UDF Value will be repeated in inner loop.
			OuterLoopIncrementBy (number): Specifies the Step Value by which the outer loop will be incremented.
			OuterLoopLoopCount (number): Specifies the number of times the outer loop will occur.
			StartValue (number): Specifies the Start Value of the UDF.
			Width (str(1|10|11|12|13|14|15|16|17|18|19|2|20|21|22|23|24|25|26|27|28|29|3|30|31|32|4|5|6|7|8|9)): Specifies the width of the UDF.

		Returns:
			self: This instance with matching nestedCounter data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of nestedCounter data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the nestedCounter data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
