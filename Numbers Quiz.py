'''
Programmed by Matthew Unrue for his Japanese students.
Version 0.3
9/18/2017 & 9/21/2017
Quiz on the pronunciation and writing of numbers between 0 and 99,999,999 in Japanese.
'''
# Imports
import random

# Version Constants
DEFAULT_LOW = 0
DEFAULT_HIGH = 99999999
MAX_LOW = 0
MAX_HIGH = 99999999

# If troubleshooting is true, more information will be displayed about the program's inner workings.
troubleshooting = False


''' Define the pronunciation function. '''
def get_pronunciation(number):
    
    # If troubleshooting, print this information
    if troubleshooting:
        print("TROUBLESHOOTING|Number: " + str(number))
        
        
    # If the given number is 0, don't bother with any of the other code.
    if number == 0:
        # If troubleshooting, print this information
        if troubleshooting:
            print("TROUBLESHOOTING|Number is 0. Returning pronunciation as れい.")
        
        pronunciation = "れい"
        return pronunciation
    
    
    # Calculate the number of digits.
    total_digits = len(str(number))
    # If troubleshooting, print this information
    if troubleshooting:
        print("TROUBLESHOOTING|Total number of digits in number: " + str(total_digits))
        print("")
    
    
    # Define the digit terms based on the array index for ease of use.
    digit_dict = {
        # Digit number from right to left: "Term for place of digit in English.",
        0: "Singles",
        1: "Tens",
        2: "Hundreds",
        3: "Thousands",
        4: "Ten Thousands",
        5: "Hundred Thousands",
        6: "Millions",
        7: "Ten Millions",
        8: "Hundred Millions"
    }
    
    # Define the pronunciations for the Singles place.
    singles_dict = {
        0: "",
        1: "いち",
        2: "に",
        3: "さん",
        4: "よん",
        5: "ご",
        6: "ろく",
        7: "なな",
        8: "はち",
        9: "きゅう"
    }
    
    # Define the pronunciations for the Tens place.
    tens_dict = {
        0: "",
        1: "じゅう",
        2: "にじゅう",
        3: "さんじゅう",
        4: "よんじゅう",
        5: "ごじゅう",
        6: "ろくじゅう",
        7: "ななじゅう",
        8: "はちじゅう",
        9: "きゅうじゅう"
    }
    
    # Define the pronunciations for the Hundreds place.
    hundreds_dict = {
        0: "",
        1: "ひゃく",
        2: "にひゃく",
        3: "さんびゃく",
        4: "よんひゃく",
        5: "ごひゃく",
        6: "ろっぴゃく",
        7: "ななひゃく",
        8: "はっぴゃく",
        9: "きゅうひゃく"
    }
    
    # Define the pronunciations for the Thousands place.
    thousands_dict = {
        0: "",
        1: "せん",
        2: "にせん",
        3: "さんぜん",
        4: "よんせん",
        5: "ごせん",
        6: "ろくせん",
        7: "ななせん",
        8: "はっせん",
        9: "きゅうせん"
    }
    
    # Define the pronunciations for the Ten Thousands place.
    ten_thousands_dict = {
        0: "",
        1: "いちまん",
        2: "にまん",
        3: "さんまん",
        4: "よんまん",
        5: "ごまん",
        6: "ろくまん",
        7: "ななまん",
        8: "はちまん",
        9: "きゅうまん"
    }
    
    
    ''' Create the pronunciation. '''
    # Create a blank string to hold each part of the pronunciation.
    pronunciation = ""
    
        
    # Recursively call the pronunciation algorithm to determine the pronunciations
    # from 100,000 to 99,999,999, then add the chunk of text to the pronunciation variable.
    
    current_number = number
    current_digits = len(str(current_number))
    
    # 6 digit numbers
    if total_digits >= 6 and total_digits <= 8:
        if total_digits == 6:
            # If troubleshooting, print this information
            if troubleshooting:
                print("TROUBLESHOOTING|Six digits.")
                print("TROUBLESHOOTING|RECURSIVELY CALLING get_pronunciaton FUNCTION.")
            
            
            # The number of ten thousands in a 6 digit number is the first 2 digits.
            ten_thousands = int(str(number)[:2])
            pronunciation = pronunciation + get_pronunciation(ten_thousands) + "まん"
            
            # Adjust the current number to account for the 5th and 6th digits being done already.
            current_number = int(str(number)[-4:])
            current_digits = 4
            
            # If troubleshooting, print this information
            if troubleshooting:
                print("")
                print("TROUBLESHOOTING|Previous Final Pronunciation was for the ten thousands and above.")
                print("TROUBLESHOOTING|Pronunciation so far: " + str(pronunciation))
                print("TROUBLESHOOTING|Remaining number: " + str(current_number))
                print("TROUBLESHOOTING|Now building the pronunciation for this number.")
            
           
        # 7 digit numbers.
        elif total_digits == 7:
            # If troubleshooting, print this information
            if troubleshooting:
                print("TROUBLESHOOTING|Seven digits.")
                print("TROUBLESHOOTING|RECURSIVELY CALLING get_pronunciaton FUNCTION.")            
            
            
            # The number of ten thousands in a 7 digit number is the first 3 digits.
            ten_thousands = int(str(number)[:3])
            pronunciation = pronunciation + get_pronunciation(ten_thousands) + "まん"
            
            # Adjust the current number to account for the 5th, 6th and 7th digits being done already.
            current_number = int(str(number)[-4:])
            current_digits = 4
            
            # If troubleshooting, print this information
            if troubleshooting:
                print("")
                print("TROUBLESHOOTING|Previous Final Pronunciation was for the ten thousands and above.")
                print("TROUBLESHOOTING|Pronunciation so far: " + str(pronunciation))
                print("TROUBLESHOOTING|Remaining number: " + str(current_number))
                print("TROUBLESHOOTING|Now building the pronunciation for this number.")
            
    
        # 8 digit numbers
        elif total_digits == 8:
            # If troubleshooting, print this information
            if troubleshooting:
                print("TROUBLESHOOTING|Eight digits.")
                print("TROUBLESHOOTING|RECURSIVELY CALLING get_pronunciaton FUNCTION.")            
            
            
            # The number of ten thousands in an 8 digit number is the first 2 digits.
            ten_thousands = int(str(number)[:4])
            pronunciation = pronunciation + get_pronunciation(ten_thousands) + "まん"
            
            # Adjust the current number to account for the 5th, 6th, 7th, and 8th digits being done already.
            current_number = int(str(number)[-4:])
            current_digits = 4
            
            # If troubleshooting, print this information
            if troubleshooting:
                print("")
                print("TROUBLESHOOTING|Previous Final Pronunciation was for the ten thousands and above.")
                print("TROUBLESHOOTING|Pronunciation so far: " + str(pronunciation))
                print("TROUBLESHOOTING|Remaining number: " + str(current_number))
                print("TROUBLESHOOTING|Now building the pronunciation for this number.")            
    
    
    
    # Check for accurate assessment of the numerals in each digit.
    for index, digit in enumerate(str(current_number)):
        
        # Print the actual number in the digit place.
        if troubleshooting:
            print("TROUBLESHOOTING|Current number: " + digit)
        
        
        # Calculate the place of the current number.
        place = current_digits - index - 1
        
        
        # If troubleshooting, print this information
        if troubleshooting:
            print("TROUBLESHOOTING|" + str(digit_dict[place]))
        
        
        
        # Get the pronunciation of each digit below 100,000.
                
        # SINGLES
        if place == 0:
            # If troubleshooting, print this information
            if troubleshooting:
                print("TROUBLESHOOTING|" + str(singles_dict[int(digit)]))
            
            # Add the digits' pronunciation to the number pronunciation.
            pronunciation = pronunciation + singles_dict[int(digit)]
            
            
        # TENS
        elif place == 1:
            # If troubleshooting, print this information
            if troubleshooting:
                print("TROUBLESHOOTING|" + str(tens_dict[int(digit)]))
            
            # Add the digits' pronunciation to the number pronunciation.
            pronunciation = pronunciation + tens_dict[int(digit)]
            
            
        # HUNDREDS
        elif place == 2:
            # If troubleshooting, print this information
            if troubleshooting:
                print("TROUBLESHOOTING|" + str(hundreds_dict[int(digit)]))
            
            # Add the digits' pronunciation to the number pronunciation.
            pronunciation = pronunciation + hundreds_dict[int(digit)]
            
            
        # THOUSANDS
        elif place == 3:
            # If troubleshooting, print this information
            if troubleshooting:
                print("TROUBLESHOOTING|" + str(thousands_dict[int(digit)]))
            
            # Add the digits' pronunciation to the number pronunciation.
            pronunciation = pronunciation + thousands_dict[int(digit)]
            
            
        # TEN THOUSANDS
        elif place == 4:
            # If troubleshooting, print this information
            if troubleshooting:
                print("TROUBLESHOOTING|" + str(ten_thousands_dict[int(digit)]))
                
            # Add the digits' pronunciation to the number pronunciation.
            pronunciation = pronunciation + ten_thousands_dict[int(digit)]
    
    
    
    # Print the final pronunciation.
    if troubleshooting:
        print("TROUBLESHOOTING|Final Pronunciation: " + str(pronunciation))
        print("TROUBLESHOOTING|Returning the final pronunciation now.")
        
    return pronunciation



''' Define the kanji function. '''
def get_kanji(number):
    # If troubleshooting, print this information
    if troubleshooting:
        print("TROUBLESHOOTING|Number: " + str(number))
        
        
    # If the given number is 0, don't bother with any of the other code.
    if number == 0:
        # If troubleshooting, print this information
        if troubleshooting:
            print("TROUBLESHOOTING|Number is 0. Returning kanji as 零.")
            
        kanji = "零"
        return kanji
    
    
    # Calculate the number of digits.
    total_digits = len(str(number))
    # If troubleshooting, print this information
    if troubleshooting:
        print("TROUBLESHOOTING|Total number of digits in number: " + str(total_digits))
        print("")
    
    
    # Define the digit terms based on the array index for ease of use.
    digit_dict = {
        0: "Singles",
        1: "Tens",
        2: "Hundreds",
        3: "Thousands",
        4: "Ten Thousands",
        5: "Hundred Thousands",
        6: "Millions",
        7: "Ten Millions",
        8: "Hundred Millions"
    }
    
    # Define the kanji for the Singles place.
    singles_dict = {
        0: "",
        1: "一",
        2: "二",
        3: "三",
        4: "四",
        5: "五",
        6: "六",
        7: "七",
        8: "八",
        9: "九"
    }
    
    # Define the kanji for the Tens place.
    tens_dict = {
        0: "",
        1: "十",
        2: "二十",
        3: "三十",
        4: "四十",
        5: "五十",
        6: "六十",
        7: "七十",
        8: "八十",
        9: "九十"
    }
    
    # Define the kanji for the Hundreds place.
    hundreds_dict = {
        0: "",
        1: "百",
        2: "二百",
        3: "三百",
        4: "四百",
        5: "五百",
        6: "六百",
        7: "七百",
        8: "八百",
        9: "九百"
    }
    
    # Define the kanji for the Thousands place.
    thousands_dict = {
        0: "",
        1: "千",
        2: "二千",
        3: "三千",
        4: "四千",
        5: "五千",
        6: "六千",
        7: "七千",
        8: "八千",
        9: "九千"
    }
    
    # Define the kanji for the Ten Thousands place.
    ten_thousands_dict = {
        0: "",
        1: "一万",
        2: "二万",
        3: "三万",
        4: "四万",
        5: "五万",
        6: "六万",
        7: "七万",
        8: "八万",
        9: "九万"
    }
    
    
    ''' Create the kanji text. '''
    # Create a blank string to hold each part of the text.
    kanji = ""
    
        
    # Recursively call the pronunciation algorithm to determine the pronunciations
    # from 100,000 to 99,999,999, then add the chunk of text to the pronunciation variable.
    
    current_number = number
    current_digits = len(str(current_number))
    
    # 6 digit numbers
    if current_digits >= 6 and current_digits <= 8:
        if current_digits == 6:
            # If troubleshooting, print this information
            if troubleshooting:
                print("TROUBLESHOOTING|Six digits.")
                print("TROUBLESHOOTING|RECURSIVELY CALLING get_kanji FUNCTION.")
            
            
            # The number of ten thousands in a 6 digit number is the first 2 digits.
            ten_thousands = int(str(number)[:2])
            kanji = kanji + get_kanji(ten_thousands) + "万"
            
            # Adjust the current number to account for the 5th and 6th digits being done already.
            current_number = int(str(number)[-4:])
            current_digits = 4
            
            # If troubleshooting, print this information
            if troubleshooting:
                print("")
                print("TROUBLESHOOTING|Previous Final Kanji was for the ten thousands and above.")
                print("TROUBLESHOOTING|Kanji so far: " + str(kanji))
                print("TROUBLESHOOTING|Remaining number: " + str(current_number))
                print("TROUBLESHOOTING|Now building the kanji for this number.")
            
           
        # 7 digit numbers.
        elif current_digits == 7:
            # If troubleshooting, print this information
            if troubleshooting:
                print("TROUBLESHOOTING|Seven digits.")
                print("TROUBLESHOOTING|RECURSIVELY CALLING get_kanji FUNCTION.")
            
            
            # The number of ten thousands in a 7 digit number is the first 3 digits.
            ten_thousands = int(str(number)[:3])
            kanji = kanji + get_kanji(ten_thousands) + "万"
            
            # Adjust the current number to account for the 5th, 6thand 7th digits being done already.
            current_number = int(str(number)[-4:])
            current_digits = 4
            
            # If troubleshooting, print this information
            if troubleshooting:
                print("")
                print("TROUBLESHOOTING|Previous Final Kanji was for the ten thousands and above.")
                print("TROUBLESHOOTING|Kanji so far: " + str(kanji))
                print("TROUBLESHOOTING|Remaining number: " + str(current_number))
                print("TROUBLESHOOTING|Now building the kanji for this number.")           
            
    
        # 8 digit numbers
        elif current_digits == 8:
            # If troubleshooting, print this information
            if troubleshooting:
                print("TROUBLESHOOTING|Eight digits.")
                print("TROUBLESHOOTING|RECURSIVELY CALLING get_kanji FUNCTION.")
            
            
            # The number of ten thousands in an 8 digit number is the first 2 digits.
            ten_thousands = int(str(number)[:4])
            kanji = kanji + get_kanji(ten_thousands) + "万"
            
            # Adjust the current number to account for the 5th, 6th, 7th, and 8th digits being done already.
            current_number = int(str(number)[-4:])
            current_digits = 4
            
            # If troubleshooting, print this information
            if troubleshooting:
                print("")
                print("TROUBLESHOOTING|Previous Final Kanji was for the ten thousands and above.")
                print("TROUBLESHOOTING|Kanji so far: " + str(kanji))
                print("TROUBLESHOOTING|Remaining number: " + str(current_number))
                print("TROUBLESHOOTING|Now building the kanji for this number.")           
    
    
    
    # Check for accurate assessment of the numerals in each digit.
    for index, digit in enumerate(str(current_number)):
        
        # Print the actual number in the digit place.
        if troubleshooting:
            print("TROUBLESHOOTING|Current number: " + digit)
        
        
        # Calculate the place of the current number.
        place = current_digits - index - 1
        
        
        # If troubleshooting, print this information
        if troubleshooting:
            print("TROUBLESHOOTING|" + str(digit_dict[place]))
        
        
        
        # Get the kanji of each digit below 100,000.
                
        # SINGLES
        if place == 0:
            # If troubleshooting, print this information
            if troubleshooting:
                print("TROUBLESHOOTING|" + str(singles_dict[int(digit)]))
            
            # Add the digits' kanji to the text.
            kanji = kanji + singles_dict[int(digit)]
            
            
        # TENS
        elif place == 1:
            # If troubleshooting, print this information
            if troubleshooting:
                print("TROUBLESHOOTING|" + str(tens_dict[int(digit)]))
            
            # Add the digits' kanji to the text.
            kanji = kanji + tens_dict[int(digit)]
            
            
        # HUNDREDS
        elif place == 2:
            # If troubleshooting, print this information
            if troubleshooting:
                print("TROUBLESHOOTING|" + str(hundreds_dict[int(digit)]))
            
            # Add the digits' kanji to the text.
            kanji = kanji + hundreds_dict[int(digit)]
            
            
        # THOUSANDS
        elif place == 3:
            # If troubleshooting, print this information
            if troubleshooting:
                print("TROUBLESHOOTING|" + str(thousands_dict[int(digit)]))
            
            # Add the digits' kanji to the text.
            kanji = kanji + thousands_dict[int(digit)]
            
            
        # TEN THOUSANDS
        elif place == 4:
            # If troubleshooting, print this information
            if troubleshooting:
                print("TROUBLESHOOTING|" + str(ten_thousands_dict[int(digit)]))
                
            # Add the digits' kanji to the text.
            kanji = kanji + ten_thousands_dict[int(digit)]
    
    
    
    # Print the final text.
    if troubleshooting:
        print("TROUBLESHOOTING|Final Kanji: " + str(kanji))
        print("TROUBLESHOOTING|Returning the final kanji now.")
        
    return kanji
    
   
   
''' Main program. '''
# Lowest number to quiz.
low_check = True
while low_check:
    low = input("What is the lowest number to quiz? The default is " + str(DEFAULT_LOW) + ". ")
    
    # If the input is blank, default to DEFAULT_LOW.
    if low == "":
        low = DEFAULT_LOW
        low_check = False
    # If the input is a valid number, save the input as an integer.
    elif int(low) < MAX_HIGH and int(low) >= MAX_LOW:
        low_check = False
        low = int(low)
    else:
        print("Please input a valid number between " + str(MAX_LOW) + " and " + str(MAX_HIGH - 1) + ".")
        print("")
        

# Highest number to quiz, default to DEFAULT_HIGH.
high_check = True
while high_check:
    high = input("What is the highest number to quiz? The default is " + str(DEFAULT_HIGH) + ". ")
    
    # If the input is blank, default to DEFAULT_HIGH.
    if high == "":
        high = DEFAULT_HIGH
        high_check = False
    # If the input is a valid number, save the input as an integer.
    elif int(high) <= MAX_HIGH and int(high) > low:
        high_check = False
        high = int(high)
    else:
        print("Please input a valid number between " + str(low + 1) + " and " + str(MAX_HIGH) + ".")
        print("")
        
        
print("")
print("Quizzing from " + str(low) + " to " + str(high) + ".")
print("")


# Select mode of quizzing. 0 = English to Japanese. 1 = Japanese to English.
mode_check = True
while mode_check:
    mode = input("Quiz from English to Japanese? True/False: ")
    if mode.lower() == "true" or mode.lower() == "":
        mode = 0
        mode_check = False
        print("Quizzing from English to Japanese.")
    elif mode.lower() == "false":
        mode = 1
        mode_check = False
        print("Quizzing from Japanese to English.")
    else:
        print("Please input true or false.")
        print("")
        
        
# Select whether or not to use Kanji instead of Hiragana.
kanji_check = True
while kanji_check:
    kanji_mode = input("Use Kanji instead of Hiragana? Default is false. True/False: ")
    if kanji_mode.lower() == "false" or kanji_mode.lower() == "":
        kanji_mode = False
        kanji_check = False
        print("Quizzing with Hiragana.")
    elif kanji_mode.lower() == "true":
        kanji_mode = True
        kanji_check = False
        print("Quizzing with Kanji.")
    else:
        print("Please input true or false.")
        print("")    
    


''' Main quiz loop. '''
quizzing = True
print('Type "quit" to quit.')
input("Press enter to continue.")
print("")

while quizzing:
    # Randomly produce the current number from the given range of numbers.
    instance_number = random.randint(low, high)
    if not kanji_mode:
        instance_pronunciation = get_pronunciation(instance_number)
    if kanji_mode:
        instance_kanji = get_kanji(instance_number)
    
    
    ''' English to Japanese '''
    if mode == 0:
        # Give the number/text to translate or answer and check for the quit command.
        number_text = "Number: " + str(instance_number) + " "
        check = input(number_text)
        
        if check.lower() == "quit":
            quizzing = False
            break
        
        # Give the pronunciation or knaji and check for the quit command.
        # Kanji
        if kanji_mode:
            kanji_text = "Kanji: " + instance_kanji + " "
            check = input(kanji_text)        
        
        # Pronunciation
        else:
            pronunciation_text = "Pronunciation: " + instance_pronunciation + " "
            check = input(pronunciation_text)
        
        if check.lower() == "quit":
            quizzing = False 
            break
        
        # Space formatting.
        print("")


    ''' Japanese to English '''
    if mode == 1:
        # Give the pronunciation or kanji and check for the quit command.
        # Kanji
        if kanji_mode:
            kanji_text = "Kanji: " + instance_kanji + " "
            check = input(kanji_text)        
        
        # Pronunciation
        else:
            pronunciation_text = "Pronunciation: " + instance_pronunciation + " "
            check = input(pronunciation_text)
        
        if check.lower() == "quit":
            quizzing = False 
            break
        
        # Give the number/text to translate or answer and check for the quit command.
        number_text = "Number: " + str(instance_number) + " "
        check = input(number_text)
        
        if check.lower() == "quit":
            quizzing = False
            break
        
        
        # Space formatting.
        print("")    
    
    
    # Program is about to loop again. Do any needed cleaning or checks.
    # If troubleshooting, print this information
    if troubleshooting:
        print("")
        print("TROUBLESHOOTING|NEW NUMBER. MAIN PROGRAM HAS LOOPED.")
