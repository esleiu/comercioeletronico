import streamlit as st
import pandas as pd
from view import View
import time

class ManterProdutoUi:
    def Main():
        st.header("cadastro de produto")
        tab1, tab2, tab3, tab4 = st.tabs(["listar", "inserir", "atualizar", "excluir"])
        with tab1: ManterProdutoUi.listar()
        with tab2: ManterProdutoUi.inserir()
        with tab3: ManterProdutoUi.atualizar()
        with tab4: ManterProdutoUi.excluir()

    def listar():
        produtos = View.produto_listar()
        if len(produtos) == 0:
            st.write("sem produtos")
        else:
            dic = []
            for obj in produtos:
                dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)
    
    def inserir():
        descricao = st.text_input("informe uma descricao")
        preco = st.text_input("informe um preco")
        estoque = st.text_input("informe a quantidade de estoque")
        
        if st.button("inserir"):
            try:
                preco = float(preco)
                estoque = int(estoque)  
                View.produto_inserir(descricao, preco, estoque)
                st.success("produto adicionado!")
                time.sleep(2)
                st.rerun()
            except ValueError:
                st.error("preço deve ser um número e estoque deve ser um inteiro")

    def atualizar():
        produtos = View.produto_listar()
        if len(produtos) == 0:
            st.write("nenhum produto cadastrado")
        else:
            op = st.selectbox("atualização de produto", produtos)
            descricao = st.text_input("digite uma nova descricao", op.get_descricao())
            preco = st.text_input("digite um novo preco", op.get_preco())
            estoque = st.text_input("digite uma nova quantidade de estoque", op.get_estoque())
            
            if st.button("atualizar"):
                try:
                    preco = float(preco)  
                    estoque = int(estoque) 
                    id = op.get_id()
                    View.produto_atualizar(id, descricao, preco, estoque)
                    st.success("produto atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError:
                    st.error("preço deve ser um número e estoque deve ser um inteiro")

    def excluir():
        produtos = View.produto_listar()
        if len(produtos) == 0:
            st.write("lista de produtos vazia!")
        else:
            op = st.selectbox("exclusao de produto", produtos)
            if st.button("excluir"):
                id = op.get_id()
                View.produto_excluir(id)
                st.success("produto excluido")
                time.sleep(2)
                st.rerun()
