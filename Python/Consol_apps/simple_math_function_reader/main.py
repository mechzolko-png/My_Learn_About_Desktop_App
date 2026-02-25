while True:
    main = input("> ")
    mainfix = main.replace(" ", "")
    mainparts = mainfix.split("=")

    main1 = mainparts[0]
    main2 = mainparts[1]

    important = main1.split("(")[1].replace(")", "")

    # x előjel kezelése
    x = int(input("x value> "))
    if important == "-x":
        x = -x

    # Megkeressük hol van az x
    x_index = main2.find("x")

    multiplier_part = main2[:x_index]
    lifting_part = main2[x_index+1:]

    # Multiplier kezelés
    if multiplier_part == "" or multiplier_part == "+":
        multiplier = 1
    elif multiplier_part == "-":
        multiplier = -1
    else:
        multiplier = int(multiplier_part)

    # Lifting kezelés
    if lifting_part == "":
        lifting = 0
    else:
        lifting = int(lifting_part)

    result = multiplier * x + lifting
    print("result:", result)