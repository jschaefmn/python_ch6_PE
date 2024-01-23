# This program allows the user to search for a file
# if the file doesn't exist, throw error
file_name = input('Enter the name of the file: ')
try:
  file_object = open(file_name)
  # loop to print first 5 lines of file, if there's less
  # print all lines
  counter = 0
  for line in file_object:
    counter += 1
    if counter > 5:
      break
    else:
      print(line.strip())
      
  file_object.close()
except FileNotFoundError:
  print(f'No file called {file_name} found.')