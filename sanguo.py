# coding:utf-8
import logging

from cocos.director import director
from sanguo.scenes.menu_scene import MenuScene


FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('tcpserver')



if __name__ == '__main__':
    director.init()
    scene = MenuScene()
    director.run(scene)
