#!/usr/bin/env
# -*- coding: utf-8 -*-

import time
import socket
import threading

from .http import HTTPServer, HTTPHandler
from .exceptions import TimeOut


class Server:
    '''Simple threaded HTTP server deamon

    @property (int) port
    @property (dict) req

    '''

    port = None

    _server = None
    _httpd = None

    def __init__(self, port=0, wait=5, handler=HTTPHandler):
        self.port = self._check_or_get_port(port)

        self._wait = wait

        self._server = HTTPServer(('', self.port), handler)

        self._httpd = threading.Thread(target=self._server.serve_forever)
        self._httpd.setDaemon(True)
        self._httpd.start()

    @property
    def req(self):
        start_time = time.time()
        while not self._server.req:
            time.sleep(0.2)
            if time.time() - start_time > self._wait:

                raise TimeOut('No request handled in %02ds' % self._wait)

        return self._server.req

    def _check_or_get_port(self, port):
        try:
            port = int(port)

        except Exception as e:

            raise e

        sock = socket.socket()

        try:
            sock.bind(('', port))

        except Exception as e:

            raise e

        port = sock.getsockname()[1]

        sock.close()

        return port
