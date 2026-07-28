# 📚 Bibliotech
Sistema para bibliotecas escolares, permitindo melhorias na eficiencia e avanço tecnologico na gestão da biblioteca.

## Visão Geral
- **Objetivo:** Busca melhorar o sistema de emprestimos e gestão das bibliotecas com eficiencia e modernidade.

- **Possivel escalabilidade (Multi-Tenant):** No inicio é voltado apenas para uma escola mas com possivel escalabilidade para diversas escolas.

# 📝 Requisitos
## Requisitos Funcionais (RF)
- **RF-01 (Gestão de Escolas):** Cadastrar, atualizar, listar e remover escolas (Multi-Tenant)

- **RF-02 (Gestão de Livros):** Cadastrar livros, categorizar por gênero/autor/ISBN, controlar exemplares físicos disponíveis e filtrar buscas

- **RF-03 (Gestão de Emprestimos e Devoluções):** Registrar retirada de livros, calcular datas de devolução, registrar devoluções e controlar renovações

- **RF-04 (Autenticação e Autorizações):** Perfis de acesso distintos (Administrador do Sistema, Bibliotecário/Gestor Escolar, Aluno/Leitor)

- **RF-05 (Notificações e Lembretes):** Notificar o usuario de prazos de devoluções ou pendencias (Futuro)

## Requisitos Não Funcionais (RNF)
- **RNF-01 (Tempo de resposta):** Tempo de respostas da API de busca inferior a 300ms

- **RNF-02 (Segurança):** Autenticação via JWT e criptografia de senhas de usuarios/gestores

- **RNF-03 (Isolamento de dados):** Não permitir que usuarios/gestores acessem ou manipulem quaisquer dados de outra escola

- **RNF-04 (Portabilidade e Containerização):** ROdar 100% em Docker e Docker-Compose

# ⚙️ Stack de Tecnologia
- **Linguagem principal:** Python 3.12+

- **Gerenciador de Dependencias:** `uv`

- **Bibliotecas/Frameworks:** Django e django-ninja

- **Banco de Dados:** PostgreSQL (Produção e Desenvolvimento Local)

- **Containerização:** Docker e Docker-Compose

# 🏷️ Estrutura
- **Padrão:** Padronizado em desenvolvimento agíl por responsabilidade para cada caso de uso

- **Tipo de padronização:** Domain-Driven Design & Clean Architecture

- **Estilo do codigo:** PEP-8

## Regras de Diretorios
| Diretorio | Responsabilidade |
|---|---|
| `api` | Responsavel por guardar tudo que estiver relacionado diretamente com os endpoints |
| `application` | Responsavel por guardar tudo que for unico da aplicação em especifico |
| `domain` | Responsavel por guardar tudo que for de regra/tipagem da aplicação |
| `infrastructure` | Responsavel por guardar tudo que for de mão-de-obra na aplicação |

# 🎲 Banco de Dados (DER simplificado)
## School (Escola)
| Campo | Tipo | Opcional | Descrição |
|---|---|---|---|
| `id` | UUID (Primary Key) | Não | Identificador da escola |
| `name` | String | Sim | Nome da escola |
| `code_inep` | String | Sim | Codigo inep da escola |
| `created_at` | Timestamp | Não | Data e hora de registro |

## User (Usuario)
| Campo | Tipo | Opcional | Descrição |
|---|---|---|---|
| ` id` | UUID (Primary Key) | Não | Identificador do usuario |
| `school_id` | UUID (Foreign Key) | Não | Escola na qual usuario pertence |
| `name` | String | Não | Nome do usuario |
| `email` | String | Não | Email do usuario |
| `password` | String | Não | Senha criptografada do usuario |
| `role` | Enum (`ADMIN`, `LIBRARIAN`, `STUDENT`) | Não | Autorização do usuario (Permissões)

## Book (Livro / Titulo)
| Campo | Tipo | Opcional | Descrição |
|---|---|---|---|
| `id` | UUID (Primary Key) | Não | Identificador do livro |
| `school_id` | UUID | Não | Escola na qual o livro pertence |
| `title` | String | Não | Titulo do livro/titulo |
| `author` | String | Não | Autor do livro |
| `isbn` | String | Não | Codigo ISBN do livro |
| `publisher` | String | Não | Distribuidora/Publicadora do livro |
| `total_copies` | Integer | Não | Total de copias do livro |
| `avaliable_copies` | Integer | Não | Total de copias disponiveis do livro |

## Loan (Eemprestimo)
| Campo | Tipo | Opcional | Descrição |
|---|---|---|---|
| `id` | UUID (Primary Key) | Não | Identificador do emprestimo |
| `book_id` | UUID (Foreign Key) | Não | Livro na qual pertence o emprestimo |
| `user_id` | UUID (Foreign Key) | Não | Usuario na qual realizou o emprestimo |
| `barrowed_at` | Timestamp | Não | Dia no qual realizou o emprestimo |
| `due_date` | Date | Não | Data de vencimento |
| `returned_at` | Timestamp, Nullable | Não | Data na qual realizou a devolução do livro |
| `status` | Enum: (`ACTIVE`, `RETURNED`, `OVERDUE`) | Não | Status do emprestimo |

# 🔌 Endpoints
## Modulo School (`api/schools`)
| Metodo | Endpoint | Descrição |
|---|---|---|
| `POST` | `api/schools/` | Registrar escola no banco de dados |
| `GET` | `api/schools/` | Lista todas as escolas cadastradas |
| `GET` | `api/schools/{id}` | Retorna detalhes de uma escola especifica |
| `PATCH` | `api/schools/{id}` | Atualiza as informações de uma escola |
| `DELETE` | `api/schools/{id}` | Remove uma escola |

## Modulo Book (`api/books`)
| Metodo | Endpoint | Descrição |
|---|---|---|
| `POST` | `api/books/` | Registra livro no banco de dados |
| `GET` | `api/books/` | Lista livros com suporte a busca por titulo/autor |
| `GET` | `api/books/{id}` | Retorna detalhes de um livro especifico |
| `PATCH` | `api/books/{id}` | Atualiza um livro |
| `DELETE` | `api/books/{id}` | Remove um livro |

## Modulo Loan (`api/loans`)
| Metodo | Endpoint | Descrição |
|---|---|---|
| `POST` | `api/loans/` | Registra novo emprestimo no banco de dados |
| `GET` | `api/loans/{id}` | Retorna detalhes de um emprestimo especifico |
| `GET` | `api/loans/status/` | Lista emprestimos filtrado por status |
| `GET` | `api/loans/user/` | Lista emprestimos de determinado usuario |
| `PATCH` | `api/loans/returned` | Finaliza o emprestimo (Devolução) |

# 💻 Padronização de Desenvolvimento
## Padrão dos Commits
| Prefixo | Descrição |
|---|---|
| `feat:` | Para adição de funcionalidades novas |
| `fix:` | Para correções de erros e adições fora de ordem |
| `refactor:` | Para refatoração ou estruturação do codigo |
| `chore:` | Para alterações que não alteram diretamente o funcionamento do codigo |
| `docs:` | Para mudanças na documentação
