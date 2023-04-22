#The bloody photocopier is broken... Just as you were sneaking around the office to print off your favourite binary code!
#Instead of copying the original, it reverses it: '1' becomes '0' and vice versa.
def broken(inp):
    return ''.join([str((int(i)+1)%2) for i in inp])