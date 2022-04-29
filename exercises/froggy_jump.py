def jumps(x, y, d):
    distance = y-x
    jumps = round(distance/d)+1
    print("Total jumps: " + str(jumps))

jumps(10,85,30)