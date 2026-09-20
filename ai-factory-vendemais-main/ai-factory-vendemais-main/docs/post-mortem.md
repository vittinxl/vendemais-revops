# Post-mortem — VendeMais

## 1. Contexto

O projeto VendeMais foi recebido a partir de um protótipo de automação para enriquecimento de leads. O objetivo da evolução foi organizar a solução, documentar as decisões técnicas, criar testes automatizados e estabelecer um processo básico de CI/CD.

## 2. Situação encontrada

A auditoria do protótipo identificou alguns pontos de atenção:

- execução manual do cenário;
- dependência de credenciais pessoais;
- ausência de versionamento adequado do workflow;
- falta de tratamento de erros;
- ausência de controle de custos;
- limitações na estrutura do Airtable;
- ausência de documentação completa para manutenção.

## 3. Ações realizadas

Durante a evolução do projeto foram realizadas as seguintes ações:

- criação da documentação de auditoria;
- definição e documentação da stack;
- criação dos ADRs técnicos;
- criação dos diagramas de arquitetura C4;
- versionamento do projeto no GitHub;
- criação de testes automatizados;
- configuração do GitHub Actions;
- criação de uma interface pública de demonstração;
- configuração do GitHub Pages;
- criação de workflow de deploy automático;
- criação dos smoke tests;
- criação da release `v1.0.0`;
- realização e documentação de um rollback;
- separação dos ambientes de desenvolvimento e produção.

## 4. Problemas encontrados durante a execução

Durante a implementação, foi identificado que a estrutura inicial do repositório possuía diretórios aninhados. Isso exigiu ajustes nos caminhos utilizados pelo workflow de testes.

Também foi necessário configurar o GitHub Actions para localizar corretamente os arquivos de teste dentro da estrutura do projeto.

Após os ajustes, os testes passaram e o pipeline ficou funcional.

## 5. Resultado

Ao final da evolução, o projeto possui:

- repositório público no GitHub;
- documentação técnica;
- testes automatizados;
- CI configurado;
- CD configurado;
- aplicação pública;
- smoke tests documentados;
- release versionada;
- evidência de rollback;
- ambientes de desenvolvimento e produção documentados.

## 6. Limitações

A aplicação pública desenvolvida para esta etapa possui caráter demonstrativo e não representa uma integração completa com as APIs externas do fluxo original.

As integrações reais com HubSpot, Google, OpenAI e Airtable dependem de credenciais e configurações externas, que não foram armazenadas no repositório.

## 7. Aprendizados

O principal aprendizado foi perceber a importância de documentar as decisões técnicas e automatizar testes e deploy.

O uso do GitHub Actions também demonstrou como um processo simples de CI/CD pode reduzir etapas manuais e tornar as alterações mais rastreáveis.

O projeto também reforçou a importância de não armazenar credenciais diretamente no código e de separar responsabilidades entre desenvolvimento, testes e publicação.

## 8. Conclusão

A evolução transformou o protótipo inicial em uma estrutura mais organizada, documentada e versionada, com testes automatizados, publicação contínua e processo de rollback.

As limitações identificadas foram registradas para que possam ser consideradas em futuras evoluções do projeto.
