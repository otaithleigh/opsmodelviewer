import enum
import os
from opsmodelviewer import Model

kinds = {
    0: 'LEFT',
    1: 'RIGHT',
    2: 'LEAN',
    3: 'BEAM',
    4: 'BRACE',
    5: 'SBACK',
    6: 'TIE',
    7: 'RIGID',
    8: 'SPRING',
}


def kind(v):
    return kinds[v]


colors = {
    'LEFT': '#a6cee3',
    'RIGHT': '#1f78b4',
    'LEAN': '#b2df8a',
    'BEAM': '#33a02c',
    'BRACE': '#fb9a99',
    'SBACK': '#e31a1c',
    'TIE': '#fdbf6f',
    'RIGID': '#ff7f00',
    'SPRING': '#cab2d6',
}

ROOT = os.path.abspath(os.path.dirname(__file__))
model = Model.from_json(os.path.join(ROOT, 'strongback.json'),
                        ['kind', 'story', 'num', 'num'], {'kind': kind},
                        colorkey='kind',
                        colormap=colors)
model.show('strongback.html')
