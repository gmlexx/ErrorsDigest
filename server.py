#!/usr/bin/python

import sys
import resources
import storage
from twisted.internet.protocol import DatagramProtocol
from twisted.web import server
from twisted.application import service, internet
from twisted.python import log
from django.conf import settings

storage.load()

settings.configure(TEMPLATE_DIRS=('templates',))

class UDPServer(DatagramProtocol):
	def datagramReceived(self, datagram, address):
 		data = datagram.strip().decode('cp1251')
		storage.put(data)

class Service(service.Service):
	def startService(self):
		log.startLogging(sys.stdout)
		service.Service.startService(self)
		log.msg('ErrorDigest server started')

_topService = service.MultiService()

_service = Service()
_service.setServiceParent(_topService)

root = resources.Root('media')
root.putChild('pattern', resources.Pattern('pattern.html'))
root.putChild('data', resources.Data('data.html'))
root.putChild('digest', resources.Digest('digest.html'))
root.putChild('patterns', resources.RawPatterns('all_patterns.html'))
root.putChild('new_pattern', resources.RawNewPattern('new_pattern.html'))

_factory = server.Site(root)

_tcpService = internet.TCPServer(8080, _factory)
_udpService = internet.UDPServer(8001, UDPServer())

_udpService.setServiceParent(_topService)
_tcpService.setServiceParent(_topService)


application = service.Application("ErrorDigest")
_topService.setServiceParent(application)
