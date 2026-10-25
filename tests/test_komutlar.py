from uzay_oyunu.komutlar import (
    KOMUTLAR,
    envanter_komutu,
    harita_komutu,
    komut,
    yardim_komutu,
)

def test_komut_kayit_ve_cakisma():
    @komut("test_cmd", aciklama="test")
    def ornek(d):
        return "ok"

    assert "test_cmd" in KOMUTLAR

    with pytest.raises(ValueError):

        @komut("test_cmd")
        def ornek_ikinci(d):
            pass

def test_yardim_komutu():
    res = yardim_komutu({})
    assert "yardim" in res

def test_envanter_komutu():
    durum={"credits": True, "copilot": True }
    res = envanter_komutu(durum)
    assert "bol kredi" in res and "yetenekli bir pilot" in res


def test_harita_komutu():
    durum = {"baglantilar": ["orion", "dünya"]}
    res = harita_komutu(durum)
    assert "orion, dünya" in res