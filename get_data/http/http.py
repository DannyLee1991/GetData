# encoding=utf8
__author__ = 'lijianan'

import urllib, httplib, urlparse


def send_http(url, params_dict={}, headers={}, method='GET'):
    host = urlparse.urlparse(url).hostname
    conn = httplib.HTTPConnection(host)
    if params_dict:
        url += "?" + urllib.urlencode(params_dict)
    conn.request(method=method, url=url, body=urllib.urlencode(params_dict), headers=headers)
    response = conn.getresponse()
    res = response.read()
    return res


def send_get(url, params_dict={}, headers={}):
    return send_http(url, params_dict, headers, method='GET')


def send_post(url, params_dict={}, headers={}):
    return send_http(url, params_dict, headers, method='POST')


def send_put(url, params_dict={}, headers={}):
    return send_http(url, params_dict, headers, method='PUT')
