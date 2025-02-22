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


class Link(Base):
	"""List of impairment links.  Each link consists of a pair of ports.
	The Link class encapsulates a list of link resources that is managed by the system.
	A list of resources can be retrieved from the server using the Link.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'link'

	def __init__(self, parent):
		super(Link, self).__init__(parent)

	@property
	def LosLof(self):
		"""An instance of the LosLof class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.link.loslof.loslof.LosLof)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.link.loslof.loslof import LosLof
		return LosLof(self)._select()

	@property
	def ForwardingInterruption(self):
		"""Emulate a link fault. Drop all packets received.

		Returns:
			bool
		"""
		return self._get_attribute('forwardingInterruption')
	@ForwardingInterruption.setter
	def ForwardingInterruption(self, value):
		self._set_attribute('forwardingInterruption', value)

	@property
	def Name(self):
		"""The name of the link: receiving port -> transmitting port.

		Returns:
			str
		"""
		return self._get_attribute('name')

	@property
	def RxPortName(self):
		"""The name of the receiving port.

		Returns:
			str
		"""
		return self._get_attribute('rxPortName')

	@property
	def TxPortName(self):
		"""The name of the transmitting port.

		Returns:
			str
		"""
		return self._get_attribute('txPortName')

	def update(self, ForwardingInterruption=None):
		"""Updates a child instance of link on the server.

		Args:
			ForwardingInterruption (bool): Emulate a link fault. Drop all packets received.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def find(self, ForwardingInterruption=None, Name=None, RxPortName=None, TxPortName=None):
		"""Finds and retrieves link data from the server.

		All named parameters support regex and can be used to selectively retrieve link data from the server.
		By default the find method takes no parameters and will retrieve all link data from the server.

		Args:
			ForwardingInterruption (bool): Emulate a link fault. Drop all packets received.
			Name (str): The name of the link: receiving port -> transmitting port.
			RxPortName (str): The name of the receiving port.
			TxPortName (str): The name of the transmitting port.

		Returns:
			self: This instance with matching link data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of link data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the link data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
