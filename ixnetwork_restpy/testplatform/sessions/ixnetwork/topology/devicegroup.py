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


class DeviceGroup(Base):
	"""Describes a set of network devices with similar configuration and the same multiplicity for devices behind.
	The DeviceGroup class encapsulates a list of deviceGroup resources that is be managed by the user.
	A list of resources can be retrieved from the server using the DeviceGroup.find() method.
	The list can be managed by the user by using the DeviceGroup.add() and DeviceGroup.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'deviceGroup'

	def __init__(self, parent):
		super(DeviceGroup, self).__init__(parent)

	@property
	def BfdRouter(self):
		"""An instance of the BfdRouter class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdrouter.BfdRouter)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdrouter import BfdRouter
		return BfdRouter(self)

	@property
	def BridgeData(self):
		"""An instance of the BridgeData class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bridgedata.BridgeData)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bridgedata import BridgeData
		return BridgeData(self)

	@property
	def DeviceGroup(self):
		"""An instance of the DeviceGroup class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.devicegroup.DeviceGroup)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.devicegroup import DeviceGroup
		return DeviceGroup(self)

	@property
	def Ethernet(self):
		"""An instance of the Ethernet class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ethernet.Ethernet)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ethernet import Ethernet
		return Ethernet(self)

	@property
	def Ipv4Loopback(self):
		"""An instance of the Ipv4Loopback class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4loopback.Ipv4Loopback)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4loopback import Ipv4Loopback
		return Ipv4Loopback(self)

	@property
	def Ipv6Loopback(self):
		"""An instance of the Ipv6Loopback class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6loopback.Ipv6Loopback)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6loopback import Ipv6Loopback
		return Ipv6Loopback(self)

	@property
	def IsisFabricPathRouter(self):
		"""An instance of the IsisFabricPathRouter class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisfabricpathrouter.IsisFabricPathRouter)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisfabricpathrouter import IsisFabricPathRouter
		return IsisFabricPathRouter(self)

	@property
	def IsisL3Router(self):
		"""An instance of the IsisL3Router class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3router.IsisL3Router)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3router import IsisL3Router
		return IsisL3Router(self)

	@property
	def IsisSpbRouter(self):
		"""An instance of the IsisSpbRouter class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbrouter.IsisSpbRouter)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbrouter import IsisSpbRouter
		return IsisSpbRouter(self)

	@property
	def IsisTrillRouter(self):
		"""An instance of the IsisTrillRouter class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillrouter.IsisTrillRouter)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillrouter import IsisTrillRouter
		return IsisTrillRouter(self)

	@property
	def LdpBasicRouter(self):
		"""An instance of the LdpBasicRouter class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouter.LdpBasicRouter)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouter import LdpBasicRouter
		return LdpBasicRouter(self)

	@property
	def LdpBasicRouterV6(self):
		"""An instance of the LdpBasicRouterV6 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouterv6.LdpBasicRouterV6)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouterv6 import LdpBasicRouterV6
		return LdpBasicRouterV6(self)

	@property
	def LdpLpbInterface(self):
		"""An instance of the LdpLpbInterface class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldplpbinterface.LdpLpbInterface)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldplpbinterface import LdpLpbInterface
		return LdpLpbInterface(self)

	@property
	def LdpTargetedRouter(self):
		"""An instance of the LdpTargetedRouter class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouter.LdpTargetedRouter)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouter import LdpTargetedRouter
		return LdpTargetedRouter(self)

	@property
	def LdpTargetedRouterV6(self):
		"""An instance of the LdpTargetedRouterV6 class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouterv6.LdpTargetedRouterV6)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouterv6 import LdpTargetedRouterV6
		return LdpTargetedRouterV6(self)

	@property
	def Ldpv6LoopbackInterface(self):
		"""An instance of the Ldpv6LoopbackInterface class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpv6loopbackinterface.Ldpv6LoopbackInterface)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpv6loopbackinterface import Ldpv6LoopbackInterface
		return Ldpv6LoopbackInterface(self)

	@property
	def MplsoamRouter(self):
		"""An instance of the MplsoamRouter class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplsoamrouter.MplsoamRouter)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplsoamrouter import MplsoamRouter
		return MplsoamRouter(self)

	@property
	def NetworkGroup(self):
		"""An instance of the NetworkGroup class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networkgroup.NetworkGroup)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networkgroup import NetworkGroup
		return NetworkGroup(self)

	@property
	def NetworkTopology(self):
		"""An instance of the NetworkTopology class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networktopology.NetworkTopology)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networktopology import NetworkTopology
		return NetworkTopology(self)

	@property
	def OfHostData(self):
		"""An instance of the OfHostData class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ofhostdata.OfHostData)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ofhostdata import OfHostData
		return OfHostData(self)

	@property
	def Ospfv2Router(self):
		"""An instance of the Ospfv2Router class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv2router.Ospfv2Router)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv2router import Ospfv2Router
		return Ospfv2Router(self)

	@property
	def Ospfv3Router(self):
		"""An instance of the Ospfv3Router class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3router.Ospfv3Router)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3router import Ospfv3Router
		return Ospfv3Router(self)

	@property
	def PimRouter(self):
		"""An instance of the PimRouter class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimrouter.PimRouter)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimrouter import PimRouter
		return PimRouter(self)

	@property
	def RouterData(self):
		"""An instance of the RouterData class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.routerdata.RouterData)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.routerdata import RouterData
		return RouterData(self)

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def Enabled(self):
		"""Enables/disables device.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enabled')

	@property
	def Errors(self):
		"""A list of errors that have occurred

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
		"""
		return self._get_attribute('errors')

	@property
	def Multiplier(self):
		"""Number of device instances per parent device instance (multiplier)

		Returns:
			number
		"""
		return self._get_attribute('multiplier')
	@Multiplier.setter
	def Multiplier(self, value):
		self._set_attribute('multiplier', value)

	@property
	def Name(self):
		"""Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	@property
	def Status(self):
		"""Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			str(configured|error|mixed|notStarted|started|starting|stopping)
		"""
		return self._get_attribute('status')

	def update(self, Multiplier=None, Name=None):
		"""Updates a child instance of deviceGroup on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			Multiplier (number): Number of device instances per parent device instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Multiplier=None, Name=None):
		"""Adds a new deviceGroup node on the server and retrieves it in this instance.

		Args:
			Multiplier (number): Number of device instances per parent device instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			self: This instance with all currently retrieved deviceGroup data using find and the newly added deviceGroup data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the deviceGroup data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Count=None, DescriptiveName=None, Errors=None, Multiplier=None, Name=None, Status=None):
		"""Finds and retrieves deviceGroup data from the server.

		All named parameters support regex and can be used to selectively retrieve deviceGroup data from the server.
		By default the find method takes no parameters and will retrieve all deviceGroup data from the server.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
			Errors (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))): A list of errors that have occurred
			Multiplier (number): Number of device instances per parent device instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			self: This instance with matching deviceGroup data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of deviceGroup data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the deviceGroup data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, Enabled=None):
		"""Base class infrastructure that gets a list of deviceGroup device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			Enabled (str): optional regex of enabled

		Returns:
			list(int): A list of device ids that meets the regex criteria provided in the method parameters

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._get_ngpf_device_ids(locals())

	def CopyPaste(self, *args, **kwargs):
		"""Executes the copyPaste operation on the server.

		Copy this node, paste it behind the destination node and return the newly copied node.

		copyPaste(Arg2:href)list
			Args:
				args[0] is Arg2 (str(None|/api/v1/sessions/1/ixnetwork/?deepchild=*)): The destination node below which the copied node will be pasted

			Returns:
				list(str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*]): The newly copied node.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('copyPaste', payload=payload, response_object=None)

	def FetchAndUpdateConfigFromCloud(self, *args, **kwargs):
		"""Executes the fetchAndUpdateConfigFromCloud operation on the server.

		fetchAndUpdateConfigFromCloud(Mode:string)
			Args:
				args[0] is Mode (str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('fetchAndUpdateConfigFromCloud', payload=payload, response_object=None)

	def RestartDown(self):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions in Device Group that are in 'Down' state.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		return self._execute('restartDown', payload=payload, response_object=None)

	def Start(self, *args, **kwargs):
		"""Executes the start operation on the server.

		Start selected Device Groups.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		start()

		start(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		start(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('start', payload=payload, response_object=None)

	def Stop(self, *args, **kwargs):
		"""Executes the stop operation on the server.

		Stop selected Device Groups.

		The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
		The following correlates the modeling Signatures to the python *args variable length list:

		stop()

		stop(SessionIndices:list)
			Args:
				args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		stop(SessionIndices:string)
			Args:
				args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('stop', payload=payload, response_object=None)
