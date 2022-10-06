item = ['buku', 'laptop', 'keyboard', 'mouse', 'tisu']

# For loop
print('For Loop : \n')
for isian in item:
    print ('Ada ' + isian)

print('\n')
    
# While loop
answer = '1'
count = 0

while (answer == '1' 
       or answer == 'y' 
       or answer == 'ya' 
       or answer == 'Ya' 
       or answer == 'True' 
       or answer == 'true' 
       or answer == 'yes' 
       or answer == 'Yes'
       ) :
    count += 1
    answer = input("Repeat ?(y/n) ")
    
print(f"Total loop : {count}")