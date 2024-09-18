import streamlit as st
from view import View
import pandas as pd
import time

class ExcluirComprasUi:
    @staticmethod
    def main():
        st.header("Cancelar Compras")
        
        #pega id cliente
        cliente_id = st.session_state.get("cliente_id")

        if cliente_id:
            compras = View.compra_listar_por_cliente(cliente_id)  # Busca compras do cliente logado
            
            if len(compras) == 0:
                st.write("Nenhuma compra registrada.")
            else:
                #mostra compras
                dic = [compra.to_json() for compra in compras]
                df = pd.DataFrame(dic)
                st.dataframe(df)

                #escolhe compra
                compra_selecionada = st.selectbox("Selecione a compra para excluir", compras, format_func=lambda c: f"Compra ID: {c.get_id()} - Total: R$ {c.get_total()}")

                #botao
                if st.button("Excluir Compra"):
                    View.compra_excluir(compra_selecionada.get_id())
                    st.success("Compra excluída com sucesso!")
                    time.sleep(2)
                    st.rerun()

        else:
            st.error("voce precisa estar logado para excluir suas compras.")
