# -*- coding: utf-8 -*-

# Import Python libs
from __future__ import absolute_import, print_function, unicode_literals

import functools
import glob
import logging
import os
import posixpath

import salt.utils.data
import salt.utils.jinja
import salt.utils.yaml
from jinja2 import Environment, FileSystemLoader

# Import Salt libs
from salt.ext import six

log = logging.getLogger(__name__)


def ext_pillar(minion_id, pillar, *args, **kwargs):
    dummy = {'dummy': 'what u want mann?'}

    return dummy

