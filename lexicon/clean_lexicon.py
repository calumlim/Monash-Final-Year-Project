f = open("lexicon.txt", "r")
w = open("lexicon_clean.txt", "w")

for line in f:
    line = line.split("\t")
    final_str = line[0] + "\t" + line[1] + "\n"
    w.write(final_str)