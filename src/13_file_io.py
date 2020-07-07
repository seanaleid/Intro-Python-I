"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

### error handling incase the file doesn't exist
### if it exists, it'll run the try portion, if it doesn't it'll run the except portion
try:
    with open("foo.txt") as f:
        text =f.read()
except FileNotFoundError:
    text = None

print(text)

### Code on lines 20-23 is one approach, but isn't the safest because you could be interrupted and then you have an open file. Using with assures that even if you don't 
### close the file with f.close() it's closed anyways.
### code block lines17 - 20 is a shorter and safer way to open and close files in python
with open("foo.txt") as f:
    text = f.read()

print(text)

f = open("foo.txt")
text = f.read()
f.close()
print(text)
### above code lines 13 - 16 work or can switch 15 and 16, they still work

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

### create, write and read a file
### create a list
pokemon = ["Bulbasaur", "Charmander", "Squirtle"]

### use this to create a file, if no file exists python will create it, if it does, BE CAREFUL!! It will write of the current content of the file. 
with open("mon.txt", "w") as f:
    for mon in pokemon:
        f.write(mon)
        ### Above (line52) just puts in the text with no spaces because Python does not assume you want spaces.
        ### If you want spaces, add a f.write("\n") command after write all the elements from the list
        f.write("\n")
