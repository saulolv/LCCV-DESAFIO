# Cadastro de Projetos

Este repositório contém uma aplicação em **Angular** para gerenciar projetos, permitindo **cadastrar**, **editar**, **listar** e **visualizar detalhes** de cada projeto. A aplicação faz uso de **Angular Material** para um design moderno e responsivo.

---

## Sumário
1. [Tecnologias](#tecnologias)
2. [Pré-requisitos](#pré-requisitos)
3. [Instalação](#instalação)
4. [Execução](#execução)
5. [Estrutura do Projeto](#estrutura-do-projeto)

---

## Tecnologias

- **[Angular](https://angular.io/)** (versão 14+ ou superior)
- **[TypeScript](https://www.typescriptlang.org/)**
- **[Angular Material](https://material.angular.io/)**
- **[RxJS](https://rxjs.dev/)**
- **[SCSS](https://sass-lang.com/)** para estilização

---

## Pré-requisitos

- **Node.js** (versão 14+ ou superior)
- **NPM** (versão 6+ ou superior) ou **Yarn**
- **Angular CLI** (instalado globalmente) - opcional, mas recomendado

---

## Instalação

1. **Clonar** o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. **Entrar na pasta do projeto**:
   ```bash
   cd seu-repositorio
   ```

3. **Instalar as dependências**:
   ```bash
   npm install
   ```
   ou
   ```bash
   yarn
   ```

---

## Execução

1. **Iniciar a aplicação**:
   ```bash
   npm start
   ```
   ou
   ```bash
   ng serve
   ```

2. **Acessar no navegador**:
   ```
   http://localhost:4200
   ```

---

## Estrutura do Projeto

Abaixo, um breve resumo de alguns diretórios importantes:

```
src/
 ┣ app/
 ┃  ┣ core/
 ┃  ┃  ┣ models/
 ┃  ┃  ┗ services/
 ┃  ┣ components/
 ┃  ┃  ┣ project-form/
 ┃  ┃  ┣ project-list/
 ┃  ┃  ┣ project-details-dialog/
 ┃  ┃   ┗ app-routing.module.ts
 ┣ assets/
 ┣ environments/
 ┗ main.ts
```

- `project-form`: Formulário (página) de cadastro e edição de projetos.
- `prtoject-details`: Diálogo (modal) para exibir detalhes do projeto.
- `project-list`: Componente para exibir a listagem de projetos.
- `core/models`: Define interfaces e tipos, como o modelo `Project`.
- `core/services`: Serviços para comunicação com API ou gerenciamento de dados.

---
