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


class L2Interface(Base):
	"""A single interface on a simulated router to be used in establishing Layer 2 VPNs.
	The L2Interface class encapsulates a list of l2Interface resources that is be managed by the user.
	A list of resources can be retrieved from the server using the L2Interface.find() method.
	The list can be managed by the user by using the L2Interface.add() and L2Interface.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'l2Interface'

	def __init__(self, parent):
		super(L2Interface, self).__init__(parent)

	@property
	def L2VcRange(self):
		"""An instance of the L2VcRange class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.l2vcrange_l2wysw50zxjmywnll2wyvmnsyw5nzq.L2VcRange)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.l2vcrange_l2wysw50zxjmywnll2wyvmnsyw5nzq import L2VcRange
		return L2VcRange(self)

	@property
	def Count(self):
		"""The number of contiguous values of groupId that will be used in generating FECs.

		Returns:
			number
		"""
		return self._get_attribute('count')
	@Count.setter
	def Count(self, value):
		self._set_attribute('count', value)

	@property
	def Enabled(self):
		"""Enables the use of this interface for the simulated router.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def GroupId(self):
		"""The group ID associated with all VC FEC elements of this interface.

		Returns:
			number
		"""
		return self._get_attribute('groupId')
	@GroupId.setter
	def GroupId(self, value):
		self._set_attribute('groupId', value)

	@property
	def TrafficGroupId(self):
		"""Contains the object reference to a traffic group identifier as configured with the trafficGroup object.

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficGroup)
		"""
		return self._get_attribute('trafficGroupId')
	@TrafficGroupId.setter
	def TrafficGroupId(self, value):
		self._set_attribute('trafficGroupId', value)

	@property
	def Type(self):
		"""The type of virtual circuit.

		Returns:
			str(frameRelay|atmaal5|atmxCell|vlan|ethernet|hdlc|ppp|cem|atmvcc|atmvpc|ip|satopE1|satopT1|satopE3|satopT3|cesoPsnBasic|cesoPsnCas|frameRelayRfc4619)
		"""
		return self._get_attribute('type')
	@Type.setter
	def Type(self, value):
		self._set_attribute('type', value)

	def update(self, Count=None, Enabled=None, GroupId=None, TrafficGroupId=None, Type=None):
		"""Updates a child instance of l2Interface on the server.

		Args:
			Count (number): The number of contiguous values of groupId that will be used in generating FECs.
			Enabled (bool): Enables the use of this interface for the simulated router.
			GroupId (number): The group ID associated with all VC FEC elements of this interface.
			TrafficGroupId (str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficGroup)): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.
			Type (str(frameRelay|atmaal5|atmxCell|vlan|ethernet|hdlc|ppp|cem|atmvcc|atmvpc|ip|satopE1|satopT1|satopE3|satopT3|cesoPsnBasic|cesoPsnCas|frameRelayRfc4619)): The type of virtual circuit.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Count=None, Enabled=None, GroupId=None, TrafficGroupId=None, Type=None):
		"""Adds a new l2Interface node on the server and retrieves it in this instance.

		Args:
			Count (number): The number of contiguous values of groupId that will be used in generating FECs.
			Enabled (bool): Enables the use of this interface for the simulated router.
			GroupId (number): The group ID associated with all VC FEC elements of this interface.
			TrafficGroupId (str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficGroup)): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.
			Type (str(frameRelay|atmaal5|atmxCell|vlan|ethernet|hdlc|ppp|cem|atmvcc|atmvpc|ip|satopE1|satopT1|satopE3|satopT3|cesoPsnBasic|cesoPsnCas|frameRelayRfc4619)): The type of virtual circuit.

		Returns:
			self: This instance with all currently retrieved l2Interface data using find and the newly added l2Interface data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the l2Interface data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Count=None, Enabled=None, GroupId=None, TrafficGroupId=None, Type=None):
		"""Finds and retrieves l2Interface data from the server.

		All named parameters support regex and can be used to selectively retrieve l2Interface data from the server.
		By default the find method takes no parameters and will retrieve all l2Interface data from the server.

		Args:
			Count (number): The number of contiguous values of groupId that will be used in generating FECs.
			Enabled (bool): Enables the use of this interface for the simulated router.
			GroupId (number): The group ID associated with all VC FEC elements of this interface.
			TrafficGroupId (str(None|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficGroup)): Contains the object reference to a traffic group identifier as configured with the trafficGroup object.
			Type (str(frameRelay|atmaal5|atmxCell|vlan|ethernet|hdlc|ppp|cem|atmvcc|atmvpc|ip|satopE1|satopT1|satopE3|satopT3|cesoPsnBasic|cesoPsnCas|frameRelayRfc4619)): The type of virtual circuit.

		Returns:
			self: This instance with matching l2Interface data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of l2Interface data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the l2Interface data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
