print("              Invoice Tagihan             ")

tanggal_transaksi = input("Masukkan tanggal transaksi: ")
nomor_invoice = input("Masukkan nomor invoice: ")
nama_pembeli = input("Masukkan nama pembeli: ")
alamat_pembeli = input("Masukkan alamat pembeli: ")

def garis ():
    print("_" * 75)

garis()
print("| No | Deskripsi Produk | Kuantitas | Harga Satuan (Rp) | Total Harga (Rp) |")
garis()
print("| 1  | Printer laserjet |     1     |     Rp 800.000    |    Rp 800.000    |")
garis()
print("| 2  | Kursi kantor     |     1     |    Rp 1.200.000   |   Rp 1.200.000   |")


# perhitungan
subtotal = 1600000 + 1200000

if subtotal > 2000000:
    diskon = subtotal * 0.10
else:
    diskon = 0

pajak = (subtotal - diskon) * 0.05
total_tagihan = subtotal - diskon + pajak

# tagihan
print(f"| {'Subtotal':<53} | Rp {subtotal:,.0f} |")
garis()
print(f"| {'Diskon 10%':<53} | Rp {diskon:,.0f} |")
garis()
print(f"| {'Pajak 5%':<53} | Rp {pajak:,.0f} |")
garis()
print(f"| {'Total Tagihan':<53} | Rp {total_tagihan:,.0f} |")
garis()
