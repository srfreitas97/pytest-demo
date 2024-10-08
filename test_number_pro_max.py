from number_pro_max import NumberProMax


def test_is_odd():
    odd_number = NumberProMax(1)
    even_number = NumberProMax(2)
    assert odd_number.is_odd()
    assert not even_number.is_odd()