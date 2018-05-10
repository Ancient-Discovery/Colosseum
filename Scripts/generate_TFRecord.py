#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Description: A script that converts raw dataset into separate TFRecord files, which
#              can be processed by TensorFlow quickly; also huge dataset will not
#              be included in a Tensorflow flow graph.
#              Tested with TensorFlow 1.7 under Python 3.5 on Ubuntu 16.04.
# Author: Yongzhen Ren
# Credits: Lin Lyu & Lulu Wang
# Date created: 2018-04-24
# Warning: TensorFlow APIs may be changed in the future.

import tensorflow as tf
import os

TARGET_DIRECTORY = "Ancient_Chinese_Character_Dataset"
TFRECORD_FILE_EXTENSION = "_gif.tfrecord"
CLASSIFICATION_DIRECTORIES = ["Oracle", "Bronze", "Seal", "LST"]
SEPARATOR = "_"

# Label index feature, which is represented as code point of each Unicode character.
def _int64_feature(value):
	return tf.train.Feature(int64_list = tf.train.Int64List(value = [value]))

# Binary data feature.
def _bytes_feature(value):
	return tf.train.Feature(bytes_list = tf.train.BytesList(value = [value]))

def generate_tfrecord_files(directory_path):
	char_dict = {}
	with tf.python_io.TFRecordWriter(directory_path + TFRECORD_FILE_EXTENSION) as tfrecord_writer:
		label_index = 0
		for root, dirs, files in os.walk(directory_path):
			for image_name in files:
				character = image_name.split(sep = SEPARATOR)[0]
				if character not in char_dict:
					label_index += 1
					char_dict[character] = label_index
				with open(os.path.join(directory_path, image_name), "rb") as fp:
					image_data = fp.read()
					features = {
					"Images": _bytes_feature(image_data),
					"Labels": _int64_feature(label_index),
					}
					example = tf.train.Example(features = tf.train.Features(feature = features))
					tfrecord_writer.write(example.SerializeToString())

def main(argv):
	os.chdir(TARGET_DIRECTORY)
	for directory in CLASSIFICATION_DIRECTORIES:
		generate_tfrecord_files(directory)

if __name__ == '__main__':
	tf.app.run()
