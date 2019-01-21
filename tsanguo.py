# coding:utf-8

import logging
import os

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger()

BASEDIR = os.path.dirname(__file__)

from sanguo.tscenes import *
from sanguo.tscenes.menuscene import MenuScene
import sanguo


if __name__ == '__main__':



    sanguo.tscenes.current_scene = MenuScene()
    while True:
        sanguo.tscenes.current_scene.run()