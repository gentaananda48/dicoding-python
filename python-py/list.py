# List tutorial in python (simple list)

data1 = ['Kinoa', 'Satoru', 'Usagi', 'Hashimoto', 'Yukihira', 'Nobita', 'Mitsugi']

totalData = 'Total Data : {}'.format(len(data1))

# Show all data
print(totalData)

for key in range(len(data1)):
    print( key + 1, data1[key])

addValue = 'n'    
addValue = input('Wanna insert new data ?(y/N) ')
while(addValue == 'Y'
       or addValue == 'y' 
       or addValue == 'ya' 
       or addValue == 'Ya') : 
# Add value data (first/custom/end)
    methodAdd = input('(first/custom/end) : ')
    # First
    if methodAdd == 'first' or methodAdd == '1' or methodAdd == 'f' :
        valueAdd = input('Input data : ')
        data1.insert(0, str(valueAdd))
    
    # Custom
    if methodAdd == 'custom' or methodAdd == '2' or methodAdd == 'c':
        indexVal = input('Input index(1-{}) : '.format(len(data1)))
        valueAdd = input('Input data : ')
        data1.insert(int(indexVal) - 1, str(valueAdd))
        
    # Custom
    if methodAdd == 'end' or methodAdd == '3' or methodAdd == 'e':
        valueAdd = input('Input data : ')
        data1.append(str(valueAdd))
    
    print('Data successfully added!')    
    addValue = input('Wanna insert new data ?(y/N) ')


# Show all data
print(totalData)

for key in range(len(data1)):
    print( key + 1, data1[key])

# Index input
indexData = input('Please input index(1-{}) : '.format(len(data1)))

# if has no input for index
if indexData == '': 
    indexData = len(data1)
    # Output of data by index
    print ('Last data from data is {}'.format(data1[int(indexData) - 1]))
elif type(indexData) != int : 
    print ('Invalid input')
elif int(indexData) > len(data1) :
     print ('total data : {}'.format(len(data1)))
elif int(indexData) <= 0:
     print ('Input must > 0')
else:
    # Output of data by index
    print ('Index {0} from data is {1}'.format(indexData, data1[int(indexData) - 1]))

# Show all data
print(totalData)

for key in range(len(data1)):
    print(key + 1, data1[key])
