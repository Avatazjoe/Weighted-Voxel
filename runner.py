#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
# Originally developed by Chris Choy <chrischoy@ai.stanford.edu>
# Updated by Haozhe Xie <cshzxie@gmail.com>
# 
# CHANGELOG:
# - 2018/02/03 Remove unused args
# - 2018/02/04 Refract the code

import logging
import multiprocessing as mp
import numpy as np
import theano.gpuarray
import sys

from argparse import ArgumentParser
from pprint import pprint

from config import cfg
from core.train import train_net
from core.test import test_net

def get_args_from_command_line():
    parser = ArgumentParser(description='Parser of Runner of Weighted-Voxel')
    parser.add_argument(
        '--gpu',
        dest='gpu_id',
        help='GPU device id to use [cuda0]',
        default=cfg.CONST.DEVICE,
        type=str)
    parser.add_argument(
        '--rand', dest='randomize', help='Randomize (do not use a fixed seed)', action='store_true')
    parser.add_argument(
        '--test', dest='test', help='Test neural networks', action='store_true')
    parser.add_argument(
        '--batch-size',
        dest='batch_size',
        help='name of the net',
        default=cfg.CONST.BATCH_SIZE,
        type=int)
    parser.add_argument(
        '--iter',
        dest='iter',
        help='number of iterations',
        default=cfg.TRAIN.NUM_ITERATION,
        type=int)
    parser.add_argument(
        '--weights', dest='weights', help='Initialize network from the weights file', default=None)
    parser.add_argument('--out', dest='out_path', help='Set output path', default=cfg.DIR.OUT_PATH)
    parser.add_argument(
        '--init-iter',
        dest='init_iter',
        help='Start from the specified iteration',
        default=cfg.TRAIN.INITIAL_ITERATION)
    args = parser.parse_args()
    return args

def main():
    # Get args from command line
    args = get_args_from_command_line()
    
    if args.gpu_id is not None:
        cfg.CONST.DEVICE = args.gpu_id
    if not args.randomize:
        np.random.seed(cfg.CONST.RNG_SEED)
    if args.batch_size is not None:
        cfg.CONST.BATCH_SIZE = args.batch_size
    if args.iter is not None:
        cfg.TRAIN.NUM_ITERATION = args.iter
    if args.out_path is not None:
        cfg.DIR.OUT_PATH = args.out_path
    if args.weights is not None:
        cfg.CONST.WEIGHTS = args.weights
        cfg.TRAIN.RESUME_TRAIN = True
        cfg.TRAIN.INITIAL_ITERATION = int(args.init_iter)

    # Print config
    print('Use config:')
    pprint(cfg)

    # Set GPU to use
    theano.gpuarray.use(cfg.CONST.DEVICE)

    # Start train/test process
    if not args.test:
        train_net(cfg)
    else:
        test_net(cfg)

if __name__ == '__main__':
    # Check python version
    if (sys.version_info < (3, 0)):
        raise Exception("Please follow the installation instruction on 'https://github.com/hzxie/Weighted-Voxel'")

    # Setup logger
    mp.log_to_stderr()
    logger = mp.get_logger()
    logger.setLevel(logging.INFO)

    main()
