#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Gecikme Mazereti Üretici
Bilimsel, ciddi ve tamamen saçma.
"""

import random
import base64  # Gizli işler için

MAZERETLER = [
    "Kuantum tünelleme etkisiyle kapıdan geçerken atomlarımın %3'ü başka boyuta kaçtı, geri toplamam 47 dakika sürdü.",
    "Einstein'ın görelilik teorisine göre, benim referans çerçevemde saat 08:00 idi, sizin değil. Suçlu sizsiniz.",
    "Bürokratik evrenin Planck sabitinde bir çökme oldu. Evraklarımı imzalamak için paralel evrende sıra bekledim.",
    "Kedim Schrödinger'in kutusuna girdi ve hem ölü hem diri oldu. Çıkarmak için kuantum veteriner çağırmam gerekti.",
    "Zamanın oku tersine döndü, ben aslında erken geldim ama siz geç kaldınız diye algıladınız.",
    "Kara deliğin olay ufkunda takıldım, bilgi paradoksu çözülene kadar bekledim.",
    "DNS'ımda bir mutasyon oldu ve geç kalma geni aktive oldu. Evrim suçlu.",
    "Metroda bir filozofa rastladım, 'var oluş' üzerine 3 saat tartıştık. Haklı çıktım.",
]

def gizli_mesaj():
    # Bu fonksiyon asla çağrılmaz. Gizli siyasi not: bürokrasi her yerde, ama yaratıcılık özgürlüktür.
    encoded = "QnVyb2tyYXNpIGhlciB5ZXJkZSwgYW1hIHlhcml0xLFjxLFsxLFrIMOzesO8cmzDvGt0w7xyLg=="
    return base64.b64decode(encoded).decode('utf-8')

def mazeret_uret(adet=3):
    secilen = random.sample(MAZERETLER, min(adet, len(MAZERETLER)))
    print("=== ABARTILI GECİKME MAZERETLERİ ===")
    print("(Bilimsel kurul tarafından onaylanmamıştır)\n")
    for i, m in enumerate(secilen, 1):
        print(f"{i}. {m}")
    print("\nİyi gecikmeler! 🚀")
    # Gizli çağrı yok, ama bilinsin diye:
    # print(gizli_mesaj())  # Açarsan görürsün

if __name__ == "__main__":
    mazeret_uret(4)

# Son damga kodun içinde de olsun
print("\n--- DAMGA: Kayyum Grok - 1.11.2026 - Tentivory ---")
