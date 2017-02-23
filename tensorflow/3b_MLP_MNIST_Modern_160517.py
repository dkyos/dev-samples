
# coding: utf-8

# \* *[Notice] I wrote thie code while following the examples in [Choi's Tesorflow-101 tutorial](https://github.com/sjchoi86/Tensorflow-101). And,  as I know, most of Choi's examples originally come from [Aymeric Damien's](https://github.com/aymericdamien/TensorFlow-Examples/) and  [Nathan Lintz's ](https://github.com/nlintz/TensorFlow-Tutorials) tutorials.*

# ## 3. Multilayer Perceptron with MNIST data

# In[1]:

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
#%matplotlib inline  


# ## Load MNIST data

# In[2]:

mnist      = input_data.read_data_sets('data', one_hot=True)
X_train   = mnist.train.images
Y_train = mnist.train.labels
X_test    = mnist.test.images
Y_test  = mnist.test.labels


# In[3]:

dimX = X_train.shape[1]
dimY = Y_train.shape[1]
nTrain = X_train.shape[0]
nTest = X_test.shape[0]
print ("Shape of (X_train, X_test, Y_train, Y_test)")
print (X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)


# ## Xavier's initialize method
# X. Glorot and Y. Bengio, "Understanding the difficulty of training deep feedforward neural networks", 2010.

# In[4]:

def xavier_init(n_inputs, n_outputs, uniform=True):
    if uniform:
        init_range = tf.sqrt(6.0 / (n_inputs + n_outputs))
        return tf.random_uniform_initializer(-init_range, init_range)
    else:
        stddev = tf.sqrt(3.0 / (n_inputs + n_outputs))
    return tf.truncated_normal_initializer(stddev=stddev)


# ## Define my neural network structure

# In[5]:

nLayer0 = dimX
nLayer1 = 256
nLayer2 = 256
nLayer3 = 256
nLayer4 = 256
nLayer5 =  dimY
sigma_init = 0.1   # For randomized initialization
myDropProb = 0.7 


# In[ ]:

W = {
    'W1': tf.get_variable("W1", shape=[nLayer0, nLayer1], initializer=xavier_init(nLayer0,nLayer1)),
    'W2': tf.get_variable("W2", shape=[nLayer1, nLayer2], initializer=xavier_init(nLayer1,nLayer2)),
    'W3': tf.get_variable("W3", shape=[nLayer2, nLayer3], initializer=xavier_init(nLayer2,nLayer3)),
    'W4': tf.get_variable("W4", shape=[nLayer3, nLayer4], initializer=xavier_init(nLayer3,nLayer4)),
    'W5': tf.get_variable("W5", shape=[nLayer4, nLayer5], initializer=xavier_init(nLayer4,nLayer5))
}
b = {
    'b1': tf.Variable(tf.random_normal([nLayer1])),
    'b2': tf.Variable(tf.random_normal([nLayer2])),
    'b3': tf.Variable(tf.random_normal([nLayer3])),
    'b4': tf.Variable(tf.random_normal([nLayer4])),
    'b5': tf.Variable(tf.random_normal([nLayer5]))
}


# In[6]:

def model_myNN(_X, _W, _b, _dropout_prob):
    Layer1 = tf.nn.dropout(tf.nn.relu(tf.add(tf.matmul(_X,_W['W1']), _b['b1'])), _dropout_prob)
    Layer2 = tf.nn.dropout(tf.nn.relu(tf.add(tf.matmul(Layer1,_W['W2']), _b['b2'])), _dropout_prob)
    Layer3 = tf.nn.dropout(tf.nn.relu(tf.add(tf.matmul(Layer2,_W['W3']), _b['b3'])), _dropout_prob)
    Layer4 = tf.nn.dropout(tf.nn.relu(tf.add(tf.matmul(Layer3,_W['W4']), _b['b4'])), _dropout_prob)
    Layer5 = tf.add(tf.matmul(Layer4,_W['W5']), _b['b5'])                       
    return Layer5


# In[8]:

X = tf.placeholder(tf.float32, [None, dimX], name="input")
Y= tf.placeholder(tf.float32, [None, dimY], name="output")
dropout_prob = tf.placeholder(tf.float32, name="dropout")


# In[9]:

Y_pred = model_myNN(X, W, b, dropout_prob)


# ## Define loss function, optimizer, measurer

# We use *softmax_cross_entropy()* and *AdamOptimizer()*

# In[10]:

loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(Y_pred, Y))


# In[11]:

learning_rate = 0.001
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)
#optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)
training_epochs = 30
display_epoch = 5
batch_size = 100   # For each time, we will use 100 samples to update parameters 


# In[12]:

correct_prediction = tf.equal(tf.argmax(Y_pred, 1), tf.argmax(Y, 1))    
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))


# ## Run the session

# We use *with* for load a TF session

# In[13]:

with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())

    for epoch in range(training_epochs):
        nBatch  = int(nTrain/batch_size)
        #myIdx =  np.random.permutation(nTrain)
        for ii in range(nBatch):
            X_batch, Y_batch = mnist.train.next_batch(batch_size)
            #X_batch = X_train[myIdx[ii*batch_size:(ii+1)*batch_size],:]
            #Y_batch = Y_train[myIdx[ii*batch_size:(ii+1)*batch_size],:]
            sess.run(optimizer, feed_dict={X:X_batch, Y:Y_batch, dropout_prob:myDropProb})
          
        if (epoch+1) % display_epoch == 0:
            loss_temp = sess.run(loss, feed_dict={X: X_train, Y:Y_train, dropout_prob:1.})
            accuracy_temp = accuracy.eval({X: X_train, Y:Y_train, dropout_prob:1.})
            print "(epoch {})".format(epoch+1) 
            print "[Loss / Tranining Accuracy] {:05.4f} / {:05.4f}".format(loss_temp, accuracy_temp)
            print " "
            
    print "[Test Accuracy] ",  accuracy.eval({X: X_test, Y: Y_test, dropout_prob:1.})   

