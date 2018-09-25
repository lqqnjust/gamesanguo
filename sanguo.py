# coding:utf-8
import logging
import os

from cocos.director import director
from sanguo.scenes.menu_scene import MenuScene
from sanguo.scenes.battle_scene import BattleScene

import pyglet

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger()

BASEDIR = os.path.dirname(__file__)


if __name__ == '__main__':

    pyglet.resource.path = [os.path.join(BASEDIR,'sanguo/resource'),os.path.join(BASEDIR,'sanguo/resource/smallbattle')]

    pyglet.resource.reindex()
    director.init(width=800,height=600)



    scene = BattleScene()
    # scene = MenuScene()

    director.run(scene)
