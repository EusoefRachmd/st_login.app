import streamlit as st

import pandas as pd

import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS usertable(username TEXT, password TEXT)')

def add_userdata(username,password):
    c.execute('INSERT INTO usertable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM usertable WHERE username =? AND password =?',(username,password))
    data = c.fetchall()
    return data


def main():

    st.title('simple login app')

    menu = ['home', 'login', 'signup']
    choice = st.sidebar.selectbox('menu', menu)

    if choice == 'home':
        st.subheader('home')

    elif choice == 'login':
        st.subheader('login section')

        username = st.sidebar.text_input('username')
        password = st.sidebar.text_input('password', type='password')
        if st.sidebar.checkbox('login'):
            # if password == '12345':

            create_usertable()
            result = login_user(username,password)
            if result:

                st.success('loged in as {}'.format(username))

                task = st.selectbox('task', ['addpost', 'analytics', 'profiles'])
                if task == 'addpost':
                    st.subheader('add your post')

                elif task == 'analytics':
                    st.subheader('analytics')

                # elif task == 'profiles':
                #     st.subheader('user profile')    
                #     user_result = view_all_users()
                #     clean_db = pd.DataFrame(user_result, columns=['username', 'password'])
                #     st.dataframe(clean_db)


            else:
                st.warning('incorrect usename/password')             

    elif choice == 'signup':
        st.subheader('create new account')
        new_user = st.text_input('username')
        new_password = st.text_input('password',type='password')

        if st.button('signup'):
            create_usertable()
            add_userdata(new_user,new_password)
            st.success('you have successfully create an valid account')
            st.info('go to login menu to login')

if __name__ == '__main__':
    main()
              