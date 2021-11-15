count = 0
for i in range(1, 7):
    for j in range(1, 4):
        if i != j:
            print(i*10+j, end="   ")
            count += 1
            if count % 5 == 0:
                print("")
print("总共有:%d个" % (count))
