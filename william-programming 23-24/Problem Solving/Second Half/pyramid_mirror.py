def pyramid_mirror(x):
    for i in range(x):
        for j in range(x - i - 1):
            print(" ")
        for j in range(i + 1):
            print("*")
        print()

a = int(input("Enter the height of the mirrored pyramid: "))
pyramid_mirror(a)
