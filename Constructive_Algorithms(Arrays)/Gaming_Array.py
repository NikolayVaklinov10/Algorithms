def gamingArray(arr):
    players = ['BOB', 'ANDY']
    i = 0; maxval = 0
    for v in arr:
        if v > maxval:
            maxval = v
            i+=1
    return players[not bool(i%2)]
