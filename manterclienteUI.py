import streamlit as st
import pandas as pd
from view import View
import time

class ManterclienteUi:
    def Main():
        st.header("cadastro de cliente")
        tab1, tab2, tab3, tab4 = st.tabs (["listar", "inserir", "atualizar", "excluir"])
        with tab1: ManterclienteUi.listar()
        with tab2: ManterclienteUi.inserir()
        with tab3: ManterclienteUi.atualizar()
        with tab4: ManterclienteUi.excluir()

    def listar():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("sem clientes")
        else:
            dic = []
            for obj in clientes: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("informe o nome")
        email = st.text_input("informe o e-mail")
        fone = st.text_input("informe o fone")
        senha = st.text_input("informe a senha")
        endereco = st.text_input("informe o endereco")

        if st.button("inserir"):
            if nome == "" or email == "" or senha == "":
                st.error("nome, e-mail e senha são obrigatórios")
            elif "@" not in email or "." not in email:
                st.error("informe um e-mail válido")
            else:
                try:
                    View.cliente_inserir(nome, email, fone, endereco, senha)
                    st.success("cliente inserido com sucesso")
                    time.sleep(2)
                    st.rerun()
                except Exception as e:
                    st.error(f"erro ao inserir cliente: {e}")

    def atualizar():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("nenhum cliente cadastrado")
        else:
            op = st.selectbox("atualização de clientes", clientes)
            nome = st.text_input("informe o novo nome", op.get_nome())
            email = st.text_input("informe o novo e-mail", op.get_email())
            fone = st.text_input("informe o novo fone", op.get_fone())
            endereco = st.text_input("informe o novo endereco", op.get_endereco())
            senha = st.text_input("informe a nova senha", op.get_senha())

            if st.button("atualizar"):
                if nome == "" or email == "" or senha == "":
                    st.error("nome, e-mail e senha são obrigatórios")
                elif "@" not in email or "." not in email:
                    st.error("informe um e-mail válido")
                else:
                    try:
                        id = op.get_id()
                        View.cliente_atualizar(id, nome, email, fone, endereco, senha)
                        st.success("cliente atualizado com sucesso")
                        time.sleep(2)
                        st.rerun()
                    except Exception as e:
                        st.error(f"erro ao atualizar cliente: {e}")

    def excluir():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("lista de clientes vazia!")
        else:
            op = st.selectbox("exclusão de cliente", clientes)
            if st.button("excluir"):
                try:
                    id = op.get_id()
                    View.cliente_excluir(id)
                    st.success("cliente excluído")
                    time.sleep(2)
                    st.rerun()
                except Exception as e:
                    st.error(f"erro ao excluir cliente: {e}")
