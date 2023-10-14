class cart_class:
  def __init__(self, name, size, price, total, totalPrice):
    self.name = name
    self.size = size
    self.price = price
    self.total = total
    self.totalPrice = totalPrice

class shirt_class:
  def __init__(self, name, s, m, l):
    self.name = name
    self.s = s
    self.m = m
    self.l = l

shirtList = []
shirtList.append(shirt_class('polo', 170000, 200000, 250000))
shirtList.append(shirt_class('alisan', 100000, 150000, 200000))
shirtList.append(shirt_class('styes', 200000, 300000, 400000))

cartList = []
answer = 'y';

while answer == 'y':
  for index, shirt in enumerate(shirtList):
    print(f"{index + 1}. {shirt.name}")

  number = int(input('ingin memesan baju nomor berapa? ')) - 1
  print('')


  if number >= 0 and number < len(shirtList):
    shirtChoosed = shirtList[number]

    sizeChoosed = ''

    while sizeChoosed == '':
      print(f'(s) {shirtChoosed.s:,.0f}')
      print(f'(m) {shirtChoosed.m:,.0f}')
      print(f'(l) {shirtChoosed.l:,.0f}')


      try:
        size = input('ukuran? ')
        print('')
        sizePrice = getattr(shirtChoosed, size)
        sizeChoosed = size
        total = int(input('berapa? '))
        print('')
        cartList.append(cart_class(shirtChoosed.name, size, sizePrice, total, sizePrice * total))
      except AttributeError:
        print("ukuran tidak tersedia, silahkan pilih ukuran kembali!")
  else:
    print("baju tidak ada")
    print('')
  print('')
  answer = input('ingin menambah baju? (y/n) ')
  print('')


print('list pesanan:')
for cart in cartList:
  print(f" {cart.name}({cart.size}) X {cart.total} = {cart.totalPrice:,.0f}")

totalPurchased = 0

for cart in cartList:
  totalPurchased += cart.totalPrice

print(f' Total yang harus kamu bayar adalah {totalPurchased:,.0f}')
