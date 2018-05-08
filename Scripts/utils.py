#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Description: It contains methods that may be used for multiple Python scripts.
#              Tested under Python 3.5 on Ubuntu 16.04.
# Author: Yongzhen Ren
# Credits: Lin Lyu & Lulu Wang
# Date created: 2018-04-14

import os
from sys import stdout

PROGRESS_BAR_LENGTH = 30

def safe_mkdir(path):
	""" Create a directory safely if there is not one already.
	"""
	if not os.path.exists(path):
		try:
			os.mkdir(path)
		except OSError:
			print("Cannot create the directory")
	elif not os.path.isdir(path):
	# There is a same-name file as the directory we want to create.
		print("The name is already used in this location.")
		raise OSError

def progress_bar(count, total):
	""" A naive implementation of progress bar in console.
	"""
	filled_length = int(round(PROGRESS_BAR_LENGTH * count / float(total)))
	percentage = round(100.0 * count / float(total), 1)
	bar = '=' * filled_length + '-' * (PROGRESS_BAR_LENGTH - filled_length)
	proportion = '(' + str(count) + ' / ' + str(total) + ')'
	stdout.write('[%s] %s%s %s \r' % (bar, percentage, '%', proportion))
	stdout.flush()
