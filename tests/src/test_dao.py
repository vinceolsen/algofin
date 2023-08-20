from ...algofin.src.dao import Dao, Price


def test_it_gets_all_symbols():
    symbols = Dao().get_all_symbols()
    assert symbols == {'QQQ', 'RITM'}


def test_it_loads_a_pricing_file():
    prices = Dao().load_csv('RITM')
    assert len(prices) == 2544
    assert len(prices[0]) == 6
    assert prices[0] == Price(symbol='RITM', date='2013-05-02', open=14.0, high=14.0, low=13.0, close=13.52)
    assert prices[-1] == Price(symbol='RITM', date='2023-06-08', open=8.88, high=8.96, low=8.81, close=8.92)


def test_it_loads_all_pricing_data():
    pricing_data = Dao().load_all_pricing_data()
    assert len(pricing_data) == 2