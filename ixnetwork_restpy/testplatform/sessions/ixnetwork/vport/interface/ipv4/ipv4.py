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


class Ipv4(Base):
	"""Controls the general IPv4 interface properties.
	The Ipv4 class encapsulates a list of ipv4 resources that is be managed by the user.
	A list of resources can be retrieved from the server using the Ipv4.find() method.
	The list can be managed by the user by using the Ipv4.add() and Ipv4.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'ipv4'

	def __init__(self, parent):
		super(Ipv4, self).__init__(parent)

	@property
	def Gateway(self):
		"""The IPv4 address of the Gateway to the network, typically an interface on the DUT.

		Returns:
			str
		"""
		return self._get_attribute('gateway')
	@Gateway.setter
	def Gateway(self, value):
		self._set_attribute('gateway', value)

	@property
	def Ip(self):
		"""The 32-bit IPv4 address assigned to this unconnected interface.

		Returns:
			str
		"""
		return self._get_attribute('ip')
	@Ip.setter
	def Ip(self, value):
		self._set_attribute('ip', value)

	@property
	def MaskWidth(self):
		"""The number of bits in the mask used with the IPv4 address. The default is 24 bits.

		Returns:
			number
		"""
		return self._get_attribute('maskWidth')
	@MaskWidth.setter
	def MaskWidth(self, value):
		self._set_attribute('maskWidth', value)

	def update(self, Gateway=None, Ip=None, MaskWidth=None):
		"""Updates a child instance of ipv4 on the server.

		Args:
			Gateway (str): The IPv4 address of the Gateway to the network, typically an interface on the DUT.
			Ip (str): The 32-bit IPv4 address assigned to this unconnected interface.
			MaskWidth (number): The number of bits in the mask used with the IPv4 address. The default is 24 bits.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Gateway=None, Ip=None, MaskWidth=None):
		"""Adds a new ipv4 node on the server and retrieves it in this instance.

		Args:
			Gateway (str): The IPv4 address of the Gateway to the network, typically an interface on the DUT.
			Ip (str): The 32-bit IPv4 address assigned to this unconnected interface.
			MaskWidth (number): The number of bits in the mask used with the IPv4 address. The default is 24 bits.

		Returns:
			self: This instance with all currently retrieved ipv4 data using find and the newly added ipv4 data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the ipv4 data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Gateway=None, Ip=None, MaskWidth=None):
		"""Finds and retrieves ipv4 data from the server.

		All named parameters support regex and can be used to selectively retrieve ipv4 data from the server.
		By default the find method takes no parameters and will retrieve all ipv4 data from the server.

		Args:
			Gateway (str): The IPv4 address of the Gateway to the network, typically an interface on the DUT.
			Ip (str): The 32-bit IPv4 address assigned to this unconnected interface.
			MaskWidth (number): The number of bits in the mask used with the IPv4 address. The default is 24 bits.

		Returns:
			self: This instance with matching ipv4 data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of ipv4 data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the ipv4 data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
