#!/usr/bin/env
# -*- coding: utf-8 -*-

import BaseHTTPServer


class HTTPServer(BaseHTTPServer.HTTPServer):
    allow_reuse_address = {}
    req = {}


class HTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
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
