import time

print("main.py is running...")

units = ['mm', 'cm', 'm', 'km', 'in', 'ft', 'yard']


def getUnit():
    """ Gets a random number and uses it to choose a random unit"""
    # using the Random Number Microservice API
    # 
    # change the file names below to the complete file directory of where the Request.txt file is located
    # that gets written to from the RandomNumberGenerator.py file

    with open("C:\\Users\\YuPheng Xiong\\PycharmProjects\\CS-361\\CS-361-Project\\Request.txt", "w") as outfile:
        outfile.write("Sent")
    # gives the program time to recieve the request and to respond with the number
    time.sleep(1)

    with open("C:\\Users\\YuPheng Xiong\\PycharmProjects\\CS-361\\CS-361-Project\\Request.txt", "r") as infile:
        number = int(infile.read())

    return units[number % len(units)]


while True:
    with open("C:\\Users\\YuPheng Xiong\\PycharmProjects\\CS-361\\CS-361-Project\\unit_request_2.txt", "r") as infile:
        log = infile.read()
    open("request.txt", "w").close()

    if log == "send a unit":
        unit = getUnit()

        with open("C:\\Users\\YuPheng Xiong\\PycharmProjects\\CS-361\\CS-361-Project\\unit_response_2.txt", "w") as outfile:
            outfile.write(unit)

    time.sleep(1)
