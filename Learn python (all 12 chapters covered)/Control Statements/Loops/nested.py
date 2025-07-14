for i in range(1,3):
    
    """
    i = 1
        j = 3, j = 4, j = 5
        
        i = 1
        j = 3
        
        1,4
        1,5
        
    i = 2
        j = 3, j = 4, j = 5
        
        2,3
        2,4
        2,5
    """
    for j in range(3,6):
        print(f'{i},{j}')