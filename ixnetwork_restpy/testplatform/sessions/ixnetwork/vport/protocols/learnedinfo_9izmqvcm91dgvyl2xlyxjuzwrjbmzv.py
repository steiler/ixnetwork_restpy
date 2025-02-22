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


class LearnedInfo(Base):
	"""Views retrieved learned session information.
	The LearnedInfo class encapsulates a list of learnedInfo resources that is managed by the system.
	A list of resources can be retrieved from the server using the LearnedInfo.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'learnedInfo'

	def __init__(self, parent):
		super(LearnedInfo, self).__init__(parent)

	@property
	def DesMinTxInterval(self):
		"""This is the minimum interval, in microseconds, that the local system would like to use when transmitting BFD Control packets. The value zero is reserved.

		Returns:
			number
		"""
		return self._get_attribute('desMinTxInterval')

	@property
	def MyDisc(self):
		"""The discriminator for the session on this interface.

		Returns:
			number
		"""
		return self._get_attribute('myDisc')

	@property
	def MyIpAddress(self):
		"""The local IP address being used by the configured or auto-created BFD session.

		Returns:
			str
		"""
		return self._get_attribute('myIpAddress')

	@property
	def PeerDisc(self):
		"""The discriminator for the for side of the BFD session.

		Returns:
			number
		"""
		return self._get_attribute('peerDisc')

	@property
	def PeerFlags(self):
		"""The number of peer generated flags received.

		Returns:
			str
		"""
		return self._get_attribute('peerFlags')

	@property
	def PeerIpAddress(self):
		"""The IP address for the far side of the BFD session.

		Returns:
			str
		"""
		return self._get_attribute('peerIpAddress')

	@property
	def PeerState(self):
		"""The state of the far side of the BFD session, either active or not.

		Returns:
			str
		"""
		return self._get_attribute('peerState')

	@property
	def PeerUpTime(self):
		"""How long the peer has been active.

		Returns:
			number
		"""
		return self._get_attribute('peerUpTime')

	@property
	def ProtocolUsingSession(self):
		"""Which protocol is using the BFD session (for example, OSPF, BGP).

		Returns:
			str
		"""
		return self._get_attribute('protocolUsingSession')

	@property
	def ReqMinEchoInterval(self):
		"""This is the minimum interval, in microseconds, between received BFD Echo packets that this system is capable of supporting. If this value is zero, the transmitting system does not support the receipt of BFD Echo packets.

		Returns:
			number
		"""
		return self._get_attribute('reqMinEchoInterval')

	@property
	def ReqMinRxInterval(self):
		"""The minimum receive interval, in microseconds, for the far side of the BFD session.

		Returns:
			number
		"""
		return self._get_attribute('reqMinRxInterval')

	@property
	def SessionState(self):
		"""Whether the session is active or not.

		Returns:
			str
		"""
		return self._get_attribute('sessionState')

	@property
	def SessionType(self):
		"""The type of BFD session, either single or multiple hop.

		Returns:
			str
		"""
		return self._get_attribute('sessionType')

	def find(self, DesMinTxInterval=None, MyDisc=None, MyIpAddress=None, PeerDisc=None, PeerFlags=None, PeerIpAddress=None, PeerState=None, PeerUpTime=None, ProtocolUsingSession=None, ReqMinEchoInterval=None, ReqMinRxInterval=None, SessionState=None, SessionType=None):
		"""Finds and retrieves learnedInfo data from the server.

		All named parameters support regex and can be used to selectively retrieve learnedInfo data from the server.
		By default the find method takes no parameters and will retrieve all learnedInfo data from the server.

		Args:
			DesMinTxInterval (number): This is the minimum interval, in microseconds, that the local system would like to use when transmitting BFD Control packets. The value zero is reserved.
			MyDisc (number): The discriminator for the session on this interface.
			MyIpAddress (str): The local IP address being used by the configured or auto-created BFD session.
			PeerDisc (number): The discriminator for the for side of the BFD session.
			PeerFlags (str): The number of peer generated flags received.
			PeerIpAddress (str): The IP address for the far side of the BFD session.
			PeerState (str): The state of the far side of the BFD session, either active or not.
			PeerUpTime (number): How long the peer has been active.
			ProtocolUsingSession (str): Which protocol is using the BFD session (for example, OSPF, BGP).
			ReqMinEchoInterval (number): This is the minimum interval, in microseconds, between received BFD Echo packets that this system is capable of supporting. If this value is zero, the transmitting system does not support the receipt of BFD Echo packets.
			ReqMinRxInterval (number): The minimum receive interval, in microseconds, for the far side of the BFD session.
			SessionState (str): Whether the session is active or not.
			SessionType (str): The type of BFD session, either single or multiple hop.

		Returns:
			self: This instance with matching learnedInfo data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of learnedInfo data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the learnedInfo data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
