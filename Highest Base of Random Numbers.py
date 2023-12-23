# Importing libraries which will be required
import random
import matplotlib.pyplot as plt

# Initialize an empty list to store randomly generated alphanumeric strings
rn=list() 

# Set the number of samples to generate, the more the amount of samples the more uniform the graph
sample=1000 

# Starting a loop for generating the random numbers, the sample size decides the number of times this loop will run
for i in range (0,sample):  
  
  # Initializing a string in which the random numbers will be appended into as words instead of numbers
  a=str() 

  # Create a dictionary mapping integers to their corresponding ASCII characters
  ascii_dict = {} 
  for i in range(0,10):
    ascii_dict[i]=i
  for i in range(65, 91):
    ascii_dict[i-55] = i

  # Convert the values in the dictionary to strings
  for k in ascii_dict.keys():
    ascii_dict[k]=str(ascii_dict[k])
    
  # Add uppercase letters to the dictionary
  for i,j in zip(range(10,36), range(65,91)):
    ascii_dict[i]=chr(j)

  # The below line of code will print the the dictionary with all the corresponding ascii values
  #print(ascii_dict)
    
  # Generate a random digit and append it to the string 'a'
  random_digit=random.randint(0,35)
  a=a+ascii_dict[random_digit]
  random_digit=random.randint(0,35)
  a=a+ascii_dict[random_digit]

  # Initialising a loop in which a number will be printed based on a probabily, the range is set to 8 because we need the maximum number of digits in the number to not be more than 8
  for i in range(0,8):
    x=random.randint(0,1)

    if x==1:
      random_digit=random.randint(0,35)
      a=a+ascii_dict[random_digit]

    else:
      break
  # Append the generated string to the 'rn' list
  rn.append(a)

# Print the generated alphanumeric strings
print(rn)

# Creating a dictionary to map ASCII characters back to their corresponding integers
reverse_ascii_dict=dict()
for k in ascii_dict.keys():
  reverse_ascii_dict[ascii_dict[k]] = k

# Creating a dictionary to store the count of each base
blank_dict=dict()

# Calculate the base of each alphanumeric string and update the 'blank_dict'
for a in rn:
  highest_digit= max(a)
  base=reverse_ascii_dict[highest_digit]+1
  if base in blank_dict.keys():
    blank_dict[base]+=1
    #(blank_dict[base])/=sample # This line of code will give the relative frequency instead of the actual frequency
  else:
    blank_dict[base]=1
  print("Highest base of {} is {}".format(a,base))

#The below code will give the amount of numbers per base, but by default it will be 0
for k in range(1,37):
    blank_dict.setdefault(k,0)

#Printing the amount of numbers per base 
print(blank_dict)

#Use matplotlib library to make a graph
plt.bar(x=blank_dict.keys(),height=blank_dict.values())