# -*- coding: utf-8 -*-
# Author: https://github.com/theShaswato
from urllib import urlencode
from urllib2 import urlopen, Request, URLError, HTTPError
from json import loads

useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'
headers = {'User-Agent': useragent}
url = 'https://domains.yougetsignal.com/domains.php'

def checkDomain(addr):
    values = {'remoteAddress':addr, 'key':''}
    params = urlencode(values)
    try:
        req = Request(url, params, headers)
        response = urlopen(req)
    except URLError:
        exit('url error')
    except HTTPError:
        exit('http error')
    else:
        data = response.read()

    def _printInfo(data):
        info = loads(data)
        if info['status'] != 'Success':
            print "Something went wrong!"
            print "message from yougetsignal.com:\n"
            print info['message']
        else:
            totalDomains = info['domainCount']
            remoteAddr = info['remoteAddress']
            remoteIp = info['remoteIpAddress']
            domains = info['domainArray']

            print 'Domain: {}'.format(remoteAddr)
            print 'Ip: {}'.format(remoteIp)
            print 'Total domains hosted: {}'.format(totalDomains)

            with open('{}[scan_log].txt'.format(remoteAddr), 'w') as f:
                f.write("Domain: {}\n".format(remoteAddr))
                f.write("Ip: {}\n".format(remoteIp))
                f.write("Total Domains found: {}\n\n\n".format(totalDomains))
                f.write("Domain list:\n")
                for domain in domains:
                    f.write("{}\n".format(domain[0]))

            print 'list has been saved in {}[scan_log].txt'.format(remoteAddr)
            if raw_input('Do you want to view sites now?[y/n]').lower() == 'y':
                print "\n"
                for domain in domains:
                    print domain[0]
                print "\n"

            exit('Done')

    _printInfo(data)

try:
    checkDomain(raw_input('Enter the domain or ip: '))
except KeyboardInterrupt:
    exit('User exits')
