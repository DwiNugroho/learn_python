sizes = []

answer = "y"

while answer == "y":
    size = input("Masukan ukuran: ")
    sizes.append(size)
    new_answer = input("ingin menambah ukuran(y/n)? ")
    answer = new_answer


for s in sizes:
  match s:
    case "M":
      print("Harga 175000")
    case "L":
      print("Harga 25000")
