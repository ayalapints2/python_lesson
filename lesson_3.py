
def invertory_summary(my_dict):
    sum = 0
    for   kay , value in my_dict.items():
        sum += value[1]

    return sum


my_dict = {
        "breade": (8, 52),
         "milk": (7, 15)
    }
print (invertory_summary (my_dict ))


def print_args_kwargs(*args,**kwargs):
    for i in args.items():
        print(i)

    for key, value in kwargs.items():
        print(f"{kay} : {value} ")
