



def safe_input(prompt,options):

    print(prompt)
    for option in options:
        first_letter = option[0]
        first_letters = first_letter.casefold()
        print("("+option[0].upper()+")"+option[1:(len(option)+1)])
    a = str(input("?"))
    a = a.casefold()
    if a not in first_letters:
        print(a, "is not an option.")
        safe_input(prompt,options)
    else: return a



