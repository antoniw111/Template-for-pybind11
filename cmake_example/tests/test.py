import cmake_example as m

def test_add():
    assert m.__version__ == "0.0.1"
    assert m.add(1, 2) == 3
    assert m.add(-1, 1) == 0