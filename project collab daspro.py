print("              Invoice Tagihan             ")

#data pembeli
tanggal_transaksi = input("Masukkan tanggal transaksi: ")
nomor_invoice = input("Masukkan nomor invoice: ")
nama_pembeli = input("Masukkan nama pembeli: ")
alamat_pembeli = input("Masukkan alamat pembeli: ")

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
