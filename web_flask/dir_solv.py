#!/usr/bin/python3
"""this modules solve the import issue"""
import sys
from os.path import abspath, dirname

sys.path.append(dirname(dirname(abspath(__file__))))
