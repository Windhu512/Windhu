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
            self.data[self.front] = None
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.max_size
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
        for i in range(self.max_size):
            rect = plt.Rectangle((i, 0), 1, 1, edgecolor='black', facecolor='white')
            ax.add_patch(rect)
            if self.data[i] is not None:
                ax.text(i + 0.5, 0.5, str(self.data[i]['np']), ha='center', va='center', fontsize=12)
        if not self.is_empty():
            ax.text(self.front, -0.5, 'Front', ha='center', va='center', color='red')
            ax.text(self.rear, 1.5, 'Rear', ha='center', va='center', color='blue')
        plt.axis('off')
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


# Fungsi validasi
def validate_gender(jk):
    return jk.upper() in ('L', 'P')


def validate_seat_number(jk, td, occupied_seats):
    try:
        seat_number = int(td)
        if jk.upper() == 'L':
            return 8 <= seat_number <= 20 and seat_number not in occupied_seats
        elif jk.upper() == 'P':
            return 1 <= seat_number <= 6 and seat_number not in occupied_seats
    except ValueError:
        return False
    return False


# Menu Utama
if __name__ == "__main__":
    queue_size = int(input("Masukkan jumlah maksimal data dalam queue: "))
    queue = Queue(queue_size)
    occupied_seats = set()

    while True:
        print("\nMenu:")
        print("1. Tambahkan data ke queue")
        print("2. Hapus data dari queue")
        print("3. Tampilkan isi queue")
        print("4. Cari data dalam queue")
        print("5. Sorting data dalam queue")
        print("6. Bersihkan queue")
        print("0. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            np = input("Masukkan nama penumpang: ")
            ap = input("Masukkan alamat penumpang: ")
            jk = input("Masukkan jenis kelamin (L/P): ")

            if not validate_gender(jk):
                print("Jenis kelamin tidak valid!")
                continue

            td = input("Masukkan nomor tempat duduk: ")

            if not validate_seat_number(jk, td, occupied_seats):
                print("Nomor tempat duduk tidak valid atau sudah ditempati!")
                continue

            occupied_seats.add(int(td))
            queue.enqueue({"np": np, "ap": ap, "jk": jk.upper(), "td": td})

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

        elif choice == "0":
            print("Keluar dari program. Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid!")
