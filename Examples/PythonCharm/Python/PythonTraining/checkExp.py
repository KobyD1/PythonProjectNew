input = 2
isRepeat = True
while isRepeat :
    input = input / 2
    inputMod = input % 2

    if inputMod != 0:
        print('not Exp of 2 number found')

        isRepeat = False

    elif input == 2:
        print('entered number is Exp of 2 ')
        isRepeat = False
    elif (inputMod == 0.0) &(input !=1.0) :
        isRepeat = True


