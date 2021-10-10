# -*-coding:utf-8-*-


import logging
import os
import re
import shutil
import platform
import subprocess
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s][%(levelname)s]%(filename)s[%(lineno)d]:  %(message)s', datefmt='%d/%b/%Y %H:%M:%S')

g_config = {'src_dir': 'origin/', 'dst_dir': 'show/'}


def get_config() -> dict:
    config = g_config
    if config['dst_dir'] in ['', './']:
        logging.error('dst_dir must have its own dir!')
        exit(-1)
    config['work_abs_path'] = os.getcwd()
    return config


def get_file_list(config: dict) -> list:
    file_list = []
    for root, _, files in os.walk(config['src_dir']):
        for file in files:
            sub_path = os.path.join(root, file)
            abs_path = os.path.join(config['work_abs_path'], sub_path)
            file_list.append(abs_path)
    return file_list


def get_file_key(file_list: list) -> dict:
    file_dict = {}
    for f in file_list:
        fd = open(f, 'r', encoding='utf-8')
        code = fd.read()
        g = re.search(r'[\s]+关键字[\s]+(.*)', code)
        if None != g:
            file_dict[f] = g.group(1).split(' ')
        else:
            file_dict[f] = ['']

        fd.close()
    return file_dict


def gen_key_dict(file_dict: dict) -> dict:
    key_dict = {}

    for k, v in file_dict.items():
        for key in v:
            if key == '':
                key = '未分类'
            if key not in key_dict:
                key_dict[key] = [k]
            else:
                key_dict[key].append(k)
    return key_dict


def gen_temp_dir(config, key_dict: dict) -> None:

    abs_dst_dir = os.path.join(config['work_abs_path'], config['dst_dir'])
    shutil.rmtree(abs_dst_dir, ignore_errors=True)
    os.mkdir(abs_dst_dir)

    for k, file_list in key_dict.items():
        os.chdir(abs_dst_dir)
        os.mkdir(k)
        os.chdir(k)
        for file_path in file_list:

            sys_str = platform.system()
            if sys_str == "Windows":
                # Windows
                logging.error('not support windows')
#               shutil.copyfile(file_path, os.path.basename(file_path))
            elif sys_str == "Linux":
                # Linux
                subprocess.run(['ln', file_path, os.path.basename(file_path)])
            else:
                logging.error(f'unknow system[{sys_str}]')


g_config = get_config()

file_list = get_file_list(g_config)

file_dict = get_file_key(file_list)

key_dict = gen_key_dict(file_dict)

gen_temp_dir(g_config, key_dict)
