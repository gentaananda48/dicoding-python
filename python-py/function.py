# Function
def myFirstFunc():
    print ('Input the param : ')
    
# Call Function
myFirstFunc()
baseParam = input('Please input base : ')
heightParam = input('Please input height : ')
sideParam = input('Please input side : ')


# Rumus lias segi 3
def areaOfTriangle(base, height):
    area = (base * height) / 2
    print ("Area of Triangle : %f" % area)
    

# Function with return
def areaOfSquare(side):
    area = side * side
    return area

def volumeOfSquare(side):
    volume = areaOfSquare(side) * side
    return volume

areaOfTriangle(int(baseParam), int(heightParam))
print('Area of Square : %f' % areaOfSquare(int(sideParam)))
print('Volume of Square : %f' % volumeOfSquare(int(sideParam)))

lambdaFunc = lambda progLang: print(f"This is {progLang}")

lambdaFunc('Lambda Function')

# *args dan **kwargs
print('*args dan **kwargs')
def sendMessage(*number):
    print (number)

def writeMessage(**content):
    print(content)
    
sendMessage(1982, 1999, 2212)
writeMessage(direction = 1987, message="How are you?")

# Average function
def average(*data):
    datas = len(data)
    sumData = sum(data)
    averageVal = float(sumData) / float(datas)    
    return averageVal

print (average(int(baseParam), int(heightParam), int(sideParam)))