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


class RateControlParameters(Base):
	"""This object holds the configuration parameters for rate control.
	The RateControlParameters class encapsulates a required rateControlParameters resource which will be retrieved from the server every time the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'rateControlParameters'

	def __init__(self, parent):
		super(RateControlParameters, self).__init__(parent)

	@property
	def ArpRefreshInterval(self):
		"""Indicates the Arp Refresh Interval per Port. Set this to override the defaul value of 60 seconds

		Returns:
			number
		"""
		return self._get_attribute('arpRefreshInterval')
	@ArpRefreshInterval.setter
	def ArpRefreshInterval(self, value):
		self._set_attribute('arpRefreshInterval', value)

	@property
	def MaxRequestsPerBurst(self):
		"""Indicates the flow pattern of the ARP/NS request for each port. Enable this, to send the ARP/NS requests in bursts of size defined by 'Max requests per Bursts'.

		Returns:
			number
		"""
		return self._get_attribute('maxRequestsPerBurst')
	@MaxRequestsPerBurst.setter
	def MaxRequestsPerBurst(self, value):
		self._set_attribute('maxRequestsPerBurst', value)

	@property
	def MaxRequestsPerSec(self):
		"""The maximum requests per second.

		Returns:
			number
		"""
		return self._get_attribute('maxRequestsPerSec')
	@MaxRequestsPerSec.setter
	def MaxRequestsPerSec(self, value):
		self._set_attribute('maxRequestsPerSec', value)

	@property
	def MinRetryInterval(self):
		"""Indicates the minimum wait time for re-sending the ARP/NS requests for a particular interface.

		Returns:
			number
		"""
		return self._get_attribute('minRetryInterval')
	@MinRetryInterval.setter
	def MinRetryInterval(self, value):
		self._set_attribute('minRetryInterval', value)

	@property
	def RetryCount(self):
		"""Indicates the number of times the ARP/NS requests will be resent for a particular interface, if there is an ARP issue.

		Returns:
			number
		"""
		return self._get_attribute('retryCount')
	@RetryCount.setter
	def RetryCount(self, value):
		self._set_attribute('retryCount', value)

	@property
	def SendInBursts(self):
		"""Indicates the flow pattern of the ARP/NS request for each port. Enable this, to send the ARP/NS requests in bursts of size defined by 'Max requests per Bursts'.

		Returns:
			bool
		"""
		return self._get_attribute('sendInBursts')
	@SendInBursts.setter
	def SendInBursts(self, value):
		self._set_attribute('sendInBursts', value)

	@property
	def SendRequestsAsFastAsPossible(self):
		"""If enabled, allows to send ARP/NS requests immediately without any rate control.

		Returns:
			bool
		"""
		return self._get_attribute('sendRequestsAsFastAsPossible')
	@SendRequestsAsFastAsPossible.setter
	def SendRequestsAsFastAsPossible(self, value):
		self._set_attribute('sendRequestsAsFastAsPossible', value)

	def update(self, ArpRefreshInterval=None, MaxRequestsPerBurst=None, MaxRequestsPerSec=None, MinRetryInterval=None, RetryCount=None, SendInBursts=None, SendRequestsAsFastAsPossible=None):
		"""Updates a child instance of rateControlParameters on the server.

		Args:
			ArpRefreshInterval (number): Indicates the Arp Refresh Interval per Port. Set this to override the defaul value of 60 seconds
			MaxRequestsPerBurst (number): Indicates the flow pattern of the ARP/NS request for each port. Enable this, to send the ARP/NS requests in bursts of size defined by 'Max requests per Bursts'.
			MaxRequestsPerSec (number): The maximum requests per second.
			MinRetryInterval (number): Indicates the minimum wait time for re-sending the ARP/NS requests for a particular interface.
			RetryCount (number): Indicates the number of times the ARP/NS requests will be resent for a particular interface, if there is an ARP issue.
			SendInBursts (bool): Indicates the flow pattern of the ARP/NS request for each port. Enable this, to send the ARP/NS requests in bursts of size defined by 'Max requests per Bursts'.
			SendRequestsAsFastAsPossible (bool): If enabled, allows to send ARP/NS requests immediately without any rate control.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())
