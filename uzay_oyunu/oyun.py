from uzay_oyunu.dekoratorler import log_cagri, sinirla, sure_olc
from uzay_oyunu.komutlar import KOMUTLAR

@sure_olc 
def rota_sayaci(adim):
    """Hafta 4'teki önbelleksiz rota sayacı simülasyonu"""
    toplam = 0
    for i in range(adim * 100000):
        toplam += i
    return toplam

@log_cagri
def hedef_menusu(gezegenler):
    return[f"[{i+1}] {g}" for i, g in enumerate(gezegenler)]

@sinirla(0, 100)
def yakit_harca(miktar, mevcut_yakit=100):
    return mevcut_yakit - miktar

def travel(durum):
    print("Mereye gitmek istersin?")
    for secenek in hedef_menusu(durum["baglantilar"]):
        print(secenek)

    while True:
        girdi = input("> ").strip().lower()

        if girdi in KOMUTLAR:
            islem_fn, _ = KOMUTLAR[girdi]
            cikti = islem_fn(durum)
            print(cikti)
            print("Nereye gitmek istersin?")
            for secenek in hedef_menusu(durum["baglantilar"]):
                print(secenek)
        elif girdi in durum["baglantilar"]:
            durum["konum"] = girdi
            print(f"{girdi} gezegenine seyehat edildi.")
            break
        else:
            print("Geçersiz komut veya gezegen!")

            