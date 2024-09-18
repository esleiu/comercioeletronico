import streamlit as st
from view import View
import pandas as pd

class MostrarComprasUi:
    @staticmethod
    def main():
        st.header("minhas compras")
        
        
        cliente_id = st.session_state.get("cliente_id")
        
        if cliente_id:
            try:
                
                compras = View.compra_listar_por_cliente(cliente_id)
                
                if len(compras) == 0:
                    st.write("nenhuma compra registrada.")
                else:
                    for compra in compras:
                        st.subheader(f"compra id: {compra.get_id()} - data: {compra.get_data()} - total: r$ {compra.get_total()}")
                        
                        #pega os itens relacionados a esta compra
                        itens = View.item_listar_por_compra(compra.get_id())
                        
                        if len(itens) == 0:
                            st.write("nenhum item nesta compra.")
                        else:
                            
                            lista_itens = []
                            for item in itens:
                                produto = View.produto_listar_id(item.get_id_produto())
                                if produto:
                                    
                                    lista_itens.append({
                                        'quantidade': item.get_qtd(),
                                        'produto': produto.get_descricao(),
                                        'preço unitário (r$)': item.get_preco(),
                                        'total (r$)': round(item.get_qtd() * item.get_preco(), 2)
                                    })
                            
                            df_itens = pd.DataFrame(lista_itens)
                            st.dataframe(df_itens)
                        
                        st.write("---")
            except Exception as e:
                st.error(f"ocorreu um erro ao buscar as compras: {e}")
        else:
            st.error("você precisa estar logado para ver suas compras.")
