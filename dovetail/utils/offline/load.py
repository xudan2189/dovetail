#!/usr/bin/env python

import os
import yaml

import dovetail.utils.dovetail_utils as dt_utils


class load(object):
    def __init__(self):
        self.curr_path = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(self.curr_path, 'config.yaml')) as f:
            self.config = yaml.safe_load(f)

    def main(self):
        keys = self.config.keys()
        if 'docker_save_path' in keys:
            save_path = self.config['docker_save_path']
        else:
            save_path = self.curr_path
        if 'docker_images' in keys:
            for key, value in self.config['docker_images'].items():
                if value is not None:
                    name = self.config['docker_images'][key]['store_name']
                    image_save_path = ''.join([save_path, name])
                    if os.path.isfile(image_save_path):
                        cmd = 'sudo docker load -i %s' % (image_save_path)
                        dt_utils.exec_cmd(cmd)
                    else:
                        print "file %s not exists" % image_save_path


if __name__ == '__main__':
    load = load()
    load.main()
