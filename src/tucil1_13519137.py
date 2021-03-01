# fungsi dan prosedur

def createListInput(f):
    # parsing file input menjadi list of list
    list_lengkap = []
    for line in f: # untuk setiap baris
        matkul = ""
        list_matkul = []
        for i in line: # untuk setiap huruf
            if i == "," or i == '.':
                list_matkul.append(matkul)
                matkul = ""
            else:
                matkul += i
        list_lengkap.append(list_matkul)
    return list_lengkap

def createGraph(list):
    # membuat DAG dalam bentuk adjacency matrix berarah
    graph = [[0 for i in range (len(list) + 1)] for j in range (len(list) + 1)]
    isiHeaderTabel(graph, list)
    for i in range (len(list)):
        for j in range (1, len(list[i])):
            for k in range (1, len(graph[0])):
                if graph[0][k] == list[i][j]:
                    graph[i + 1][k] = 1
    return graph

def isiHeaderTabel(tabel, list):
    # mengisi header (nama matkul) pada baris dan kolom tabel
    for i in range (len(list)):
        tabel[i + 1][0] = list[i][0]
        tabel[0][i + 1] = list[i][0]

def getBarisAllNol(graph):
    # mendapatkan indeks baris yang prasyaratnya tidak ada atau sudah terpenuhi
    indeks = []
    for i in range (len(graph) - 1, 0, -1):
        # urutan dibalik agar indeks tidak berubah saat di-pop
        all_nol = True
        for j in range (1, len(graph[i])):
            if graph[i][j] != 0:
                all_nol = False
        if (all_nol):
            indeks.append(i)
    return indeks

# main

# inisialisasi
f = open("input.txt", "r")
list_input = createListInput(f)
f.close()
graph = createGraph(list_input)
hasil_lengkap = []

# main
while len(graph) > 1:
    hasil = []
    listindeks = getBarisAllNol(graph)
    for indeks in listindeks:
        baris = graph.pop(indeks)
        hasil.append(baris[0])
        # penghilangan busur yang masuk pada simpul
        for j in range (1, len(graph[0])):
            if graph[0][j] == baris[0]:
                for i in range (1, len(graph)):
                    graph[i][j] = 0
    hasil_lengkap.append(hasil)

# output
for i in range (len(hasil_lengkap)):
    print("Semester " + str(i + 1) + ": ", end='')
    for j in range (len(hasil_lengkap[i]) - 1):
        print(hasil_lengkap[i][j] + ", ", end='')
    print(hasil_lengkap[i][len(hasil_lengkap[i]) - 1])