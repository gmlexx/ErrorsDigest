import threading, time, logging
import SocketServer
import backend
import storage
from BaseHTTPServer import HTTPServer
import ConfigParser

class UDPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        try:
            data = unicode(self.request[0].strip().decode('windows-1251'))
            storage.put(data)
        except Exception:
            logging.error("Storage put crash", exc_info=1)

def run_server(server):
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
    return server_thread

if __name__ == "__main__":

    config = ConfigParser.RawConfigParser()
    config.read('feeder.cfg')
    logging.basicConfig(filename=config.get("General","logfile"), level=logging.INFO, format="%(message)s")
    storage.load()

    HOST, UDP_PORT, HTTP_PORT = config.get("General","ip"), config.getint("General", "udp_port"), config.getint("General", "http_port")
    try:
        udp_server = SocketServer.UDPServer((HOST, UDP_PORT), UDPHandler)
        run_server(udp_server)
        logging.info("Listening %s on port %s" % (HOST, UDP_PORT))

        http_server = HTTPServer((HOST, HTTP_PORT), backend.HTTPRequestHandler)
        run_server(http_server)
        logging.info("Listening %s on port %s" % (HOST, HTTP_PORT))

        while True:
            time.sleep(10)

    except KeyboardInterrupt:
        logging.info('Shutting down server')
        udp_server.shutdown()
        http_server.shutdown()
