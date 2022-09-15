def draw_park():
    print("This is a park")
    
    
    side = 9
    i = 0

    while(i < side):
        j = 0
        while(j < side):      
            j = j + 1
            print('*', end = '  ')
        i = i + 1
        print('')
    return
