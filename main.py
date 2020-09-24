number = input()

if len(number) > 3:
    print("Polysynthetic")
elif len(number) >= 2:
    print("Synthetic")
elif len(number) < 2:
    print("Analytic")
