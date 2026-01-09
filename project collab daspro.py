import pandas as pd

print("              Invoice Tagihan             ")

tanggal_transaksi = input("Masukkan tanggal transaksi: ")
nomor_invoice = input("Masukkan nomor invoice: ")
nama_pembeli = input("Masukkan nama pembeli: ")
alamat_pembeli = input("Masukkan alamat pembeli: ")


def garis():
    print("-" * 82) 

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

# Menampilkan Menu
garis()
print("| No | Deskripsi Produk | Kuantitas | Harga Satuan (Rp) | Total Harga (Rp) |")
garis()
print("| 1  | Printer laserjet |     1     |    Rp 800.000     |    Rp 800.000    |")
print("| 2  | Kursi kantor     |     1     |    Rp 1.200.000   |   Rp 1.200.000   |")
garis()

#Input Data ke dalam List 
data_barang = [] 
jumlah_barang = int(input("Masukkan jumlah barang yang ingin dibeli: "))

for i in range(jumlah_barang):
    print(f"\nBarang ke-{i+1}:")
    nama_barang = input("Masukkan nama barang (Printer laserjet/Kursi kantor): ")
    kuantitas = int(input("kuantitas barang: "))

    harga_satuan = 0 
    if nama_barang == "Printer laserjet":
        harga_satuan = 800000
    elif nama_barang == "Kursi kantor":
        harga_satuan = 1200000
    elif nama_barang == "Meja kantor":
        harga_satuan = 1750000
    else:
        print("Barang tidak tersedia.")
        continue 

    total_harga_item = hitung_total(kuantitas, harga_satuan)
    
    # Simpan data
    data_barang.append({
        "No": i + 1,
        "Deskripsi Produk": nama_barang,
        "Kuantitas": kuantitas,
        "Harga Satuan": harga_satuan,
        "Total Harga": total_harga_item
    })

#membuat DataFrame Pandas
if not data_barang:
    print("\nTidak ada barang yang dibeli.")
    exit()

df = pd.DataFrame(data_barang)

#Perhitungan Menggunakan Pandas
invoice_subtotal = df['Total Harga'].sum()
diskon = hitung_diskon(invoice_subtotal) 
pajak = hitung_pajak(invoice_subtotal - diskon) 
total_tagihan = hitung_total_tagihan(invoice_subtotal, diskon, pajak) 

#tamilan data frame
df_display = df.copy()

#Format kolom angka menjadi string
df_display['Harga Satuan'] = df_display['Harga Satuan'].apply(lambda x: f"Rp {x:,.0f}")
df_display['Total Harga'] = df_display['Total Harga'].apply(lambda x: f"Rp {x:,.0f}")

df_display = df_display.rename(columns={
    "Harga Satuan": "Harga Satuan (Rp)", 
    "Total Harga": "Total Harga (Rp)"
})
#Cetak Hasil Akhir
print("\n")
garis()
print(f"{'INVOICE TAGIHAN':^82}")
garis()
print(f" Tanggal Transaksi : {tanggal_transaksi}")
print(f" Nomor Invoice     : {nomor_invoice}")
print(f" Nama Pembeli      : {nama_pembeli}")
print(f" Alamat Pembeli    : {alamat_pembeli}")

# ==============================================================================
# bagian pemisah kolom (header)
# ==============================================================================
garis()
print(f"| {'No':<2} | {'Deskripsi Produk':<18} | {'Kuantitas':^9} | {'Harga Satuan (Rp)':>17} | {'Total Harga (Rp)':>17} |")
garis()

# iterrows() mengambil data baris per baris dari Pandas DataFrame
for index, row in df_display.iterrows():
    print(f"| {row['No']:<2} | {row['Deskripsi Produk']:<18} | {row['Kuantitas']:^9} | {row['Harga Satuan (Rp)']:>17} | {row['Total Harga (Rp)']:>17} |")

garis()

print(f"| {'Subtotal':<56} : Rp {invoice_subtotal:>15,.0f} |")
print(f"| {'Diskon':<56} : Rp {diskon:>15,.0f} |")
print(f"| {'Pajak (5%)':<56} : Rp {pajak:>15,.0f} |")
garis()
print(f"| {'Total Tagihan':<56} : Rp {total_tagihan:>15,.0f} |")
garis()

# Catatan
print("Catatan:")
print("- Diskon 10% berlaku untuk pembelian di atas Rp 2.000.000")
print("- Pajak 5% dikenakan sesuai peraturan yang berlaku")