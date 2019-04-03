f = open("rating.review", "r+")
w = open("preprocessed_data.txt", "w")

unwanted_words = ["&quot;", "&quot;mr.&quot;;", "<num>", "<year>", "<dash-num>", "<fraction>"]
count_total = 0

for line in f:
    arr = line.split(" ")
    n = len(arr)
    final_str = ""
    count_total+=1
    for i in range(n):
        state = False
        for x in range(len(unwanted_words)):
            if arr[i].find(unwanted_words[x])!=-1:
                state=True
        if state==True:
            continue
        if i==n-1:
            label = arr[i][8:9]
            final_str+=label+"\n"
        elif "_" in arr[i]:
            count = int(arr[i][arr[i].find(":")+1:])
            arr[i] = arr[i].replace("_", " ")
            arr[i] = arr[i].split(" ")
            for j in range(len(arr[i])):
                for k in range(count):
                    final_str+=arr[i][j].replace(":"+str(count), "").replace(".","").replace("(", "").replace(")", "") + " "
        else:
            count = int(arr[i][arr[i].find(":")+1:])
            for k in range(count):
                final_str+=arr[i].replace(":"+str(count),"").replace(".", "").replace("(", "").replace(")", "") + " "
    w.write(final_str)

f.close()
w.close()
print("Total number of entries: " + count_total)