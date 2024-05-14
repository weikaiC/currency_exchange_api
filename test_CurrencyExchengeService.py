from main import CurrencyExchangeService, currencies


def test_source():
    """ source系統並不提供時的案例
    """
    
    currency_dependency = CurrencyExchangeService(currencies)
    currency_dependency(source='TW', target='JPY', amount='1,525')


def test_target():
    """ target系統並不提供時的案例
    """
    currency_dependency = CurrencyExchangeService(currencies)
    currency_dependency(source='TWD', target='JP', amount='1,525')


def test_amount():
    """輸入的金額為非數字或無法辨認時的案例
    """
    currency_dependency = CurrencyExchangeService(currencies)
    currency_dependency(source='TWD', target='JPY', amount='1,525a')


def test_float_amount():
    """輸入的數字有小數
    """
    currency_dependency = CurrencyExchangeService(currencies)
    target_value, amount = currency_dependency(source='TWD', target='JPY', amount='1,525.5')
    assert isinstance(amount, float)


def test_integer_amount():
    """輸入的數字沒有小數
    """
    currency_dependency = CurrencyExchangeService(currencies)
    target_value, amount = currency_dependency(source='TWD', target='JPY', amount='1,525')
    assert isinstance(amount, int)

