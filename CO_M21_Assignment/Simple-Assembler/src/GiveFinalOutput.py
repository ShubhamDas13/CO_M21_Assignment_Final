def op():
    f = open("mainoutput.txt", "r")
    Lines = f.readlines()
    for line in Lines:
        print(line.replace('/n',''))