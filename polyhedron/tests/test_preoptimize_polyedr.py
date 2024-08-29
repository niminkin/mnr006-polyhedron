from preoptimize.polyedr import Polyedr

class TestPolyedr:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.s = Polyedr()

    # Сумма длин "плохих" рёбер вычисляется корректно
    def test_cube(self):
        poly = Polyedr(f"data/cube.geom")
        assert poly.good_edges_length() == 120
    
    def test_twofacets1(self):
        poly = Polyedr(f"data/ccc.geom")
        assert poly.good_edges_length() == 40

    def test_twofacets2():
        poly = Polyedr(f"data/ccc2.geom")
        assert poly.good_edges_length() == 0

    def test_box(self):
        poly = Polyedr(f"data/box.geom")
        assert poly.good_edges_length() == 26