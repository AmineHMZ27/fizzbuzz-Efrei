def fizzbuzz(number):
    result = ""
    if number % 3 == 0 :
        result += "Fizz"

    if number % 5 == 0 :
        result += "Buzz"

    # Amine Bouffon
    
    return result if result else str(number)