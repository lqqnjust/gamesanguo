# coding:utf-8
from sanguo.core.engine import Game
from sanguo.scenes import MenuScene


if __name__ == '__main__':
    game = Game(800, 600, 60, "三国")
    scene = MenuScene()
    game.set_scene(scene)
    game.run()