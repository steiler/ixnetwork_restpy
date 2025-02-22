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


class DceNodeMacGroups(Base):
	"""Sets the DCE Node MAC Groups for a particular DCE ISIS Network Range.
	The DceNodeMacGroups class encapsulates a list of dceNodeMacGroups resources that is be managed by the user.
	A list of resources can be retrieved from the server using the DceNodeMacGroups.find() method.
	The list can be managed by the user by using the DceNodeMacGroups.add() and DceNodeMacGroups.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'dceNodeMacGroups'

	def __init__(self, parent):
		super(DceNodeMacGroups, self).__init__(parent)

	@property
	def IncludeMacGroups(self):
		"""If true, includes MAC groups for this Network Range.

		Returns:
			bool
		"""
		return self._get_attribute('includeMacGroups')
	@IncludeMacGroups.setter
	def IncludeMacGroups(self, value):
		self._set_attribute('includeMacGroups', value)

	@property
	def InterGroupUnicastMacIncrement(self):
		"""The MAC address format of the Unicast MAC between one or more node groups.

		Returns:
			str
		"""
		return self._get_attribute('interGroupUnicastMacIncrement')
	@InterGroupUnicastMacIncrement.setter
	def InterGroupUnicastMacIncrement(self, value):
		self._set_attribute('interGroupUnicastMacIncrement', value)

	@property
	def IntraGroupUnicastMacIncrement(self):
		"""The MAC address format of the Unicast MAC within a node group.

		Returns:
			str
		"""
		return self._get_attribute('intraGroupUnicastMacIncrement')
	@IntraGroupUnicastMacIncrement.setter
	def IntraGroupUnicastMacIncrement(self, value):
		self._set_attribute('intraGroupUnicastMacIncrement', value)

	@property
	def MulticastAddressNodeStep(self):
		"""The Multicast MAC address that configures the increment across the Network Range simulated RBridges.

		Returns:
			str
		"""
		return self._get_attribute('multicastAddressNodeStep')
	@MulticastAddressNodeStep.setter
	def MulticastAddressNodeStep(self, value):
		self._set_attribute('multicastAddressNodeStep', value)

	@property
	def MulticastMacCount(self):
		"""The number of Multicast MAC addresses.

		Returns:
			number
		"""
		return self._get_attribute('multicastMacCount')
	@MulticastMacCount.setter
	def MulticastMacCount(self, value):
		self._set_attribute('multicastMacCount', value)

	@property
	def MulticastMacStep(self):
		"""The incremental value of Multicast MAC address.

		Returns:
			str
		"""
		return self._get_attribute('multicastMacStep')
	@MulticastMacStep.setter
	def MulticastMacStep(self, value):
		self._set_attribute('multicastMacStep', value)

	@property
	def NoOfUnicastScrMacsPerMulicastMac(self):
		"""The number of Unicast Source for each Multicast MAC address.

		Returns:
			number
		"""
		return self._get_attribute('noOfUnicastScrMacsPerMulicastMac')
	@NoOfUnicastScrMacsPerMulicastMac.setter
	def NoOfUnicastScrMacsPerMulicastMac(self, value):
		self._set_attribute('noOfUnicastScrMacsPerMulicastMac', value)

	@property
	def SourceGroupMapping(self):
		"""The Source Group mapping type.

		Returns:
			str(fullyMeshed|oneToOne|manualMapping)
		"""
		return self._get_attribute('sourceGroupMapping')
	@SourceGroupMapping.setter
	def SourceGroupMapping(self, value):
		self._set_attribute('sourceGroupMapping', value)

	@property
	def StartMulticastMac(self):
		"""The MAC address format of the starting Multicast MAC.

		Returns:
			str
		"""
		return self._get_attribute('startMulticastMac')
	@StartMulticastMac.setter
	def StartMulticastMac(self, value):
		self._set_attribute('startMulticastMac', value)

	@property
	def StartUnicastSourceMac(self):
		"""The MAC address format of the starting Unicast Source MAC.

		Returns:
			str
		"""
		return self._get_attribute('startUnicastSourceMac')
	@StartUnicastSourceMac.setter
	def StartUnicastSourceMac(self, value):
		self._set_attribute('startUnicastSourceMac', value)

	@property
	def UnicastAddressNodeStep(self):
		"""The Unicast MAC address that configures the increment across the Network Range simulated RBridges.

		Returns:
			str
		"""
		return self._get_attribute('unicastAddressNodeStep')
	@UnicastAddressNodeStep.setter
	def UnicastAddressNodeStep(self, value):
		self._set_attribute('unicastAddressNodeStep', value)

	@property
	def VlanId(self):
		"""The VLAN ID of the enabled Multicast MAC Range.

		Returns:
			number
		"""
		return self._get_attribute('vlanId')
	@VlanId.setter
	def VlanId(self, value):
		self._set_attribute('vlanId', value)

	def update(self, IncludeMacGroups=None, InterGroupUnicastMacIncrement=None, IntraGroupUnicastMacIncrement=None, MulticastAddressNodeStep=None, MulticastMacCount=None, MulticastMacStep=None, NoOfUnicastScrMacsPerMulicastMac=None, SourceGroupMapping=None, StartMulticastMac=None, StartUnicastSourceMac=None, UnicastAddressNodeStep=None, VlanId=None):
		"""Updates a child instance of dceNodeMacGroups on the server.

		Args:
			IncludeMacGroups (bool): If true, includes MAC groups for this Network Range.
			InterGroupUnicastMacIncrement (str): The MAC address format of the Unicast MAC between one or more node groups.
			IntraGroupUnicastMacIncrement (str): The MAC address format of the Unicast MAC within a node group.
			MulticastAddressNodeStep (str): The Multicast MAC address that configures the increment across the Network Range simulated RBridges.
			MulticastMacCount (number): The number of Multicast MAC addresses.
			MulticastMacStep (str): The incremental value of Multicast MAC address.
			NoOfUnicastScrMacsPerMulicastMac (number): The number of Unicast Source for each Multicast MAC address.
			SourceGroupMapping (str(fullyMeshed|oneToOne|manualMapping)): The Source Group mapping type.
			StartMulticastMac (str): The MAC address format of the starting Multicast MAC.
			StartUnicastSourceMac (str): The MAC address format of the starting Unicast Source MAC.
			UnicastAddressNodeStep (str): The Unicast MAC address that configures the increment across the Network Range simulated RBridges.
			VlanId (number): The VLAN ID of the enabled Multicast MAC Range.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, IncludeMacGroups=None, InterGroupUnicastMacIncrement=None, IntraGroupUnicastMacIncrement=None, MulticastAddressNodeStep=None, MulticastMacCount=None, MulticastMacStep=None, NoOfUnicastScrMacsPerMulicastMac=None, SourceGroupMapping=None, StartMulticastMac=None, StartUnicastSourceMac=None, UnicastAddressNodeStep=None, VlanId=None):
		"""Adds a new dceNodeMacGroups node on the server and retrieves it in this instance.

		Args:
			IncludeMacGroups (bool): If true, includes MAC groups for this Network Range.
			InterGroupUnicastMacIncrement (str): The MAC address format of the Unicast MAC between one or more node groups.
			IntraGroupUnicastMacIncrement (str): The MAC address format of the Unicast MAC within a node group.
			MulticastAddressNodeStep (str): The Multicast MAC address that configures the increment across the Network Range simulated RBridges.
			MulticastMacCount (number): The number of Multicast MAC addresses.
			MulticastMacStep (str): The incremental value of Multicast MAC address.
			NoOfUnicastScrMacsPerMulicastMac (number): The number of Unicast Source for each Multicast MAC address.
			SourceGroupMapping (str(fullyMeshed|oneToOne|manualMapping)): The Source Group mapping type.
			StartMulticastMac (str): The MAC address format of the starting Multicast MAC.
			StartUnicastSourceMac (str): The MAC address format of the starting Unicast Source MAC.
			UnicastAddressNodeStep (str): The Unicast MAC address that configures the increment across the Network Range simulated RBridges.
			VlanId (number): The VLAN ID of the enabled Multicast MAC Range.

		Returns:
			self: This instance with all currently retrieved dceNodeMacGroups data using find and the newly added dceNodeMacGroups data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the dceNodeMacGroups data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, IncludeMacGroups=None, InterGroupUnicastMacIncrement=None, IntraGroupUnicastMacIncrement=None, MulticastAddressNodeStep=None, MulticastMacCount=None, MulticastMacStep=None, NoOfUnicastScrMacsPerMulicastMac=None, SourceGroupMapping=None, StartMulticastMac=None, StartUnicastSourceMac=None, UnicastAddressNodeStep=None, VlanId=None):
		"""Finds and retrieves dceNodeMacGroups data from the server.

		All named parameters support regex and can be used to selectively retrieve dceNodeMacGroups data from the server.
		By default the find method takes no parameters and will retrieve all dceNodeMacGroups data from the server.

		Args:
			IncludeMacGroups (bool): If true, includes MAC groups for this Network Range.
			InterGroupUnicastMacIncrement (str): The MAC address format of the Unicast MAC between one or more node groups.
			IntraGroupUnicastMacIncrement (str): The MAC address format of the Unicast MAC within a node group.
			MulticastAddressNodeStep (str): The Multicast MAC address that configures the increment across the Network Range simulated RBridges.
			MulticastMacCount (number): The number of Multicast MAC addresses.
			MulticastMacStep (str): The incremental value of Multicast MAC address.
			NoOfUnicastScrMacsPerMulicastMac (number): The number of Unicast Source for each Multicast MAC address.
			SourceGroupMapping (str(fullyMeshed|oneToOne|manualMapping)): The Source Group mapping type.
			StartMulticastMac (str): The MAC address format of the starting Multicast MAC.
			StartUnicastSourceMac (str): The MAC address format of the starting Unicast Source MAC.
			UnicastAddressNodeStep (str): The Unicast MAC address that configures the increment across the Network Range simulated RBridges.
			VlanId (number): The VLAN ID of the enabled Multicast MAC Range.

		Returns:
			self: This instance with matching dceNodeMacGroups data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of dceNodeMacGroups data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the dceNodeMacGroups data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
