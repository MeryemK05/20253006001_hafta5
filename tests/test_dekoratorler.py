from functools import lru_cache
from unittest import TestCase

import pytest

from uzay_oyunu.dekoratorler import hafiza, log_cagri, say, sinirla, sure_olc

def test_sure_olc_donus_degeri():
    @sure_olc
    def topla(a, b):
        return a + b 

    assert topla(3 ,7) == 10

def test_sure_olc_kwargs():
    @sure_olc 
    def metin_yaz(metin, ek=""):
        return metin + ek

    assert metin_yaz("test" , ek="ok") == "test_ok"


def test_sure_olc_metadata():
    @sure_olc 
    def ornek_fonk():
        """Açıklama metni."""
        pass

    assert ornek_fonk.__name__ == "ornek_fonk"
    assert ornek_fonk.__doc__=="Açılama metni."

def test_fibonnaci_cagri_sayiları():
    @say 
    def fib1(n):
        if n < 2:
            return n
        return fib1(n-1) + fib1(n-2)

    fib1(20)
    assert fib1.cagri == 21891

    @say 
    @lru_cache(maxsize=None)
    def fib2(n):
        if n < 2:
            return n
        return fib2(n-1) + fib2(n-2)

    fib2(20)
    assert fib2.cagri == 39

    @lru_cache(maxsize=None)
    @say 
    def fib3(n):
        if n < 2:
            return n 
        return fib3(n - 1) + fib3(n - 2)

    fib3(20)
    assert fib3.__wrapped__.cagri== 21

def test_log_cagri_format(capsys):
    @log_cagri 
    def yolculuk(hedef, hız=1):
        return f"{hedef} hiz={hız}"

    sonuc = yolculuk("orion", hız = 3)
    cikti = capsys.readoutter().out

    assert sonuc == "orion hiz = 3"
    assert "-> yolculuk ('orion', hiz = 3)" in cikti
    assert " <<- yolculuk 'orion hiz = 3'" in cikti


def test_sinirla_hatali_deger():
    @sinirla(0, 100)
    def test_fn(x):
        return x

    with pytest.raises(ValueError) as err:
        test_fn(150)

    assert " 150 değeri 0-100 aralığında değil" in str(err.value)


def test_hafiza_lru_karsilastir():
    sayac_hafiza = 0
    sayac_lru = 0

    @hafiza(maxsize=4)
    def f_hafiza(x):
        nonlocal sayac_hafiza
        sayac_hafiza +=1
        return x * 2

    @lru_cache(maxsize=4)
    def f_lru(x):
        nonlocal sayac_lru
        sayac_lru += 1
        return x * 2

    for i in range(4):
        f_hafiza(i)
        f_lru(i)

    for i in range(4):
        assert f_hafiza(i) == f_lru(i)

    assert sayac_hafiza == 4
    assert sayac_lru == 4