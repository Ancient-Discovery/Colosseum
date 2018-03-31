#!/usr/bin/env bash

# Description: Capitalise all file names and divide all .gif images into four
#              pre-set categories.
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

ls | xargs rename 's/([^.]*)/\U$1/'
# Capitalise all letters in the file name, excluding ones in file extension.
# If an error message "Argument list too long" is raised, which is caused by
# a Linux kernel limitation; just do not panic and run the script for multiple times.
# This issue is explained by two links below:
# https://wiki.debian.org/CommonErrorMessages/ArgumentListTooLong
# and
# https://stackoverflow.com/questions/11289551/argument-list-too-long-error-for-rm-cp-mv-commands

for directory in ${CLASSIFICATION_DIRECTORY[@]:0}
do
	if [ ! -d $directory ]
	then
		mkdir $directory
	fi
done

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
