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


class EgtpNbS5S8Range(Base):
	"""eNodeB Range
	The EgtpNbS5S8Range class encapsulates a required egtpNbS5S8Range resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'egtpNbS5S8Range'

	def __init__(self, parent):
		super(EgtpNbS5S8Range, self).__init__(parent)

	@property
	def ECI(self):
		"""EUTRAN Cell Identifier

		Returns:
			str
		"""
		return self._get_attribute('eCI')
	@ECI.setter
	def ECI(self, value):
		self._set_attribute('eCI', value)

	@property
	def Enabled(self):
		"""Disabled ranges won't be configured nor validated.

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def MCC(self):
		"""Mobile Country Code

		Returns:
			str
		"""
		return self._get_attribute('mCC')
	@MCC.setter
	def MCC(self, value):
		self._set_attribute('mCC', value)

	@property
	def MNC(self):
		"""Mobile Network Code

		Returns:
			str
		"""
		return self._get_attribute('mNC')
	@MNC.setter
	def MNC(self, value):
		self._set_attribute('mNC', value)

	@property
	def Name(self):
		"""Name of range

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	@property
	def ObjectId(self):
		"""Unique identifier for this object

		Returns:
			str
		"""
		return self._get_attribute('objectId')

	@property
	def ParentMme(self):
		"""Id of parent MME range

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=mmeS5S8SecondaryRange)
		"""
		return self._get_attribute('parentMme')
	@ParentMme.setter
	def ParentMme(self, value):
		self._set_attribute('parentMme', value)

	@property
	def ParentSgw(self):
		"""Id of parent SGW range

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=range)
		"""
		return self._get_attribute('parentSgw')
	@ParentSgw.setter
	def ParentSgw(self, value):
		self._set_attribute('parentSgw', value)

	@property
	def RAILAC(self):
		"""LAC for UEs (Hexa value)

		Returns:
			str
		"""
		return self._get_attribute('rAILAC')
	@RAILAC.setter
	def RAILAC(self, value):
		self._set_attribute('rAILAC', value)

	@property
	def RAIMCC1(self):
		"""First digit of MCC location for UEs

		Returns:
			number
		"""
		return self._get_attribute('rAIMCC1')
	@RAIMCC1.setter
	def RAIMCC1(self, value):
		self._set_attribute('rAIMCC1', value)

	@property
	def RAIMCC2(self):
		"""Second digit of MCC location for UEs

		Returns:
			number
		"""
		return self._get_attribute('rAIMCC2')
	@RAIMCC2.setter
	def RAIMCC2(self, value):
		self._set_attribute('rAIMCC2', value)

	@property
	def RAIMCC3(self):
		"""3rd digit of MCC location for UEs

		Returns:
			number
		"""
		return self._get_attribute('rAIMCC3')
	@RAIMCC3.setter
	def RAIMCC3(self, value):
		self._set_attribute('rAIMCC3', value)

	@property
	def RAIMNC1(self):
		"""first digit of MNC location for UEs

		Returns:
			number
		"""
		return self._get_attribute('rAIMNC1')
	@RAIMNC1.setter
	def RAIMNC1(self, value):
		self._set_attribute('rAIMNC1', value)

	@property
	def RAIMNC2(self):
		"""Second digit of MNC location for UEs

		Returns:
			number
		"""
		return self._get_attribute('rAIMNC2')
	@RAIMNC2.setter
	def RAIMNC2(self, value):
		self._set_attribute('rAIMNC2', value)

	@property
	def RAIMNC3(self):
		"""Third digit of MNC location for UEs

		Returns:
			number
		"""
		return self._get_attribute('rAIMNC3')
	@RAIMNC3.setter
	def RAIMNC3(self, value):
		self._set_attribute('rAIMNC3', value)

	@property
	def RAIRAC(self):
		"""RAC for UEs (Hexa value)

		Returns:
			str
		"""
		return self._get_attribute('rAIRAC')
	@RAIRAC.setter
	def RAIRAC(self, value):
		self._set_attribute('rAIRAC', value)

	@property
	def TAC(self):
		"""Tracking Area Code

		Returns:
			str
		"""
		return self._get_attribute('tAC')
	@TAC.setter
	def TAC(self, value):
		self._set_attribute('tAC', value)

	def update(self, ECI=None, Enabled=None, MCC=None, MNC=None, Name=None, ParentMme=None, ParentSgw=None, RAILAC=None, RAIMCC1=None, RAIMCC2=None, RAIMCC3=None, RAIMNC1=None, RAIMNC2=None, RAIMNC3=None, RAIRAC=None, TAC=None):
		"""Updates a child instance of egtpNbS5S8Range on the server.

		Args:
			ECI (str): EUTRAN Cell Identifier
			Enabled (bool): Disabled ranges won't be configured nor validated.
			MCC (str): Mobile Country Code
			MNC (str): Mobile Network Code
			Name (str): Name of range
			ParentMme (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=mmeS5S8SecondaryRange)): Id of parent MME range
			ParentSgw (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=range)): Id of parent SGW range
			RAILAC (str): LAC for UEs (Hexa value)
			RAIMCC1 (number): First digit of MCC location for UEs
			RAIMCC2 (number): Second digit of MCC location for UEs
			RAIMCC3 (number): 3rd digit of MCC location for UEs
			RAIMNC1 (number): first digit of MNC location for UEs
			RAIMNC2 (number): Second digit of MNC location for UEs
			RAIMNC3 (number): Third digit of MNC location for UEs
			RAIRAC (str): RAC for UEs (Hexa value)
			TAC (str): Tracking Area Code

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def CustomProtocolStack(self, *args, **kwargs):
		"""Executes the customProtocolStack operation on the server.

		Create custom protocol stack under /vport/protocolStack

		customProtocolStack(Arg2:list, Arg3:enum)
			Args:
				args[0] is Arg2 (list(str)): List of plugin types to be added in the new custom stack
				args[1] is Arg3 (str(kAppend|kMerge|kOverwrite)): Append, merge or overwrite existing protocol stack

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('customProtocolStack', payload=payload, response_object=None)

	def DisableProtocolStack(self, *args, **kwargs):
		"""Executes the disableProtocolStack operation on the server.

		Disable a protocol under protocolStack using the class name

		disableProtocolStack(Arg2:string)string
			Args:
				args[0] is Arg2 (str): Protocol class name to disable

			Returns:
				str: Status of the exec

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('disableProtocolStack', payload=payload, response_object=None)

	def EnableProtocolStack(self, *args, **kwargs):
		"""Executes the enableProtocolStack operation on the server.

		Enable a protocol under protocolStack using the class name

		enableProtocolStack(Arg2:string)string
			Args:
				args[0] is Arg2 (str): Protocol class name to enable

			Returns:
				str: Status of the exec

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		payload = { "Arg1": self.href }
		for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
		for item in kwargs.items(): payload[item[0]] = item[1]
		return self._execute('enableProtocolStack', payload=payload, response_object=None)
