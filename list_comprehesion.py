def correr():

    #squares = []
    #for i in range(1,101):
    #    squares.append(i**2)
    #print(squares)

    #squares = []
    #for i in range(1,101):
    #    if i % 3 !=0:
    #        squares.append(i**2)
    #print(squares)

    #squares = [i**2 for i in range(1,101) if i%3 !=0]
    #print(squares)
    numbers = [i for i in range(100000) if i % 9 == 0 and i % 6 == 0 and i % 4 == 0]
    print(numbers)

if __name__ == '__main__': # Es para inicializar la funcion
    correr()
