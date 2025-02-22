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


class CustomTopologyNodeTopologyRange(Base):
	"""NOT DEFINED
	The CustomTopologyNodeTopologyRange class encapsulates a list of customTopologyNodeTopologyRange resources that is be managed by the user.
	A list of resources can be retrieved from the server using the CustomTopologyNodeTopologyRange.find() method.
	The list can be managed by the user by using the CustomTopologyNodeTopologyRange.add() and CustomTopologyNodeTopologyRange.remove() methods.
	"""

	__slots__ = ()
	_SDM_NAME = 'customTopologyNodeTopologyRange'

	def __init__(self, parent):
		super(CustomTopologyNodeTopologyRange, self).__init__(parent)

	@property
	def CustomTopologyInterestedVlanRange(self):
		"""An instance of the CustomTopologyInterestedVlanRange class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyinterestedvlanrange_b2d5sw50zxjlc3rlzfzsyw5syw5nzq.CustomTopologyInterestedVlanRange)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyinterestedvlanrange_b2d5sw50zxjlc3rlzfzsyw5syw5nzq import CustomTopologyInterestedVlanRange
		return CustomTopologyInterestedVlanRange(self)

	@property
	def NicknameCount(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('nicknameCount')
	@NicknameCount.setter
	def NicknameCount(self, value):
		self._set_attribute('nicknameCount', value)

	@property
	def NodeNicknameIncrement(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('nodeNicknameIncrement')
	@NodeNicknameIncrement.setter
	def NodeNicknameIncrement(self, value):
		self._set_attribute('nodeNicknameIncrement', value)

	@property
	def NumberOftreesToCompute(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('numberOftreesToCompute')
	@NumberOftreesToCompute.setter
	def NumberOftreesToCompute(self, value):
		self._set_attribute('numberOftreesToCompute', value)

	@property
	def StartNickname(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('startNickname')
	@StartNickname.setter
	def StartNickname(self, value):
		self._set_attribute('startNickname', value)

	def update(self, NicknameCount=None, NodeNicknameIncrement=None, NumberOftreesToCompute=None, StartNickname=None):
		"""Updates a child instance of customTopologyNodeTopologyRange on the server.

		Args:
			NicknameCount (number): NOT DEFINED
			NodeNicknameIncrement (number): NOT DEFINED
			NumberOftreesToCompute (number): NOT DEFINED
			StartNickname (number): NOT DEFINED

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, NicknameCount=None, NodeNicknameIncrement=None, NumberOftreesToCompute=None, StartNickname=None):
		"""Adds a new customTopologyNodeTopologyRange node on the server and retrieves it in this instance.

		Args:
			NicknameCount (number): NOT DEFINED
			NodeNicknameIncrement (number): NOT DEFINED
			NumberOftreesToCompute (number): NOT DEFINED
			StartNickname (number): NOT DEFINED

		Returns:
			self: This instance with all currently retrieved customTopologyNodeTopologyRange data using find and the newly added customTopologyNodeTopologyRange data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the customTopologyNodeTopologyRange data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, NicknameCount=None, NodeNicknameIncrement=None, NumberOftreesToCompute=None, StartNickname=None):
		"""Finds and retrieves customTopologyNodeTopologyRange data from the server.

		All named parameters support regex and can be used to selectively retrieve customTopologyNodeTopologyRange data from the server.
		By default the find method takes no parameters and will retrieve all customTopologyNodeTopologyRange data from the server.

		Args:
			NicknameCount (number): NOT DEFINED
			NodeNicknameIncrement (number): NOT DEFINED
			NumberOftreesToCompute (number): NOT DEFINED
			StartNickname (number): NOT DEFINED

		Returns:
			self: This instance with matching customTopologyNodeTopologyRange data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of customTopologyNodeTopologyRange data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the customTopologyNodeTopologyRange data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
