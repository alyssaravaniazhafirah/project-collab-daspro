print("              Invoice Tagihan             ")

tanggal_transaksi = input("Masukkan tanggal transaksi: ")
nomor_invoice = input("Masukkan nomor invoice: ")
nama_pembeli = input("Masukkan nama pembeli: ")
alamat_pembeli = input("Masukkan alamat pembeli: ")

def garis():
    print("_" * 75)

print("\nTanggal Transaksi :", tanggal_transaksi)
print("Nomor Invoice     :", nomor_invoice)
print("Nama Pembeli      :", nama_pembeli)
print("Alamat Pembeli    :", alamat_pembeli)

# ======================
# DATA PRODUK (FIX)
# ======================
qty1 = 2
harga1 = 800000
total1 = qty1 * harga1

qty2 = 1
harga2 = 1200000
total2 = qty2 * harga2

# ======================
# TABEL PRODUK
# ======================
garis()
print("| No | Deskripsi Produk | Kuantitas | Harga Satuan (Rp) | Total Harga (Rp) |")
garis()
print(f"| 1  | Printer laserjet |     {qty1}     |   Rp {harga1:,}    |  Rp {total1:,}   |")
garis()
print(f"| 2  | Kursi kantor     |     {qty2}     |  Rp {harga2:,}   | Rp {total2:,}   |")
garis()

# ======================
# PERHITUNGAN TOTAL
# ======================
subtotal = total1 + total2
diskon = 0

if subtotal > 2000000:
    diskon = subtotal * 0.10

pajak = (subtotal - diskon) * 0.05
total_tagihan = subtotal - diskon + pajak

# ======================
# RINGKASAN TAGIHAN
# ======================
print(f"| {'Subtotal':<53} | Rp {subtotal:,.0f} |")
garis()
print(f"| {'Diskon 10%':<53} | Rp {diskon:,.0f} |")
garis()
print(f"| {'Pajak 5%':<53} | Rp {pajak:,.0f} |")
garis()
print(f"| {'Total Tagihan':<53} | Rp {total_tagihan:,.0f} |")
garis()

print("\nCatatan:")
print("- Diskon 10% diberikan untuk total pembelian di atas Rp2.000.000")
print("- Pajak 5% dikenakan sesuai peraturan yang berlaku")

