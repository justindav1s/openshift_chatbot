import tflearn
import tensorflow as tf
import cb_utils
import json

words = cb_utils.loadFromFile('words.csv')
classes = cb_utils.loadFromFile('classes.csv')

# reset underlying graph data
tf.reset_default_graph()
# Build neural network
net = tflearn.input_data(shape=[None, len(words)])
net = tflearn.fully_connected(net, cb_utils.nn_width)
net = tflearn.fully_connected(net, cb_utils.nn_width)
net = tflearn.fully_connected(net, len(classes), activation='softmax')
net = tflearn.regression(net)

# Define model and setup tensorboard
model = tflearn.DNN(net)
model.load('models/airline_chatbot_model.tflearn')

cb_utils.predictThis(model, 'are you open')
cb_utils.predictThis(model, 'you open')
cb_utils.predictThis(model, 'when do you open')
cb_utils.predictThis(model, 'what time do you open')
cb_utils.predictThis(model, 'what can I hire from you')
cb_utils.predictThis(model, 'I would like a flight to New York please.')
cb_utils.predictThis(model, 'like York flight I would a to New please.')