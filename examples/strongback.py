import enum
import os

import bokeh.palettes
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


# Colors are specified by hex codes. bokeh contains various palettes built-in,
# which can save you the effort of looking them up.
colors = bokeh.palettes.Category10[len(kinds)]

# The tag spec defines how your tags are structured. Each digit is assigned to
# a field; the names are not important. For example, a tag processed according
# to the spec below would have one digit assigned to `kind`, one to `story`, and
# two to `num`. So 2210 is the tag for kind 2, story 2, num 10. Missing digits
# filled with zeroes; 210 is the tag for kind 0, story 2, num 10.
tag_spec = ['kind', 'story', 'num', 'num']

# The tag mapping takes the integers parsed from the tag and applies a function
# to transform them into something else. In this case, integers are passed to
# the `kind` function, which returns a string depending on which integer was
# received. The only limitation is that the result of these mappings must be
# JSON serializable -- that is, not an object that can't be represented in text.
tag_mapping = {'kind': kind}

ROOT = os.path.abspath(os.path.dirname(__file__))
model = Model.from_json(os.path.join(ROOT, 'strongback.json'),
                        spec=tag_spec,
                        mapping=tag_mapping,
                        colorkey='kind',
                        palette=colors)
model.show(os.path.join(ROOT, 'strongback.html'))
