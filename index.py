from loginUI import LoginUI, LogoutUI, CadastroUI
from view import View
import streamlit as st
from manterprodutoUI import ManterProdutoUi
from mantercompraUI import ManterComprasUi
from manteritemUI import ManterItemUi
from mostrarcomprasUi import MostrarComprasUi
from realizarcompraUI import RealizarCompraUI
from excluircompraUI import ExcluirComprasUi
from manterclienteUI import ManterclienteUi

class indexUI:
    @staticmethod
    def menu_adm():
        op = st.sidebar.selectbox("Menu Admin", ["Manter Produto", "Manter Compra", "Manter Item","Manter cliente", "Logout"])
        if op == "Manter Produto":
            ManterProdutoUi.Main()
        elif op == "Manter Compra":
            ManterComprasUi.Main()
        elif op == "Manter Item":
            ManterItemUi.Main()
        elif op == "Manter cliente":
            ManterclienteUi.Main()
        elif op == "Logout":
            LogoutUI.main()
            

    @staticmethod
    def menu_usuario():
        op = st.sidebar.selectbox("Menu Usuário", ["Realizar Compra", "Mostrar Compras", "Cancelar compras", "Logout"])
        if op == "Realizar Compra":
            RealizarCompraUI.main()
        elif op == "Mostrar Compras":
            MostrarComprasUi.main()
        elif op == "Cancelar compras":
            ExcluirComprasUi.main()
        elif op == "Logout":
            LogoutUI.main()
        

    @staticmethod
    def sidebar():
        if "cliente_id" not in st.session_state:
            op = st.sidebar.selectbox("Acesso", ["Login", "Cadastrar-se"])
            if op == "Login":
                LoginUI.Main()
            elif op == "Cadastrar-se":
                CadastroUI.main()
        else:
            cliente_nome = st.session_state["cliente_nome"]
            st.sidebar.write(f"Bem-vindo(a), {cliente_nome}!")
            
            if cliente_nome == "admin":# administrador
                indexUI.menu_adm()  
            else:
                indexUI.menu_usuario()  #usuário comum

    @staticmethod
    def main():
        indexUI.sidebar()

indexUI.main()
