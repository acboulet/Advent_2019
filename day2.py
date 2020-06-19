#code = '1,0,0,3,99'
#code = '1,9,10,3,2,3,11,0,99,30,40,50'


def int_comp(code_file, noun, verb):
    code = open(code_file, 'r')
    code = code.readline()
    code = code.split(',')
    new_code = [int(x) for x in code]
    code = new_code
    # Restore code to before alarm
    code[1] = noun
    code[2] = verb
    n = 0
    while code[n] != 99:
        # Assign location values based on 1st, 2nd, and 3rd values
        loc1 = code[n+1]
        loc2 = code[n+2]
        target = code[n+3]
        # Check operator value
        if code[n] == 1:
            code[ target ] = code[loc1] + code[loc2]
        elif code[n] == 2:
            code[ target ] = code[loc1] * code[loc2]
        n += 4
    return code       

# final = int_comp('day2.txt', 82, 50)
# print(final[0])
if __name__ == "__main__":
    for noun in range(100):
        for verb in range(100):
            final = int_comp('day2.txt', noun, verb)
            if final[0] == 19690720:
                print('Noun %i' % (noun))
                print('Verb %i' % (verb))
                print('Answer %s' % (verb + noun * 100))