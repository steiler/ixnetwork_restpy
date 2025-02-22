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


class Lisp(Base):
	"""Details about the list processing are provided here
	The Lisp class encapsulates a required lisp resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'lisp'

	def __init__(self, parent):
		super(Lisp, self).__init__(parent)

	@property
	def Router(self):
		"""An instance of the Router class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_l3byb3rvy29scy9saxnwl3jvdxrlcg.Router)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_l3byb3rvy29scy9saxnwl3jvdxrlcg import Router
		return Router(self)

	@property
	def SiteEidRange(self):
		"""An instance of the SiteEidRange class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.siteeidrange_y29scy9saxnwl3npdgvfawrsyw5nzq.SiteEidRange)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.siteeidrange_y29scy9saxnwl3npdgvfawrsyw5nzq import SiteEidRange
		return SiteEidRange(self)

	@property
	def BurstIntervalInMs(self):
		"""It shows the details abou the burst interval in micro seconds

		Returns:
			number
		"""
		return self._get_attribute('burstIntervalInMs')
	@BurstIntervalInMs.setter
	def BurstIntervalInMs(self, value):
		self._set_attribute('burstIntervalInMs', value)

	@property
	def Enabled(self):
		"""If true, it shows enabled.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def Ipv4MapRegisterPacketsPerBurst(self):
		"""It gives details about the ip v4 map register packets per burst

		Returns:
			number
		"""
		return self._get_attribute('ipv4MapRegisterPacketsPerBurst')
	@Ipv4MapRegisterPacketsPerBurst.setter
	def Ipv4MapRegisterPacketsPerBurst(self, value):
		self._set_attribute('ipv4MapRegisterPacketsPerBurst', value)

	@property
	def Ipv4MapRequestPacketsPerBurst(self):
		"""It gives details about the ip v4 map requests packets per burst

		Returns:
			number
		"""
		return self._get_attribute('ipv4MapRequestPacketsPerBurst')
	@Ipv4MapRequestPacketsPerBurst.setter
	def Ipv4MapRequestPacketsPerBurst(self, value):
		self._set_attribute('ipv4MapRequestPacketsPerBurst', value)

	@property
	def Ipv4SmrPacketsPerBurst(self):
		"""It gives details about the Ip v4 Smr packets per bursts

		Returns:
			number
		"""
		return self._get_attribute('ipv4SmrPacketsPerBurst')
	@Ipv4SmrPacketsPerBurst.setter
	def Ipv4SmrPacketsPerBurst(self, value):
		self._set_attribute('ipv4SmrPacketsPerBurst', value)

	@property
	def Ipv6MapRegisterPacketsPerBurst(self):
		"""It gives details about the ip v6 map register packets per burst

		Returns:
			number
		"""
		return self._get_attribute('ipv6MapRegisterPacketsPerBurst')
	@Ipv6MapRegisterPacketsPerBurst.setter
	def Ipv6MapRegisterPacketsPerBurst(self, value):
		self._set_attribute('ipv6MapRegisterPacketsPerBurst', value)

	@property
	def Ipv6MapRequestPacketsPerBurst(self):
		"""It gives details about the ip v6 map requests packets per burst

		Returns:
			number
		"""
		return self._get_attribute('ipv6MapRequestPacketsPerBurst')
	@Ipv6MapRequestPacketsPerBurst.setter
	def Ipv6MapRequestPacketsPerBurst(self, value):
		self._set_attribute('ipv6MapRequestPacketsPerBurst', value)

	@property
	def Ipv6SmrPacketsPerBurst(self):
		"""It gives details about the Ip v6 Smr packets per bursts

		Returns:
			number
		"""
		return self._get_attribute('ipv6SmrPacketsPerBurst')
	@Ipv6SmrPacketsPerBurst.setter
	def Ipv6SmrPacketsPerBurst(self, value):
		self._set_attribute('ipv6SmrPacketsPerBurst', value)

	@property
	def ProtocolState(self):
		"""Shows different protocol states (read-only)

		Returns:
			str(stopped|unknown|stopping|started|starting)
		"""
		return self._get_attribute('protocolState')

	def update(self, BurstIntervalInMs=None, Enabled=None, Ipv4MapRegisterPacketsPerBurst=None, Ipv4MapRequestPacketsPerBurst=None, Ipv4SmrPacketsPerBurst=None, Ipv6MapRegisterPacketsPerBurst=None, Ipv6MapRequestPacketsPerBurst=None, Ipv6SmrPacketsPerBurst=None):
		"""Updates a child instance of lisp on the server.

		Args:
			BurstIntervalInMs (number): It shows the details abou the burst interval in micro seconds
			Enabled (bool): If true, it shows enabled.
			Ipv4MapRegisterPacketsPerBurst (number): It gives details about the ip v4 map register packets per burst
			Ipv4MapRequestPacketsPerBurst (number): It gives details about the ip v4 map requests packets per burst
			Ipv4SmrPacketsPerBurst (number): It gives details about the Ip v4 Smr packets per bursts
			Ipv6MapRegisterPacketsPerBurst (number): It gives details about the ip v6 map register packets per burst
			Ipv6MapRequestPacketsPerBurst (number): It gives details about the ip v6 map requests packets per burst
			Ipv6SmrPacketsPerBurst (number): It gives details about the Ip v6 Smr packets per bursts

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def Start(self):
		"""Executes the start operation on the server.

		NOT DEFINED

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('start', payload=payload, response_object=None)

	def Stop(self):
		"""Executes the stop operation on the server.

		NOT DEFINED

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		return self._execute('stop', payload=payload, response_object=None)
