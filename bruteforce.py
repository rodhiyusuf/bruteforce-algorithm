def BruteForce():
    Text=input("(Text) Judul Buku:\n")
    Pattern=input("(Pattern) Masukkan kata kunci:\n")
    for i in range(0,len(Text)-len(Pattern)+1):
        j = 0
        while j < len(Pattern) and Pattern[j] == Text[i+j]:
          j = j + 1
        if j == len(Pattern):
          print("Kata kunci ditemukan pada index ke : "+str(i))
          

    return -1

if __name__ == "__main__":

    BruteForce()