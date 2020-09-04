# !/usr/bin/env python
# coding: utf-8
import logging
from argparse import ArgumentParser

from config import RunConfig
from futures import futures_demo
from margin import margin_demo
from spot import spot_demo

logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main():
    parser = ArgumentParser(description="Run Gate APIv4 demo application")
    parser.add_argument("-k", "--key", required=True, help="Gate APIv4 Key")
    parser.add_argument("-s", "--secret", required=True, help="Gate APIv4 Secret")
    parser.add_argument("-u", "--url", required=False, help="API base URL used to test")
    parser.add_argument("tests", nargs='+', help="tests to run")
    options = parser.parse_args()

    host_used = options.url
    if not host_used:
        host_used = "https://api.gateio.ws/api/v4"
    if not host_used.startswith("http"):
        host_used = "https://" + host_used
    host_used = host_used.rstrip("/")
    if not host_used.endswith("/api/v4"):
        host_used += '/api/v4'

    run_config = RunConfig(options.key, options.secret, host_used)
    for t in options.tests:
        logger.info("run %s API demo", t)
        if t == 'spot':
            spot_demo(run_config)
        elif t == 'margin':
            margin_demo(run_config)
        elif t == 'futures':
            futures_demo(run_config)
        else:
            logger.warning("ignore unknown test %s", t)


if __name__ == '__main__':
    main()
