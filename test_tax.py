from tax_calc import cal_tax

def test_one_tax():
    assert cal_tax(5000) == 0

def test_two_tax():
    assert cal_tax(23500) == (20/100)

def test_three_tax():
    assert cal_tax(43000) == (0.4)
