[![Build Status](https://travis-ci.org/vporoshok/testserver.png?branch=master)](https://travis-ci.org/vporoshok/testserver)

testserver
==========

Threaded daemon localhost http server. Simple HEAD, GET and POST request parsing for unittest.

Simple usage:

        import testserver
        import urllib2

        server = testserver.Server()

        port = server.port
        req = urllib2.Request(url='http://localhost:%4d' % port,
                              data='This data is passed to stdin of the CGI')
        urllib2.urlopen(req)

        print server.req['body']
