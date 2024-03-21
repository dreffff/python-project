def calc():
    ask = input("Operasi apa yang ingin digunakan?")
    operation = ["+", "-", "*", "/"]
    match ask:
        case "+":
            angka = int(input("berapa banyak angka yang ingin di jumlahkan?")) 
            awal = 1
            while awal <= angka:
                print("masukkan angka: ")
                awal = awal + 1

        case "-":
            angka = int(input("berapa banyak angka yang ingin di jumlahkan?")) 
            awal = 1
            while awal <= angka:
                print("masukkan angka: ")
                awal = awal + 1

        case "*":
            angka = int(input("berapa banyak angka yang ingin di jumlahkan?")) 
            awal = 1
            while awal <= angka:
                print("masukkan angka: ")
                awal = awal + 1

        case "/":
            angka = int(input("berapa banyak angka yang ingin di jumlahkan?")) 
            awal = 1
            while awal <= angka:
                print("masukkan angka: ")
                awal = awal + 1
