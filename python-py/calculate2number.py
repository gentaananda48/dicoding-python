# Input number & operator
n1 = input('Input 1 : ')
c = input('input operator : ')
n2 = input('Input 2 : ')

# Konversi inputan (if/elif/else)
if c == '+': 
    sum = int(n1) + int(n2) 

if c == '-': 
    sum = int(n1) - int(n2)

if c == '/': 
    sum = int(n1) / int(n2)

if c == '*': 
    sum = int(n1) * int(n2)

# Menampilkan hasil
print ('hasil kalkulasi {0} dan {1} adalah {2}'.format(n1, n2, sum))
