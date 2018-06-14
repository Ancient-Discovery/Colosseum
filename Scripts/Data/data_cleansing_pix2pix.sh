#!/usr/bin/env bash

# Description: Remove all corrupted .gif image files and process them for pix2pix
#              alogrithm (https://phillipi.github.io/pix2pix/) by adding
#              white / random noise as background and converting .gif format into .png one.
#              Tested on GNU Bash v4.3.
# Author: Yongzhen Ren
# Credits: Lin Lyu & Lulu Wang
# Date created: 2018-05-20
# Usage: run the script by `bash data_cleansing.sh [white / random]`.
# N.B.: ImageMagick software suite must be available. If not, please install
#       by the command `sudo apt-get install imagemagick` on Ubuntu.

TARGET_DIRECTORY='Ancient_Chinese_Character_Dataset'
FILE_EXTENSION='*.gif'
SIZE_IN_PIXEL=48

cd $TARGET_DIRECTORY

for file in $FILE_EXTENSION
do
	mogrify -trim +repage -sample ${SIZE_IN_PIXEL}x${SIZE_IN_PIXEL} -transparent '#FFFFFF' $file
	# Make white background transparent.
	if [ $1 == "white" ]
	then
		convert $file -background '#FFFFFF' -gravity center -extent ${SIZE_IN_PIXEL}x${SIZE_IN_PIXEL} -layers flatten "${file%.gif}.png"
	fi
	if [ $1 == "random" ]
	then
		convert -size ${SIZE_IN_PIXEL}x${SIZE_IN_PIXEL} xc: +noise Random -gravity center $file -composite "${file%.gif}.png"
	fi
done

rm $FILE_EXTENSION # Remove all .gif files and only leave .png files.
