import enum
from opsmodelviewer import TagSpec


def test_basic_tag():
    tagspec = TagSpec('aabbc')
    ptag = tagspec.process_tag(20104)
    assert ptag.a == 20
    assert ptag.b == 10
    assert ptag.c == 4


def test_short_tag():
    tagspec = TagSpec('aabbc')
    ptag = tagspec.process_tag(104)
    assert ptag.a == 0
    assert ptag.b == 10
    assert ptag.c == 4


def test_enum_tag():
    class TagKind(enum.Enum):
        COLUMN = 0
        BEAM = 1
        BRACE = 2
    tagspec = TagSpec('aabbc', mapping={'a': TagKind})
    ptag = tagspec.process_tag(104)
    assert ptag.a == TagKind.COLUMN
    assert ptag.b == 10
    assert ptag.c == 4
