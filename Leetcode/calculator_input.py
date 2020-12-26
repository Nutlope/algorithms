# Take string input coming from a calculator and output the right value
# Start with just + or -

# Input  -> '5 + 6 - 3 + 10'
# Output -> 18

# More Inputs

# Input -> '5+6  -3 +10'
# Output -> 18

# Input -> '-5-2-2-2'
# Output -> -11

def Eval(expr):
    # turn it into a list
    # new_list = expr.split(' ')
    new_list = list(expr)
    # loop thru and check if number or operator
    num_list = []
    opr_list = []

# .isnumeric() method

    for val in new_list:
        try:
            int(val)
            num_list.append(int(val))
        except ValueError:
            opr_list.append(val)

    result = 0
    print(num_list)
    print(opr_list)
    for i in range(max(len(num_list)-1, len(opr_list))):
        if opr_list[i] == "+":
            result += num_list[i] + num_list[i+1]
        if opr_list[i] == "-":
            result += num_list[i] - num_list[i+1]

    print(result)

# This solution doesn't account for the last edge case
Eval('5+6  -3 +10')