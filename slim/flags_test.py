''' Test flag script '''

import tensorflow as tf

tf.app.flags.DEFINE_string('dataset_name', 'imagenet', '')
FLAGS = tf.app.flags.FLAGS

def main(_):
    ''' Invoked by dcos_train.py '''
    print FLAGS.dataset_name
    print FLAGS.train_dir
    print FLAGS.master
