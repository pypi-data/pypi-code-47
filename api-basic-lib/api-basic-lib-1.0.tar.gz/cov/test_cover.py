from cov.cau import cau
class Test_cover:
    def test_add1(self):
        a=cau(1,2,3)
        assert a==5
    def test_add2(self):
       a = cau(2, 2, 3)
       assert a == -1
    def test_add0(self):
       a = cau(0, 2, 3)
       assert a == 6