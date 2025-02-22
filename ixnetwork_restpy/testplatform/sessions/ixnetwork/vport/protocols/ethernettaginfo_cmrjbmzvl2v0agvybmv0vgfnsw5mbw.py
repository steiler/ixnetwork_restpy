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


class EthernetTagInfo(Base):
	"""(Read Only) List of ethernet tags for an EVI.
	The EthernetTagInfo class encapsulates a list of ethernetTagInfo resources that is managed by the system.
	A list of resources can be retrieved from the server using the EthernetTagInfo.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'ethernetTagInfo'

	def __init__(self, parent):
		super(EthernetTagInfo, self).__init__(parent)

	@property
	def EsiLabel(self):
		"""(Read Only) ESI label learned.

		Returns:
			str
		"""
		return self._get_attribute('esiLabel')

	@property
	def EthernetTag(self):
		"""(Read Only) Ethernet Tag id in hex format.

		Returns:
			str
		"""
		return self._get_attribute('ethernetTag')

	@property
	def Labels(self):
		"""(Read Only) Per EVI/EthernetTag A-D label learned for an EVI or an Ethernet Tag.

		Returns:
			str
		"""
		return self._get_attribute('labels')

	def find(self, EsiLabel=None, EthernetTag=None, Labels=None):
		"""Finds and retrieves ethernetTagInfo data from the server.

		All named parameters support regex and can be used to selectively retrieve ethernetTagInfo data from the server.
		By default the find method takes no parameters and will retrieve all ethernetTagInfo data from the server.

		Args:
			EsiLabel (str): (Read Only) ESI label learned.
			EthernetTag (str): (Read Only) Ethernet Tag id in hex format.
			Labels (str): (Read Only) Per EVI/EthernetTag A-D label learned for an EVI or an Ethernet Tag.

		Returns:
			self: This instance with matching ethernetTagInfo data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of ethernetTagInfo data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the ethernetTagInfo data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
