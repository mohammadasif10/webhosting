FILEPATH = "new.txt"
def gettodo(filename = FILEPATH):#defines variable in name, makes it a default argument
  with open(filename, 'r') as fileLocal:
      todosLocal = fileLocal.readlines()
  return todosLocal#returns list of items bc we need to edit list. needs a return
"""gets old todo"""

def writeTodos(content, filepath = FILEPATH):
  with open(filepath, 'w') as file:
        file.writelines(content)#only writing to file, does not need output, no return line
"""Writes new todo"""