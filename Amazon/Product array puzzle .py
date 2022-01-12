if n == 1:
            #print(0)
            return [1]
    
        i, temp = 1, 1
    
        # Allocate memory for the product array
        prod = [1 for i in range(n)]
    
        # Initialize the product array as 1
    
        # In this loop, temp variable contains product of
        # elements on left side excluding arr[i]
        for i in range(n):
            prod[i] = temp
            temp *= arr[i]
    
            # Initialize temp to 1 for product on right side
        temp = 1
    
        # In this loop, temp variable contains product of
        # elements on right side excluding arr[i]
        for i in range(n - 1, -1, -1):
            prod[i] *= temp
            temp *= arr[i]
    
            # Print the constructed prod array
        # for i in range(n):
        #     print(prod[i], end=" ")
    
        return prod
