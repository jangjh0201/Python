import logging
import time
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy

req_proxy = RequestProxy()
proxies = req_proxy.get_proxy_list()
proxies