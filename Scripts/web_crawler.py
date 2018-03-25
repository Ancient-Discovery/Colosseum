#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Description: A web crawler for Chinese Etymology (http://chineseetymology.org)
#              gathers all renamed pictures (in .gif format) into a newly-created
#              folder under the current directory.
#              Tested under Python 3.5 on Ubuntu 16.04.
# Author: Yongzhen Ren
# Credits: Lin Lyu & Lulu Wang
# Date created: 2018-03-09
# Known issues: The script treats the same character from simplified and
#               traditional Chinese differently.

import os
import time
import re
import requests
from sys import stdout

FOLDER_NAME = "Ancient_Chinese_Character_Dataset"
CHAR_LIST_NAME = "CJK_Unified_Characters.txt"

FIELD_TOKENS = ["SealImages", "LstImages", "BronzeImages", "OracleImages"]
DOMAIN_NAME = "http://chineseetymology.org"
INPUT_SRC = "/CharacterEtymology.aspx?characterInput="

TIMEOUT_SECONDS = 30 # Read / Connect timeout.
RECONNECTION_INTERVAL = 10

REGEX_GIF = r"\/[^\s\\]+\.gif" # Used to find all .gif file links.
REGEX_PICTURE = r"\w+.\.gif" # Used to form final file name partially.

PROGRESS_BAR_LENGTH = 30

def progress_bar(count, total):
''' A naive implementation of progress bar in console.
'''
	filled_length = int(round(PROGRESS_BAR_LENGTH * count / float(total)))
	percentage = round(100.0 * count / float(total), 1)
	bar = '=' * filled_length + '-' * (PROGRESS_BAR_LENGTH - filled_length)
	proportion = '(' + str(count) + ' / ' + str(total) + ')'
	stdout.write('[%s] %s%s %s \r' % (bar, percentage, '%', proportion))
	stdout.flush()

if __name__ == "__main__":
	if not os.path.isdir(FOLDER_NAME):
		try:
			os.mkdir(FOLDER_NAME)
		except OSError:
			print("Cannot create the directory")
		os.mkdir(FOLDER_NAME)
	elif not os.path.isdir(FOLDER_NAME):
	# There is a same-name file as the directory we want to create.
		print("The name is already used in this location.")
		raise OSError

	with open(CHAR_LIST_NAME, "r") as fp:
		char_list = fp.read().split('\n')
	# The file `CHAR_LIST_NAME` has to be in the same directory of this script.
	os.chdir(FOLDER_NAME)

	overall_progress = len(char_list)
	current_progress = 1

	for index in range(0, overall_progress):
		progress_bar(current_progress, overall_progress)
		URL = DOMAIN_NAME + INPUT_SRC + char_list[index]
		try:
			html = requests.request("GET", URL, timeout = TIMEOUT_SECONDS)
		except requests.exceptions.ReadTimeout:
			time.sleep(RECONNECTION_INTERVAL)
			html = requests.request("GET", URL, timeout = TIMEOUT_SECONDS * 2)
		lines = html.text.split('\n')

		i, j = 0, 0
		while i < len(FIELD_TOKENS) and j < len(lines):
		# A little ugly "non-Pythonic" way to improve run-time performance.
			current_line = lines[j]
			if FIELD_TOKENS[i] in current_line:
				gif_paths = re.findall(REGEX_GIF, current_line)
				if gif_paths:
					for gif_directory in gif_paths:
						try:
							gif_file = requests.request("GET", DOMAIN_NAME + gif_directory, timeout = TIMEOUT_SECONDS)
						except requests.exceptions.ReadTimeout:
							time.sleep(RECONNECTION_INTERVAL)
							gif_file = requests.request("GET", DOMAIN_NAME + gif_directory, timeout = TIMEOUT_SECONDS * 2)
						# Renaming rule: <Character>_<Type><5-digit Index>.gif
						gif_file_name = char_list[index] + '_' + re.search(REGEX_PICTURE, gif_directory).group(0)
						with open(gif_file_name, "wb") as fp:
							fp.write(gif_file.content)
				i += 1 # Prepare to read from next token.
			j += 1 # Check next line.
		current_progress += 1
