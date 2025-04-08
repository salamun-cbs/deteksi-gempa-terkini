"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
"""


def ekstraksi_data():
    """
    Tanggal: 08 Apr 2025
    Waktu: 02:48:52 WIB
    Magnitudo: 6,2
    Kedalaman: 10 Km
    Lokasi: LU=2,82 BT=94,67
    Pusat Gempa: Pusat gempaLU=2,82 BT=94,67 berada di laut 192 km barat laut Sinabang
    Saran BMKG: Hati-hati terhadap gempabumi susulan yang mungkin terjadi
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '08 Apr 2025'
    hasil['waktu'] = '02:48:52 WIB'
    hasil['magnitudo'] = 6.2
    hasil['lokasi'] = {'lu': 2.82, 'bt': 94.67}
    hasil['pusat'] = 'Pusat gempaLU=2,82 BT=94,67 berada di laut 192 km barat laut Sinabang'
    hasil['saran'] = 'Hati-hati terhadap gempabumi susulan yang mungkin terjadi'

    return hasil


def tampilkan_data(result):
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi: LU {result['lokasi']['lu']}, BT {result['lokasi']['bt']} ")
    print(f"Pusat {result['pusat']}")
    print(f"Saran {result['saran']}")


if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)