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


class TraceRouteLearnedInfo(Base):
	"""This object holds lists of the trace route learned information.
	The TraceRouteLearnedInfo class encapsulates a list of traceRouteLearnedInfo resources that is managed by the system.
	A list of resources can be retrieved from the server using the TraceRouteLearnedInfo.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'traceRouteLearnedInfo'

	def __init__(self, parent):
		super(TraceRouteLearnedInfo, self).__init__(parent)

	@property
	def Hops(self):
		"""An instance of the Hops class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.hops_zvjvdxrltgvhcm5lzeluzm8vag9wcw.Hops)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.hops_zvjvdxrltgvhcm5lzeluzm8vag9wcw import Hops
		return Hops(self)

	@property
	def IncomingLabelOuterInner(self):
		"""This signifies the incoming label information.

		Returns:
			str
		"""
		return self._get_attribute('incomingLabelOuterInner')

	@property
	def NumberOfReplyingHops(self):
		"""This signifies the total number of replying hops.

		Returns:
			number
		"""
		return self._get_attribute('numberOfReplyingHops')

	@property
	def OutgoingLabelOuterInner(self):
		"""This signifies the Outgoing Label information.

		Returns:
			str
		"""
		return self._get_attribute('outgoingLabelOuterInner')

	@property
	def Reachability(self):
		"""This specifies whether the queried MEP could be reached or not, Failure or, Partial or, Complete.

		Returns:
			str
		"""
		return self._get_attribute('reachability')

	@property
	def SenderHandle(self):
		"""This signifies the sender handle details.

		Returns:
			number
		"""
		return self._get_attribute('senderHandle')

	@property
	def Type(self):
		"""This signifies the type of path over which the traceroute is carried over, can be LSP, PW or Nested PW and LSP.

		Returns:
			str
		"""
		return self._get_attribute('type')

	def find(self, IncomingLabelOuterInner=None, NumberOfReplyingHops=None, OutgoingLabelOuterInner=None, Reachability=None, SenderHandle=None, Type=None):
		"""Finds and retrieves traceRouteLearnedInfo data from the server.

		All named parameters support regex and can be used to selectively retrieve traceRouteLearnedInfo data from the server.
		By default the find method takes no parameters and will retrieve all traceRouteLearnedInfo data from the server.

		Args:
			IncomingLabelOuterInner (str): This signifies the incoming label information.
			NumberOfReplyingHops (number): This signifies the total number of replying hops.
			OutgoingLabelOuterInner (str): This signifies the Outgoing Label information.
			Reachability (str): This specifies whether the queried MEP could be reached or not, Failure or, Partial or, Complete.
			SenderHandle (number): This signifies the sender handle details.
			Type (str): This signifies the type of path over which the traceroute is carried over, can be LSP, PW or Nested PW and LSP.

		Returns:
			self: This instance with matching traceRouteLearnedInfo data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of traceRouteLearnedInfo data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the traceRouteLearnedInfo data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
