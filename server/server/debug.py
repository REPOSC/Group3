def debug(debug):
    my_file = open('debug.txt', 'a')
    print(debug, file=my_file, end='\n')
    my_file.close()