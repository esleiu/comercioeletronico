import streamlit as st
from view import View
import time

class RealizarCompraUI:
    @staticmethod
    def main():
        st.header("Carrinho de Compras")

        #cria um novo carrinho
        if "carrinho" not in st.session_state:
            st.session_state["carrinho"] = []

        produtos = View.produto_listar()

        if len(produtos) == 0:
            st.write("Nenhum produto disponível.")
        else:
            try:
                #preço seja convertido para float
                produto_escolhido = st.selectbox("Escolha um produto", produtos, format_func=lambda p: f"{p.get_descricao()} - R$ {round(float(p.get_preco()), 2)} (Estoque: {p.get_estoque()})")
                quantidade = st.number_input("Quantidade", min_value=1)

                if st.button("Adicionar ao Carrinho"):
                    if quantidade > int(produto_escolhido.get_estoque()):
                        st.error("Quantidade solicitada excede o estoque disponível.")
                    else:
                        #converte o preço para float e a quantidade para int
                        preco = round(float(produto_escolhido.get_preco()), 2)  # Garantindo que o preço seja float
                        quantidade = int(quantidade)

                        #adiciona o produto ao carrinho
                        st.session_state["carrinho"].append({
                            "produto_id": produto_escolhido.get_id(),
                            "descricao": produto_escolhido.get_descricao(),
                            "preco": preco,
                            "quantidade": quantidade
                        })
                        st.success(f"{quantidade} unidade(s) de {produto_escolhido.get_descricao()} adicionadas ao carrinho.")
                        time.sleep(1)
                        st.rerun()
            except Exception as e:
                st.error(f"Erro ao adicionar produto ao carrinho: {e}")

        #itens no carrinho
        st.subheader("Itens no Carrinho")
        if len(st.session_state["carrinho"]) == 0:
            st.write("Seu carrinho está vazio.")
        else:
            total = 0
            for item in st.session_state["carrinho"]:
                #converte
                preco_item = round(float(item['preco']), 2)
                qtd_item = int(item['quantidade'])

                #faz o cálculo total
                st.write(f"{qtd_item}x {item['descricao']} - R$ {round(preco_item * qtd_item, 2)}")
                total += round(preco_item * qtd_item, 2)

            st.write(f"Total: R$ {round(total, 2)}")

            #botao para finalizar a compra
            if st.button("Finalizar Compra"):
                try:
                    #erifica se o cliente está logado
                    if "cliente_id" not in st.session_state:
                        raise ValueError("Nenhum cliente logado. Por favor, faça login para finalizar a compra.")

                    cliente_id = st.session_state["cliente_id"]

                    #cria a compra
                    compra_id = View.compra_inserir(cliente_id, total)

                    #adiciona cada item do carrinho a compra
                    for item in st.session_state["carrinho"]:
                        produto_id = item["produto_id"]
                        qtd_item = int(item["quantidade"])
                        preco_item = round(float(item["preco"]), 2)

                        #registra o item na compra
                        View.item_inserir(produto_id, compra_id, qtd_item, preco_item)

                        #atualizaestoque do produto
                        produto = View.produto_listar_id(produto_id)
                        novo_estoque = int(produto.get_estoque()) - qtd_item
                        View.produto_atualizar(produto.get_id(), produto.get_descricao(), produto.get_preco(), novo_estoque)

                    #limpa carrinho
                    st.session_state["carrinho"] = []
                    st.success("Compra finalizada com sucesso!")
                    time.sleep(2)
                    st.rerun()
                except ValueError as ve:
                    st.error(f"Erro: {ve}")
                except Exception as e:
                    st.error(f"Erro ao finalizar compra: {e}")
