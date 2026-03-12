# Automação de Cadastro de Produtos (RPA Python)

Este projeto consiste em um script de **RPA (Robotic Process Automation)** desenvolvido em Python para automatizar o preenchimento de formulários de cadastro de produtos em um sistema web.

## Descrição do Projeto
O script automatiza as seguintes etapas:
1.  **Abertura do Navegador:** Utiliza comandos de sistema para abrir o Google Chrome de forma segura.
2.  **Login Automatizado:** Acessa o portal da empresa e realiza o login com credenciais pré-definidas.
3.  **Processamento de Dados:** Lê uma base de dados em formato `.csv` utilizando a biblioteca **Pandas**.
4.  **Cadastro em Lote:** Percorre cada linha da tabela e preenche os campos do formulário (Código, Marca, Tipo, Categoria, Preço, Custo e Observações) automaticamente.

## Tecnologias e Bibliotecas
* **Python 3.13+**
* **PyAutoGUI**: Controle de mouse e teclado.
* **Pandas**: Manipulação e leitura da base de dados.
* **Time**: Gerenciamento de pausas e sincronismo.
