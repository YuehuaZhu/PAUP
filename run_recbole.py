# @Time   : 2022/04/05
# @Author : Yuehua Zhu
# @Email  : yhzhu.vip@gmail.com



import argparse
from recbole.quick_start import run_recbole


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', '-m', type=str, default='PAUP', help='name of models')
    parser.add_argument('--dataset', '-d', type=str, default='ml-1m', help='name of datasets')
    parser.add_argument('--config_files', type=str, default='./recbole/properties/dataset/ml-1m.yaml', help='config files')

    args, _ = parser.parse_known_args()

    config_file_list = args.config_files.strip().split(' ') if args.config_files else None
    run_recbole(model=args.model, dataset=args.dataset, config_file_list=config_file_list)
