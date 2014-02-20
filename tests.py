#!/usr/bin/env
#-*- coding: utf-8 -*-

import unittest

import testserver

import socket
import errno
import httplib2


class TestBase(unittest.TestCase):
    def test_init(self):
        server = testserver.Server()
        self.assertIsInstance(server, testserver.Server,
                              'Initialization')

    def test_system_port(self):
        try:
            testserver.Server(port=80)

        except socket.error as e:

            self.assertEqual(e[0], errno.EACCES,
                             'Initialization with system port')

    def test_illegal_port(self):
        self.assertRaises(ValueError, testserver.Server, port='blah')
        'Initialization with illegal port'

    def test_timeout(self):
        server = testserver.Server(wait=0)
        try:
            server.req

        except testserver.TimeOut:

            self.assertTrue(True, 'Timeout wait request')

    def test_head(self):
        h = httplib2.Http()

        server = testserver.Server()

        port = server.port

        h.request('http://localhost:%d/head' % port, 'HEAD')

        req = server.req

        self.assertIsInstance(req, dict,
                              'Request catched')
        self.assertEqual('/head', req['path'],
                         'Head request with path')

    def test_get(self):
        h = httplib2.Http()

        server = testserver.Server()

        port = server.port

        h.request('http://localhost:%d/?key=value' % port, 'GET')

        req = server.req

        self.assertIsInstance(req, dict,
                              'Request catched')
        self.assertEqual('/?key=value', req['path'],
                         'Get request with path')

    def test_put(self):
        h = httplib2.Http()

        server = testserver.Server()

        port = server.port

        h.request('http://localhost:%d' % port, 'PUT',
                  body='Test')

        req = server.req

        self.assertIsInstance(req, dict,
                              'Request catched')
        self.assertEqual(req['body'], 'Test')

    def test_post(self):
        h = httplib2.Http()

        server = testserver.Server()

        port = server.port

        h.request('http://localhost:%d' % port, 'POST',
                  body='Test')

        req = server.req

        self.assertIsInstance(req, dict,
                              'Request catched')
        self.assertEqual(req['body'], 'Test')


if __name__ == '__main__':
    unittest.main()
