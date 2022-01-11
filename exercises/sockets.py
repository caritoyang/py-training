def pairs(sockets):
    sockets.sort()
    sock=0
    pair=0
    for i in sockets:
        if i == sock:
            pair=pair+1
            sock=0
        else:
            sock=i
    print("Pares: " + str(pair))
    print("Sueltas: " + str(len(sockets)-pair*2))

pairs([1,2,1,2,1,2,3])