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


class MacMulticast(Base):
	"""The DCE ISIS Learned Information option fetches the learned information for the Multicast MAC Range of a particular DCE ISIS router.
	The MacMulticast class encapsulates a list of macMulticast resources that is managed by the system.
	A list of resources can be retrieved from the server using the MacMulticast.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'macMulticast'

	def __init__(self, parent):
		super(MacMulticast, self).__init__(parent)

	@property
	def UnicastMacItem(self):
		"""An instance of the UnicastMacItem class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.unicastmacitem_vsdgljyxn0l3vuawnhc3rnywnjdgvt.UnicastMacItem)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.unicastmacitem_vsdgljyxn0l3vuawnhc3rnywnjdgvt import UnicastMacItem
		return UnicastMacItem(self)

	@property
	def Age(self):
		"""This indicates the age in time, in seconds, since it was last refreshed.

		Returns:
			number
		"""
		return self._get_attribute('age')

	@property
	def HostName(self):
		"""The host name as retrieved from the related packets.

		Returns:
			str
		"""
		return self._get_attribute('hostName')

	@property
	def LspId(self):
		"""This indicates the LSP identification number.

		Returns:
			str
		"""
		return self._get_attribute('lspId')

	@property
	def MulticastGroupMacAddress(self):
		"""This indicates the MAC Multicast Group Address in the Group Record.

		Returns:
			str
		"""
		return self._get_attribute('multicastGroupMacAddress')

	@property
	def SequenceNumber(self):
		"""This indicates the sequence number of the LSP containing the route.

		Returns:
			number
		"""
		return self._get_attribute('sequenceNumber')

	@property
	def VlanId(self):
		"""This indicates the VLAN ID in the Group Record.

		Returns:
			number
		"""
		return self._get_attribute('vlanId')

	def find(self, Age=None, HostName=None, LspId=None, MulticastGroupMacAddress=None, SequenceNumber=None, VlanId=None):
		"""Finds and retrieves macMulticast data from the server.

		All named parameters support regex and can be used to selectively retrieve macMulticast data from the server.
		By default the find method takes no parameters and will retrieve all macMulticast data from the server.

		Args:
			Age (number): This indicates the age in time, in seconds, since it was last refreshed.
			HostName (str): The host name as retrieved from the related packets.
			LspId (str): This indicates the LSP identification number.
			MulticastGroupMacAddress (str): This indicates the MAC Multicast Group Address in the Group Record.
			SequenceNumber (number): This indicates the sequence number of the LSP containing the route.
			VlanId (number): This indicates the VLAN ID in the Group Record.

		Returns:
			self: This instance with matching macMulticast data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of macMulticast data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the macMulticast data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
