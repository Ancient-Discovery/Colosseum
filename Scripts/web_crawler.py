#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Description: A web crawler for Chinese Etymology (http://chineseetymology.org)
#              gathers all renamed pictures (in .gif format) into a newly-created
#              folder under the current directory.
#              Tested on Python 3.5.
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

folder_name = "Ancient_Chinese_Character_Dataset"
char_list_name = "CJK_Unified_Characters.txt"

field_tokens = ["SealImages", "LstImages", "BronzeImages", "OracleImages"]
domain_name = "http://chineseetymology.org"
input_src = "/CharacterEtymology.aspx?characterInput="

time_out_seconds = 30 # Read / Connect timeout.
reconnection_interval = 10

regex_gif = r"\/[^\s\\]+\.gif" # Used to find all .gif file links.
regex_picture = r"\w+.\.gif" # Used to form final file name partially.

bar_length = 30

def progress_bar(count, total):
# A naive implementation of progress bar in console.
	filled_length = int(round(bar_length * count / float(total)))
	percentage = round(100.0 * count / float(total), 1)
	bar = '=' * filled_length + '-' * (bar_length - filled_length)
	proportion = '(' + str(count) + ' / ' + str(total) + ')'
	stdout.write('[%s] %s%s %s \r' % (bar, percentage, '%', proportion))
	stdout.flush()

if __name__ == "__main__":
	if not os.path.isdir(folder_name):
		os.mkdir(folder_name)
	with open(char_list_name, "r") as fp:
		char_list = fp.read().split('\n')
	# The file `char_list_name` has to be in the same directory of this script.
	os.chdir(folder_name)

	overall_progress = len(char_list)
	current_progress = 1

	for index in range(0, overall_progress):
		progress_bar(current_progress, overall_progress)
		URL = domain_name + input_src + char_list[index]
		try:
			html = requests.request("GET", URL, timeout = time_out_seconds)
		except requests.exceptions.ReadTimeout:
			time.sleep(reconnection_interval)
			html = requests.request("GET", URL, timeout = time_out_seconds * 2)
		lines = html.text.split('\n')

		i, j = 0, 0
		while i < len(field_tokens) and j < len(lines):
		# A little ugly "non-Pythonic" way to improve run-time performance.
			current_line = lines[j]
			if field_tokens[i] in current_line:
				gif_paths = re.findall(regex_gif, current_line)
				if gif_paths:
					for gif_directory in gif_paths:
						try:
							gif_file = requests.request("GET", domain_name + gif_directory, timeout = time_out_seconds)
						except requests.exceptions.ReadTimeout:
							time.sleep(reconnection_interval)
							gif_file = requests.request("GET", domain_name + gif_directory, timeout = time_out_seconds * 2)
						# Renaming rule: <Character>_<Type><5-digit Index>.gif
						gif_file_name = char_list[index] + '_' + re.search(regex_picture, gif_directory).group(0)
						with open(gif_file_name, "wb") as fp:
							fp.write(gif_file.content)
				i += 1 # Prepare to read from next token.
			j += 1 # Check next line.
		current_progress += 1
