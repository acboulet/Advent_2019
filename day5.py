

def int_comp(code_file):
    """
    Purpose:
        Uses the int_comp to process a set of directions relying on parameter codes
        ABCDE
        1002
            DE - two-digit opcode,      02 == opcode 2
            C - mode of 1st parameter,  0 == position mode
            B - mode of 2nd parameter,  1 == immediate mode
            A - mode of 3rd parameter,  0 == position mode,
                                            omitted due to being a leading zero
    Param:
        code_file: .txt file with input values
    Return:
        Final int_code as a list
    """
    new_code = open(code_file, 'r')
    new_code = new_code.readline()
    new_code = new_code.split(',')
    code = [int(x) for x in new_code]
    # Restore code to before alarm
    # code[1] = noun
    # code[2] = verb
    n = 0
    while code[n] != 99:
        # Breakdown the OP code
        OP = str(code[n])
        # Checks if math opcode
        if OP[-1] in '125678':
            # Tracks whether tracker has moved.
            moved = False
            # Adds values so that every OP  code is 4 digits
            while len(OP) != 4:
                OP = '0' + OP
            # Check if parameter values are immediate or position
            if OP[-3] == '1':
                value1 = code[n+1]
            else:
                value1 = code[ code[n+1] ]
            if OP[-4] == '1':
                value2 = code[n+2]
            else:
                value2 = code[ code[n+2] ]
            # Check operator value
            # If OP code is 1, then adds values and assigns to 3rd parameter
            print('---')
            print('n:', n)
            print('OP:', OP)
            print('Value1:', value1)
            print('Value2:', value2)
            # print('Target:', code[code[n+3]])
            if OP[-1] == '1':
                code[ code[n+3] ] = value1 + value2
            # If OP code is 2, then adds values and assigns to 3rd parameter
            elif OP[-1] == '2':
                code[ code[n+3] ] = value1 * value2
            # If OP code is 5, checks if does not equal to zero and moves to second parameter spot
            # If 0, then skips the next two parameters
            elif OP[-1] == '5':
                if value1 != 0:
                    n = value2
                else:
                    n += 3
                moved = True
            # If OP code is 6, checks if equal to 0 and moves to second parameter spot
            # If not 0 then skips next two parameters
            elif OP[-1] == '6':
                if value1 == 0:
                    n = value2
                else:
                    n += 3
                moved = True
            # If OP code is 7, will assign 1 to parameter 3 when v2 > v1   
            elif OP[-1] == '7':
                if value1 < value2:
                    code[ code[n+3] ] = 1
                else:
                    code[ code[n+3] ] = 0
            # If OP code is 8, will assign 1 to parameter 3 when v2 = v1
            elif OP[-1] == '8':
                if value1 == value2:
                    code[ code[n+3] ] = 1
                else:
                    code[ code[n+3] ] = 0
            # If tracker has moved yet because of 5 or 6, then moves 4 spaces
            if not moved:
                n +=4

        # If not a math opcode, then it must be 
        elif OP[-1] in '34':
            while not len(OP) > 3:
                OP = '0' + OP
            print('---')
            print('n', n)
            print('OP:', OP)
            if OP[-1] == '3':
                code[ code[n+1] ]  = int(input('Value to input:'))
            # Need to account for immediate parameter assignment
            elif OP[-1] == '4':
                if OP[-3] == '1':
                    print('Value printed because of int_code: %i' % (code[n+1]))
                else:
                    print('Value printed because of int_code: %i' % (code[ code[n+1] ]))
            n += 2
        else:
            print('Failed with %s' % (OP))
            return code
    return code   

int_comp('day5.txt')