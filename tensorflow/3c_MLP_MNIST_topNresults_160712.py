
# coding: utf-8

# \* *[Notice] I wrote thie code while following the examples in [Choi's Tesorflow-101 tutorial](https://github.com/sjchoi86/Tensorflow-101). And,  as I know, most of Choi's examples originally come from [Aymeric Damien's](https://github.com/aymericdamien/TensorFlow-Examples/) and  [Nathan Lintz's ](https://github.com/nlintz/TensorFlow-Tutorials) tutorials.*

# ## 3. Multilayer Perceptron with MNIST data

# In[1]:

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
#%matplotlib inline  


# ### Load MNIST data

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


# ## Define my neural network structure

# In[4]:

nLayer0 = dimX
nLayer1 = 256
nLayer2 = 256
nLayer3 =  dimY
sigma_init = 0.1   # For randomized initialization


# In[5]:

W = {
    'W1': tf.Variable(tf.random_normal([nLayer0, nLayer1], stddev = sigma_init)),
    'W2': tf.Variable(tf.random_normal([nLayer1, nLayer2], stddev = sigma_init)),
    'W3': tf.Variable(tf.random_normal([nLayer2, nLayer3], stddev = sigma_init))
}
b = {
    'b1': tf.Variable(tf.random_normal([nLayer1])),
    'b2': tf.Variable(tf.random_normal([nLayer2])),
    'b3': tf.Variable(tf.random_normal([nLayer3]))
}


# In[6]:

def model_myNN(_X, _W, _b):
    Layer1 = tf.nn.sigmoid(tf.add(tf.matmul(_X,_W['W1']), _b['b1']))
    Layer2 = tf.nn.sigmoid(tf.add(tf.matmul(Layer1,_W['W2']), _b['b2']))
    Layer3 = tf.add(tf.matmul(Layer2,_W['W3']), _b['b3'])    
    #Layer3 = tf.nn.sigmoid(tf.add(tf.matmul(Layer2,_W['W3']), _b['b3']))
    return Layer3


# In[7]:

X = tf.placeholder(tf.float32, [None, dimX], name="input")
Y= tf.placeholder(tf.float32, [None, dimY], name="output")


# In[8]:

Y_pred = model_myNN(X, W, b)


# ### Define loss function, optimizer, measurer

# We use *softmax_cross_entropy()* and *AdamOptimizer()*

# In[9]:

loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(Y_pred, Y))


# In[10]:

learning_rate = 0.001
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)
# optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)
training_epochs = 10
display_epoch = 1
batch_size = 100   # For each time, we will use 100 samples to update parameters 


# ### Evaluation - Top1, Top2, Top3

# In[11]:

correct_prediction = tf.equal(tf.argmax(Y_pred, 1), tf.argmax(Y, 1))    
accuracy0 = tf.reduce_mean(tf.cast(correct_prediction, "float"))


# In[12]:

accuracy1 = tf.reduce_mean(tf.cast(tf.nn.in_top_k(Y_pred,tf.argmax(Y, 1), k=1), "float"))
accuracy2 = tf.reduce_mean(tf.cast(tf.nn.in_top_k(Y_pred,tf.argmax(Y, 1), k=2), "float"))
accuracy3 = tf.reduce_mean(tf.cast(tf.nn.in_top_k(Y_pred,tf.argmax(Y, 1), k=3), "float"))


# In[13]:

is_top1 = tf.equal(tf.nn.top_k(Y_pred, k=1)[1][:,0], tf.cast(tf.argmax(Y, 1), "int32"))
is_top2 = tf.equal(tf.nn.top_k(Y_pred, k=2)[1][:,1], tf.cast(tf.argmax(Y, 1), "int32"))
is_top3 = tf.equal(tf.nn.top_k(Y_pred, k=3)[1][:,2], tf.cast(tf.argmax(Y, 1), "int32"))
is_in_top1 = is_top1
is_in_top2 = tf.logical_or(is_in_top1, is_top2)
is_in_top3 = tf.logical_or(is_in_top2, is_top3)
                   
accuracy11 = tf.reduce_mean(tf.cast(is_in_top1, "float"))
accuracy22 = tf.reduce_mean(tf.cast(is_in_top2, "float"))
accuracy33 = tf.reduce_mean(tf.cast(is_in_top3, "float"))


# ### Run the session

# We use *with* for load a TF session

# In[14]:

# Because of the memory allocation problem in evaluation
divide_train = 45;
divide_test = 5;
nTrainSub = (int)(nTrain/divide_train);
nTestSub = (int)(nTest/divide_test);


# In[15]:

with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())

    for epoch in range(training_epochs):
        nBatch  = int(nTrain/batch_size)
        myIdx =  np.random.permutation(nTrain)
        for ii in range(nBatch):
            X_batch = X_train[myIdx[ii*batch_size:(ii+1)*batch_size],:]
            Y_batch = Y_train[myIdx[ii*batch_size:(ii+1)*batch_size],:]
            #print X_batch.shape, Y_batch.shape
            sess.run(optimizer, feed_dict={X:X_batch, Y:Y_batch})
          
        if (epoch+1) % display_epoch == 0:
            # Because of the memory allocation problem in evaluation
            loss_temp = accuracy0_train_temp = accuracy0_test_temp = 0
            accuracy1_train_temp = accuracy1_test_temp = 0
            accuracy2_train_temp = accuracy2_test_temp = 0
            accuracy3_train_temp = accuracy3_test_temp = 0
            accuracy11_train_temp = accuracy11_test_temp = 0
            accuracy22_train_temp = accuracy22_test_temp = 0
            accuracy33_train_temp = accuracy33_test_temp = 0
            
            for jj in range(divide_train):
                myIdx1 = jj*nTrainSub
                myIdx2 = (jj+1)*nTrainSub
                loss_temp += sess.run(loss, feed_dict={X: X_train[myIdx1:myIdx2,:], Y:Y_train[myIdx1:myIdx2,:]})
                accuracy0_train_temp += accuracy0.eval({X: X_train[myIdx1:myIdx2,:], Y:Y_train[myIdx1:myIdx2,:]})
                accuracy1_train_temp += accuracy1.eval({X: X_train[myIdx1:myIdx2,:], Y:Y_train[myIdx1:myIdx2,:]})
                accuracy2_train_temp += accuracy2.eval({X: X_train[myIdx1:myIdx2,:], Y:Y_train[myIdx1:myIdx2,:]})
                accuracy3_train_temp += accuracy3.eval({X: X_train[myIdx1:myIdx2,:], Y:Y_train[myIdx1:myIdx2,:]})
                accuracy11_train_temp += accuracy11.eval({X: X_train[myIdx1:myIdx2,:], Y:Y_train[myIdx1:myIdx2,:]})
                accuracy22_train_temp += accuracy22.eval({X: X_train[myIdx1:myIdx2,:], Y:Y_train[myIdx1:myIdx2,:]})
                accuracy33_train_temp += accuracy33.eval({X: X_train[myIdx1:myIdx2,:], Y:Y_train[myIdx1:myIdx2,:]})

            for kk in range(divide_test):
                myIdx1 = kk*nTestSub
                myIdx2 = (kk+1)*nTestSub
                accuracy0_test_temp += accuracy0.eval({X: X_test[myIdx1:myIdx2,:], Y: Y_test[myIdx1:myIdx2,:]}) 
                accuracy1_test_temp += accuracy1.eval({X: X_test[myIdx1:myIdx2,:], Y:Y_test[myIdx1:myIdx2,:]})
                accuracy2_test_temp += accuracy2.eval({X: X_test[myIdx1:myIdx2,:], Y:Y_test[myIdx1:myIdx2,:]})
                accuracy3_test_temp += accuracy3.eval({X: X_test[myIdx1:myIdx2,:], Y:Y_test[myIdx1:myIdx2,:]})
                accuracy11_test_temp += accuracy11.eval({X: X_test[myIdx1:myIdx2,:], Y:Y_test[myIdx1:myIdx2,:]})
                accuracy22_test_temp += accuracy22.eval({X: X_test[myIdx1:myIdx2,:], Y:Y_test[myIdx1:myIdx2,:]})
                accuracy33_test_temp += accuracy33.eval({X: X_test[myIdx1:myIdx2,:], Y:Y_test[myIdx1:myIdx2,:]})
            print "(epoch {})".format(epoch+1) 
            print "[Loss / Tranin / Test] {:05.4f} / {:05.4f} / {:05.4f}".format(loss_temp/divide_train, accuracy0_train_temp/divide_train, accuracy0_test_temp/divide_test)
            print "[in_top_k: 1] [Train / Test] {:05.4f} / {:05.4f}".format(accuracy1_train_temp/divide_train, accuracy1_test_temp/divide_test)
            print "[in_top_k: 2] [Train / Test] {:05.4f} / {:05.4f}".format(accuracy2_train_temp/divide_train, accuracy2_test_temp/divide_test)
            print "[in_top_k: 3] [Train / Test] {:05.4f} / {:05.4f}".format(accuracy3_train_temp/divide_train, accuracy3_test_temp/divide_test)
            print "[top_k: 1] [Train / Test] {:05.4f} / {:05.4f}".format(accuracy11_train_temp/divide_train, accuracy11_test_temp/divide_test)
            print "[top_k: 2] [Train / Test] {:05.4f} / {:05.4f}".format(accuracy22_train_temp/divide_train, accuracy22_test_temp/divide_test)
            print "[top_k: 3] [Train / Test] {:05.4f} / {:05.4f}".format(accuracy33_train_temp/divide_train, accuracy33_test_temp/divide_test)
            print "[Test accuracy1] ",  accuracy1.eval({X: X_test, Y: Y_test})   
            print " "
    
    print "[Test accuracy1] ",  accuracy1.eval({X: X_test, Y: Y_test})   

