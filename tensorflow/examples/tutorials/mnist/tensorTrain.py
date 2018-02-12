'''
/****************************************Copyright (c)**************************************************
**                                        ICT
**
**---------------------------------------File Info-----------------------------------------------------
** File name:           train
** Last modified Date:  xx-xx-xx
** Last Version:        1.0
** Descriptions:        xxxxxxxxxxxxxxxxxx
**------------------------------------------------------------------------------------------------------
** Created by:          xiaohang
** Created date:        2017-11-30 18:00:21
** Version:             1.0
** Descriptions:        train tensorflow script
** params:              --trainfile,--input_data_dir,--log_dir
**
**------------------------------------------------------------------------------------------------------
** Modified by:         user-name
** Modified date:        x-x-x    
** Version:             1.0
** Descriptions:        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
**
**------------------------------------------------------------------------------------------------------
********************************************************************************************************/
'''

import os
import argparse
import time

def main():
    currentTime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    currenLogDir=args.log_dir+'/'+currentTime
    currenrLog=args.log_dir+'/'+currentTime+'.log'
    os.system('mkdir '+args.log_dir)
    os.system('python '+args.trainfile+' --input_data_dir=' + args.data_dir+' --log_dir='+currenLogDir + ' $@ 2>&1 | tee '+currenrLog)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--trainfile',
        type=str,
        default=None,
        help='Tensorflow training file.'
    )
    parser.add_argument(
        '--data_dir',
        type=str,
        default=None,
        help='Directory to put the input data.'
    )
    parser.add_argument(
        '--log_dir',
        type=str,
        default=None,
        help='Directory to put the log data.'
    )
    args = parser.parse_args()
    Dargs= vars(args)
    if None in Dargs.values():
       print 'Invalid params'
       print 'params: please input 3 params'
    else:
        main()
