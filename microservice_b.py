import time

print("Microservice_B is running...")

unit = ["mm", "cm", "m", "km", "in", "ft", "yard"]


def unit_maker():
    with open("Request_2.txt", "w") as outfile:
        outfile.write("Sent")
    time.sleep(1)

    with open("Request_2.txt", "r") as infile:
        number = int(infile.read())
    return unit[number % len(unit)]


while True:
    with open("unit_request.txt", "r") as infile:
        log = infile.read()
    open("unit_request.txt", "w").close()

    if log == "Sent":
        unit = unit_maker()

        with open("unit_response.txt", "w") as outfile:
            outfile.write(unit)

    time.sleep(1)
