'''
@author: Pedro Canoas <pedro_canoassilva@hotmail.com
@name: conversor.py
'''

'''
@desc converte uma coluna do excel para um numero decimal
@param String xls_col
@return Number
'''

coluns = []

def ordColuns():
    indexFirstLetter = 0
    indexSecondLetter = 0
    for i in range(ord('A'), ord('Z')+1):
        #ele começa inserindo a letra A no end 0
        coluns.insert(indexFirstLetter, chr(i))
        for j in range(ord('A'), ord('Z')+1):
            # o endereço da segunda letra será no end 1
            indexSecondLetter += 1
            # aqui será inserido a letra A no end 0 e a letra A no end 1
            # mas como o A do end 0 já existia, ele foi substituido
            coluns.insert(indexFirstLetter+indexSecondLetter, chr(i)+chr(j))
            for k in range(ord('A'), ord('Z')+1):
                #e aqui a última letra da ordem é apenas acrescentada
                coluns.append(chr(i)+chr(j)+chr(k))
        indexFirstLetter += 1

def xls2Dec(letter):
    letter = coluns.index(lines[index])+1
    return letter

ordColuns()
file = open('arquivo.txt', 'r')
lines = file.readlines()
print(lines[0].rstrip('\n'))

for index in range(1,int(lines[0])+1):
    lines[index] = lines[index].rstrip('\n')
    print('{}={}'.format(lines[index],xls2Dec(index)))

file.close()