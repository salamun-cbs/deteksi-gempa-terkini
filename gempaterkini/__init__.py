import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    """
    Tanggal: 08 Apr 2025
    Waktu: 02:48:52 WIB
    Magnitudo: 6,2
    Kedalaman: 10 Km
    Lokasi: LU=2,82 BT=94,67
    Pusat Gempa: Pusat gempa LU=2,82 BT=94,67 berada di laut 192 km barat laut Sinabang
    Saran BMKG: Hati-hati terhadap gempabumi susulan yang mungkin terjadi
    :return:
    """
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('p', {'class':'mt-2 text-sm leading-[22px] font-medium text-gray-primary'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        container = soup.find('div', class_='mt-5 flex flex-wrap lg:flex-nowrap gap-3')

        if container:
            cards = container.find_all('div', class_='px-4 py-3 border border-[#CBD5E1] rounded-xl', recursive=False)
            data = {}

            for card in cards:
                label_tag = card.find('p', class_='text-sm lg:text-base text-gray-primary')
                value_tag = card.find('span', class_='text-base lg:text-lg font-bold text-black-primary')

                if label_tag and value_tag:
                    label = label_tag.get_text(strip=True).replace(':', '')
                    value = value_tag.get_text(strip=True)
                    data[label] = value

                # Print hasil
            i = 0
            magnitudo = None
            kedalaman = None
            ls = None
            bt = None
            pusat = None

            for k, v in data.items():
                # print(i, f"{k}: {v}")  # jika dibuka untuk melihat hasil print
                if i == 0:
                    magnitudo = v
                elif i == 1:
                    kedalaman = v
                elif i == 2:
                    koordinat = v.split(' - ')
                    ls = koordinat[0]
                    bt = koordinat[1]
                i = i + 1

        result = soup.find('p', {'class':'mt-4 text-xl lg:text-2xl font-bold text-black-primary'})
        result = result.text
        lokasi = result

        result = soup.find('p', {'class':'text-sm font-medium text-black-primary'})
        result = result.text.split(':')
        result = result[1]
        saran = result

        hasil = dict()
        hasil['tanggal'] = tanggal #'08 Apr 2025'
        hasil['waktu'] = waktu # '02:48:52 WIB'
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls':ls, 'bt':bt}
        hasil['lokasi'] = lokasi
        hasil['saran'] = saran
        return hasil
    else:
        return None

def tampilkan_data(result):
    if result is None:
        print("Tidak bisa menemukan data gempa terkini")
        return

    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Koordinat: LS= {result['koordinat']['ls']}, BT= {result['koordinat']['bt']}")
    print(f"Lokasi: {result['lokasi']}")
    print(f"Saran BMKG: {result['saran']}")
