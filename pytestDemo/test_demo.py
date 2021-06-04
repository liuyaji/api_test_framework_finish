def add(a,b):
    return a+b

def minus(a,b):
    return a-b

class TestClass:
    def test_add(self):
        assert add(2,3) == 5
    def test_minus(self):
        assert minus(3,2) == 2
