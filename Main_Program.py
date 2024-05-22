class color:
    """Sets the color class, used for font of certain displays."""
    RED = '\033[31m'
    BOLD = '\033[1m'
    END = '\033[0m'


# Creates a title for the software in the color of red.
print(color.RED + "Metric system to U.S. System Measurement converter" + color.END)


def main():
    """This function runs the software by stating the current status as True, then goes into the called function
     measurement_conversion, where it will gather the user inputs of what whole number they want to convert to a
     specific measurement between metric and U.S. systems. Then lastly ask the user whether they would like to run
     the system again, if yes, reruns the software, and if no, will thank the user and ends the software."""
    while True:
        measurement_conversion()
        q = input("You would like to use the system again? (yes/no): ").lower()
        if q == 'yes':
            """This describes that if the user input is equal to yes, then we rerun the system.
            Since the statement is still true."""
            pass
        elif q == 'no':
            print(color.BOLD + "Thank you for using my Software, Hope it was helpful." + color.END)
            break
        else:
            break


def measurement_conversion():
    """A function that gathers user's input and uses the inputs to convert to what the user wants, and displays it to
    the user."""
    try:
        q1 = int(input("Enter a value that you want to convert: "))
    except:
        print(color.BOLD + "This is not a number, please try again" + color.END)
        return True
    q2 = input("Enter the measure of the value you entered before: ")
    # If inches, will convert to ft, yard, etc.
    if q2 == 'in':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'ft':
            a1 = q1 / 12
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a1}{q3} {color.END}")
        elif q3 == 'yard':
            a2 = q1 / 36
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a2}{q3} {color.END}")
        elif q3 == 'mm':
            a3 = q1 * 25.4
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a3}{q3} {color.END}")
        elif q3 == "cm":
            a4 = q1 * 2.54
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a4}{q3} {color.END}")
        elif q3 == "m":
            a5 = q1 / 39.37
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a5}{q3} {color.END}")
        elif q3 == "km":
            a6 = q1 / 39370
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a6}{q3} {color.END}")
        else:
            # If the software can't convert, then will state the following statement to the user.
            print("This value can't be converted")

    # If ft, will convert to in, yard, etc.
    elif q2 == 'ft':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'in':
            a7 = q1 * 12
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a7}{q3} {color.END}")
        elif q3 == 'yard':
            a8 = q1 / 3
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a8}{q3} {color.END}")
        elif q3 == 'mm':
            a9 = q1 * 304.8
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a9}{q3} {color.END}")
        elif q3 == 'cm':
            a10 = q1 * 30.48
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a10}{q3} {color.END}")
        elif q3 == 'm':
            a11 = q1 * 0.3048
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a11}{q3} {color.END}")
        elif q3 == 'km':
            a12 = q1 * 0.0003048
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a12}{q3} {color.END}")
        else:
            # If the software can't convert, then will state the following statement to the user.
            print("This value can't be converted")

    # If yard, will convert to in, ft, etc.
    elif q2 == 'yard':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'in':
            a13 = q1 * 36
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a13}{q3} {color.END}")
        elif q3 == 'ft':
            a14 = q1 * 3
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a14}{q3} {color.END}")
        elif q3 == 'mm':
            a15 = q1 * 914.4
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a15}{q3} {color.END}")
        elif q3 == 'cm':
            a16 = q1 * 91.44
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a16}{q3} {color.END}")
        elif q3 == 'm':
            a17 = q1 * 0.9144
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a17}{q3} {color.END}")
        elif q3 == 'km':
            a18 = q1 * 0.0009144
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a18}{q3} {color.END}")
        else:
            # If the software can't convert, then will state the following statement to the user.
            print("This value can't be converted")

    # If millimeter, will convert to centimeter, meter, etc.
    elif q2 == 'mm':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'in':
            a19 = q1 / 25.4
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a19}{q3} {color.END}")
        elif q3 == 'ft':
            a20 = q1 / 304.8
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a20}{q3} {color.END}")
        elif q3 == 'yard':
            a21 = q1 / 914.4
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a21}{q3} {color.END}")
        elif q3 == 'cm':
            a22 = q1 / 10
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a22}{q3} {color.END}")
        elif q3 == 'm':
            a23 = q1 / 1000
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a23}{q3} {color.END}")
        elif q3 == 'km':
            a24 = q1 / 1000000
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a24}{q3} {color.END}")
        else:
            # If the software can't convert, then will state the following statement to the user.
            print("This value can't be converted")

    # If centimeter, will convert to millimeter, meter, etc.
    elif q2 == 'cm':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'in':
            a13 = q1 / 2.54
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a13}{q3} {color.END}")
        elif q3 == 'ft':
            a14 = q1 / 30.48
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a14}{q3} {color.END}")
        elif q3 == 'yard':
            a15 = q1 / 91.44
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a15}{q3} {color.END}")
        elif q3 == 'mm':
            a16 = q1 * 10
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a16}{q3} {color.END}")
        elif q3 == 'm':
            a17 = q1 / 100
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a17}{q3} {color.END}")
        elif q3 == 'km':
            a18 = q1 / 100000
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a18}{q3} {color.END}")
        else:
            # If the software can't convert, then will state the following statement to the user.
            print("This value can't be converted")

    # If meter, will convert to millimeter, centimeter, etc.
    if q2 == 'm':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'in':
            a1 = q1 * 39.36
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a1}{q3} {color.END}")
        elif q3 == 'ft':
            a2 = q1 * 3.28
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a2}{q3} {color.END}")
        elif q3 == 'yard':
            a3 = q1 * 1.0936
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a3}{q3} {color.END}")
        elif q3 == "mm":
            a4 = q1 * 1000
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a4}{q3} {color.END}")
        elif q3 == "cm":
            a5 = q1 * 100
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a5}{q3} {color.END}")
        elif q3 == "km":
            a6 = q1 / 1000
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a6}{q3} {color.END}")
        else:
            # If the software can't convert, then will state the following statement to the user.
            print("This value can't be converted")

    # If kilometer, will convert to millimeter, centimeter, etc.
    if q2 == 'km':
        q3 = input("Enter the measurement you want to convert: ")
        if q3 == 'in':
            a1 = q1 * 39370
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a1}{q3} {color.END}")
        elif q3 == 'ft':
            a2 = q1 * 3281
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a2}{q3} {color.END}")
        elif q3 == 'yard':
            a3 = q1 * 1094
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a3}{q3} {color.END}")
        elif q3 == "mm":
            a4 = q1 * 1000000
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a4}{q3} {color.END}")
        elif q3 == "cm":
            a5 = q1 * 100000
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a5}{q3} {color.END}")
        elif q3 == "m":
            a6 = q1 * 1000
            print(f"{color.BOLD} {q1}{q2} in {q3} its {a6}{q3} {color.END}")
        else:
            # If the software can't convert, then will state the following statement to the user.
            print("This value can't be converted")


if __name__ == "__main__":
    main()
