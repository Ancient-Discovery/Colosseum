#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Description: Generate a set of images of all CJK unified characters (87870)
#              except 12 ones in the block named CJK Compatibility Ideographs
#              according to Unicode 10.0.
#              Tested under Python 3.5 on Ubuntu 16.04 with Hanazono v20170904
#              (https://osdn.net/projects/hanazono-font/downloads/68253/hanazono-20170904.zip/).
# Author: Yongzhen Ren
# Credits: Lin Lyu & Lulu Wang
# Date created: 2018-04-09
# N.B.: Two Hanazono fonts file must be available in the same directory.
#       If not, please download the newest version from here: http://fonts.jp/hanazono/.

from PIL import Image, ImageDraw, ImageFont
import random
import os

import utils

# CJK Unified Ideographs.
CJK_UI = (0x4E00, 0x9FEA)
CJK_UI_EX_A = (0x3400, 0x4DB5)
CJK_UI_EX_B = (0x20000, 0x2A6D6)
CJK_UI_EX_C = (0x2A700, 0x2B734)
CJK_UI_EX_D = (0x2B740, 0x2B81D)
CJK_UI_EX_E = (0x2B820, 0x2CEA1)
CJK_UI_EX_F = (0x2CEB0, 0x2EBE0)
SET_A = [CJK_UI, CJK_UI_EX_A]
SET_B = [CJK_UI_EX_B, CJK_UI_EX_C, CJK_UI_EX_D, CJK_UI_EX_E, CJK_UI_EX_F]
LIST_OF_TWO_SETS = [SET_A, SET_B]

SIZE_IN_PIXEL = 48 # Size of images in training set.
COLOUR_MODE = "L"
# 8-bit pixels, black and white; the default background colour is black.
IMAGE_SIZE = (SIZE_IN_PIXEL, SIZE_IN_PIXEL)
BACKGROUND_COLOUR = 0
CHARACTER_COLOUR = 255

FONT_A_PATH = "HanaMinA.ttf" # It contains CJK Unified Ideographs and extension A.
FONT_B_PATH = "HanaMinB.ttf" # It contains extension B to F.
FONT_LIST = [FONT_A_PATH, FONT_B_PATH]
FONT_SIZE = SIZE_IN_PIXEL
STARTING_POSITION_A = (0, -8) # A magic number determined by try and trial.
STARTING_POSITION_B = (0, 0)
STARTING_POSITIONS = [STARTING_POSITION_A, STARTING_POSITION_B]

FILE_EXTENSION = ".gif"
OUTPUT_IMAGE_DIRECTORY = "All_CJK_Character_Dataset"

if __name__ == "__main__":
	utils.safe_mkdir(OUTPUT_IMAGE_DIRECTORY)

	for i in range(2):
		current_font = ImageFont.truetype(FONT_LIST[i], FONT_SIZE)
		for block in LIST_OF_TWO_SETS[i]:
			for code_point in range(block[0], block[1] + 1):
				char = chr(code_point)
				image = Image.new(COLOUR_MODE, IMAGE_SIZE, color = BACKGROUND_COLOUR)
				draw = ImageDraw.Draw(image)
				draw.fontmode = "1"
				# The mask `fontmode` is set to 1, which means NO anti-alias effect.
				# Further details are explained here:
				# https://mail.python.org/pipermail/image-sig/2005-August/003497.html
				draw.text(STARTING_POSITIONS[i], char, fill = CHARACTER_COLOUR, font = current_font)
				output_path = os.path.join(OUTPUT_IMAGE_DIRECTORY, char + FILE_EXTENSION)
				image.save(output_path)
