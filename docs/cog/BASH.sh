#!/bin/bash

# Basic Commands
echo "Hello, Unix Learners!"
ls
pwd

# Variables
name="Alice"
age=25
echo "My name is $name and I am $age years old."

# Redirection
echo "This is a test." > output.txt
cat output.txt

# Input and Output Redirection
echo "What's your favorite color?"
read color
echo "Your favorite color is $color."

# Pipes
echo "Counting files in the current directory:"
ls | wc -l

# Command Substitution
files_count=$(ls | wc -l)
echo "There are $files_count files in the current directory."

# Conditional Execution
echo "Checking if a file exists:"
if [ -e output.txt ]; then
    echo "output.txt exists."
else
    echo "output.txt does not exist."
fi

# Loops
echo "Printing numbers 1 to 5:"
for i in {1..5}; do
    echo $i
done

# Functions
greet() {
    echo "Hello, $1!"
}
greet "Bob"
