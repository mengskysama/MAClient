import urllib2
from urllib2 import HTTPError
from urllib import unquote
import time

def sea_do_ras(_str):
    req = urllib2.Request('http://1.pycrypto.sinaapp.com/?s=%s' % unquote(_str))
    fd = urllib2.urlopen(req)
    d = fd.read().replace('\n','')
    return d