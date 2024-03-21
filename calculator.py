def calc():
    ask = input("Operasi apa yang ingin digunakan (+, *)? ")
    operation = ["+", "*"]
    match ask:
        case "+":
            angka = int(input("\nberapa banyak angka yang ingin dijumlahkan? ")) 
            awal = 1
            nominal_awal = 0
            while awal <= angka:
                nominal = int(input("masukkan angka: "))
                nominal_awal += nominal
                awal = awal + 1
            print(f"\nHasilnya adalah {nominal_awal}")

        case "*":
            angka = int(input("berapa banyak angka yang ingin dikalikan?")) 
            awal = 1
            nominal_awal = 0
            while awal <= angka:
                nominal = int(input("masukkan angka: "))
                nominal_awal *= nominal
                awal = awal + 1
            print(f"\nHasilnya adalah {nominal_awal}")