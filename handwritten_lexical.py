import re

def tokenize(code):

    token_specification = [
        ('DECIMAL', r'\d+.\d+'),
        ('NUMBER',   r'\d+'),       
        ('ASSIGN',   r'='),                     
        ('HEADER', r'<stdio.h>'),
        ('COMMENT', r'//.*'), 
        ('OPERATOR', r'[+\-*/]'),               
        ('KEYWORD', r'(int|float|double|void)'),
        ('SYMBOL',r'[,;()\[\]\{\}\>\<\\\/\"\.]'),           
        ('NEWLINE', r'\n'),                   
        ('SKIP', r'[ \t]+'),               
        ('PREPROCESSING_DIRECTIVE', r'#include'),
        
        ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z_0-9]*'),
        ('MISMATCH', r'.'),                     
    ]
    
    tokens_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for match in re.finditer(tokens_regex, code):
        type = match.lastgroup
        value = match.group()
        column = match.start() - line_start
        if type == 'NUMBER':
            yield (type, value, line_num)
        elif type == 'IDENTIFIER':
            yield (type, value, line_num)
        elif type == "DECIMAL":
            yield (type, value, line_num)
        elif type == 'OPERATOR':
            yield (type, value, line_num)
        elif type == 'ASSIGN':
            yield (type, value, line_num)
        elif type == 'KEYWORD':
            yield (type, value, line_num)
        elif type == 'SYMBOL':
            yield (type, value, line_num)
        elif type == 'PREPROCESSING_DIRECTIVE':
            yield (type, value, line_num)
        elif type == 'HEADER':
            yield (type, value, line_num)
        elif type == "COMMENT":
            yield (type, value, line_num)
        elif type == 'NEWLINE':
            line_start = match.end()
            line_num += 1
        elif type == 'SKIP':
            pass
        else:
            yield ('MISMATCH', value, line_num, column)
            print(f'Illegal character: {value}')


with open('sample.c', 'r') as file:
    code = file.read()
for token in tokenize(code):
    print(token)
