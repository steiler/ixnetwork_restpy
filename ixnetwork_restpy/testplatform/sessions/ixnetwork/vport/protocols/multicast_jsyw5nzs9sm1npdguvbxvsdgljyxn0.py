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


class Multicast(Base):
	"""This object configures the multicast attributes for the L3 Site route ranges.
	The Multicast class encapsulates a required multicast resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'multicast'

	def __init__(self, parent):
		super(Multicast, self).__init__(parent)

	@property
	def Cluster(self):
		"""An instance of the Cluster class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cluster_1npdguvbxvsdgljyxn0l2nsdxn0zxi.Cluster)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cluster_1npdguvbxvsdgljyxn0l2nsdxn0zxi import Cluster
		return Cluster(self)._select()

	@property
	def RouteDistinguisher(self):
		"""An instance of the RouteDistinguisher class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routedistinguisher_yxn0l3jvdxrlrglzdgluz3vpc2hlcg.RouteDistinguisher)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.routedistinguisher_yxn0l3jvdxrlrglzdgluz3vpc2hlcg import RouteDistinguisher
		return RouteDistinguisher(self)._select()

	@property
	def EnableMulticast(self):
		"""Enables the use of Multicast VRFs (MVRFs). (default = false)

		Returns:
			bool
		"""
		return self._get_attribute('enableMulticast')
	@EnableMulticast.setter
	def EnableMulticast(self, value):
		self._set_attribute('enableMulticast', value)

	@property
	def EnableMulticastCluster(self):
		"""If true, enables the use of BGP route reflection clusters for multicast VPN route distribution. (default = false)

		Returns:
			bool
		"""
		return self._get_attribute('enableMulticastCluster')
	@EnableMulticastCluster.setter
	def EnableMulticastCluster(self, value):
		self._set_attribute('enableMulticastCluster', value)

	@property
	def GroupAddress(self):
		"""The IP address for the Multicast Group. The default value is the default MDT group address, used as the Multicast Group address used as the destination for the MVPN tunnel. (default = 239.1.1.1

		Returns:
			str
		"""
		return self._get_attribute('groupAddress')
	@GroupAddress.setter
	def GroupAddress(self, value):
		self._set_attribute('groupAddress', value)

	def update(self, EnableMulticast=None, EnableMulticastCluster=None, GroupAddress=None):
		"""Updates a child instance of multicast on the server.

		Args:
			EnableMulticast (bool): Enables the use of Multicast VRFs (MVRFs). (default = false)
			EnableMulticastCluster (bool): If true, enables the use of BGP route reflection clusters for multicast VPN route distribution. (default = false)
			GroupAddress (str): The IP address for the Multicast Group. The default value is the default MDT group address, used as the Multicast Group address used as the destination for the MVPN tunnel. (default = 239.1.1.1

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
