import streamlit as st
from streamlit.errors import DuplicateWidgetID

import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] +'\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This app is to increase productivity")
st.write("Click on a todo to complete it")

for i,todo in enumerate(todos):
    try:
        checkbox = st.checkbox(todo, key=todo)
        if checkbox:
            todos.pop(i)
            functions.write_todos(todos)
            del st.session_state[todo]
            st.rerun()

    except DuplicateWidgetID:
        pass

st.text_input(label='add a todo',placeholder='Add new todo...',
              on_change=add_todo, key='new_todo')