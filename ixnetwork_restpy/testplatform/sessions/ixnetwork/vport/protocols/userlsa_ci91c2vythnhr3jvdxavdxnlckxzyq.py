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


class UserLsa(Base):
	"""
	The UserLsa class encapsulates a list of userLsa resources that is be managed by the user.
	A list of resources can be retrieved from the server using the UserLsa.find() method.
	The list can be managed by the user by using the UserLsa.add() and UserLsa.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'userLsa'

	def __init__(self, parent):
		super(UserLsa, self).__init__(parent)

	@property
	def External(self):
		"""An instance of the External class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.external_r3jvdxavdxnlckxzys9lehrlcm5hba.External)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.external_r3jvdxavdxnlckxzys9lehrlcm5hba import External
		return External(self)

	@property
	def Network(self):
		"""An instance of the Network class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.network_nhr3jvdxavdxnlckxzys9uzxr3b3jr.Network)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.network_nhr3jvdxavdxnlckxzys9uzxr3b3jr import Network
		return Network(self)

	@property
	def Nssa(self):
		"""An instance of the Nssa class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nssa_vythnhr3jvdxavdxnlckxzys9uc3nh.Nssa)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.nssa_vythnhr3jvdxavdxnlckxzys9uc3nh import Nssa
		return Nssa(self)

	@property
	def Opaque(self):
		"""An instance of the Opaque class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaque_hnhr3jvdxavdxnlckxzys9vcgfxdwu.Opaque)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaque_hnhr3jvdxavdxnlckxzys9vcgfxdwu import Opaque
		return Opaque(self)

	@property
	def Router(self):
		"""An instance of the Router class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_hnhr3jvdxavdxnlckxzys9yb3v0zxi.Router)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.router_hnhr3jvdxavdxnlckxzys9yb3v0zxi import Router
		return Router(self)

	@property
	def SummaryIp(self):
		"""An instance of the SummaryIp class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.summaryip_3jvdxavdxnlckxzys9zdw1tyxj5sxa.SummaryIp)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.summaryip_3jvdxavdxnlckxzys9zdw1tyxj5sxa import SummaryIp
		return SummaryIp(self)

	@property
	def AdvertisingRouterId(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('advertisingRouterId')
	@AdvertisingRouterId.setter
	def AdvertisingRouterId(self, value):
		self._set_attribute('advertisingRouterId', value)

	@property
	def Enabled(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def ExpandIntoLinksOrAttachedRouters(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('expandIntoLinksOrAttachedRouters')
	@ExpandIntoLinksOrAttachedRouters.setter
	def ExpandIntoLinksOrAttachedRouters(self, value):
		self._set_attribute('expandIntoLinksOrAttachedRouters', value)

	@property
	def LinkStateId(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('linkStateId')
	@LinkStateId.setter
	def LinkStateId(self, value):
		self._set_attribute('linkStateId', value)

	@property
	def LsaType(self):
		"""

		Returns:
			str(router|network|areaSummary|externalSummary|external|nssa|opaqueLocalScope|opaqueAreaScope|opaqueAsScope)
		"""
		return self._get_attribute('lsaType')
	@LsaType.setter
	def LsaType(self, value):
		self._set_attribute('lsaType', value)

	@property
	def OptBitDemandCircuit(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('optBitDemandCircuit')
	@OptBitDemandCircuit.setter
	def OptBitDemandCircuit(self, value):
		self._set_attribute('optBitDemandCircuit', value)

	@property
	def OptBitExternalAttributes(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('optBitExternalAttributes')
	@OptBitExternalAttributes.setter
	def OptBitExternalAttributes(self, value):
		self._set_attribute('optBitExternalAttributes', value)

	@property
	def OptBitExternalRouting(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('optBitExternalRouting')
	@OptBitExternalRouting.setter
	def OptBitExternalRouting(self, value):
		self._set_attribute('optBitExternalRouting', value)

	@property
	def OptBitLsaNoForward(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('optBitLsaNoForward')
	@OptBitLsaNoForward.setter
	def OptBitLsaNoForward(self, value):
		self._set_attribute('optBitLsaNoForward', value)

	@property
	def OptBitMulticast(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('optBitMulticast')
	@OptBitMulticast.setter
	def OptBitMulticast(self, value):
		self._set_attribute('optBitMulticast', value)

	@property
	def OptBitNssaCapability(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('optBitNssaCapability')
	@OptBitNssaCapability.setter
	def OptBitNssaCapability(self, value):
		self._set_attribute('optBitNssaCapability', value)

	@property
	def OptBitTypeOfService(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('optBitTypeOfService')
	@OptBitTypeOfService.setter
	def OptBitTypeOfService(self, value):
		self._set_attribute('optBitTypeOfService', value)

	@property
	def Option(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('option')
	@Option.setter
	def Option(self, value):
		self._set_attribute('option', value)

	def update(self, AdvertisingRouterId=None, Enabled=None, ExpandIntoLinksOrAttachedRouters=None, LinkStateId=None, LsaType=None, OptBitDemandCircuit=None, OptBitExternalAttributes=None, OptBitExternalRouting=None, OptBitLsaNoForward=None, OptBitMulticast=None, OptBitNssaCapability=None, OptBitTypeOfService=None, Option=None):
		"""Updates a child instance of userLsa on the server.

		Args:
			AdvertisingRouterId (str): 
			Enabled (bool): 
			ExpandIntoLinksOrAttachedRouters (bool): 
			LinkStateId (str): 
			LsaType (str(router|network|areaSummary|externalSummary|external|nssa|opaqueLocalScope|opaqueAreaScope|opaqueAsScope)): 
			OptBitDemandCircuit (bool): 
			OptBitExternalAttributes (bool): 
			OptBitExternalRouting (bool): 
			OptBitLsaNoForward (bool): 
			OptBitMulticast (bool): 
			OptBitNssaCapability (bool): 
			OptBitTypeOfService (bool): 
			Option (number): 

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, AdvertisingRouterId=None, Enabled=None, ExpandIntoLinksOrAttachedRouters=None, LinkStateId=None, LsaType=None, OptBitDemandCircuit=None, OptBitExternalAttributes=None, OptBitExternalRouting=None, OptBitLsaNoForward=None, OptBitMulticast=None, OptBitNssaCapability=None, OptBitTypeOfService=None, Option=None):
		"""Adds a new userLsa node on the server and retrieves it in this instance.

		Args:
			AdvertisingRouterId (str): 
			Enabled (bool): 
			ExpandIntoLinksOrAttachedRouters (bool): 
			LinkStateId (str): 
			LsaType (str(router|network|areaSummary|externalSummary|external|nssa|opaqueLocalScope|opaqueAreaScope|opaqueAsScope)): 
			OptBitDemandCircuit (bool): 
			OptBitExternalAttributes (bool): 
			OptBitExternalRouting (bool): 
			OptBitLsaNoForward (bool): 
			OptBitMulticast (bool): 
			OptBitNssaCapability (bool): 
			OptBitTypeOfService (bool): 
			Option (number): 

		Returns:
			self: This instance with all currently retrieved userLsa data using find and the newly added userLsa data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the userLsa data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, AdvertisingRouterId=None, Enabled=None, ExpandIntoLinksOrAttachedRouters=None, LinkStateId=None, LsaType=None, OptBitDemandCircuit=None, OptBitExternalAttributes=None, OptBitExternalRouting=None, OptBitLsaNoForward=None, OptBitMulticast=None, OptBitNssaCapability=None, OptBitTypeOfService=None, Option=None):
		"""Finds and retrieves userLsa data from the server.

		All named parameters support regex and can be used to selectively retrieve userLsa data from the server.
		By default the find method takes no parameters and will retrieve all userLsa data from the server.

		Args:
			AdvertisingRouterId (str): 
			Enabled (bool): 
			ExpandIntoLinksOrAttachedRouters (bool): 
			LinkStateId (str): 
			LsaType (str(router|network|areaSummary|externalSummary|external|nssa|opaqueLocalScope|opaqueAreaScope|opaqueAsScope)): 
			OptBitDemandCircuit (bool): 
			OptBitExternalAttributes (bool): 
			OptBitExternalRouting (bool): 
			OptBitLsaNoForward (bool): 
			OptBitMulticast (bool): 
			OptBitNssaCapability (bool): 
			OptBitTypeOfService (bool): 
			Option (number): 

		Returns:
			self: This instance with matching userLsa data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of userLsa data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the userLsa data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
