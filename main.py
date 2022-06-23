from email import message
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# Gerador de senhas
def gerador_password():
  letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

  numeros=['0','1','2','3','4','5','6','7','8','9']

  simbolos=['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_letras = [choice(letras)for _ in range(randint(8,10))]
  password_simbolos = [choice(simbolos)for _ in range(randint(2,4))]
  password_numeros = [choice(numeros)for _ in range(randint(2,4))]

  password_list = password_letras + password_simbolos + password_numeros

  shuffle(password_list)

  password = "".join(password_list)
  senha_atual = password_input.get()
  if len(senha_atual) > 0:
    password_input.delete(0, END)
  
  password_input.insert(0,password)
  pyperclip.copy(password) #comando que copia a senha para ser colada em outro lugar


#-----------------------------------------------------------#
#Função para salvar os dados no arquivo txt
def save():
  site = site_input.get()
  email = email_input.get()
  password = password_input.get()
  new_data = {
    site: {
      "email": email,
      "password": password,
    }
  }

  #Verificação dos campos vazios
  if len(site) == 0 or len(password) == 0:
    messagebox.showinfo(title="Atenção!",message="Por favor, preencha todos os campos")
  else:
    try:    
      with open("data.json", "r") as data_file:
        #Leitura dos antigos dados
        data = json.load(data_file)
    except FileNotFoundError:
      with open("data.json", "w") as data_file:
        #Salvando dados atualizados
        json.dump(new_data, data_file, indent=4)
        #Atualizando os dados novos e antigos
      
    else:
      data.update(new_data)
      with open("data.json", "w") as data_file:
        #Salvando dados atualizados
        json.dump(data, data_file, indent=4)
    finally:
        #Para apagar os dados do formulário, quando inserir novamente
        site_input.delete(0, END)
        password_input.delete(0, END)
    
#-----------------------------------------------------------#
#Função para pesquisar 
def find_password():
  site = site_input.get()
  try:
    with open("data.json") as data_file:
      data = json.load(data_file)
  except FileNotFoundError:
    messagebox.showinfo(title="Erro", message="Dados não encontrados")
  
  else:
    if site in data:
      email = data[site]["email"]
      password = data[site]["password"]
      messagebox.showinfo(title=site, message=f"Email: {email}\nPassword: {password}")
    else:
      messagebox.showinfo(title="Erro", message=f"Não há detalhes para {site}!")

#-----------------------------------------------------------#
#Criando a Janela
window = Tk()
window.title("Gerenciador de Password")
window.config(padx=50, pady=50, bg="white")

#Inserindo a imagem
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="imagem2.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#Texto Site
site = Label(text="Site:", bg="white")
site.grid(row=1, column=0)
#Campo Site
site_input = Entry(width=23)
site_input.focus()
site_input.grid(row=1,column=1)

#Texto Email
email = Label(text="Email/Username:", bg="white")
email.grid(row=2, column=0)
#Campo Email
email_input = Entry(width=36)
email_input.grid(row=2,column=1, columnspan=2)
email_input.insert(0, "teste@teste.com") #pré preenchido

#Texto Password
password = Label(text="Password:", bg="white")
password.grid(row=3, column=0)
#Campo Senha
password_input = Entry(width=23)
password_input.grid(row=3,column=1)

#Botão para gerar
gerador = Button(text="Gerar Senha", command=gerador_password, width=10)
gerador.grid(row=3, column=2)


#Botão para adicionar
adicionar = Button(text="Add", width=30, command=save)
adicionar.grid(row=4, column=1, columnspan=2)

#Botão para pesquisar
pesquisar = Button(text="Pesquisar", width=10, command=find_password)
pesquisar.grid(row=1, column=2)

window.mainloop()