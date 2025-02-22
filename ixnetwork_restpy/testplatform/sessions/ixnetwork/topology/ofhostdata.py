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


class OfHostData(Base):
	"""Contains number of host ports per switch and number of hosts per host port
	The OfHostData class encapsulates a list of ofHostData resources that is be managed by the user.
	A list of resources can be retrieved from the server using the OfHostData.find() method.
	The list can be managed by the user by using the OfHostData.add() and OfHostData.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'ofHostData'

	def __init__(self, parent):
		super(OfHostData, self).__init__(parent)

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
	def NumberOfHostPorts(self):
		"""number of Host Ports per OF Switch.

		Returns:
			number
		"""
		return self._get_attribute('numberOfHostPorts')
	@NumberOfHostPorts.setter
	def NumberOfHostPorts(self, value):
		self._set_attribute('numberOfHostPorts', value)

	@property
	def NumberOfHostsPerPort(self):
		"""Number of Host Groups for each Host Port. Configure Number of Hosts Per Host Group using the Count field in Encapsulations Tab

		Returns:
			number
		"""
		return self._get_attribute('numberOfHostsPerPort')
	@NumberOfHostsPerPort.setter
	def NumberOfHostsPerPort(self, value):
		self._set_attribute('numberOfHostsPerPort', value)

	@property
	def ParentSwitchPortName(self):
		"""Description of the parent Switch Port.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('parentSwitchPortName')

	def update(self, Name=None, NumberOfHostPorts=None, NumberOfHostsPerPort=None):
		"""Updates a child instance of ofHostData on the server.

		This method has some named parameters with a type: obj (Multivalue).
		The Multivalue class has the associated documentation that details the possible values for those named parameters.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfHostPorts (number): number of Host Ports per OF Switch.
			NumberOfHostsPerPort (number): Number of Host Groups for each Host Port. Configure Number of Hosts Per Host Group using the Count field in Encapsulations Tab

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, Name=None, NumberOfHostPorts=None, NumberOfHostsPerPort=None):
		"""Adds a new ofHostData node on the server and retrieves it in this instance.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfHostPorts (number): number of Host Ports per OF Switch.
			NumberOfHostsPerPort (number): Number of Host Groups for each Host Port. Configure Number of Hosts Per Host Group using the Count field in Encapsulations Tab

		Returns:
			self: This instance with all currently retrieved ofHostData data using find and the newly added ofHostData data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the ofHostData data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, Count=None, DescriptiveName=None, Name=None, NumberOfHostPorts=None, NumberOfHostsPerPort=None):
		"""Finds and retrieves ofHostData data from the server.

		All named parameters support regex and can be used to selectively retrieve ofHostData data from the server.
		By default the find method takes no parameters and will retrieve all ofHostData data from the server.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfHostPorts (number): number of Host Ports per OF Switch.
			NumberOfHostsPerPort (number): Number of Host Groups for each Host Port. Configure Number of Hosts Per Host Group using the Count field in Encapsulations Tab

		Returns:
			self: This instance with matching ofHostData data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of ofHostData data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the ofHostData data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def get_device_ids(self, PortNames=None, ParentSwitchPortName=None):
		"""Base class infrastructure that gets a list of ofHostData device ids encapsulated by this object.

		Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

		Args:
			PortNames (str): optional regex of port names
			ParentSwitchPortName (str): optional regex of parentSwitchPortName

		Returns:
			list(int): A list of device ids that meets the regex criteria provided in the method parameters

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._get_ngpf_device_ids(locals())

	def SendPacketWithTraverseLI(self, *args, **kwargs):
		"""Executes the sendPacketWithTraverseLI operation on the server.

		Send an Host Packet (ARP/PING/CUSTOM) from the given device instance to the given destination instance.

		sendPacketWithTraverseLI(Arg2:list, Arg3:number, Arg4:enum, Arg5:number, Arg6:number, Arg7:bool, Arg8:number, Arg9:number)list
			Args:
				args[0] is Arg2 (list(number)): List of indices into the device group for the corresponding device instances whose IP addresses are used as the source of the request messages.
				args[1] is Arg3 (number): Destination Host index.
				args[2] is Arg4 (str(aRP|pING|custom)): Packet Type.
				args[3] is Arg5 (number): Encapsulation index.
				args[4] is Arg6 (number): Response Timeout.
				args[5] is Arg7 (bool): Periodic.
				args[6] is Arg8 (number): Periodic Interval.
				args[7] is Arg9 (number): Number of Iteration.

			Returns:
				list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('sendPacketWithTraverseLI', payload=payload, response_object=None)
