# !/usr/bin/env python
# coding: utf-8

from six.moves.urllib.parse import urlparse


class RunConfig(object):

    def __init__(self, api_key=None, api_secret=None, host_used=None):
        # type: (str, str, str) -> None
        self.api_key = api_key
        self.api_secret = api_secret
        self.host_used = host_used
        self.use_test = urlparse(host_used).hostname == "fx-api-testnet.gateio.ws"
