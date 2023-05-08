import sys
sys.setrecursionlimit(60)

def first(string):

    first_ = set()
    if string in non_terminals:
        alternatives = productions_dict[string]

        for alternative in alternatives:
            first_2 = first(alternative)
            first_ = first_ |first_2

    elif string in terminals:
        first_ = {string}

    elif string=='' or string=='ε':
        first_ = {'ε'}

    else:
        first_2 = first(string[0])
        if 'ε' in first_2:
            i = 1
            while 'ε' in first_2:
           

                first_ = first_ | (first_2 - {'ε'})
               
                if string[i:] in terminals:
                    first_ = first_ | {string[i:]}
                    break
                elif string[i:] == '':
                    first_ = first_ | {'ε'}
                    break
                first_2 = first(string[i:])
                first_ = first_ | first_2 - {'ε'}
                i += 1
        else:
            first_ = first_ | first_2

    return  first_

def follow(nT):

    follow_ = set()

    prods = productions_dict.items()
    if nT==starting_symbol:
        follow_ = follow_ | {'$'}
    for nt,rhs in prods:
 
        for alt in rhs:
            for char in alt:
                if char==nT:
                    following_str = alt[alt.index(char) + 1:]
                    if following_str=='':
                        if nt==nT:
                            continue
                        else:
                            follow_ = follow_ | follow(nt)
                    else:
                        follow_2 = first(following_str)
                        if 'ε' in follow_2:
                            follow_ = follow_ | follow_2-{'ε'}
                            follow_ = follow_ | follow(nt)
                        else:
                            follow_ = follow_ | follow_2

    return follow_
# terminals = list(map(str, input("Enter the terminals: ").split()))

# non_terminals = list(map(str, input("Enter the non terminals: ").split()))

terminals = ['+','*','a','(',')']

non_terminals = ['E','B','T','Y','F']

starting_symbol = 'E'

productions = ['E->TB','B->+TB/ε','T->FY','Y->*FY/ε','F->a/(E)']

productions_dict = {}

for nT in non_terminals:
    productions_dict[nT] = []

for production in productions:
    nonterm_to_prod = production.split("->")
    alternatives = nonterm_to_prod[1].split("/")
    for alternative in alternatives:
        productions_dict[nonterm_to_prod[0]].append(alternative)

FIRST = {}
FOLLOW = {}

for non_terminal in non_terminals:
    FIRST[non_terminal] = set()

for non_terminal in non_terminals:
    FOLLOW[non_terminal] = set()

for non_terminal in non_terminals:
    FIRST[non_terminal] = FIRST[non_terminal] | first(non_terminal)

FOLLOW[starting_symbol] = FOLLOW[starting_symbol] | {'$'}
for non_terminal in non_terminals:
    FOLLOW[non_terminal] = FOLLOW[non_terminal] | follow(non_terminal)

print("{: ^20}{: ^20}{: ^20}".format('Non Terminals','First','Follow'))
for non_terminal in non_terminals:
    print("{: ^20}{: ^20}{: ^20}".format(non_terminal,str(FIRST[non_terminal]),str(FOLLOW[non_terminal])))
