def make_pizza(size,*toppings):
    
    if size == 16:
        menu = 1
    elif size == 18:
        menu = 2
    print("\nMaking a" + str(size) + "-inch pizzawith the")
    for toping in toppings:
        print("-",size, toping,menu)
    print(type(menu))

make_pizza(16,'pepperoni')

make_pizza(18,'mushrooms','green peppers','extra cheese')




    
