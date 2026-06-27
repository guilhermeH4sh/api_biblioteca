# Guia de Aprendizado - API para Biblioteca 📚

Este guia foi desenvolvido para orientar você no desenvolvimento da API da biblioteca passo a passo. O objetivo é que você compreenda a lógica de cada arquivo e escreva o código por conta própria, aprendendo como cada parte funciona.

---

## 🛠️ 1. Camada de Utilitários (`utils/helpers.py`)

O objetivo desse arquivo é criar funções que ajudam a lidar com arquivos JSON de forma simples, evitando repetir código de abertura e salvamento de arquivos em outras partes do projeto.

### 📖 Função `ler_json(caminho_arquivo)`
Essa função deve carregar o conteúdo de um arquivo JSON e convertê-lo em dados do Python (listas ou dicionários).
* **O que usar**:
  * O módulo `json` (use `import json`).
  * Tratamento de exceções com `try` e `except`.
  * Gerenciador de contexto `with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:`.
  * `json.load(arquivo)` para transformar o texto do JSON em objetos Python.
* **O que tratar no `except`**:
  * Se o arquivo não existir (`FileNotFoundError`) ou se o arquivo JSON estiver vazio/inválido (`json.JSONDecodeError`), retorne uma lista vazia `[]`.

### 💾 Função `salvar_json(caminho_arquivo, dados)`
Essa função recebe uma lista ou dicionário Python e grava essa informação estruturada em formato JSON no arquivo correspondente.
* **O que usar**:
  * Modo de escrita `'w'` no `with open()`.
  * `json.dump(dados, arquivo, indent=4, ensure_ascii=False)`.
* **O que tratar**:
  * Use um `try/except` geral. Se der certo, retorne `True`. Se ocorrer algum erro ao tentar salvar, capture a exceção e retorne `False`.

---

## 📦 2. Camada de Modelos (`models/`)

Os modelos servem para moldar as nossas entidades do mundo real em objetos no Python. Todos devem ser representados como classes.

### 📕 Classe Livro (`models/livro.py`)
Representa a estrutura de um livro.
* **Atributos no construtor `__init__`**:
  * `id` (número inteiro)
  * `titulo` (texto)
  * `autor` (texto)
  * `ano` (número inteiro)
  * `disponivel` (booleano que deve iniciar como `True` por padrão)
* **Método `to_dict(self)`**:
  * Deve retornar um dicionário (`{}`) com chaves correspondentes aos atributos do livro (Ex: `"id": self.id`). Isso é essencial para que o `json.dump` consiga salvar o livro depois.
* **Método `@classmethod` `from_dict(cls, dados_dict)`**:
  * Deve receber um dicionário (geralmente vindo do arquivo JSON) e retornar uma nova instância da classe `Livro` com esses dados. Ex: `return cls(id=dados_dict["id"], ...)`

### 👤 Classe Usuario (`models/usuario.py`)
Representa quem utilizará a biblioteca.
* **Atributos no construtor `__init__`**:
  * `id` (inteiro)
  * `nome` (texto)
  * `email` (texto)
* **Métodos**:
  * Implemente os mesmos métodos `to_dict(self)` e o método de classe `from_dict(cls, dados_dict)` correspondentes para os atributos do usuário.

### 🤝 Classe Emprestimo (`models/emprestimo.py`)
Representa o registro de quando um livro é retirado por um usuário.
* **Atributos no construtor `__init__`**:
  * `id` (inteiro)
  * `id_usuario` (inteiro)
  * `id_livro` (inteiro)
  * `data_emprestimo` (texto contendo a data que foi emprestado)
  * `data_devolucao` (texto contendo a data de devolução, deve aceitar `None` caso o livro ainda não tenha sido devolvido, com padrão `None`)
* **Métodos**:
  * Implemente `to_dict(self)` e `from_dict(cls, dados_dict)` correspondentes.

---

## ⚙️ 3. Camada de Serviços (`services/`)

Os serviços representam a "regra de negócio". Eles serão responsáveis por coordenar a lógica real do aplicativo e manipular os arquivos da pasta `data/` usando as funções que você fez no `helpers.py`.

### 📙 Serviço de Livros (`services/livro_service.py`)
Deve gerenciar os livros salvos no banco de dados (`data/livros.json`).
* **Dependências**: Importar as funções de `utils/helpers.py`.
* **Funções sugeridas**:
  * `cadastrar_livro(titulo, autor, ano)`:
    1. Carrega todos os livros do JSON usando `ler_json`.
    2. Descobre o novo ID (pode ser o ID do último livro na lista + 1, ou se a lista estiver vazia, o ID será 1).
    3. Cria o objeto `Livro` e o converte para dicionário usando `to_dict()`.
    4. Adiciona esse dicionário na lista de livros.
    5. Salva a lista de volta no arquivo JSON usando `salvar_json`.
  * `listar_livros()`:
    1. Lê a lista de livros do JSON e a retorna.
  * `buscar_livro_por_id(id_livro)`:
    1. Lê todos os livros do JSON.
    2. Percorre a lista buscando o livro com o ID informado.
    3. Retorna o dicionário do livro se encontrar, ou `None` se não existir.
  * `remover_livro(id_livro)`:
    1. Lê todos os livros.
    2. Remove o livro desejado (ou cria uma nova lista filtrando para remover o livro que possui aquele ID).
    3. Salva a nova lista de livros no JSON.
  * `atualizar_disponibilidade(id_livro, disponivel)`:
    1. Lê os livros.
    2. Encontra o livro pelo ID e altera seu campo `disponivel` para o novo booleano (`True` ou `False`).
    3. Salva as alterações no JSON.

### 👤 Serviço de Usuários (`services/usuario_service.py`)
Controla o gerenciamento de usuários em `data/usuarios.json`.
* **Funções sugeridas**:
  * `cadastrar_usuario(nome, email)`: Lê usuários do JSON, gera um ID sequencial, adiciona o novo usuário formatado em dicionário e salva no JSON.
  * `listar_usuarios()`: Lê e retorna a lista de todos os usuários do JSON.
  * `buscar_usuario_por_id(id_usuario)`: Busca um usuário específico pelo ID e o retorna (ou `None` se não achar).
  * `remover_usuario(id_usuario)`: Filtra a lista de usuários para retirar o usuário com aquele ID e salva de volta no JSON.

### 🔄 Serviço de Empréstimos (`services/emprestimo_service.py`)
Este serviço interage com os outros dois serviços para realizar validações complexas. Manipula `data/emprestimos.json`.
* **Dependências**: Importar `usuario_service` e `livro_service`.
* **Funções sugeridas**:
  * `realizar_emprestimo(id_usuario, id_livro)`:
    1. Verifica se o usuário de fato existe buscando-o por ID no `usuario_service`. Se não existir, cancela a operação informando que o usuário é inválido.
    2. Verifica se o livro existe buscando-o por ID no `livro_service` e se ele está disponível (`disponivel == True`). Se não existir ou estiver emprestado, cancela a operação.
    3. Caso passe nas validações, gera um novo ID sequencial de empréstimo.
    4. Salva a data atual em formato texto (dica: use `datetime.date.today().strftime('%d/%m/%Y')` do módulo nativo `datetime`).
    5. Atualiza a disponibilidade do livro para `False` usando o `livro_service.atualizar_disponibilidade(id_livro, False)`.
    6. Salva o novo registro de empréstimo no JSON de empréstimos (deixando `data_devolucao` como `None`).
  * `devolver_livro(id_emprestimo)`:
    1. Lê a lista de empréstimos.
    2. Encontra o empréstimo correspondente pelo ID que ainda não possua uma data de devolução (ativo).
    3. Altera a `data_devolucao` do empréstimo para a data atual.
    4. Atualiza a disponibilidade do livro associado de volta para `True` usando `livro_service.atualizar_disponibilidade(id_livro, True)`.
    5. Salva as alterações de volta em `data/emprestimos.json`.
  * `listar_emprestimos_ativos()`:
    1. Carrega todos os empréstimos e retorna apenas aqueles que ainda não têm data de devolução (`data_devolucao == None`).

---

## 💻 4. Integrando Tudo na CLI (`main.py`)

O seu arquivo principal deve deixar de usar a variável temporária `livros = []` na memória global e passar a usar as funções dos serviços que você criou.

### 📝 Estrutura Recomendada para o Loop Principal
1. **Importações**: No início do arquivo, faça os imports dos serviços:
   ```python
   import services.livro_service as livro_service
   import services.usuario_service as usuario_service
   import services.emprestimo_service as emprestimo_service
   ```
2. **Menu Principal**: Apresente um menu com categorias para facilitar:
   * **1. Menu de Livros** (ao escolher, abre um sub-menu com as opções Cadastrar, Listar, Buscar por ID, Remover).
   * **2. Menu de Usuários** (abre sub-menu com Cadastrar Usuário, Listar Usuários, Remover Usuário).
   * **3. Menu de Empréstimos** (abre sub-menu com Pegar Livro Emprestado, Devolver Livro, Listar Empréstimos Ativos).
   * **4. Sair**.
3. **Fluxo de Entrada e Validação**:
   * Sempre envolva entradas de números (como IDs e anos) em blocos `try/except ValueError` para garantir que o usuário não cause travamento digitando letras.
   * Chame as respectivas funções de serviço que você construiu, exibindo mensagens de sucesso ou de erro amigáveis na tela baseado nos retornos obtidos.
