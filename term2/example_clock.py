from time import sleep

secend = 0
mineute = 0
hour = 0

for i in range(1000):
    secend += 1
    print(hour,":",mineute,":",secend)
    sleep(1)
    if secend == 59:
        mineute += 1
        secend = 0
        if mineute == 59:
            hour += 1
            mineute = 0
