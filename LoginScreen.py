import sqlite3
from tkinter import *

conn = sqlite3.connect('usuarios.db')
c = conn.cursor()

# Criar a tabela se não existir
c.execute('''CREATE TABLE IF NOT EXISTS usuarios (username text, password text)''')
conn.commit()

def create_account():
    username = username_entry.get()
    password = password_entry.get()

    c.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, password))
    conn.commit()

    # Limpa os campos após a inserção
    username_entry.delete(0, END)
    password_entry.delete(0, END)

def login():
    username = username_login.get()
    password = password_login.get()

    c.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
    result = c.fetchone()

    if result:
        print("Login bem-sucedido")
    else:
        print("Nome de usuário ou senha incorretos")

root = Tk()
root.title("Tela de Login")

# Interface para criar conta
Label(root, text="Criar conta").grid(row=0, column=0, columnspan=2)

Label(root, text="Username:").grid(row=1, column=0)
username_entry = Entry(root)
username_entry.grid(row=1, column=1)

Label(root, text="Password:").grid(row=2, column=0)
password_entry = Entry(root, show="*")
password_entry.grid(row=2, column=1)

Button(root, text="Criar conta", command=create_account).grid(row=3, column=0, columnspan=2)

# Interface para fazer login
Label(root, text="Login").grid(row=4, column=0, columnspan=2)

Label(root, text="Username:").grid(row=5, column=0)
username_login = Entry(root)
username_login.grid(row=5, column=1)

Label(root, text="Password:").grid(row=6, column=0)
password_login = Entry(root, show="*")
password_login.grid(row=6, column=1)

Button(root, text="Login", command=login).grid(row=7, column=0, columnspan=2)

root.mainloop()

# Fechar a conexão com o banco de dados
conn.close()