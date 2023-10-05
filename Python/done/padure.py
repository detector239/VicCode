# 1. De citit fisierul padure.orc, de salvat intr-o lista toate randurile, de afisat fiecare element din lista

file = open('padure.orc', 'r')
Lines = file.readlines()
file.close()

lines_num = len(Lines)

# for i in range(lines_num):
#     print(Lines[i])

# 3. De salvat in lista "idnp" randurile care incep cu 'C;X1;K', de afisat fiecare element din idnp (folosind i=0..n-1)

idnp = []
for i in range(lines_num):
    if Lines[i].startswith('C;X1;K'):
        Lines[i] = Lines[i].replace('C;X1;K', '')
        Lines[i] = Lines[i].replace('\n', '')
        idnp.append(Lines[i])



# 4. De salvat in lista "nume" randurile care incep cu 'C;X2;K', de afisat fiecare element din idnp si nume concomitent (folosind i=0..n-1)
nume = []
for i in range(lines_num):
    if Lines[i].startswith('C;X2;K'):
        Lines[i] = Lines[i].replace('C;X2;K', '')
        Lines[i] = Lines[i].replace('\n', '')
        nume.append(Lines[i])



# 5. De salvat in lista "prenume" randurile care incep cu 'C;X3;K', de afisat fiecare element din toate listele deja create

prenume = []
for i in range(lines_num):
    if Lines[i].startswith('C;X3;K'):
        Lines[i] = Lines[i].replace('C;X3;K', '')
        Lines[i] = Lines[i].replace('\n', '')
        prenume.append(Lines[i])



# 5. De salvat in lista "raion" randurile care incep cu 'C;X4;K', de afisat fiecare element din toate listele deja create

raion = []
for i in range(lines_num):
    if Lines[i].startswith('C;X4;K'):
        Lines[i] = Lines[i].replace('C;X4;K', '')
        Lines[i] = Lines[i].replace('\n', '')
        raion.append(Lines[i])


# 5. De salvat in lista "localitate" randurile care incep cu 'C;X5;K', de afisat fiecare element din toate listele deja create

localitate = []
for i in range(lines_num):
    if Lines[i].startswith('C;X5;K'):
        Lines[i] = Lines[i].replace('C;X5;K', '')
        Lines[i] = Lines[i].replace('\n', '')
        localitate.append(Lines[i])


# 5. De salvat in lista "strada" randurile care incep cu 'C;X6;K', de afisat fiecare element din toate listele deja create

strada = []
for i in range(lines_num):
    if Lines[i].startswith('C;X6;K'):
        Lines[i] = Lines[i].replace('C;X6;K', '')
        Lines[i] = Lines[i].replace('\n', '')
        strada.append(Lines[i])


# 5. De salvat in lista "datanast" randurile care incep cu 'C;X7;K', de afisat fiecare element din toate listele deja create

datanast = []
for i in range(lines_num):
    if Lines[i].startswith('C;X7;K'):
        Lines[i] = Lines[i].replace('C;X7;K', '')
        Lines[i] = Lines[i].replace('\n', '')
        datanast.append(Lines[i])


file_2 = open('padure.csv', 'a')
idnp_num = len(idnp)

for i in range(idnp_num):
    a = idnp[i] +";"+ nume[i] +";"+ prenume[i] +";"+ raion[i] +";"+ localitate[i] +";"+ strada[i] +";"+ datanast[i]
    file_2.write(a + "\n" )


file_2.close()
