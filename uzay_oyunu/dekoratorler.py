import time
from functools import wraps

def sure_olc(fonk):
    """Fonksiyonun çalışma süresini time.perf_counter ile ölçer."""

    @wraps(fonk)
    def sarmal(*args, **kwargs):
        baslangic = time.perd_counter()
        sonuc = fonk(*args, *kwargs)
        bitis = time.perf_counter()
        gece = bitis - baslangic
        print(f"{fonk.__name__}: {gece:.4f} sn")
        return sonuc
    return sarmal

def say(fonk):
    """"Fonkisyonun toplam çağrı sayısını çağrı sayı niteliğinde saklar"""

    @wraps(fonk)
    def sarmal(*args, **kwargs):
        sarmal.cagri +=1
        return fonk (*args, **kwargs)

    sarmal.cagri = 0
    return sarmal

def log_cagri(fonk):
    """Çağrı öncesi parametreleri, çağrı sonrası dönüş değerini yazdırır."""

    @wraps(fonk)
    def sarmal(*args, **kwargs):
        konumsal = [repr(a) for a in args]
        isimli = [f"{k}={v!r}" for k, v in kwargs.items()]
        param_metni = ", ".join(konumsal + isimli)

        print(f" -> {fonk.__name__}({param_metni})")
        sonuc = fonk(*args, **kwargs)
        print(f"<<- {fonk._name__} {sonuc!r}")
        return sonuc

    return sarmal

def sinirla(alt,ust):
    """İki parametrenin [alt, ust] aralığında olup olmadığını denetler."""

    def dekorator(fonk):
        @wraps(fonk)
        def sarmal(*args, **kwargs):
            if not args:
                raise ValueError("En az bir parametre verilmelidir.")

            deger = args[0]
            if not (alt <= deger <= ust):
                raise ValueError (
                    f"{fonk.__name__}: {deger} değeri {alt}-{ust} aralığında değil"
                )
            return fonk(*args, **kwargs)

        return sarmal

    return dekorator

def hafiza (maxsize=None):
    """Cloosure kullanarak çalışan önbellekleme (cachinh) dekoratörü."""

    def dekorator(fonk):
        cache = {}

        @wraps(fonk)
        def sarmal(*args, **kwargs):
            anahtar = (args, tuple(sorted(kwargs.items())))

            if anahtar in cache:
                return cache [anahtar]

            sonuc = fonk(*args, *kwargs)

            if maxsize is not None and len(cache) >= maxsize:
                en_eski = next(iter(cache))
                del cache[en_eski]

            cache[anahtar] = sonuc
            return sonuc

        sarmal.cache = cache
        return sarmal

    return dekorator    