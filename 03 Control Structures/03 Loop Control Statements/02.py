
for i in range(1, 11):
    if i % 2 == 0:
        print("Skipping even number:", i)
        continue
    if i == 7:
        print("Found the lucky number 7, breaking out of the loop.")
        break
    print("Current number is:", i)
