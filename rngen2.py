import random
'''created by clive hunt date /17/11/2018'''
file_text=open('numm.txt', 'w')
cont = 0
st = str
for cont in range(0,1000000):
    numbers = random.sample(range(10),7)#10 is then number from 0-9, 7 is then amount of digital placements to be generated
    file_text.write('07'+''.join(map(str,numbers))+'16\n')
#constraints/e.g area code 07 can be changed to desired area location
#str is where the string of numbers are stored
#constraints/e.g 16 is the ending digits of moblie number targets, this can also be change to your desired target



