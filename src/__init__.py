# coding=utf-8

import os
import time
import glob
import importlib

from src.handlers import index
from src.handlers import ErrorHandler

routes = []
routes.extend(index.routes)
routes.append((r"/(.*)", ErrorHandler))
