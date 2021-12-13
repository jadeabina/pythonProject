
a=int(input('primeiro bimestre:'))
while a>10:
    a =int(input('vc digitou errado. primeiro bimeste:'))
b=int(input('segundo bimestre:'))
while b>10:
    b =int(input('vc digitou errado. segundo bimeste:'))
c=int(input('terceiro bimestre:'))
while c>10:
    c =int(input('vc digitou errado. terceiro bimeste:'))
d=int(input('quarto bimestre:'))
while d>10:
    d =int(input('vc digitou errado. quarto bimeste:'))
media=(a+b+c+d)/4
print('media{}'.format(media))



# if a <=10 and b <=10 and c <=10 and d<=10:
#     print('media:{}'.format(media))
# else:
#     print('foi informado alguma nota errada')











# a=0
# while a <= 10:
#     print(a)
#     a+=1










# a = int(input('entre com um valor:'))
# for num in range(a+1):
#     div=0
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x,resto)
#         if resto ==0:
#             div +=1
#     if div ==2:
#         print(num)
#
#






# a = int(input('entre com um numero:'))
#
# div=0
# for x in range(1,a+1):
#     resto =a % x
#     print(x,resto)
#     if resto ==0:
#         div +=1
#
#
# if div ==2:
#     print('numero {} é primo'.format(a))
# else:
#     print('numero {} não é primo' .format(a))














# for x in range(101):
#     print(x)