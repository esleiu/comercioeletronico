import streamlit as st
from view import View
import time

class LoginUI:
    @staticmethod
    def Main():
        st.header("Login no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Login"):
            cliente = View.cliente_login(email, senha)
            if cliente is not None:
                st.session_state["cliente_id"] = cliente.get_id()
                st.session_state["cliente_nome"] = cliente.get_nome()
                st.success(f"Bem-vindo(a), {cliente.get_nome()}!")
            else:
                st.error("Usuário ou senha incorretos")
            time.sleep(2)
            st.rerun()

class LogoutUI:
    @staticmethod
    def main():
        if st.button("Logout"):
            del st.session_state["cliente_id"]
            del st.session_state["cliente_nome"]
            st.success("Logout realizado com sucesso!")
            st.rerun()

class CadastroUI:
    @staticmethod
    def main():
        st.header("Cadastro de Novo Cliente")
        nome = st.text_input("Informe o seu nome")
        email = st.text_input("Informe o seu e-mail")
        fone = st.text_input("Informe o seu telefone")
        endereco = st.text_input("Informe o seu endereço")
        senha = st.text_input("Informe a sua senha", type="password")

        if st.button("Cadastrar"):
            # Cria o novo cliente
            View.cliente_inserir(nome, email, fone, endereco, senha)
            st.success("Cliente cadastrado com sucesso!")
            time.sleep(2)
            st.rerun()
