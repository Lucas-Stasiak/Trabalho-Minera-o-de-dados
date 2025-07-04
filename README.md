# Trabalho de Mineração de Dados - Redes e Telecomunicações

## 📁 Dataset Utilizado

- **Nome:** USA House Sales Data  
- **Origem:** [Kaggle - USA House Sales](https://www.kaggle.com/datasets/shivachandel/kc-house-data)
- **Descrição:** O dataset contém dados de vendas de casas nos Estados Unidos, com informações como preço, número de quartos, área útil, ano de construção, entre outros.  
- **Total de registros:** Mais de 21.000 linhas e 21 colunas.

---

## ⚙️ Técnica Aplicada

A técnica utilizada foi **KMeans (Clusterização)**, um algoritmo de aprendizado não supervisionado que separa os dados em grupos baseados na similaridade entre as amostras.

### Etapas:
1. Carregamento do arquivo `.csv` com `pandas`.
2. Seleção apenas das colunas numéricas.
3. Remoção de valores ausentes.
4. Aplicação do KMeans com 3 grupos (clusters).
5. Visualização dos resultados com um gráfico de dispersão (`matplotlib`).

---

## 📊 Resultados

O algoritmo foi capaz de agrupar os dados das casas em 3 grupos distintos com base nas variáveis numéricas.  
Esses grupos representam padrões de semelhança entre os imóveis, como faixas de preço, tamanho, etc.  
O gráfico gerado mostra a separação dos clusters de forma visual.

---

## 🖥️ Como Executar o Projeto

Coloque o arquivo kc_house_data.csv na mesma pasta do main.py e execute: python main.py

### ✅ Requisitos
Certifique-se de ter Python 3 instalado. Instale as bibliotecas necessárias com:

```bash
pip install pandas scikit-learn matplotlib
# Trabalho-Minera-o-de-dados