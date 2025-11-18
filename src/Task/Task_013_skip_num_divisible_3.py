#Skip numbers divisible by 3, from (0,100)
for i in range(101): # 0 to 100
    if i % 3 == 0:
        continue
    else:
        print(i)