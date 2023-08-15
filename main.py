def char_appearances(strr):
    letters = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
    strr = strr.lower()
    words = strr.split()
    count = 0
    for i in letters:
        for j in words:
            for k in j:
                if k == i:
                    count+=1
        letters[i] = count
        count = 0
    return letters


def total_words(strr):
    words = strr.split()
    return len(words)

with open("books/frankestein.txt") as f:
    print("--- Begin report of books/frankestein.txt ---")
    file_contents = f.read()
    print(f"{total_words(file_contents)} words found in the document")
    dict = char_appearances(file_contents)
    for key in dict:
        print(f"The {key} character was found {dict[key]} times")