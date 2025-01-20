import matplotlib.pyplot as plt
from rich.console import Console
from rich.table import Table


class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.front = -1
        self.rear = -1
        self.data = [None] * self.max_size

    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, value):
        if self.is_full():
            print("Maaf, queue penuh.")
        else:
            if self.is_empty():
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.max_size
            self.data[self.rear] = value
            print(f"Data {value['np']} masuk ke queue.")
            self.visualize()

    def dequeue(self):
        if self.is_empty():
            print("Data telah kosong!")
        else:
            print(f"Data yang terambil: {self.data[self.front]['np']}")
            for i in range(self.front, self.rear):
                self.data[i] = self.data[i + 1]
            self.data[self.rear] = None
            self.rear -= 1

            if self.rear < self.front:
                self.front = self.rear = -1

            print(f"self: {self}")
            self.visualize()


    def print_queue(self, highlight_name=None):
        if self.is_empty():
            print("Queue kosong.")
        else:
            table = Table(title="Data yang terdapat dalam queue")
            table.add_column("No", justify="center")
            table.add_column("Nama Penumpang", justify="left")
            table.add_column("Alamat Penumpang", justify="left")
            table.add_column("Jenis Kelamin", justify="center")
            table.add_column("No Tempat Duduk", justify="center")
            table.add_column("Biaya", justify="right")
            i = self.front
            idx = 1
            while True:
                p = self.data[i]
                name_display = f"[red]{p['np']}[/red]" if p['np'] == highlight_name else p['np']
                table.add_row(str(idx), name_display, p['ap'], p['jk'], p['td'], str(350000))
                if i == self.rear:
                    break
                i = (i + 1) % self.max_size
                idx += 1
            console = Console()
            console.print(table)

    def clear(self):
        self.front = self.rear = -1
        self.data = [None] * self.max_size
        print("\nSekarang queue kosong.")
        self.visualize()

    def visualize(self):
        fig, ax = plt.subplots(figsize=(20, 4))
        ax.set_xlim(-1, self.max_size)
        ax.set_ylim(-1, 2)
        ax.axis('off')

        for i in range(self.max_size):
            rect = plt.Rectangle((i, 0), 1, 1, edgecolor='black', facecolor='white')
            ax.add_patch(rect)
            if self.data[i] is not None:
                ax.text(i + 0.5, 0.5, str(self.data[i]['np']), ha='center', va='center', fontsize=12)

        if not self.is_empty():
            ax.text(self.front + 0.5, -0.5, 'Front', ha='center', va='center', color='red', fontsize=14)
            ax.text(self.rear + 0.5, 1.5, 'Rear', ha='center', va='center', color='blue', fontsize=14)

        plt.show()

    def search(self, name):
        if self.is_empty():
            print("Queue kosong.")
        else:
            i = self.front
            found = False
            while True:
                if self.data[i] is not None and self.data[i]['np'] == name:
                    found = True
                    break
                if i == self.rear:
                    break
                i = (i + 1) % self.max_size
            if found:
                print(f"\nData {name} ditemukan:")
                self.print_queue(highlight_name=name)
            else:
                print(f"Data {name} tidak ditemukan dalam queue.")

    def bubble_sort(self):
        if self.is_empty():
            print("Queue kosong, tidak bisa melakukan sorting.")
            return
        n = (self.rear - self.front + self.max_size) % self.max_size + 1
        for i in range(n):
            for j in range(0, n - i - 1):
                idx1 = (self.front + j) % self.max_size
                idx2 = (self.front + j + 1) % self.max_size
                if self.data[idx1]['np'] > self.data[idx2]['np']:
                    self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]
        print("Queue telah di-sort berdasarkan nama penumpang menggunakan Bubble Sort.")


class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.top = -1
        self.data = [None] * self.max_size

    def is_full(self):
        return self.top == self.max_size - 1

    def is_empty(self):
        return self.top == -1

    def push(self, value):
        if self.is_full():
            print("History penuh, tidak bisa menambahkan data.")
        else:
            self.top += 1
            self.data[self.top] = value
            print(f"Pembelian {value['np']} ditambahkan ke history.")

    def pop(self):
        if self.is_empty():
            print("History kosong, tidak ada data untuk dihapus.")
        else:
            value = self.data[self.top]
            self.data[self.top] = None
            self.top -= 1
            print(f"Data {value['np']} dihapus dari history.")

    def print_stack(self):
        if self.is_empty():
            print("History kosong.")
        else:
            table = Table(title="Riwayat Pembelian Tiket")
            table.add_column("Index", justify="center")
            table.add_column("Nama Penumpang", justify="left")
            table.add_column("Alamat Penumpang", justify="left")
            table.add_column("Jenis Kelamin", justify="center")
            table.add_column("No Tempat Duduk", justify="center")
            table.add_column("Total Biaya", justify="right")

            for i in range(self.top, -1, -1):
                p = self.data[i]
                table.add_row(
                    str(i + 1),
                    p["np"],
                    p["ap"],
                    p["jk"],
                    p["td"],
                    f"Rp. {p['tb']:,}",
                )

            console = Console()
            console.print(table)


def validate_gender(jk):
    return jk.upper() in ('L', 'P')


def validate_seat_number(jenis_kelamin, tempat_duduk, occupied_seats):
    try:
        seat_number = int(tempat_duduk)
        if jenis_kelamin.upper() == 'L':
            return 8 <= seat_number <= 20 and seat_number not in occupied_seats
        elif jenis_kelamin.upper() == 'P':
            return 1 <= seat_number <= 6 and seat_number not in occupied_seats
    except ValueError:
        return False
    return False


def validate_jenis_tiket(jenisTiket):
    return jenisTiket.upper() in ('SE', 'EP', 'EK')


def get_tiket_info(jenisTiket):
    tiket_mapping = {
        'SE': ("Super Eksklusif", 350000, 2.5),
        'EP': ("Eksekutif Plus", 325000, 2),
        'EK': ("Eksekutif", 300000, 1.5),
    }
    return tiket_mapping.get(jenisTiket.upper())


def validate_uang_pembayaran(up, gt):
    return up >= gt


def check_bonus(total, jenis_tiket):
    bonus_message = "Tidak Dapat Bonus"
    print(f"cb total : {total}")
    print(f"cb jt : {jenis_tiket}")
    if jenis_tiket.upper() == 'SE':
        if 5250000 <= total <= 7000000:
            bonus_message = "Anda Mendapatkan Bonus Liburan Ke Bali"
        elif 4550000 <= total <= 4900000:
            bonus_message = "Anda Mendapatkan Bonus Liburan Ke Surabaya"
        elif 3850000 <= total <= 4200000:
            bonus_message = "Anda Mendapatkan Bonus Liburan Ke Yogyakarta"
        elif 3150000 <= total <= 3500000:
            bonus_message = "Anda Mendapatkan Bonus Liburan Ke Bandung"
        elif 2100000 <= total <= 2800000:
            bonus_message = "Anda Mendapatkan Bonus Liburan Ke Jakarta"
    elif jenis_tiket.upper() == 'EP':  # Eksekutif Plus
        if 5000000 <= total <= 6500000:
            bonus_message = "Anda Mendapatkan Bonus Liburan Ke Bali"
        elif 4500000 <= total <= 4900000:
            bonus_message = "Anda Mendapatkan Bonus Liburan Ke Surabaya"
        elif 3800000 <= total <= 4200000:
            bonus_message = "Anda Mendapatkan Bonus Liburan Ke Yogyakarta"
        elif 3000000 <= total <= 3500000:
            bonus_message = "Anda Mendapatkan Bonus Liburan Ke Bandung"
        elif 2100000 <= total <= 2800000:
            bonus_message = "Anda Mendapatkan Bonus Liburan Ke Jakarta"
    elif jenis_tiket.upper() == 'EK':
        if 4500000 <= total <= 6000000:
            bonus_message = "Anda Mendapatkan Bonus Liburan Ke Bali"
        elif 4000000 <= total <= 4300000:
            bonus_message = "Anda Mendapatkan Bonus Liburan Ke Surabaya"
        elif 3800000 <= total <= 3900000:
            bonus_message = "Anda Mendapatkan Bonus Liburan Ke Yogyakarta"
        elif 3500000 <= total <= 3700000:
            bonus_message = "Anda Mendapatkan Bonus Liburan Ke Bandung"
        elif 3000000 <= total <= 3300000:
            bonus_message = "Anda Mendapatkan Bonus Liburan Ke Jakarta"
    return bonus_message


def print_ticket(np, ap, jk, td, jb, hs):
    table = Table(title="")
    table.add_column("No", justify="center")
    table.add_column("Nama Penumpang", justify="left")
    table.add_column("Alamat Penumpang", justify="left")
    table.add_column("Jenis Kelamin", justify="center")
    table.add_column("No Tempat Duduk", justify="center")
    table.add_column("Jumalh Beli", justify="center")
    table.add_column("Biaya", justify="center")

    table.add_row(str(1), np, ap, jk, td, f"{jb}", f"Rp. {int(hs)}")
    console = Console()
    console.print(table)


# Menu Utama
if __name__ == "__main__":
    while True:
        try:
            queue_size = int(input("Masukkan jumlah maksimal data dalam queue: "))
            if queue_size <= 0:
                print("Jumlah maksimal queue harus lebih dari 0. Silakan coba lagi.")
                continue
            break
        except ValueError:
            print("Mohon untuk memasukkan angka untuk jumlah maksimal queue")

    queue = Queue(queue_size)
    occupied_seats = set()
    stack_size = 100
    history_stack = Stack(stack_size)

    while True:
        print("\nMenu:")
        print("1. Tambahkan data ke queue")
        print("2. Hapus data dari queue")
        print("3. Tampilkan isi queue")
        print("4. Cari data dalam queue")
        print("5. Sorting data dalam queue")
        print("6. Bersihkan queue")
        print("7. History Stack")
        print("8. Hapus transaksi terakhir")
        print("0. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            print("")
            print("#---------------------------------------------------------#")
            print("#------------------  PROGRAM TIKET BUS  ------------------#")
            print("#---------------------------------------------------------#")
            print("")
            while True:
                jenisTiket = input("Silahkan Pilih Tiket (SE/EP/EK): ")

                if not validate_jenis_tiket(jenisTiket):
                    print("Pilihan tiket tidak tersedia! Harap pilih antara SE, EP, atau EK.")
                else:
                    break

            tiket_info = get_tiket_info(jenisTiket)
            kelas_bus, harga, pajak = tiket_info
            print(f"Kelas bus yang dipilih       : {kelas_bus}")
            print(f"Dengan Harga                 : Rp. {harga:,} / orang")

            while True:
                try:
                    jumlahBeli = int(input("Masukan Jumlah Beli          : "))
                    break
                except ValueError:
                    print("Jumlah beli harus berupa angka. Silakan coba lagi.")

            total_harga = harga * jumlahBeli
            total_pajak = total_harga * (pajak / 100)
            grand_total = total_harga + total_pajak

            while True:
                namaPenumpang = input("Masukkan nama penumpang      : ")
                if not namaPenumpang.isalpha():
                    print("Nama penumpang harus berupa huruf saja. Silakan coba lagi.")
                else:
                    break

            alamatPenumpang = input("Masukkan alamat penumpang    : ")

            while True:
              jenisKelamin = input("Masukkan jenis kelamin (L/P) : ")
              if not validate_gender(jenisKelamin):
                print("Jenis kelamin tidak valid!")
              else:
                  break

            check_seat = True
            while check_seat:
                tempatDuduk = input("Masukkan nomor tempat duduk  : ")

                if not validate_seat_number(jenisKelamin, tempatDuduk, occupied_seats):
                    print("Nomor tempat duduk tidak valid atau sudah ditempati!")
                else:
                    check_seat = False

            occupied_seats.add(int(tempatDuduk))
            queue.enqueue({"np": namaPenumpang, "ap": alamatPenumpang, "jk": jenisKelamin.upper(), "td": tempatDuduk})
            bonus = check_bonus(grand_total, jenisTiket)
            print("")
            print(f"Bonus Anda           :          {bonus}")
            print_ticket(namaPenumpang, alamatPenumpang, jenisKelamin, tempatDuduk, jumlahBeli, harga)
            print(f"Pajak Pembayaran Anda Adalah       : Rp. {int(total_pajak)}")
            print(f"Total Pembayaran Anda Adalah       : Rp. {int(grand_total)}")
            uang_pembayaran = int(input("Masukan uang pembayaran            : Rp. "))
            if not validate_uang_pembayaran(uang_pembayaran, grand_total):
                print("Uang pembayaran harus lebih dari total pembayaran")
                queue.dequeue()
                continue

            kembalian = uang_pembayaran - grand_total
            print(f"Uang kembalian adalah              : Rp. {int(kembalian)}")

            cancel = input(f"Ingin membatalkan pembelian? (y/t) : ")

            if cancel.upper() == 'Y':
                queue.dequeue()
            else:
                history_stack.push({
                    "np": namaPenumpang,
                    "ap": alamatPenumpang,
                    "jk": jenisKelamin.upper(),
                    "td": tempatDuduk,
                    "tb": grand_total
                })

        elif choice == "2":
            queue.dequeue()

        elif choice == "3":
            queue.print_queue()

        elif choice == "4":
            name = input("Masukkan nama yang ingin dicari: ")
            queue.search(name)

        elif choice == "5":
            queue.bubble_sort()
            queue.print_queue()

        elif choice == "6":
            queue.clear()
            occupied_seats.clear()

        elif choice == "7":
            history_stack.print_stack()

        elif choice == "8":
            history_stack.pop()

        elif choice == "0":
            print("Keluar dari program. Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid!")

