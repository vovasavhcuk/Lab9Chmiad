from ctypes import Array
from typing import List, Any

from Actor import Actor
import collections


class ActorList:
    actorList = []

    def add(self, actor: Actor):
        self.actorList.append(actor.copy())

    def delete(self):
        self.actorList.pop()

    def __str__(self):
        for x in self.actorList:
            print(x[0], x[1])


