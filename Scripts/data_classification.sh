#!/usr/bin/env bash

# Description: Capitalise all file names and divide all .gif images into four
#              pre-set groups.
#              Tested on GNU Bash v4.3.
# Author: Yongzhen Ren
# Credits: Lin Lyu & Lulu Wang
# Date created: 2018-03-22
# N.B.: Run the script before BACKING UP raw data since it will change folder
#       structure permenantly.

TARGET_DIRECTORY='Ancient_Chinese_Character_Dataset'
# For two arrays below, the order of items DOES matters.
CLASSIFICATION_DIRECTORY=('Oracle' 'Bronze' 'Seal' 'LST')
LABELS=('J' 'B' 'S' 'L')
FILES='*.gif'

cd $TARGET_DIRECTORY
for directory in ${CLASSIFICATION_DIRECTORY[@]:0}
do
	if [ ! -d $directory ]
	then
		mkdir $directory
	fi
done

ls $FILES | xargs rename 's/([^.]*)/\U$1/'
# Capitalise all letters in the file name, excluding ones in file extension.
# `ls` and `xargs` command are used to avoid "Argument list too long" error.

for file in $FILES
do
	for (( index=0; index<${#LABELS[@]}; index++ ))
	do
		if [[ $file =~ ${LABELS[$index]} ]]
		then
			mv $file -t ${CLASSIFICATION_DIRECTORY[$index]}
			break
		fi
	done
done
