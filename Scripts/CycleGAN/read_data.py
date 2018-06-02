import tensorflow as tf
# from sklearn import datasets
import numpy as np
import os
from PIL import Image
from sys import stdout
import matplotlib.pyplot as plt
import time
import utils

class Read_data():
	def  __init__(self,class_path='',border_pixel_size=80,batch_size=1):
		self.class_path=class_path
		self.border_pixel_size=border_pixel_size
		self.batch_size=batch_size
	def read_data(self):
		state=0
		count=0
		all_pictures=np.zeros(shape=(1,self.border_pixel_size,self.border_pixel_size,1))
		for img_name in os.listdir(self.class_path):
			img_path=self.class_path+"\\"+img_name
			# 处理图像将80x80转化为1x6400
			img_current=np.array(Image.open(img_path))
			img=img_current.reshape(1,self.border_pixel_size,self.border_pixel_size,1)
			if state == 0:
				all_pictures=img
			else:
				all_pictures=np.concatenate((all_pictures,img))
			state=state+1
		idx = np.random.randint(len(all_pictures), size=1)
		batch_image=all_pictures[idx,:]
		img_tensor= tf.convert_to_tensor(batch_image)
		# t2 = tf.cast(img_tensor,dtype=tf.float32) 

		# t2= tf.convert_to_tensor(all_pictures)
		# image = self._preprocess(t2)
		# images = tf.train.shuffle_batch(
  #           [image], batch_size=1, num_threads=8,
  #           capacity=1004,
  #           min_after_dequeue=1000
  #         )
		# # print(images.shape)
		# with tf.name_scope("read_data"):
		# 	tf.summary.image('_input', t2)
		t2= tf.convert_to_tensor(all_pictures)
		# image = self._preprocess(t2)
		input_batch,output_batch=tf.train.shuffle_batch([t2[0],batch_size=self.batch_size,capacity=1010,min_after_dequeue=1000,enqueue_many=True,allow_smaller_final_batch=True)
		return img_tensor
	def _preprocess(self, image):
		image = tf.image.resize_images(image, size=(self.border_pixel_size, self.border_pixel_size))
		image = utils.convert2float(image)
		image.set_shape([self.border_pixel_size, self.border_pixel_size, 1])
		return image

