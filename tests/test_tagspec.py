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


def test_create_basic_tag():
    tagspec = TagSpec('aabbc')
    tag = tagspec.create_tag(a=20, b=10, c=4)
    assert tag == 20104


def test_create_short_tag():
    tagspec = TagSpec('aabbc')
    tag = tagspec.create_tag(a=0, b=10, c=4)
    assert tag == 104
