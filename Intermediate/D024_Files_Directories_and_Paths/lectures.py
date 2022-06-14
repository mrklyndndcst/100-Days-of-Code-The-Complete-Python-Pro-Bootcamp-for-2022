# read 
with open("/Users/mdecosto/Desktop/my_file.txt") as file:
  contents = file.read()
  print(contents)

# write
with open("Intermediate/D024_Files_Directories_and_Paths/new_file.txt", mode="w") as file:
  file.write('\nNew text again x2.')
  
# append
with open("Intermediate/D024_Files_Directories_and_Paths/new_file.txt", mode="a") as file:
  file.write('\nNew text again x2.')

