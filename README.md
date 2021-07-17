# Python Junior Projects

 This repository will contain all the Python projects that I have created since I started learning Python.
 
 ## Run Locally

Clone the project

```bash
  git clone https://github.com/gaurtvin/python-project
```

## Prerequisites

Make sure that these things were installed before running the code file.

• [Python 3.x](https://www.python.org/downloads/)

•  Tkinter
```cmd
pip install tk
```
• Plyer
```cmd
pip install plyer
```
• Pyshorteners
```cmd
pip install pyshorteners
```

## Contributing

Contributions are always welcome!

## Authors

•  Gaurav Pandey [@gaurtvin](https://www.github.com/gaurtvin)

## Feedback

If you have any feedback, please reach out to me at gauravpandey.feedback@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Code

### All Source will be availabel at here 👇
  
## 1. Acronyms

``` python
def fxn(stng):
        
    # add first letter
    oupt = stng[0]
        
    # iterate over string
    for i in range(1, len(stng)):
        if stng[i-1] == ' ':
              
            # add letter next to space
            oupt += stng[i]

    # uppercase ouput
    oupt = oupt.upper()
    return oupt
  
# input string
inpt1 = input("Enter a First Word Here : ")
  
# output acronym
print(fxn(inpt1))
  
# input string
inpt1 = input("Enter a Second Word Here : ")
  
# output acronym
print(fxn(inpt1))
  
# input string
inpt1 = input("Enter a Third Word Here : ")
  
# output acronym
print(fxn(inpt1))
```
## 2. Age Finder

``` python
birth_year = input('Birth Year : ')
age = 2021 - int(birth_year)
print("You are " + str(age) + " Years Old")
```

## 3. Biography Info

``` python 
def personal_details():
    name = input("Enter your Name here : ")
    age = input("Enter your Age here : ")
    address = input("Enter your Address here : ")
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

personal_details()
``` 
## 4. Dice Simulator
``` python 
import random

while True:
    print('1. roll the dice  2. exit')
    user = int(input("What you want to do\n"))

    if user == 1:
        number = rndom.randint(1,6)
        print(number)
    else:
        break
```
## 5. Digital Clock
``` python 
from tkinter import*
from tkinter.ttk import *

from time import strftime

root =  Tk()
root.title("Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(100, time)

label = Label(root, font=("JetBrains Mono", 80), background="black", foreground="cyan")
label.pack(anchor='center')
time()

mainloop()
```

## 6. Email Slicer
``` python 
email = input("Enter Your Email: ").strip()

domain = email[email.index('@') + 1:]

print(f"Your domain is {domain}")
```

## 7. Madlib Generator
``` python 
color = input("Enter a color: ")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)
```
## 8. Message Notifier
``` python
from plyer import notification

notification.notify( 
	title = "Hello World!", 
	message= "My test Message!", 
	# displaying time 
  timeout=10 
)
```
## 9. Odd or Even
``` python 
import random
number = int(input('Which Number you are thinking: '))

if (number % 2) == 0:
    print("This is Even Number \nGreat..!!")
else:
    print('This is Odd Number \nGreat..!!')
```
## 10. Password Generator
``` python
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-"

all = lower + upper + numbers + symbols
length = 16
password = "".join(random.sample(all, length))
print(password)
```
## 11. Quiz

``` python
# Simple game in python

print('Hi, welcome to the quiz!')
print('Try to get as many questions correct as possible...')

totalQuestions = 4
score = 0

ans = input('1. What is the name of captain of Indian Cricket Team ? ')

if ans.lower() == 'virat kholi':
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('2. What is my age? ')

if ans == "14":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('3. What is my favourite sport? ')

if ans.lower() == "cricket":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('4. What is my favourite food? ')

if ans.lower() == "cheese burger":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


print("Thank you for playing, you got " + str(score) + ' questions correct!' )
percent = (score/totalQuestions) * 100
print("Mark: " + str(int(percent)) + '%')

if percent >= 50:
    print('Nice! You passed!')
else:
    print('Better luck next time')
```
## 12. Quote Bot
``` python
import random

def primary():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  primary()
```
## 13. Url Shortner
``` python
import pyshorteners

s = pyshorteners.Shortener()

print(s.gitio.short('https://github.com/gaurtvin'))
```
