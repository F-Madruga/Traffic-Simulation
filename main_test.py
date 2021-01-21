from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import City_gen as cg

#_file="Exemplos/intersec_2.txt"
inp = cg.read_block(_file="Exemplos/intersec_3.txt")
block = cg.block_gen(inp=inp)
print(block)

cg.display(block)
