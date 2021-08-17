#!/usr/bin/env python3

import logging

from app import app as application

logging.basicConfig(stream=sys.stderr)

app = application