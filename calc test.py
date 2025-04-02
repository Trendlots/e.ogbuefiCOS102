from enum import Enum


class RPS(Enum):
    ADDITION = "1"
    SUBTRACTION = 2
    DIVISION = 3
    MULTIPLICATION = 4


title = "KEY".upper()
print(title.center(50, "="))
print("ADDTION".ljust(45, ".") + "1".rjust(5))
print("SUBTARCTION".ljust(45, ".") + "2".rjust(5))
print("DIVISION".ljust(45, ".") + "3".rjust(5))
print("MULTIPLICATION".ljust(45, ".") + "4".rjust(5))

print(" ")
print("Hello there i am a calculator")
func = (input("What type of maths do you want to be carried out:"))


if func == "1":
    print("So you choose"+" "+str(RPS(func)).replace("RPS.", " "))
    num1_add = (int(input("Give me the First number:")))
    num2_add = (int(input("Give me the Second number:")))
    num1_add_str = str(num1_add)
    num2_add_str = str(num2_add)
    con = input("So youre trying to add"+" "+num1_add_str +
                " "+"and"+' '+num2_add_str+"(Y/N):")
    ok = "Y"
    rty = "y"
    if con == ok or con == rty:
        add = num1_add+num2_add
        add_str = str(add)
        print("And your answer is:"+" "+add_str)
    else:
        print("Is that so? ok im ending the Program 🤦‍♂️")
        quit(" ")


elif func == "2":
    num1_sub = (int(input("Give me the First number:")))
    num2_sub = (int(input("Give me the Second number:")))
    num1_sub_str = str(num1_sub)
    num2_sub_str = str(num2_sub)
    con = input("So its going to be"+" "+num1_sub_str+" " +
                "subtracted by"+" "+num2_sub_str+"(Y/N):")
    ok = "Y"
    ik = "y"
    on = "yes"
    if con == ok or con == ik or on == "yes":
        sub = num1_sub - num2_sub
        sub_str = str(sub)
        print("And your answer is:"+" "+sub_str)
    else:
        print("R u sure that not the correct number? if so bye bye")
        quit(" ")
elif func == "3":
    num1_div = (int(input("Give me the First number:")))
    num2_div = (int(input("Give me the Second number:")))
    num1_div_str = str(num1_div)
    num2_div_str = str(num2_div)
    con = input("So its going to be"+" "+num1_div_str +
                " "+"divided by"+" "+num2_div_str+" (Y/N):")
    ok = "Y"
    ik = "y"
    if con == ok or con == ik:
        div = num1_div/num2_div
        div_str = str(div)
        print("And your answer is:"+" "+div_str)
    else:
        print("Are you sure abt that? I mean if you say so¯\\_(ツ)_/¯")
        quit(" ")
elif func == "4":
    num1_mul = (int(input("Give me the First number:")))
    num2_mul = (int(input("Give me the Second number:")))
    num1_mul_str = str(num1_mul)
    num2_mul_str = str(num1_mul)
    con = input("So its going to be"+" "+num1_mul_str+" " +
                "multiplied by"+" "+num2_mul_str+"(Y/N):")
    ok = "Y"
    ik = "y"
    if con == ok or con == ik:
        mul = num1_mul*num2_mul
        mul_str = str(mul)
        print("And your answer is:"+" "+mul_str)
    else:
        print("Are you sure abt that? I mean If you say so¯\\_(ツ)_/¯ BYE BYE")
        quit(" ")

# THIS PLACE IS NOT NEEDED LIKE THAT
# THIS PLACE IS NOT NEEDED LIKE THAT
# THIS PLACE IS NOT NEEDED LIKE THAT
# ===================================================================================================================

else:
    print(" ")
    input("Input a number from the KEY. (Either from 1-4)")
    input("Lets run that one more time")
    title = "KEY".upper()
    print(title.center(50, "="))
    print("ADDTION".ljust(45, ".") + "1".rjust(5))
    print("SUBTARCTION".ljust(45, ".") + "3".rjust(5))
    print("DIVISION".ljust(45, ".") + "3".rjust(5))
    print("MULTIPLICATION".ljust(45, ".") + "4".rjust(5))

    print(" ")
    print("Hello there i am a calculator")
    func = (input("What type of maths do you want to be carried out:"))
    if func == "1":
        num1_add = (int(input("Give me the First number:")))
        num2_add = (int(input("Give me the Second number:")))
        num1_add_str = str(num1_add)
        num2_add_str = str(num2_add)
        con = input("So youre trying to add"+" "+num1_add_str +
                    " "+"and"+' '+num2_add_str+"(Y/N):")
        ok = "Y"
        ik = "y"
        if con == ok or con == ik:
            add = num1_add+num2_add
            add_str = str(add)
            print("And your answer is:"+" "+add_str)
        else:
            print("Is that so? ok im ending the Program")
            quit()
    elif func == "2":
        num1_sub = (int(input("Give me the First number:")))
        num2_sub = (int(input("Give me the Second number:")))
        num1_sub_str = str(num1_sub)
        num2_sub_str = str(num2_sub)
        con = input("So its going to be"+" "+num1_sub_str+" " +
                    "subtracted by"+" "+num2_sub_str+"(Y/N):")
        ok = "Y"
        ik = "y"
        if con == ok or con == ik:
            sub = num1_sub - num2_sub
            sub_str = str(sub)
            print(f"And your answer is:{sub_str}")
        else:
            print("R u sure that not the correct number? if so bye bye")
            quit()
    elif func == "3":
        num1_div = (int(input("Give me the First number:")))
        num2_div = (int(input("Give me the Second number:")))
        num1_div_str = str(num1_div)
        num2_div_str = str(num2_div)
        con = input("So its going to be"+" "+num1_div_str +
                    " "+"divided by"+" "+num2_div_str+" (Y/N):")
        ok = "Y"
        ik = "y"
        if con == ok or con == ik:
            div = num1_div/num2_div
            div_str = str(div)
            print("And your answer is:"+" "+div_str)
        else:
            print("Are you sure abt that? I mean if you say so¯\\_(ツ)_/¯")
            quit()
    elif func == "4":
        num1_mul = (int(input("Give me the First number:")))
        num2_mul = (int(input("Give me the Second number:")))
        num1_mul_str = str(num1_mul)
        num2_mul_str = str(num1_mul)
        con = input("So its going to be"+" "+num1_mul_str+" " +
                    "multiplied by"+" "+num2_mul_str+"(Y/N):")
        ok = "Y"
        ik = "y"
        if con == ok or con == ik:
            mul = num1_mul*num2_mul
            mul_str = str(mul)
            print("And your answer is:"+" "+mul_str)
        else:
            print("Are you sure abt that? I mean If you say so¯\\_(ツ)_/¯ BYE BYE")
            quit()
    else:
        quit("its like youre not ready, bye bye")
