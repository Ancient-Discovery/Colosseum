#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Description: Split data set into training sets and testing tests randomly 
#              for each character.
#              Tested under Python 3.5 on Ubuntu 16.04.
# Author: Yongzhen Ren
# Credits: Lin Lyu & Lulu Wang
# Date created: 2018-03-22
# N.B.: Run the script before BACKING UP raw data since it will change folder
#       structure permenantly.

import os
import random
import shutil

TARGET_DIRECTORY = "./Ancient_Chinese_Character_Dataset"
CLASSIFICATION_DIRECTORIES = ['Oracle', 'Bronze', 'Seal', 'LST']
TRAINING_DIRECTORY = "Training_Set"
TESTING_DIRECTORY = "Test_Set"
SEPARATOR = '_'
THRESHOLD = 10
# Each character which has less than or equal to $THRESHOLD images will be used only for testing.
TRAINING_SET_RATE = 0.8
# Percentage of selecting images from each character into training set.

if __name__ == "__main__":
	os.chdir(TARGET_DIRECTORY)
	for directory in CLASSIFICATION_DIRECTORIES:
		character_dict = {}
		os.chdir(directory)
		if not os.path.isdir(TRAINING_DIRECTORY):
			os.mkdir(TRAINING_DIRECTORY)
		if not os.path.isdir(TESTING_DIRECTORY):
			os.mkdir(TESTING_DIRECTORY)
		for root, dirs, files in os.walk("."):
			for name in files:
				character = name.split(sep = SEPARATOR)[0]
				if character in character_dict:
					character_dict[character].append(name)
				else:
					character_dict[character] = [name]

		for character in character_dict.keys():
			filename_list = character_dict[character]
			if len(filename_list) >= THRESHOLD:
				random.seed()
				random.shuffle(filename_list)
				stop = int(len(filename_list) * TRAINING_SET_RATE)
				for item in filename_list[0:stop]:
				# After shuffling, take previous $stop variables into training set.
					shutil.move(item, TRAINING_DIRECTORY)
				for item in filename_list[stop:]:
					shutil.move(item, TESTING_DIRECTORY)

				# Leave the rest of files in original directory.

		os.chdir("..") # Go back to parent directory.
