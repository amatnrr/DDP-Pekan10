def fungsi(kalimat):
    vokal = 'aiueoAIUEO'
    hasil = ''
    for huruf in kalimat:
        if huruf not in vokal:
            hasil += huruf
    return hasil

print(fungsi('Nurul Fikri'))