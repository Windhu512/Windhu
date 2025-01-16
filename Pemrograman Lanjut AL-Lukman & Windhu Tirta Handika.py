class Stack:
    def __init__(self):
        self.box = []

    def push(self, item):
        self.box.append(item)

    def pop(self):
        if not self.is_empty():
            return self.box.pop()
        else:
            raise IndexError("Stack kosong")

    def peek(self):
        if not self.is_empty():
            return self.box[-1]
        else:
            raise IndexError("Stack kosong")

    def is_empty(self):
        return len(self.box) == 0

    def size(self):
        return len(self.box)

    def display(self):
        if self.is_empty():
            print("Box kosong")
        else:
            print("Isi Box (Top -> Bottom):")
            for item in reversed(self.box):
                print(f"| {item} |")
            print(" -----")


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Antrian kosong")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Antrian kosong")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        if self.is_empty():
            print("Antrian kosong.")
        else:
            print("Isi Antrian (Depan -> Belakang):")
            for index, (nama, buku) in enumerate(self.queue, start=1):
                print(f"{index}. Nama: {nama}, Buku: {buku}")


def pilih_kategori():
    print("\nHalo! Mau Pilih Buku Kategori Apa?")
    print("Kalau Mau Buku Fiksi Tekan 1, Ilmiah Tekan 2, Sejarah Tekan 3")
    pilihan = input("Masukkan pilihan Anda (1/2/3): ")

    if pilihan == "1":
        print("Anda memilih kategori: Buku Fiksi")
        return "Box Buku Fiksi"
    elif pilihan == "2":
        print("Anda memilih kategori: Buku Ilmiah")
        return "Box Buku Ilmiah"
    elif pilihan == "3":
        print("Anda memilih kategori: Buku Sejarah")
        return "Box Buku Sejarah"
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        return None


def menu_box(box_name, box_stack, queue):
    while True:
        print(f"\nAnda berada di {box_name}.")
        print("1. Lihat daftar buku")
        print("2. Ambil buku")
        print("3. Letakkan buku")
        print("4. Kembali ke menu sebelumnya")
        print("5. Lanjutkan ke antrian")
        pilihan = input("Masukkan pilihan Anda (1/2/3/4/5): ")

        if pilihan == "1":
            print(f"\nDaftar buku dalam {box_name}:")
            box_stack.display()

        elif pilihan == "2":
            try:
                buku_diambil = box_stack.pop()
                print(f"Buku '{buku_diambil}' berhasil diambil dari {box_name}.")
                return buku_diambil  
            except IndexError:
                print("Tidak ada buku untuk diambil.")

        elif pilihan == "3":
            buku_baru = input("Masukkan nama buku yang ingin diletakkan: ")
            box_stack.push(buku_baru)
            print(f"Buku '{buku_baru}' berhasil ditambahkan ke {box_name}.")

        elif pilihan == "4":
            print("Kembali ke menu utama.")
            break

        elif pilihan == "5":
            print("Anda harus mengambil buku terlebih dahulu sebelum masuk ke antrian.")
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


def proses_antrian(queue):
    if queue.is_empty():
        print("Tidak ada antrian saat ini.")
    else:
        print("\nMemproses antrian:")
        pelanggan, buku = queue.dequeue()
        print(f"Giliran {pelanggan} memproses buku '{buku}'.")
        print("Proses selesai. Kembali ke menu utama.")


Boxes = {
    "Box Buku Fiksi": Stack(),
    "Box Buku Ilmiah": Stack(),
    "Box Buku Sejarah": Stack()
}

Boxes["Box Buku Fiksi"].push("One Piece")
Boxes["Box Buku Fiksi"].push("Naruto")
Boxes["Box Buku Fiksi"].push("Sousou no Frieren")
Boxes["Box Buku Ilmiah"].push("Ensiklopedia X")
Boxes["Box Buku Ilmiah"].push("Biology")
Boxes["Box Buku Sejarah"].push("Jejak Zaman Neolithikum")
Boxes["Box Buku Sejarah"].push("Sejarah Islam")
Boxes["Box Buku Ilmiah"].push("Ilmiah banget")

queue = Queue()

while True:
    print("\nMenu Utama:")
    print("1. Pilih kategori buku")
    print("2. Proses antrian")
    print("3. Keluar")
    print("4. Lihat antrean")
    pilihan = input("Masukkan pilihan Anda (1/2/3/4): ")

    if pilihan == "1":
        box_terpilih = pilih_kategori()
        if box_terpilih and box_terpilih in Boxes:
            buku_diambil = menu_box(box_terpilih, Boxes[box_terpilih], queue)
            if buku_diambil:
                nama = input("Masukkan nama Anda untuk masuk ke antrian: ")
                queue.enqueue((nama, buku_diambil))
                print(f"{nama} dengan buku '{buku_diambil}' berhasil masuk ke antrian.")
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

    elif pilihan == "2":
        proses_antrian(queue)

    elif pilihan == "3":
        print("Terima kasih! Program selesai.")
        break

    elif pilihan == "4":
        print("\nMelihat isi antrean:")
        queue.display()

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")