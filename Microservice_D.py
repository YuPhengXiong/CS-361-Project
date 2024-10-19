import time
import random


print("Microservice_D is running...")

while True:
    time.sleep(1)
    f = open("Request_3.txt", "r")
    read_text = f.readline()
    print(read_text)
    f.close()

    if read_text == "Sent":
        value = random.randint(1, 10)
        print(value)
        f = open("Request_3.txt", "w")
        f.write(str(value))
    f.close()