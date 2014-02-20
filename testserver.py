#!/usr/bin/env
# -*- coding: utf-8 -*-

import time
import socket
import threading
import BaseHTTPServer


class Server:
    '''Simple threaded HTTP server deamon

    @property (int) port
    @property (dict) req

    '''

    port = None

    _server = None
    _httpd = None

    def __init__(self, port=0, wait=5):
        self.port = self._check_or_get_port(port)

        self._wait = wait

        try:
            self._server = HTTPServer(('', self.port), Handler)

        except Exception as e:

            raise e

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


class HTTPServer(BaseHTTPServer.HTTPServer):
    allow_reuse_address = {}
    req = {}


class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self):
        req = {}
        req['headers'] = self.headers
        req['client_address'] = self.client_address
        req['command'] = self.command
        req['path'] = self.path
        req['request_version'] = self.request_version

        if 'Content-Length' in self.headers:
            length = int(self.headers['Content-Length'])
            self.rfile.flush()
            req['body'] = self.rfile.read(length)

        self.server.req = req

        self.send_header('Content-Length', '0')

    do_HEAD = do_GET = do_PUT = do_POST


class TimeOut(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
