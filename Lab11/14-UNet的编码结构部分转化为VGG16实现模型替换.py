from Networks import TensorFlow_utils as tf_utils
import tensorflow as tf

def maxPoolLayer(x, kHeight, kWidth, strideX, strideY, name, padding = "SAME"):
    """max-pooling"""
    return tf.nn.max_pool(x, ksize = [1, kHeight, kWidth, 1],
                          strides = [1, strideX, strideY, 1], padding = padding, name = name)

def dropout(x, keepPro, name = None):
    """dropout"""
    return tf.nn.dropout(x, keepPro, name)

def fcLayer(x, inputD, outputD, reluFlag, name):
    """fully-connect"""
    with tf.variable_scope(name) as scope:
        w = tf.get_variable("w", shape = [inputD, outputD], dtype = "float")
        b = tf.get_variable("b", [outputD], dtype = "float")
        out = tf.nn.xw_plus_b(x, w, b, name = scope.name)
        if reluFlag:
            return tf.nn.relu(out)
        else:
            return out

def convLayer(x, kHeight, kWidth, strideX, strideY,
              featureNum, name, padding = "SAME"):
    """convlutional"""
    channel = int(x.get_shape()[-1])
    with tf.variable_scope(name) as scope:
        w = tf.get_variable("w", shape = [kHeight, kWidth, channel, featureNum])
        b = tf.get_variable("b", shape = [featureNum])
        featureMap = tf.nn.conv2d(x, w, strides = [1, strideY, strideX, 1], padding = padding)
        out = tf.nn.bias_add(featureMap, b)
        return tf.nn.relu(tf.reshape(out, featureMap.get_shape().as_list()), name = scope.name)

class VGG19(object):
    """VGG model"""
    def __init__(self, x, keepPro, classNum, skip, modelPath = "vgg19.npy"):
        self.X = x
        self.KEEPPRO = keepPro
        self.CLASSNUM = classNum
        self.SKIP = skip
        self.MODELPATH = modelPath
        #build CNN
        self.buildCNN()

    def buildCNN(self):
        """build model"""
        conv1_1 = convLayer(self.X, 3, 3, 1, 1, 64, "conv1_1" )
        conv1_2 = convLayer(conv1_1, 3, 3, 1, 1, 64, "conv1_2")
        pool1 = maxPoolLayer(conv1_2, 2, 2, 2, 2, "pool1")

        conv2_1 = convLayer(pool1, 3, 3, 1, 1, 128, "conv2_1")
        conv2_2 = convLayer(conv2_1, 3, 3, 1, 1, 128, "conv2_2")
        pool2 = maxPoolLayer(conv2_2, 2, 2, 2, 2, "pool2")

        conv3_1 = convLayer(pool2, 3, 3, 1, 1, 256, "conv3_1")
        conv3_2 = convLayer(conv3_1, 3, 3, 1, 1, 256, "conv3_2")
        conv3_3 = convLayer(conv3_2, 3, 3, 1, 1, 256, "conv3_3")
        conv3_4 = convLayer(conv3_3, 3, 3, 1, 1, 256, "conv3_4")
        pool3 = maxPoolLayer(conv3_4, 2, 2, 2, 2, "pool3")

        conv4_1 = convLayer(pool3, 3, 3, 1, 1, 512, "conv4_1")
        conv4_2 = convLayer(conv4_1, 3, 3, 1, 1, 512, "conv4_2")
        conv4_3 = convLayer(conv4_2, 3, 3, 1, 1, 512, "conv4_3")
        conv4_4 = convLayer(conv4_3, 3, 3, 1, 1, 512, "conv4_4")
        pool4 = maxPoolLayer(conv4_4, 2, 2, 2, 2, "pool4")

        conv5_1 = convLayer(pool4, 3, 3, 1, 1, 512, "conv5_1")
        conv5_2 = convLayer(conv5_1, 3, 3, 1, 1, 512, "conv5_2")
        conv5_3 = convLayer(conv5_2, 3, 3, 1, 1, 512, "conv5_3")
        conv5_4 = convLayer(conv5_3, 3, 3, 1, 1, 512, "conv5_4")


class Unet(object):
    def __init__(self, flags):
        self.flags = flags

    def build(self, input, name = 'Unet'):
        with tf.variable_scope(name):
            # conv1_1 = tf_utils.conv2d(input, 64, 3, 3, 1, 1, name='conv1_1')
            # conv1_1 = tf_utils.batch_norm(conv1_1, name='conv1_batch1')
            # conv1_1 = tf.nn.relu(conv1_1, name='conv1_relu1')
            # conv1_2 = tf_utils.conv2d(conv1_1, 64, 3, 3, 1, 1, name='conv1_2')
            # conv1_2 = tf_utils.batch_norm(conv1_2, name='conv1_batch2')
            # conv1_2 = tf.nn.relu(conv1_2, name='conv1_relu2')
            # pool1 = tf_utils.max_pool_2x2(conv1_2, name='pool1')
            #
            # conv2_1 = tf_utils.conv2d(pool1, 128, 3, 3, 1, 1, name='conv2_1')
            # conv2_1 = tf_utils.batch_norm(conv2_1, name='conv2_batch1')
            # conv2_1 = tf.nn.relu(conv2_1, name='conv2_relu1')
            # conv2_2 = tf_utils.conv2d(conv2_1, 128, 3, 3, 1, 1, name='conv2_2')
            # conv2_2 = tf_utils.batch_norm(conv2_2, name='conv2_batch2')
            # conv2_2 = tf.nn.relu(conv2_2, name='conv2_relu2')
            # pool2 = tf_utils.max_pool_2x2(conv2_2, name='pool2')
            #
            # conv3_1 = tf_utils.conv2d(pool2, 256, 3, 3, 1, 1, name='conv3_1')
            # conv3_1 = tf_utils.batch_norm(conv3_1, name='conv3_batch1')
            # conv3_1 = tf.nn.relu(conv3_1, name='conv3_relu1')
            # conv3_2 = tf_utils.conv2d(conv3_1, 256, 3, 3, 1, 1, name='conv3_2')
            # conv3_2 = tf_utils.batch_norm(conv3_2, name='conv3_batch2')
            # conv3_2 = tf.nn.relu(conv3_2, name='conv3_relu2')
            # pool3 = tf_utils.max_pool_2x2(conv3_2, name='pool3')
            #
            # conv4_1 = tf_utils.conv2d(pool3, 512, 3, 3, 1, 1, name='conv4_1')
            # conv4_1 = tf_utils.batch_norm(conv4_1, name='conv4_batch1')
            # conv4_1 = tf.nn.relu(conv4_1, name='conv4_relu1')
            # conv4_2 = tf_utils.conv2d(conv4_1, 512, 3, 3, 1, 1, name='conv4_2')
            # conv4_2 = tf_utils.batch_norm(conv4_2, name='conv4_batch2')
            # conv4_2 = tf.nn.relu(conv4_2, name='conv4_relu2')
            # pool4 = tf_utils.max_pool_2x2(conv4_2, name='pool4')
            #
            # conv5_1 = tf_utils.conv2d(pool4, 1024, 3, 3, 1, 1, name='conv5_1')
            # conv5_1 = tf_utils.batch_norm(conv5_1, name='conv5_batch1')
            # conv5_1 = tf.nn.relu(conv5_1, name='conv5_relu1')
            # conv5_2 = tf_utils.conv2d(conv5_1, 1024, 3, 3, 1, 1, name='conv5_2')
            # conv5_2 = tf_utils.batch_norm(conv5_2, name='conv5_batch2')
            # conv5_2 = tf.nn.relu(conv5_2, name='conv5_relu2')

            conv1_1 = convLayer(input, 3, 3, 1, 1, 64, "conv1_1")
            conv1_2 = convLayer(conv1_1, 3, 3, 1, 1, 64, "conv1_2")
            pool1 = maxPoolLayer(conv1_2, 2, 2, 2, 2, "pool1")

            conv2_1 = convLayer(pool1, 3, 3, 1, 1, 128, "conv2_1")
            conv2_2 = convLayer(conv2_1, 3, 3, 1, 1, 128, "conv2_2")
            pool2 = maxPoolLayer(conv2_2, 2, 2, 2, 2, "pool2")

            conv3_1 = convLayer(pool2, 3, 3, 1, 1, 256, "conv3_1")
            conv3_2 = convLayer(conv3_1, 3, 3, 1, 1, 256, "conv3_2")
            conv3_3 = convLayer(conv3_2, 3, 3, 1, 1, 256, "conv3_3")
            conv3_4 = convLayer(conv3_3, 3, 3, 1, 1, 256, "conv3_4")
            pool3 = maxPoolLayer(conv3_4, 2, 2, 2, 2, "pool3")

            conv4_1 = convLayer(pool3, 3, 3, 1, 1, 512, "conv4_1")
            conv4_2 = convLayer(conv4_1, 3, 3, 1, 1, 512, "conv4_2")
            conv4_3 = convLayer(conv4_2, 3, 3, 1, 1, 512, "conv4_3")
            conv4_4 = convLayer(conv4_3, 3, 3, 1, 1, 512, "conv4_4")
            pool4 = maxPoolLayer(conv4_4, 2, 2, 2, 2, "pool4")

            conv5_1 = convLayer(pool4, 3, 3, 1, 1, 512, "conv5_1")
            conv5_2 = convLayer(conv5_1, 3, 3, 1, 1, 512, "conv5_2")
            conv5_3 = convLayer(conv5_2, 3, 3, 1, 1, 512, "conv5_3")
            conv5_4 = convLayer(conv5_3, 3, 3, 1, 1, 512, "conv5_4")

            # ******
            unconv6 = tf_utils.deconv2d(conv5_2, conv4_2.get_shape(), k_h=2, k_w=2, name='unconv6')
            unconv6 = tf_utils.batch_norm(unconv6, name='unconv6_batch')
            unconv6 = tf.nn.relu(unconv6, name='unconv6_relu')

            merge6 = tf.concat(values=[conv4_2, unconv6], axis=-1)

            conv7_1 = tf_utils.conv2d(merge6, 512, 3, 3, 1, 1, name='conv7_1')
            conv7_1 = tf_utils.batch_norm(conv7_1, name='conv7_batch1')
            conv7_1 = tf.nn.relu(conv7_1, name='conv7_relu1')
            conv7_2 = tf_utils.conv2d(conv7_1, 512, 3, 3, 1, 1, name='conv7_2')
            conv7_2 = tf_utils.batch_norm(conv7_2, name='conv7_batch2')
            conv7_2 = tf.nn.relu(conv7_2, name='conv7_relu2')

            unconv8 = tf_utils.deconv2d(conv7_2, conv3_2.get_shape(), k_h=2, k_w=2, name='unconv8')
            unconv8 = tf_utils.batch_norm(unconv8, name='unconv8_batch')
            unconv8 = tf.nn.relu(unconv8, name='unconv8_relu')

            merge8 = tf.concat(values=[conv3_2, unconv8], axis=-1)

            conv9_1 = tf_utils.conv2d(merge8, 256, 3, 3, 1, 1, name='conv9_1')
            conv9_1 = tf_utils.batch_norm(conv9_1, name='conv9_batch1')
            conv9_1 = tf.nn.relu(conv9_1, name='conv9_relu1')
            conv9_2 = tf_utils.conv2d(conv9_1, 256, 3, 3, 1, 1, name='conv9_2')
            conv9_2 = tf_utils.batch_norm(conv9_2, name='conv9_batch2')
            conv9_2 = tf.nn.relu(conv9_2, name='conv9_relu2')

            unconv10 = tf_utils.deconv2d(conv9_2, conv2_2.get_shape(), k_h=2, k_w=2, name='unconv10')
            unconv10 = tf_utils.batch_norm(unconv10, name='unconv10_batch')
            unconv10 = tf.nn.relu(unconv10, name='unconv10_relu')

            merge10 = tf.concat(values=[conv2_2, unconv10], axis=-1)

            conv11_1 = tf_utils.conv2d(merge10, 128, 3, 3, 1, 1, name='conv11_1')
            conv11_1 = tf_utils.batch_norm(conv11_1, name='conv11_batch1')
            conv11_1 = tf.nn.relu(conv11_1, name='conv11_relu1')
            conv11_2 = tf_utils.conv2d(conv11_1, 128, 3, 3, 1, 1, name='conv11_2')
            conv11_2 = tf_utils.batch_norm(conv11_2, name='conv11_batch2')
            conv11_2 = tf.nn.relu(conv11_2, name='conv11_relu2')

            unconv12 = tf_utils.deconv2d(conv11_2, conv1_2.get_shape(), k_h=2, k_w=2, name='unconv12')
            unconv12 = tf_utils.batch_norm(unconv12, name='unconv12_batch')
            unconv12 = tf.nn.relu(unconv12, name='unconv12_relu')

            merge12 = tf.concat(values=[conv1_2, unconv12], axis=-1)

            conv13_1 = tf_utils.conv2d(merge12, 64, 3, 3, 1, 1, name='conv13_1')
            conv13_1 = tf_utils.batch_norm(conv13_1, name='conv13_batch1')
            conv13_1 = tf.nn.relu(conv13_1, name='conv13_relu1')
            conv13_2 = tf_utils.conv2d(conv13_1, 64, 3, 3, 1, 1, name='conv13_2')
            conv13_2 = tf_utils.batch_norm(conv13_2, name='conv13_batch2')
            conv13_2 = tf.nn.relu(conv13_2, name='conv13_relu2')

            result = tf_utils.conv2d(conv13_2, self.flags.output_channel, 1, 1, 1, 1, name='unet_output')

            return tf.nn.sigmoid(result)