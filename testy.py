x = "ten znak: '\\' to backslash"
print(x)
print(ord("A"))
print(chr(75))

x = 'Ala ma kota'
print(x.ljust(20,'!'))
print('['+'Ala ma kota'.ljust(20,'!')+']')
print('www.zut.pl'.lstrip('w.'))
print("Jan".swapcase())
lista = [1,2,5,4,23]
lista.sort(reverse=True)
print(lista)
print('aab.ap.ty'.lstrip('ab'))

def powitanie(imie, nazwisko):
  print('Dzień dobry, nazywam się ' + \
        nazwisko + '... ' + imie + ' '+\
        nazwisko + '...')
powitanie('James', 'Bond')
