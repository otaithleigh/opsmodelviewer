import enum
import os
from opsmodelviewer import Model


class Kind(enum.Enum):
    LEFT = 0
    RIGHT = 1
    LEAN = 2
    BEAM = 3
    BRACE = 4
    SBACK = 5
    TIE = 6
    RIGID = 7
    SPRING = 8


colors = {
    Kind.LEFT: '#a6cee3',
    Kind.RIGHT: '#1f78b4',
    Kind.LEAN: '#b2df8a',
    Kind.BEAM: '#33a02c',
    Kind.BRACE: '#fb9a99',
    Kind.SBACK: '#e31a1c',
    Kind.TIE: '#fdbf6f',
    Kind.RIGID: '#ff7f00',
    Kind.SPRING: '#cab2d6',
}

ROOT = os.path.abspath(os.path.dirname(__file__))
model = Model.from_json(os.path.join(ROOT, 'StrongbackFrameModel.json'),
                        ['kind', 'story', 'num', 'num'], {'kind': Kind},
                        colorkey='kind',
                        colormap=colors)
model.show('model.html')
