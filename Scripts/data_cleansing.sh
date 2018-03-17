#!/usr/bin/env bash

# Description: Remove all broken .gif image files and resize them under the
#              same size for deep learning training.
# Author: Yongzhen Ren
# Credits: Lin Lyu & Lulu Wang
# Date created: 2018-03-15
# N.B.: ImageMagick software suite must be available. If not, please install
#       by the command `sudo apt-get install imagemagick` on Ubuntu.

TARGET_DIRECTORY='./Ancient_Chinese_Character_Dataset'
TRASH_BIN_DIRECTORY='trash_bin'
FILES='*.gif'
FILE_TYPE='GIF image data'
SIZE_IN_PIXEL=100

cd $TARGET_DIRECTORY
if [ ! -d $TRASH_BIN_DIRECTORY ]; then
	mkdir $TRASH_BIN_DIRECTORY
fi

for file in $FILES;
do
	magic_number=$(file --brief $file)
	if [[ $magic_number =~ $FILE_TYPE ]]; then

		mogrify -sample ${SIZE_IN_PIXEL}x${SIZE_IN_PIXEL} $file
		# Without using `-resize` parametre, aliasing effect will appear,
		# fortunately, which is exactly what we want here.
		# Details are explained here:
		# https://www.imagemagick.org/Usage/filter/#aliasing

		convert $file -background '#FFFFFF' -compose Copy -gravity center -extent\
		${SIZE_IN_PIXEL}x${SIZE_IN_PIXEL} $file
	else
		mv $file $TRASH_BIN_DIRECTORY
		# `file` command may produce wrong result since it simply uses magic
		# number; therefore do check $TRASH_BIN_DIRECTORY in $TARGET_DIRECTORY
		# after running the script to make sure no normal .gif files are in it.
	fi
done
