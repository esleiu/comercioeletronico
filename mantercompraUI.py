import streamlit as st
import pandas as pd
from view import View
import time

class ManterComprasUi:
    def Main():
        st.header("Cadastro de Compra")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterComprasUi.listar()
        with tab2: ManterComprasUi.inserir()
        with tab3: ManterComprasUi.atualizar()
        with tab4: ManterComprasUi.excluir()

    def listar():
        compras = View.compra_listar()
        if len(compras) == 0:
            st.write("Sem compras")
        else:
            for compra in compras:
                st.subheader(f"Compra ID: {compra.get_id()} - Cliente ID: {compra.get_id_cliente()} - Data: {compra.get_data()} - Total: R$ {round(compra.get_total(), 2)}")
                st.write("Itens comprados:")
                itens = View.item_listar_por_compra(compra.get_id())
                if len(itens) == 0:
                    st.write("Nenhum item nesta compra.")
                else:
                    lista_itens = []
                    for item in itens:
                        produto = View.produto_listar_id(item.get_id_produto())
                        if produto:
                            
                            lista_itens.append({
                                'Quantidade': item.get_qtd(),
                                'Produto': produto.get_descricao(),
                                'Preço unitário (R$)': item.get_preco(),
                                'Total (R$)': round(item.get_qtd() * item.get_preco(), 2)
                            })
                    
                    df_itens = pd.DataFrame(lista_itens)
                    st.dataframe(df_itens)
                
            
                st.write("---")

    def inserir():
        id_cliente = st.text_input("Informe o ID do cliente")
        total = st.text_input("Informe o valor total")
        if st.button("Inserir"):
            try:
                total = float(total) 
                if total <= 0:
                    raise ValueError("O valor total deve ser positivo.")
                View.compra_inserir(id_cliente, total)
                st.success("Compra inserida com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.error(f"Erro: {e}")

    def atualizar():
        compras = View.compra_listar()
        if len(compras) == 0:
            st.write("Nenhuma compra cadastrada")
        else:
            op = st.selectbox("Atualização de Compra", compras)
            id_cliente = st.text_input("Informe o novo ID do cliente", op.get_id_cliente())
            total = st.text_input("Informe o novo valor total", op.get_total())
            
            st.subheader("Itens relacionados a esta compra:")
            itens = View.item_listar_por_compra(op.get_id())
            for item in itens:
                st.write(f"Item: {item.get_id_produto()} - Quantidade: {item.get_qtd()} - Preço: {item.get_preco()}")

            if st.button("Atualizar"):
                try:
                    total = float(total) 
                    if total <= 0:
                        raise ValueError("O valor total deve ser positivo.")
                    id = op.get_id()
                    View.compra_atualizar(id, id_cliente, total)
                    st.success("Compra atualizada com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(f"Erro: {e}")

    def excluir():
        compras = View.compra_listar()
        if len(compras) == 0:
            st.write("Lista de compras vazia!")
        else:
            op = st.selectbox("Exclusão de compra", compras)
            if st.button("Excluir"):
                id = op.get_id()
                View.compra_excluir(id)
                st.success("Compra excluída")
                time.sleep(2)
                st.rerun()
