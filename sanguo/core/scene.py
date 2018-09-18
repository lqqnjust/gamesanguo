# coding:utf-8

from .view import View


class Scene(View):
    """A view that takes up the entire window content area."""

    def __init__(self, width=800, height=600):
        View.__init__(self,width, height)

