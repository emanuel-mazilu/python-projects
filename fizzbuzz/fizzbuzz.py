numarMaxim = 100

for i in range(1, numarMaxim):
    
    output = ""
    if i % 3 == 0: output = "FIZZ"
    if i % 5 == 0: output += "BUZZ"
    if output == "": output = i

    print(output)