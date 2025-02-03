import tkinter as tk
from tkinter import messagebox
import math

def fibo():
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    n = int(entry_number.get())
    result = [fibonacci(i) for i in range(n)]
    messagebox.showinfo("Fibonacci", f"Fibonacci Sequence: {result}")

def fact():
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    n = int(entry_number.get())
    if n < 0:
        messagebox.showerror("Error", "Enter a Non-Negative Number")
    else:
        result = factorial(n)
        messagebox.showinfo("Factorial", f"Factorial of {n}: {result}")

def prime():
    def isprime(num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    n = int(entry_number.get())
    if isprime(n):
        messagebox.showinfo("Prime Number", "Prime Number")
    else:
        messagebox.showinfo("Prime Number", "Not a Prime Number")

def rev():
    def reverse(x):
        l = x[::-1]
        messagebox.showinfo("Reversed String", f"Reversed String: {l}")
    string = entry_string.get()
    reverse(string)

def sum_of_digits():
    def sod(n):
        if n == 0:
            return 0
        else:
            return n % 10 + sod(n // 10)
    n = int(entry_number.get())
    result = sod(n)
    messagebox.showinfo("Sum of Digits", f"Sum of Digits: {result}")

def mx():
    def max_of_list(l):
        m = max(l)
        messagebox.showinfo("Max of List", f"Max Value: {m}")
    l = [int(x) for x in entry_list.get().split(",")]
    max_of_list(l)

def mn():
    def min_of_list(l):
        m = min(l)
        messagebox.showinfo("Min of List", f"Min Value: {m}")
    l = [int(x) for x in entry_list.get().split(",")]
    min_of_list(l)

def greatest_common_divisor():
    m = int(entry_number1.get())
    n = int(entry_number2.get())
    result = math.gcd(m, n)
    messagebox.showinfo("GCD", f"GCD: {result}")

def least_common_multiple():
    m = int(entry_number1.get())
    n = int(entry_number2.get())
    result = math.lcm(m, n)
    messagebox.showinfo("LCM", f"LCM: {result}")

def vc_check():
    a = entry_string.get()
    v, c = 0, 0
    for n in a.lower():
        if n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u':
            v += 1
        elif n.isalpha():
            c += 1
    messagebox.showinfo("Vowel and Consonant Count", f"Vowel Count: {v}\nConsonant Count: {c}")

def linear_Search():
    l = [int(x) for x in entry_list.get().split(",")]
    s = int(entry_number.get())
    if s in l:
        messagebox.showinfo("Search Result", "Element Found")
    else:
        messagebox.showinfo("Search Result", "Element Not Found")

def binary_search():
    l = [int(x) for x in entry_list.get().split(",")]
    l.sort()
    s = int(entry_number.get())
    low = 0
    high = len(l) - 1
    found = False
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == s:
            found = True
            break
        elif l[mid] < s:
            low = mid + 1
        else:
            high = mid - 1
    if found:
        messagebox.showinfo("Search Result", "Element Found")
    else:
        messagebox.showinfo("Search Result", "Element Not Found")

def armstrong():
    def is_armstrong(number):
        num_str = str(number)
        num_digits = len(num_str)
        sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
        return sum_of_powers == number
    num = int(entry_number.get())
    if is_armstrong(num):
        messagebox.showinfo("Armstrong", f"{num} is an Armstrong number")
    else:
        messagebox.showinfo("Armstrong", f"{num} is not an Armstrong number")

def anagram():
    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    str1 = entry_string.get()
    str2 = entry_string2.get()
    if is_anagram(str1, str2):
        messagebox.showinfo("Anagram", "They are anagrams")
    else:
        messagebox.showinfo("Anagram", "Not anagrams")

root = tk.Tk()
root.title("Math Operations")
root.geometry("500x600")
root.configure(bg="#e6f7ff")

entry_number = tk.Entry(root, width=20)
entry_string = tk.Entry(root, width=20)
entry_string2 = tk.Entry(root, width=20)
entry_number1 = tk.Entry(root, width=20)
entry_number2 = tk.Entry(root, width=20)
entry_list = tk.Entry(root, width=30)

label_number = tk.Label(root, text="Enter a Number", bg="#e6f7ff", font=("Arial", 12))
label_string = tk.Label(root, text="Enter a String", bg="#e6f7ff", font=("Arial", 12))
label_list = tk.Label(root, text="Enter List (comma-separated)", bg="#e6f7ff", font=("Arial", 12))

label_number.grid(row=0, column=0, padx=10, pady=10)
entry_number.grid(row=0, column=1, padx=10, pady=10)
label_string.grid(row=1, column=0, padx=10, pady=10)
entry_string.grid(row=1, column=1, padx=10, pady=10)
label_list.grid(row=2, column=0, padx=10, pady=10)
entry_list.grid(row=2, column=1, padx=10, pady=10)

entry_number1.grid(row=3, column=0, padx=10, pady=10)
entry_number2.grid(row=3, column=1, padx=10, pady=10)

buttons = [
    ("Fibonacci", fibo),
    ("Factorial", fact),
    ("Prime", prime),
    ("Reverse String", rev),
    ("Sum of Digits", sum_of_digits),
    ("Max of List", mx),
    ("Min of List", mn),
    ("GCD", greatest_common_divisor),
    ("LCM", least_common_multiple),
    ("Vowel & Consonant Count", vc_check),
    ("Linear Search", linear_Search),
    ("Binary Search", binary_search),
    ("Armstrong Number", armstrong),
    ("Anagram Check", anagram),
]

for i, (text, command) in enumerate(buttons):
    button = tk.Button(root, text=text, width=20, height=2, command=command, bg="#3399ff", fg="white", font=("Arial", 12))
    button.grid(row=4 + i // 2, column=i % 2, padx=10, pady=10)

root.mainloop()
