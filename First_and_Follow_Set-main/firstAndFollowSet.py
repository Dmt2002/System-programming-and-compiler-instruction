import json


with open('grammar.json') as f:
    grammar = json.load(f)


first = {}
follow = {}


def is_terminal(symbol):
    return symbol.islower()


def compute_first(symbol):

    if symbol in first:
        return first[symbol]

    if is_terminal(symbol):
        first[symbol] = {symbol}
        return {symbol}

    first[symbol] = set()
    for production in grammar[symbol]:
        for i in range(len(production)):
            first_i = compute_first(production[i])
            first[symbol] |= first_i
            if not 'epsilon' in first_i:
                break
        else:
            first[symbol].add('epsilon')
    return first[symbol]


def compute_follow(symbol):

    if symbol in follow:
        return follow[symbol]

    follow[symbol] = set()

    for nonterminal in grammar:
        for production in grammar[nonterminal]:
            for i in range(len(production)):
                if production[i] == symbol:
                    if i == len(production) - 1:

                        if nonterminal != symbol:
                            follow[symbol] |= compute_follow(nonterminal)
                    else:

                        if is_terminal(production[i+1]):
                            follow[symbol].add(production[i+1])

                        else:
                            follow[symbol] |= compute_first(production[i+1])

                            if 'epsilon' in compute_first(production[i+1]):
                                if nonterminal != symbol:
                                    follow[symbol] |= compute_follow(nonterminal)
    return follow[symbol]


for nonterminal in grammar:
    compute_first(nonterminal)
    compute_follow(nonterminal)
    
for nonterminal in grammar:
    first_set = ' | '.join(sorted(first[nonterminal]))
    follow_set = ' | '.join(sorted(follow[nonterminal] | {'$'}))
    print(f'First({nonterminal}) = { {first_set} }')
    print(f'Follow({nonterminal}) = { {follow_set} }')
    print('----------------------------------------')
