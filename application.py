#!/usr/bin/env python

import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

# noinspection PyUnresolvedReferences
from enchant.server import app as application  # noqa
