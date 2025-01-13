import os

# Direktori tempat file berada
directory = r"add\to\your\path"  # Pastikan path sesuai dengan lokasi folder

# Loop melalui semua file di direktori
for filename in os.listdir(directory):
    # Pastikan hanya file dengan ekstensi .jpg yang diproses
    if filename.endswith(".jpg"):
        # Ganti spasi dengan tanda "-"
        new_name = filename.replace(" ", "-")
        # Opsional: Tambahkan penggantian karakter tambahan
        new_name = new_name.replace(",", "-").replace("_-", "_")
        
        # Bangun jalur lengkap file lama dan file baru
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)
        
        # Ganti nama file
        os.rename(old_file, new_file)
        print(f"Renamed: {filename} -> {new_name}")

print("Rename selesai!")
