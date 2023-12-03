def duplikasi(list_buah):
    list_duplikat = []
    for buah in list_buah:
        list_duplikat.append(buah)
        list_duplikat.append(buah)
    return list_duplikat

print(duplikasi(['pepaya', 'mangga', 'pisang', 'durian', 'jambu']))
