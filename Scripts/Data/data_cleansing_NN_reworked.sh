#!/usr/bin/env bash

# Description: Remove all corrupted .gif image files and process them for training
#              convolutional neural networks; and mathematical morphology techniques
#              are applied to extract structures of characters.
#              It is the reworked version of the original script; compared to previous
#              one, it will generate much more efficient data for network training
#              and reduce tremendous calculation time. Also the new dataset is easier
#              to apply 2-D sparse matrix package from Numpy.
#              Tested on GNU Bash v4.3.
# Author: Yongzhen Ren
# Credits: Lin Lyu & Lulu Wang
# Date created: 2018-04-11
# N.B.: ImageMagick software suite must be available. If not, please install
#       by the command `sudo apt-get install imagemagick` on Ubuntu.

TARGET_DIRECTORY='Ancient_Chinese_Character_Dataset'
TRASH_BIN_DIRECTORY='trash_bin'
FILE_EXTENSION='*.gif'
FILE_TYPE='GIF image data'
SIZE_IN_PIXEL=48

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
		# `+repage` is used to adjust the canvas to the same size of the actual image;
		# `-negate` option is used to reverse image colors.
		# Without using `-resize` parametre, aliasing effect will appear when `-sample` is applied,
		# fortunately, which is exactly what we want here.
		# Details are explained here:
		# https://www.imagemagick.org/Usage/filter/#aliasing
		convert $file -background '#000000' -compose Copy -gravity center -extent\
		${SIZE_IN_PIXEL}x${SIZE_IN_PIXEL} -morphology Thinning:-1 Skeleton:2 $file
		# Put current image in the centre of black background and thin it down to a skeleton.
		# Details are explained here:
		# https://www.imagemagick.org/Usage/morphology/
	else
		mv $file $TRASH_BIN_DIRECTORY
		# `file` command may produce wrong results since it simply uses magic
		# number; therefore DO check $TRASH_BIN_DIRECTORY in $TARGET_DIRECTORY
		# after running the script to make sure no normal .gif files are in it.
	fi
done
