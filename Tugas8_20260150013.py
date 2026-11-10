import modul_sensor

# Struktur data utama: list yang berisi tuple (suhu, kelembaban)
log_kebun = []


def input_sensor():
    """Meminta input suhu & kelembaban secara aman. Mengembalikan tuple (suhu, lembab)."""
    while True:
        try:
            suhu = float(input("Masukkan suhu udara (0-100 C)   : "))
            lembab = float(input("Masukkan kelembaban tanah (0-100 %): "))

            if 0 <= suhu <= 100 and 0 <= lembab <= 100:
                return (suhu, lembab)
            else:
                print(">> Error: suhu dan kelembaban harus di rentang 0-100. Ulangi!\n")
        except ValueError:
            print(">> Error: input harus berupa angka, bukan huruf. Ulangi!\n")


def analisis_tren():
    """Menganalisis maksimal 3 data terakhir dari log_kebun."""
    if len(log_kebun) == 0:
        print(">> Belum ada data. Rekam data terlebih dahulu (menu 1).")
        return

    # Slicing: ambil maksimal 3 data terakhir
    tiga_terakhir = log_kebun[-3:]

    print(f"\n=== Data {len(tiga_terakhir)} Terakhir ===")
    nomor = 1
    for suhu, lembab in tiga_terakhir:  # List iteration
        print(f"{nomor}. Suhu: {suhu:.1f} C | Kelembaban: {lembab:.1f} %")
        nomor += 1

    # Panggil fungsi dari modul
    rata_suhu, rata_lembab = modul_sensor.hitung_tren(tiga_terakhir)
    status = modul_sensor.evaluasi_irigasi(rata_suhu, rata_lembab, modul_sensor.AMBANG_KRITIS)

    print(f"\nRata-rata suhu       : {rata_suhu:.2f} C")
    print(f"Rata-rata kelembaban : {rata_lembab:.2f} %")
    print(f"Status               : {status}")


def main():
    nama, lintang, bujur = modul_sensor.LOKASI  # unpacking tuple

    while True:
        print("\n" + "=" * 45)
        print("  SISTEM MONITORING PRESISI IoT")
        print(f"  Lokasi: {nama} ({lintang}, {bujur})")
        print("=" * 45)
        print("[1] Rekam Data")
        print("[2] Analisis Tren (3 Terakhir)")
        print("[3] Keluar")

        pilihan = input("Pilih menu (1/2/3): ").strip()

        if pilihan == "1":
            data = input_sensor()
            log_kebun.append(data)
            print(f">> Data tersimpan: {data}. Total data: {len(log_kebun)}")
        elif pilihan == "2":
            analisis_tren()
        elif pilihan == "3":
            print("Terima kasih. Program selesai.")
            break
        else:
            print(">> Pilihan tidak valid. Pilih 1, 2, atau 3.")


if __name__ == "__main__":
    main()