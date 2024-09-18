import streamlit as st
import pandas as pd
from view import View
import time

class ManterItemUi:
    def Main():
        st.header("Cadastro de Item")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterItemUi.listar()
        with tab2: ManterItemUi.inserir()
        with tab3: ManterItemUi.atualizar()
        with tab4: ManterItemUi.excluir()

    def listar():
        itens = View.item_listar()
        if len(itens) == 0:
            st.write("Sem itens")
        else:
            dic = []
            for obj in itens: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        id_produto = st.text_input("Informe o ID do produto")
        id_compra = st.text_input("Informe o ID da compra")
        qtd = st.text_input("Informe a quantidade")
        preco = st.text_input("Informe o preço do item")
        if st.button("Inserir"):
            View.item_inserir(id_produto, id_compra, qtd, preco)
            st.success("Item inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        itens = View.item_listar()
        if len(itens) == 0:
            st.write("Nenhum item cadastrado")
        else:
            op = st.selectbox("Atualização de Item", itens)
            id_produto = st.text_input("Informe o novo ID do produto", op.get_id_produto())
            id_compra = st.text_input("Informe o novo ID da compra", op.get_id_compra())
            qtd = st.text_input("Informe a nova quantidade", op.get_qtd())
            preco = st.text_input("Informe o novo preço", op.get_preco())
            if st.button("Atualizar"):
                id = op.get_id()
                View.item_atualizar(id, id_produto, id_compra, qtd, preco)
                st.success("Item atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        itens = View.item_listar()
        if len(itens) == 0:
            st.write("Lista de itens vazia!")
        else:
            op = st.selectbox("Exclusão de item", itens)
            if st.button("Excluir"):
                id = op.get_id()
                View.item_excluir(id)
                st.success("Item excluído")
                time.sleep(2)
                st.rerun()
