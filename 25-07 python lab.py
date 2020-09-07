1) sozluge eleman ekledik ve her degerini arttiriyoruz,

a)

sentence = input("Enter a sentence: ")
dict_sentence = {}
for i in sentence:
    if i in dict_sentence:
        dict_sentence[i] += 1
    else:
        dict_sentence[i] = 1
print(dict_sentence)

b)

words = input('Enter a sentence : ')
dct = dict()
for word in words:
    if word not in dct:
        dct[word]=words.count(word)
print(dct)


2) sozlukler ile lambda kullanalim

toplacikar = {'topla' : lambda x, y : x + y,
	       'cikar' : lambda x, y : x - y,}

toplacikar['topla'](9,3)

toplacikar['cikar'](9,3)


3) bunu hesap makinasi icinnde yapabiliriz

hesap = {'+' : (lambda x, y :x+y), '-': (lambda x, y :x-y), '*' : (lambda x, y :x*y), '/' : (lambda x, y :x/y)}

hesap['-'](8,8)

4) baska bir yol baska bir ornek

for x in [1,2,3,4,5]
print(x, ':', (lambda x : 'even' if x %2==0 else 'odd' )(i))
print(1 : ':',  'odd')

5) icinde bulunduumuz yil :
 icinde bulundugumuz ay :
 icinde bulundugumuz gun :

nasil yazariz?

a)

from datetime import date, datetime
today = date.today() 
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

b)

from datetime import date 

date.today( )

t = date.today( )
t.(tab basilinca her alternatif cikar karsimiza)

t.
print('icinde bulundugumuz yil :', t.year)
print('icinde bulundugumuz ay :', t.ay)
print('icinde bulundugumuz gun :', t.gun)

6)
list comperation

benim = [1, 2, 3, 4, 5]

[str(i) for i in benim] 
#print yapinca [1, 2, 3, 4, 5]

bos = [ ]
for in benim bos.append(i)
bos


#dicsenery kullanrak yeniden yaplaim

dic = { i : i*i for i in range(6)}

baska ornek

dic = {f'{i} nin karesi' : i**2 for i in range(6)}
dic


dic = {f"{i}'nin karesi": i**2 for i in [1,2,3,4,5]}


7)

{0:0, 1:1, 2:4, 3:9}

{0'in karesi: 0
1' inkaresi :1
....
.......
}

{str(i) + 'in karesi' : i *i for i in range(8)




8)dersteki notlar

bos_liste = []
for i in "clarusway":
    bos_liste.append(i)
print(bos_liste)
print([i for i in "clarusway"])
print([i for i in "clarusway"])
print([i for i in "beri gel berber" if i != "e"])
['c', 'l', 'a', 'r', 'u', 's', 'w', 'a', 'y']
['c', 'l', 'a', 'r', 'u', 's', 'w', 'a', 'y']
['c', 'l', 'a', 'r', 'u', 's', 'w', 'a', 'y']
['b', 'r', 'i', ' ', 'g', 'l', ' ', 'b', 'r', 'b', 'r']

9)
L = ['right 20', 'right 30', left 50', up 10', 'down 20' ]
[x, y]
[0, -10]

x = y = 0

for i in range(len(L)) :
if L[i].startswith('r') : x = x + int(L[i].split()[1])
elif L[i].startswith('l)' : x = x - int(L[i].split()[1])
eliif L[i].startswith('u') : y = y + int(L[i].split()[1])
elif L[i].startswith('d') : y = y - int(L[i].split()[1])


[x, y]


