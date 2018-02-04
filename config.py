#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
# Originally developed by Chris Choy <chrischoy@ai.stanford.edu>
# Updated by Haozhe Xie <cshzxie@gmail.com>
# 
# CHANGELOG:
# - 2018/01/10 Add option: DATASET.MIN_VOXEL_VALUE 
# - 2018/01/20 Add option: TRAIN.DYNAMIC_LR_ITERATION 
# - 2018/02/04 Remove unused config items


from easydict import EasyDict as edict

__C = edict()
# Consumers can get config by:
#   from fast_rcnn_config import cfg
cfg = __C

#
# Common
#
__C.CONST                           = edict()
__C.CONST.DEVICE                    = 'cuda0'
__C.CONST.RNG_SEED                  = 0
__C.CONST.IMG_W                     = 127
__C.CONST.IMG_H                     = 127
__C.CONST.N_VOX                     = 32
__C.CONST.N_GRU_VOX                 = 4
__C.CONST.N_VIEWS                   = 5
__C.CONST.BATCH_SIZE                = 20
__C.CONST.WEIGHTS                   = ''         # When set, load the weights from the file
__C.CONST.MIN_VOXEL_VALUE           = -53

#
# Directories
#
__C.DIR = edict()
__C.DIR.DATASET_TAXONOMY_FILE_PATH  = './datasets/ShapeNet.json'
__C.DIR.DATASET_QUERY_PATH          = './datasets/ShapeNet/ShapeNetVox32/'
__C.DIR.VOXEL_PATH                  = './datasets/ShapeNet/ShapeNetVox32/%s/%s/model.binvox'
__C.DIR.RENDERING_PATH              = './datasets/ShapeNet/ShapeNetRendering/%s/%s/rendering'
__C.DIR.OUT_PATH                    = './output'

#
# Training
#
__C.TRAIN                           = edict()
__C.TRAIN.RESUME_TRAIN              = False
__C.TRAIN.INITIAL_ITERATION         = 0         # when the training resumes, set the iteration number
__C.TRAIN.DATASET_PORTION           = [0, .8]
## Data worker
__C.TRAIN.NUM_WORKER                = 1         # number of data workers
__C.TRAIN.NUM_ITERATION             = 20000     # maximum number of training iterations
__C.TRAIN.NUM_RENDERING             = 24
__C.TRAIN.NUM_VALIDATION_ITERATIONS = 24
__C.TRAIN.VALIDATION_FREQ           = 500
__C.TRAIN.NAN_CHECK_FREQ            = 1000
__C.TRAIN.RANDOM_NUM_VIEWS          = True      # feed in random # views if n_views > 1
__C.TRAIN.QUEUE_SIZE                = 15        # maximum number of minibatches that can be put in a data queue
## Data augmentation
__C.TRAIN.RANDOM_CROP               = True
__C.TRAIN.PAD_X                     = 10
__C.TRAIN.PAD_Y                     = 10
__C.TRAIN.FLIP                      = True
__C.TRAIN.NO_BG_COLOR_RANGE         = [[225, 255], [225, 255], [225, 255]]
## Learning
__C.TRAIN.DEFAULT_LEARNING_RATE     = 1e-5      # for SGD use 0.1, for ADAM, use 1e-5
__C.TRAIN.POLICY                    = 'adam'    # available options: sgd, adam
__C.TRAIN.LEARNING_RATES            = {}		# example: {'250': 7.5e-6, '500': '5e-6'}
__C.TRAIN.MOMENTUM                  = .9
__C.TRAIN.DYNAMIC_LR_ITERATION      = 500       # the interation number that uses the policy to adjust learning rate
__C.TRAIN.WEIGHT_DECAY              = 5e-6
__C.TRAIN.LOSS_LIMIT                = 3000      # stop training if the loss exceeds the limit
__C.TRAIN.SAVE_FREQ                 = 1000     # weights will be overwritten every save_freq
__C.TRAIN.PRINT_FREQ                = 50

#
# Testing options
#
__C.TEST                            = edict()
__C.TEST.EXP_NAME                   = 'test'
__C.TEST.DATASET_PORTION            = [.8, 1]
__C.TEST.NO_BG_COLOR_RANGE          = [[240, 240], [240, 240], [240, 240]]
__C.TEST.VOXEL_THRESH               = [5e-14]
