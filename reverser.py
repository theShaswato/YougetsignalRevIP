# -*- coding: utf-8 -*-
# Author: https://github.com/theShaswato
from urllib.parse import urlencode
from urllib.request import urlopen, Request, URLError, HTTPError
from json import loads

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'}
url = 'https://domains.yougetsignal.com/domains.php'

class Reverser(object):

    def __init__(self, inp):
        self.inp = inp
        self.check()

    def check(self):
        values = urlencode({'remoteAddress': self.inp, 'key': ''}).encode('utf-8')
        try:
            req = Request(url, values, header)
            res = urlopen(req)
        except HTTPError:
            exit('HTTP Error')
        except URLError:
            exit('URL Error');
        else:
            self.data = loads(res.read())

    def info(self):
        if self.data['status'] != 'Success':
            print('Something went wrong')
            print('Message from "yougetsignal.com":\n ')
            print(self.data['message'])
            exit()
        else:
            print('Domain: ' + self.data['remoteAddress'])
            print('Ip: ' + self.data['remoteIpAddress'])
            print('Domains hosted: ' + str(self.data['domainCount']) + '\n')
            with open('result.txt', 'w') as result:
                result.write('Domain: ' + self.data['remoteAddress'] + '\n')
                result.write('Ip: ' + self.data['remoteIpAddress'] + '\n')
                result.write('Domains hosted: ' + str(self.data['domainCount']) + '\n\n')
                for domain in self.data['domainArray']:
                    result.write(domain[0] + '\n')
                    print(domain[0])

def main():
    inp = input('Enter domain or IP: ')
    result = Reverser(inp)
    result.info()

if __name__ == '__main__':
    main()