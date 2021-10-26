import random
cs=0
ps=0

for i in range(0,5):
    list=["s","r","p"]
    comp=random.choice(list)
    player=input("select s/r/p")

    if player=="s" or "r" or "p":
        print("computer",comp)
        if (comp=="s" and player=="p") or (comp=="r" and player=="s") or (comp=="p" and player=="r"):
            print("you lose....hahaha")
            cs=2+cs
            print("COMPUTER--", cs, "PLAYER--",ps)

        elif comp==player:
            print("draw")
            cs=1+cs
            ps=1+ps
            print("COMPUTER--", cs, "PLAYER--", ps)
        else:
            print("you won ")
            ps=2+ps
            print("COMPUTER--", cs, "PLAYER--", ps)
    else:
        break
print("--------------TOTAL SCORE---------------")
print("COMPUTER--", cs, "           PLAYER--",ps)