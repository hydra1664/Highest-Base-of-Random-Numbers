# Highest-Base-of-Random-Numbers
The code in the repository generates a random number which may comprise of intergers from 0 to 9 and of alphabets (A to Z). This number can't be longer than 8 digits and not shorter than 2 digits. After the generation of this number, the highest base of each of the number is determined and then later displayed. After all the numbers are done being generated and the highest base of each of the number is determined, we use matplotlib to get a graph of which base had the most occurrences./n
We first import the required libraries.
Next we initialize an empty list 'rn' to store randomly generated alphanumeric strings.
Then we set the number of samples to generate, the more the amount of samples the more uniform the graph.
Next we start a loop for generating the random numbers, the sample size decides the number of times this loop will run.
Then we initializing a string 'a' in which the random numbers will be appended into as words instead of numbers.
Next step is to create a dictionary 'ascii_dict' mapping integers to their corresponding ASCII characters.
Then we convert the values in the dictionary to strings.
Next we add uppercase letters to the dictionary.
Then we generate 2 random digits and append it to the string 'a' since the number generated has to be at least 2 digits long.
Next we initialize a loop in which a number will be added into the string based on a probability, the range is set to 6 because we need the maximum number of digits in the number to not be more than 8.
Then we append the generated string to the 'rn' list.
Next step is to print the generated alphanumeric strings.
Then we create a dictionary 'reverse_ascii_dict' to map ASCII characters back to their corresponding integers.
Next we create a dictionary 'blank_dict'to store the count of each base.
Then we calculate the base of each alphanumeric string and update blank_dict.
Next we create a loop to give the amount of numbers per base, which will be set to default as 0.
Then we print the amount of numbers per base.
Last but not the least we use matplotlib library to make a graph.
