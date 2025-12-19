print("              Invoice Tagihan             ")

#data pembeli
tanggal_transaksi = input("Masukkan tanggal transaksi: ")
nomor_invoice = input("Masukkan nomor invoice: ")
nama_pembeli = input("Masukkan nama pembeli: ")
alamat_pembeli = input("Masukkan alamat pembeli: ")
<<<<<<< HEAD

#fungsi
def garis ():
    print("-" * 75)

def hitung_total(kuantitas, harga_satuan):
    return kuantitas * harga_satuan 

def hitung_diskon(subtotal):
    if subtotal > 2000000:
       return subtotal * 0.10
    return 0 

def hitung_pajak(jumlah):
    return jumlah * 0.05

def hitung_total_tagihan(subtotal, diskon, pajak):
    return subtotal - diskon + pajak 

garis()
print("| No | Deskripsi Produk | Kuantitas | Harga Satuan (Rp) | Total Harga (Rp) |")
garis()
print("| 1  | Printer laserjet |     1     |     Rp 800.000    |    Rp 800.000    |")
garis()
print("| 2  | Kursi kantor     |     1     |    Rp 1.200.000   |   Rp 1.200.000   |")
garis()

#input data
barang= []
jumlah_barang = int(input("Masukkan jumlah barang yang ingin dibeli: "))

invoice_subtotal = 0 

for i in range(jumlah_barang):
    print(f"\nBarang ke-{i+1}:")
    nama_barang = input("Masukkan nama barang (Printer laserjet/Kursi kantor): ")
    kuantitas = int(input("kuantitas barang:"))

    harga_satuan = 0 
    if nama_barang == "Printer laserjet":
        harga_satuan = 800000
    elif nama_barang == "Kursi kantor":
        harga_satuan = 1200000
    else:
        print("Barang tidak tersedia.")
        continue 

    total_harga_item = hitung_total(kuantitas, harga_satuan) 
    barang.append((nama_barang, kuantitas, harga_satuan, total_harga_item))
    invoice_subtotal += total_harga_item 

# perhitungan
diskon = hitung_diskon(invoice_subtotal) 
pajak = hitung_pajak(invoice_subtotal - diskon) 
total_tagihan = hitung_total_tagihan(invoice_subtotal, diskon, pajak) 

#cetak hasil
print("\n                          Invoice Tagihan                                ")
print(f"Tanggal Transaksi : {tanggal_transaksi}")
print(f"Nomor Invoice     : {nomor_invoice}")
print(f"Nama Pembeli     : {nama_pembeli}")
print(f"Alamat Pembeli   : {alamat_pembeli}")

garis()
print("| No | Deskripsi Produk | Kuantitas | Harga Satuan (Rp) | Total Harga (Rp) |")
garis()
for idx, item in enumerate(barang):
    nama, kuantitas, harga_satuan, total_harga = item
    print(f"| {idx+1:<2} | {nama:<16} | {kuantitas:^10} | Rp {harga_satuan:>15,} | Rp {total_harga:>15,} |") 
garis()
print(f"|Subtotal               : Rp {invoice_subtotal:,.0f}                           |") 
garis()
print(f"|Diskon                 : Rp {diskon:,.0f}                                     |")
garis()
print(f"|Pajak (5%)             : Rp {pajak:,.0f}                                      |")
garis()
print(f"|Total Tagihan          : Rp {total_tagihan:,.0f}                              |")
garis()

print("Catatan:")
print("- Diskon 10% berlaku untuk pembelian di atas Rp 2.000.000")
print("- Pajak 5% dikenakan sesuai peraturan yang berlaku")
=======
# ======================
# DATA PRODUK
# ======================
>>>>>>> 802b7688cd3997d671930b1ad838bf4efcfc2c4d
