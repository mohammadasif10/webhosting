import streamlit as st
import functions
#for webhosts to install all pacakages necessary to run your website, type pip freeze > requirements.txt to get a file detailing all the specifications needed to run your file. command is just pip freeze and you can see what it outputs in the shell. this is taking the information from there and piping it to a new file. In this case does not save visibly but you can acess it from the shell
todoList = functions.gettodo()#defeine it up here so method can access it

def addTodo():
  todo = st.session_state['addfrominputfield']
  todoList.append(todo + "\n")
  functions.writeTodos(todoList)
  return todo


st.title("Moho's To-do List App")
st.subheader("Developed by Mohammad Asif")
st.write("This app helps in organization and productivity")

for index, todos in enumerate(todoList):
  checkboxvalue = st.checkbox(todos, key=todos)
                             
  if checkboxvalue:
    todoList.pop(index)
    functions.writeTodos(todoList)
    del st.session_state[todos]
  
st.text_input(label="Add To Do", placeholder="Enter a to do item here...",
              on_change=addTodo, key=("addfrominputfield"))

st.session_state