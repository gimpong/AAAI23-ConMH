# model
model_name = 'conmh'
use_checkpoint = None
feature_size = 2048
hidden_size = 256
max_frames = 30
nbits = 64
transformer_type = 'small'

# dataset
dataset = 'activitynet'
workers = 1
batch_size = 128
mask_prob = 0.5

# train
seed = 1
num_epochs = 505
a = 0.2
temperature = 0.5
tau_plus = 0.05
train_num_sample = 9722

# test
test_batch_size = 128
test_num_sample = 3758
query_num_sample = 1000

# optimizer
optimizer_name = 'Adam'
schedule = 'StepLR'
lr = 1e-4
min_lr = 1e-5
lr_decay_rate = 20
lr_decay_gamma = 0.9
weight_decay = 0.0

# path
data_root = '/data/dataset/activitynet/'
home_root = '/data/conmh/'

train_feat_path = [data_root + 'train_feats.h5']
test_feat_path = [data_root + 'test_feats.h5']
label_path = [data_root + 're_label.mat']
query_feat_path = [data_root + 'query_feats.h5']
query_label_path = [data_root + 'q_label.mat']

save_dir = home_root + 'saved_model/' + model_name + '_' + dataset
file_path = save_dir + '_' + str(nbits) + 'bit'
