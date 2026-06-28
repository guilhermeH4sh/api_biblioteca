# API para Biblioteca

Uma API de linha de comando (CLI) síncrona estruturada em camadas para o gerenciamento de uma biblioteca, incluindo controle de livros, usuários e registro de empréstimos/devoluções com persistência de dados local em formato JSON.

## Arquitetura do Projeto

O projeto é organizado seguindo o padrão de separação de responsabilidades (camadas):

* **models**: Contém as classes de modelo que estruturam as entidades (Livro, Usuário, Empréstimo) e tratam a serialização de dados (to_dict/from_dict).
* **services**: Camada responsável pelas regras de negócio e validações da aplicação.
* **utils**: Módulos auxiliares, como o leitor/gravador síncrono de arquivos JSON.
* **data**: Diretório onde são persistidos os dados em formato JSON.
* **main.py**: Ponto de entrada da aplicação que gerencia a interface do usuário (CLI) por meio de menus interativos.

## Funcionalidades

### Gerenciamento de Livros
* Cadastro de livros com ID auto-incremental.
* Listagem de livros e busca individual por ID.
* Exclusão física de livros.
* Controle automático de disponibilidade para empréstimo.

### Gerenciamento de Usuários
* Cadastro de usuários com ID sequencial.
* Validação sintática de endereço de e-mail por expressões regulares (Regex).
* Listagem e exclusão de usuários cadastrados.

### Controle de Empréstimos e Devoluções
* Registro de empréstimos ativos com checagem de integridade referencial (existência prévia de usuário e livro).
* Validação de disponibilidade do livro (bloqueio de empréstimo duplo).
* Registro de devoluções com atualização automática do status do livro para disponível.
* Listagem de todos os empréstimos ativos no sistema.

## Stack Tecnológica

* Python 3.x
* Biblioteca padrão `json` para persistência de dados
* Biblioteca padrão `re` para validação de expressões regulares
* Biblioteca padrão `datetime` para registro de transações temporais

## Como Executar o Projeto

1. Certifique-se de ter o Python instalado em seu ambiente de execução.
2. Clone este repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/guilhermeH4sh/api_biblioteca.git
   ```
3. Navegue até a pasta raiz do projeto.
4. Execute o arquivo principal:
   ```bash
   python main.py
   ```
