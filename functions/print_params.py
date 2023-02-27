# - Create a function called `print_params`
#   which prints the input parameters
#   (can have multiple number of arguments)


def print_params(*arguments):
    parameters_list = list(arguments)
    for item in parameters_list:
        print(item, end="")
    print("")


print_params(1)
print_params(1, 2, 3, 4, 5)