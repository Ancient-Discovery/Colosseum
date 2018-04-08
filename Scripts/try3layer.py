import tensorflow as tf
# from sklearn import datasets
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
import os
from PIL import Image
from sys import stdout
import matplotlib.pyplot as plt
import time

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
start=time.clock()

# 获取当前目录
def retrieveImageAndLabels(border_pixel_size,class_path):
	words=all_word_dict(class_path)
	character_number=len(words)
	img=np.zeros(shape=(1,border_pixel_size))
	label=np.zeros(shape=(1,character_number))
	state=0
	count=0
	for img_name in os.listdir(class_path):
		img_path=class_path+img_name
		# 处理图像将100x100转化为1x10000
		img_current=np.array(Image.open(img_path))
		img_current=img_current.reshape(1,border_pixel_size*border_pixel_size)
		# 处理标签
		label_current=np.zeros(shape=(1,character_number))
		if img_name[0] in words:
			# print(img_name[0]+str(words[img_name[0]]))
			label_current.itemset(words[img_name[0]],1)

		if state==0:
			img=img_current
			label=label_current
			state=state+1
		else:
			img=np.append(img,img_current)
			label=np.append(label,label_current)
			# Apply ensemble training.
		
	number=img.shape[0]//border_pixel_size//border_pixel_size
	labelNumber=label.shape[0]//character_number
	img=img.reshape(number,border_pixel_size*border_pixel_size)
	label=label.reshape(labelNumber,character_number)
	return img,label
	# print(img)


# 把所有图对应的汉字放在dic里面，数值是顺序，返回这个dic
def all_word_dict(picture_dir):
	pic_id_dic={} 
	all_word_dic={}
	i=0
	for root, dirs, pictures in os.walk(picture_dir):  
		for val in pictures:
			if val[0] not in all_word_dic:
				all_word_dic[val[0]]=i
				i=i+1
				# print(val[0]+str(i))
	return all_word_dic

def variable_summaries(var):
    """Attach a lot of summaries to a Tensor (for TensorBoard visualization)."""
    with tf.name_scope('summaries'):
      # 计算参数的均值，并使用tf.summary.scaler记录
      mean = tf.reduce_mean(var)
      tf.summary.scalar('mean', mean)

      # 计算参数的标准差
      with tf.name_scope('stddev'):
        stddev = tf.sqrt(tf.reduce_mean(tf.square(var - mean)))
      # 使用tf.summary.scaler记录记录下标准差，最大值，最小值
      tf.summary.scalar('stddev', stddev)
      tf.summary.scalar('max', tf.reduce_max(var))
      tf.summary.scalar('min', tf.reduce_min(var))
      # 用直方图记录参数的分布
      tf.summary.histogram('histogram', var)

def compute_accuracy(v_xs,v_ys):
	global prediction
	# 预测值 每一个分类的概率
	y_pre=sess.run(prediction,feed_dict={xs:v_xs,keep_prob:1})
	# 预测与真实的差距
	correct_prediction=tf.equal(tf.argmax(y_pre,1),tf.argmax(v_ys,1))
	# 正确比例
	accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
	result=sess.run(accuracy,feed_dict={xs:v_xs,ys:v_ys,keep_prob:1})
	# 百分比 越高越准确 a
	return result

def weight_variable(shape):
	initial=tf.truncated_normal(shape,stddev=0.1)
	return tf.Variable(initial)

def bias_variable(shape):
	initial=tf.constant(0.1,shape=shape)
	return tf.Variable(initial)

def conv2d(x,W):
	#stride [1,x_move,y_move,1]
	return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')

def max_pool_2x2(x):
	return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')



border_pixel_size=100
class_path=r"G:\Final_Project\Oracle_5K\Oracle_1\Training_Set"+'\\'
image_all,label_all=retrieveImageAndLabels(border_pixel_size,class_path)
character_number=label_all.shape[1]
image_number=label_all.shape[0]

get_image_time=time.clock()-start
print("文件已读取完毕，用时"+str(get_image_time)+"秒")

# print(batch_xs.shape)
# print(batch_ys.shape)

test_pic_path=r"G:\Final_Project\Oracle_5K\Oracle_1\Test_Set"+"\\"
test_x,test_y=retrieveImageAndLabels(border_pixel_size,test_pic_path)

# 28x28=784wo
with tf.name_scope('input'):
	xs=tf.placeholder(tf.float32,[None,border_pixel_size*border_pixel_size],name='x-input')
	ys=tf.placeholder(tf.float32,[None,character_number],name='y-input')
keep_prob=tf.placeholder(tf.float32)
# 1颜色黑白
with tf.name_scope('input'):
	x_image=tf.reshape(xs,[-1,border_pixel_size,border_pixel_size,1])
	tf.summary.image('input_image',x_image,10)
# print(x_image.shape) #[n_samples,28,28,1]
# 5x5 patch 1:in size, out size:32高度
with tf.name_scope('layer1'):
	with tf.name_scope('weights'):
		W_conv1=weight_variable([3,3,1,32])
	with tf.name_scope('biases'):
		b_conv1=bias_variable([32])
		variable_summaries(b_conv1)

h_conv1=tf.nn.relu(conv2d(x_image,W_conv1)+b_conv1) #output size 100x100x32
h_pool1=max_pool_2x2(h_conv1)  #output size 50x50x32
with tf.name_scope('layer2'):
	with tf.name_scope('weights'):
		W_conv2=weight_variable([3,3,32,64])
	with tf.name_scope('biases'):
		b_conv2=bias_variable([64])
h_conv2=tf.nn.relu(conv2d(h_pool1,W_conv2)+b_conv2) #output size 50x50x64
h_pool2=max_pool_2x2(h_conv2)  #output size 25x25x64

# with tf.name_scope('layer3'):
# 	with tf.name_scope('weights'):
# 		W_conv3=weight_variable([3,3,64,128])
# 	with tf.name_scope('biases'):
# 		b_conv3=bias_variable([128])
# h_conv3=tf.nn.relu(conv2d(h_pool2,W_conv3)+b_conv3) #output size 50x50x64
# h_pool3=max_pool_2x2(h_conv3)  #output size 25x25x64


#function 1 layer
with tf.name_scope('layer_1'):
	with tf.name_scope('weights'):
		W_fc1=weight_variable([25*25*64,1024])
	with tf.name_scope('bias'):	
		b_fc1=bias_variable([1024])
		variable_summaries(b_fc1)

h_pool3_flat=tf.reshape(h_pool2,[-1,25*25*64]) #[n_samples,7,7,64]->> 7*7*64
with tf.name_scope('linear_compute'):
	preactivate=tf.matmul(h_pool3_flat,W_fc1)+b_fc1
	tf.summary.histogram('linear',preactivate)

h_fc1=tf.nn.relu(preactivate)
h_fc1_drop=tf.nn.dropout(h_fc1,keep_prob)

#function 2 layer
with tf.name_scope('layer_2'):
	with tf.name_scope('weights'):
		W_fc2=weight_variable([1024,character_number])
	with tf.name_scope('bias'):	
		b_fc2=bias_variable([character_number])
		variable_summaries(b_fc2)
prediction=tf.nn.softmax(tf.matmul(h_fc1_drop,W_fc2)+b_fc2)

with tf.name_scope('loss'):
	cross_entropy=tf.reduce_mean(-tf.reduce_sum(ys*tf.log(tf.clip_by_value(prediction,1e-10,1.0)),reduction_indices=[1]))
	tf.summary.scalar('loss',cross_entropy)
with tf.name_scope('train'):
	train_step=tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

sess=tf.Session()
merged=tf.summary.merge_all()
writer=tf.summary.FileWriter('./log100',sess.graph)
sess.run(tf.global_variables_initializer())

start_loop_time=time.clock()
print("开始训练...")

for i in range(2000):
	# 从下载好的database提取出100个来学习 
	# SGD
	# batch_xs,batch_ys=mnist.train.next_batch(100)
	idx = np.random.randint(image_number, size=50)
	batch_xs=image_all[idx,:]
	batch_ys=label_all[idx,:]

	sess.run(train_step,feed_dict={xs:batch_xs,ys:batch_ys,keep_prob:0.5})
	if i%50==0:
		print(compute_accuracy(test_x,test_y))
		# print(compute_accuracy(batch_test_x,batch_test_y))
		result=sess.run(merged,feed_dict={xs:batch_xs,ys:batch_ys,keep_prob:1})
		writer.add_summary(result,i)
	stdout.flush()

end=time.clock()-start
end_loop=time.clock()-start_loop_time
print("训练用时"+str(end_loop)+"秒")
print("总用时"+str(end)+"秒")
