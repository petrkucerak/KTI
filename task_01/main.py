import csv
path = 'data/IDS/20'
file1 = open(path + '.txt', 'r')

Lines = file1.readlines()
c=0
header=["timestamp","cpu","mem free","disk","eth"]
dataArr=[]
ln=""
lastDval = ""

f=open(path + '.csv', 'w', encoding='UTF8',newline='')
writer = csv.writer(f)
writer.writerow(header)
for line in Lines:
    c=c+1
    if line.startswith('-'):
        print(ln)
        if c!=1:
            writer.writerow(dataArr)
        dataArr = []
        c=0
    elif c==3:
        arr = line.split()
        dataArr.append(arr[0])
        dataArr.append(arr[2])
        ln+=arr[0]+" "
        ln+="cpu ut: "
        ln+=arr[2]
    elif c==8:
        arr = line.split()
        dataArr.append(arr[2])
        ln+=" mem- tot: "+arr[1]+" free: "+arr[2]
    elif c==11:
        arr = line.split()
        if(len(arr)>2):
            dataArr.append(arr[2])
            ln+=" disk: "+arr[2]
            lastDval= arr[2]
        else:
            dataArr.append(lastDval)
            ln += " disk: " + lastDval

    elif c==14:
        arr = line.split()
        if(arr[1]=="enp2s0"):
            dataArr.append(arr[2])
            ln += " enp2: " + arr[2]
    elif c == 15:
        arr = line.split()
        if (arr[1] == "enp2s0"):
            dataArr.append(arr[2])
            ln += " enp2: " + arr[2]
        elif(arr[1]== "enp3s0"):
            dataArr.append(arr[2])
            ln += " enp3: " + arr[2] +"\n"
    elif c == 16:
        arr = line.split()
        if(len(arr)>1):
            if (arr[1] == "enp3s0"):
                dataArr.append(arr[2])
                ln += " enp3: " + arr[2] + "\n"








