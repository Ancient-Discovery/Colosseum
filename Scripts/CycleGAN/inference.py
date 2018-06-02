"""Translate an image to another image
An example of command-line usage is:
python export_graph.py --model pretrained/oracle2word.pb \
                       --input input_sample.jpg \
                       --output output_sample.jpg \
                       --image_size 256
"""

import tensorflow as tf
import os
from model import CycleGAN
import utils

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

FLAGS = tf.flags.FLAGS

tf.flags.DEFINE_string('model',r'.\pretrained\oralce2bronze.pb', 'model path (.pb)')
tf.flags.DEFINE_string('input',r".\data\oracle2bronze\\TestB", 'input image path (.jpg)')
tf.flags.DEFINE_string('output',r".\data\oracle2bronze\\BpredictionA", 'output image path (.jpg)')
tf.flags.DEFINE_integer('image_size', '80', 'image size, default: 80')
 #input图片所在文件夹
files= os.listdir(FLAGS.input)

def inference():
  graph = tf.Graph()

  with graph.as_default():
    for file in files:
      nameL=file.split('.')
      name=nameL[0]
      with tf.gfile.FastGFile(FLAGS.input+'\\'+file, 'rb') as f:
        image_data = f.read()
        input_image = tf.image.decode_jpeg(image_data, channels=0)
        input_image = tf.image.resize_images(input_image, size=(FLAGS.image_size, FLAGS.image_size))
        input_image = utils.convert2float(input_image)
        input_image.set_shape([FLAGS.image_size, FLAGS.image_size,1])

      with tf.gfile.FastGFile(FLAGS.model, 'rb') as model_file:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(model_file.read())
      [output_image] = tf.import_graph_def(graph_def,
                            input_map={'input_image': input_image},
                            return_elements=['output_image:0'],
                            name='output')

      with tf.Session(graph=graph) as sess:
        generated = output_image.eval()
        with open(FLAGS.output+'\\'+name+'_fake.jpg', 'wb') as f:
          f.write(generated)

def main(unused_argv):
  inference()

if __name__ == '__main__':
  tf.app.run()
