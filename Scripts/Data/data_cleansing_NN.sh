#!/usr/bin/env bash

# Description: Remove all corrupted .gif image files and process them for training
#              convolutional neural networks.
#              Tested on GNU Bash v4.3.
# Author: Yongzhen Ren
# Credits: Lin Lyu & Lulu Wang
# Date created: 2018-03-15
# N.B.: ImageMagick software suite must be available. If not, please install
#       by the command `sudo apt-get install imagemagick` on Ubuntu.

TARGET_DIRECTORY='Ancient_Chinese_Character_Dataset'
TRASH_BIN_DIRECTORY='trash_bin'
FILE_EXTENSION='*.gif'
FILE_TYPE='GIF image data'
SIZE_IN_PIXEL=80

cd $TARGET_DIRECTORY
if [ ! -d $TRASH_BIN_DIRECTORY ]
then
	mkdir $TRASH_BIN_DIRECTORY
fi

for file in $FILE_EXTENSION
do
	magic_number=$(file --brief $file)
	if [[ $magic_number =~ $FILE_TYPE ]]
	then
		mogrify -trim +repage -negate -sample ${SIZE_IN_PIXEL}x${SIZE_IN_PIXEL} $file
		# `-trim` option is used to remove white borders around the original images;
		# `+repage` is used to adjust the canvas to the same size of the actual image.
		# `-negate` is used to reverse image colors.
		# Without using `-resize` parametre, aliasing effect will appear when `-sample` is applied,
		# fortunately, which is exactly what we want here.
		# Details are explained here:
		# https://www.imagemagick.org/Usage/filter/#aliasing
		convert $file -background '#000000' -compose Copy -gravity center -extent\
		${SIZE_IN_PIXEL}x${SIZE_IN_PIXEL} $file
	else
		mv $file $TRASH_BIN_DIRECTORY
		# `file` command may produce wrong results since it simply uses magic
		# number; therefore DO check $TRASH_BIN_DIRECTORY in $TARGET_DIRECTORY
		# after running the script to make sure no normal .gif files are in it.
	fi
done
