import os
import re

globalConcelhosCount = []
obrasConcelhosCount = []

def printGlobalCount():
    for concelho in globalConcelhosCount:
        if concelho[1] > 0:
            print concelho[0] + ":" + str(concelho[1])

def printMatrix():
    for obra in obrasConcelhosCount:
        line = obra[0]
        for concelho in obra[1]:
            line += "," + str(concelho[1])
        file.write(line + "\n")

def contains(small, big):
    for i in xrange(len(big)-len(small)+1):
        for j in xrange(len(small)):
            if big[i+j] != small[j]:
                break
        else:
            return i, i+len(small)
    return False

def checkIfConcelhoOnLine(concelho,line):
    # we might want to remove more
    analyzingLine = re.sub('[,?;!@#$]', '', line).split(" ")
    # amazing regex that took forever
    # re.compile(r'(\W|^){0}(\W|$)'.format().search(analyzingLine)
    analyzingConcelho = concelho[0].replace(" ","\s").split(" ")
    return contains(analyzingConcelho,analyzingLine)

def countLocations(title,line):
    for concelho in globalConcelhosCount:
        if checkIfConcelhoOnLine(concelho,line):
            concelho[1] += 1
            # obra-location count
            for obra in obrasConcelhosCount:
                obraTitle = obra[0]
                if obraTitle == title:
                    # increment concelho count -- dictionaries would probably be welcome
                    obraConcelhos = obra[1]
                    count = 0
                    for obraConcelho in obraConcelhos:
                        if obraConcelho[0] == concelho[0]:
                            # might be nice to print line number on console to check it out later
                            obra[1][count][1] += 1
                            print concelho[0] + " found in " + title + " " + str(obra[1][count][1]) + " time" + ("s." if obra[1][count][1] > 1 else ".")
                            # uncomment next line to see how things are going
                            # print line
                            break
                        count += 1
                    break
    return

def setLocations():
    # reads locations file - optionaly this could fetch from central de dados
    file = open("concelhos.csv","r")
    count = -1
    for line in file:
        count += 1
        if count == 0:
            continue
        #concelho = [line.split(",")[2].rsplit("\n")[0],0]
        globalConcelhosCount.append([line.split(",")[2].rsplit("\n")[0],0])
        for obra in obrasConcelhosCount:
            obra[1].append([line.split(",")[2].rsplit("\n")[0],0])
    return

def getBooks():
    # ideally we would scrape the books from adamastor but for now lets assume they are already in pubs/
    for file in os.listdir("pubs/"):
        if file.endswith(".epub"):
            title = file.replace(".epub","")
            obrasConcelhosCount.append([title,[]])
    return

def main():
    getBooks()
    setLocations()
    bookNumber = 0
    for file in os.listdir("pubs/"):
        if file.endswith(".epub"):
            # convert to txt and open it
            os.system('epub2txt.py "pubs/'+file+'"')
            livro = open('pubs/'+file.replace("epub","txt"),"r")
            title = file.replace(".epub","")
            print "Analyzing " + title + " ("+str(bookNumber+1)+")"
            [countLocations(title, line) for line in livro]
            bookNumber += 1

if __name__ == "__main__":
    main()

    def getCount(item):
        return item[1]
    globalConcelhosCount = sorted(globalConcelhosCount, key=getCount)
    printGlobalCount()
    file = open("matrizLocalizacao.csv","w")
    header = "obra"
    for concelho in globalConcelhosCount:
        header += "," + concelho[0]
    file.write(header + "\n")
    printMatrix()
