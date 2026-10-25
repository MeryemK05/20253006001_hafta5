KOMUTLAR = {} 

def komut (ad, aciklama= ""):
    """Komutları KOMUTLAR sözlüğüne kaydeder."""

    def dekorator(fonk):
        if ad in KOMUTLAR:
            raise ValueError(f"'{ad}' adında bir komut zaten kayıtlı!")

        KOMUTLAR[ad] = (fonk, aciklama)
        return fonk

    return dekorator


@komut ("yardim", aciklama="komutları listeler")
def yardim_komutu(durum):
    satirlar=[]
    for k_ad, (_, k_aciklama) in KOMUTLAR.itmes():
        if k_aciklama:
            satirlar.append(f"{k_ad} {k_aciklama}")
        else:
            satirlar.append(k_ad)

    return "/n".join(satirlar)

@komut("envanter", aciklama="eşyalarını gösterir")
def envanter_komutu(durum):
    esyalar = []
    if durum.get("credits"):
        esyalar.append("bol kredi")
    if durum.get("engines"):
        esyalar.append("güçlü motorlar")
    if durum.get("copilot"):
        esyalar.append("yetenekli bir pilot")

    if not esyalar:
        return "Envanterin boş."
    return "Sende: "+",".join(esyalar)

@komut("harita", aciklama=" gidebileceğin gezegeni gösterir")
def harita_komutu(durum):
    baglantilar = durum.get("bağlantılar", [])
    if not baglantilar:
        return "Bağlantılı gezegen yok."
    return ", ".join(baglantilar)