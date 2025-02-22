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


class Udf(Base):
	"""This object provides different options for UDF.
	The Udf class encapsulates a list of udf resources that is managed by the system.
	A list of resources can be retrieved from the server using the Udf.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'udf'

	def __init__(self, parent):
		super(Udf, self).__init__(parent)

	@property
	def Counter(self):
		"""An instance of the Counter class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.counter.counter.Counter)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.counter.counter import Counter
		return Counter(self)

	@property
	def Ipv4(self):
		"""An instance of the Ipv4 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.ipv4.ipv4.Ipv4)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.ipv4.ipv4 import Ipv4
		return Ipv4(self)

	@property
	def NestedCounter(self):
		"""An instance of the NestedCounter class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.nestedcounter.nestedcounter.NestedCounter)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.nestedcounter.nestedcounter import NestedCounter
		return NestedCounter(self)

	@property
	def Random(self):
		"""An instance of the Random class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.random.random.Random)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.random.random import Random
		return Random(self)

	@property
	def RangeList(self):
		"""An instance of the RangeList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.rangelist.rangelist.RangeList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.rangelist.rangelist import RangeList
		return RangeList(self)

	@property
	def ValueList(self):
		"""An instance of the ValueList class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.valuelist.valuelist.ValueList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.highlevelstream.udf.valuelist.valuelist import ValueList
		return ValueList(self)

	@property
	def ByteOffset(self):
		"""The offset from the start of the frame in bytes. Default is 0.

		Returns:
			number
		"""
		return self._get_attribute('byteOffset')
	@ByteOffset.setter
	def ByteOffset(self, value):
		self._set_attribute('byteOffset', value)

	@property
	def Chained(self):
		"""Sets the UDF chain.

		Returns:
			bool
		"""
		return self._get_attribute('chained')

	@property
	def ChainedFromUdf(self):
		"""Allows to set what UDF the current UDF should chain from. If enabled, the UDF stays in its initial value until the UDF it is chained from reaches its terminating value.

		Returns:
			str(none|udf1|udf2|udf3|udf4|udf5)
		"""
		return self._get_attribute('chainedFromUdf')
	@ChainedFromUdf.setter
	def ChainedFromUdf(self, value):
		self._set_attribute('chainedFromUdf', value)

	@property
	def Enabled(self):
		"""If enabled, enables this User Defined Field.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def Type(self):
		"""The counter types of this UDF.

		Returns:
			str(counter|ipv4|nestedCounter|random|rangeList|valueList)
		"""
		return self._get_attribute('type')
	@Type.setter
	def Type(self, value):
		self._set_attribute('type', value)

	def update(self, ByteOffset=None, ChainedFromUdf=None, Enabled=None, Type=None):
		"""Updates a child instance of udf on the server.

		Args:
			ByteOffset (number): The offset from the start of the frame in bytes. Default is 0.
			ChainedFromUdf (str(none|udf1|udf2|udf3|udf4|udf5)): Allows to set what UDF the current UDF should chain from. If enabled, the UDF stays in its initial value until the UDF it is chained from reaches its terminating value.
			Enabled (bool): If enabled, enables this User Defined Field.
			Type (str(counter|ipv4|nestedCounter|random|rangeList|valueList)): The counter types of this UDF.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def find(self, ByteOffset=None, Chained=None, ChainedFromUdf=None, Enabled=None, Type=None):
		"""Finds and retrieves udf data from the server.

		All named parameters support regex and can be used to selectively retrieve udf data from the server.
		By default the find method takes no parameters and will retrieve all udf data from the server.

		Args:
			ByteOffset (number): The offset from the start of the frame in bytes. Default is 0.
			Chained (bool): Sets the UDF chain.
			ChainedFromUdf (str(none|udf1|udf2|udf3|udf4|udf5)): Allows to set what UDF the current UDF should chain from. If enabled, the UDF stays in its initial value until the UDF it is chained from reaches its terminating value.
			Enabled (bool): If enabled, enables this User Defined Field.
			Type (str(counter|ipv4|nestedCounter|random|rangeList|valueList)): The counter types of this UDF.

		Returns:
			self: This instance with matching udf data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of udf data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the udf data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
