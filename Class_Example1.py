## String
#myMessage = "Hello World"
#print(myMessage)

## Integer Number
#myNumber = 40
#print(myNumber)

## Decimal Number
#myNumber = 5.10
#print(myNumber)

#Average = (1+2+3) / 3
#print(Average)

#import statistics


## List:
#pythonList = [1,2,3]
#print(pythonList)

#A = 100
#print('This is a text and embedded variable: ' + str(A))


#var = 4
#if (var >= 5):
#    print('var is greater than or equal 5')
#elif (var < 0):
#    print('var is negative')
#elif (var == 0):
#    print('var is zero')
#else:
#    print('var is less than 5')

#for i in range(10):
#    print(i)

#var = 10
#while(var < 20):
#    print('var is less than 20')
#    var+=2


## If Statements:
#variable = 5
#if (variable > 5):
#    print("> 5")  #<-- Only 5 value will execute this line
#elif (variable == 5):
#    print("=5")
#else:
#    print("Everything Else")


## If Statements:
#variable = 6
#if (variable >= 5):
#    if (variable >= 10):
#        print("Nested If")
#    else:
#        print("Nested if else")
#else:
#    print("Variable NOT >=5")



#array = ['Kamarin Nicholes','Orie Wyatt','Lee Beebe']

## Loop by index number
#for i in range(0,len(array)):
#    print(i)

## Print Names out of Array (Strip Leading or Trailing spaces):
#for x in array:
#  print(x)
#  x_stripped = x.rstrip(" ")
#  x_stripped = x_stripped.lstrip(" ")
#  print(x_stripped)

## Print Names out of Array (Strip Leading or Trailing spaces):
#for x in array:
#  print(x)
#  x_split = x.split(" ")
#  print(x_split)


#var = 10
#while(var <= 20):
#    print('var is less than 20: ', var)
#    var+=1      # Increment


#print("STOP")



class phasor:
    def __init__(self, r=0, p=0):
        self.r = r
        self.p = p
    def real(self):
        return (self.r * math.cos(self.p))
    def imag(self):
        return (self.r * math.sin(self.p))

z = phasor(2.7, 0.4 * 3.14159)
print(z)