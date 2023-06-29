from tax_calc import cal_tax

def test_one_tax():
    assert cal_tax(5000) == 0
