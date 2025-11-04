bills = list(map(int,input().split()))
changes = True
wallet = {"5":0,"10":0,"20":0}
for b in bills:
    if b == 5:
        wallet["5"] = wallet["5"] + 1
    elif b == 10:
        if wallet["5"] >= 1 :
            wallet["10"] = wallet["10"] + 1
            wallet["5"] = wallet["5"] - 1
        else:
            changes = False
            break
    else:
        if wallet["5"] >= 3 :
            wallet["20"] = wallet["20"] + 1
            wallet["5"] = wallet["5"] - 3
        elif wallet["10"] >= 1 and wallet["5"] >= 1:
            wallet["20"] = wallet["20"] + 1
            wallet["5"] = wallet["5"] - 1
            wallet["10"] = wallet["10"] - 1
        else:
            changes = False
            break
if changes:
    print("true")
else:
    print("false")
