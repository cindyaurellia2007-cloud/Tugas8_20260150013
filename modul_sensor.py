# ---------- Konstanta (Tuple) ----------
LOKASI = ("Kampung Anggur Plumbungan", -7.828, 110.378)

# (Suhu Max dalam C, Kelembaban Min dalam %)
AMBANG_KRITIS = (35.0, 40.0)


# ---------- Fungsi ----------
def hitung_tren(data_slice):
    """
    Menerima list (hasil slicing) berisi tuple (suhu, kelembaban).
    Mengembalikan (rata_suhu, rata_lembab).
    """
    if len(data_slice) == 0:
        return 0.0, 0.0

    total_suhu = 0.0
    total_lembab = 0.0

    for suhu, lembab in data_slice:  # unpacking tuple
        total_suhu += suhu
        total_lembab += lembab

    jumlah = len(data_slice)
    rata_suhu = total_suhu / jumlah
    rata_lembab = total_lembab / jumlah
    return rata_suhu, rata_lembab


def evaluasi_irigasi(rata_suhu, rata_lembab, tuple_kritis):
    """
    tuple_kritis = (suhu_max, lembab_min)
    KRITIS jika rata_suhu > suhu_max ATAU rata_lembab < lembab_min.
    """
    suhu_max, lembab_min = tuple_kritis  # unpacking tuple

    if rata_suhu > suhu_max or rata_lembab < lembab_min:
        return "KRITIS: Nyalakan Pompa Irigasi!"
    else:
        return "NORMAL: Pompa Mati."