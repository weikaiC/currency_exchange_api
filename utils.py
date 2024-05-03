from typing import Union

def real_round(num: float, ndigits: int = 0) -> Union[float, int]:
    """ 嚴格定義上的四捨五入，解決 Python 內建 round(2.5)==2 的問題
    """
    if ndigits == 0:
        return int(num + 0.5)
    digit_value = 10 ** ndigits
    return int(num * digit_value + 0.5) / digit_value