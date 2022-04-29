from datetime import datetime

presidents ={"Johnson":(1908, 8,27),
            "Nixon":(1913, 1, 9),
            "Ford": (1913, 7, 14),
            "Carter": (1924, 10, 1),
            "Reagan": (1911, 2, 6),
            "G H Bush": (1924, 6, 12),
            "Clinton": (1946, 8, 19),
            "G Bush": (1946, 7, 6),
            "Obama": (1961, 8, 4),
            "Trump": (1946, 6, 14)}

    # for each president

for president in presidents:

    # look at their birthday
    birthday = datetime(*presidents[president])
    formattedbirthday = birthday.strftime("%d %B %Y")

    #display the name and the birthday
    s = f"{president}, born on {formattedbirthday}"


    #birthday
    if birthday.weekday()==0:
        s = s + " : Born on a Monday"

    print(s)

