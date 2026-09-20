# Ambientes — VendeMais

## Objetivo

Documentar a separação dos ambientes utilizados no projeto e sua relação com o processo de testes e deploy.

## Ambiente de desenvolvimento

O ambiente `development` é utilizado pelo workflow de testes automatizados.

Sempre que ocorre uma alteração na branch `main`, o GitHub Actions executa os testes automatizados associados ao ambiente de desenvolvimento.

Testes executados:

- Validação do workflow Make/n8n;
- Testes da lógica de enriquecimento de leads.

## Ambiente de produção

O ambiente `github-pages` é utilizado para publicação da aplicação de demonstração.

O deploy é realizado automaticamente pelo GitHub Actions após alterações na branch `main`.

URL pública:

https://vittinxl.github.io/vendemais-revops/

## Secrets e credenciais

O projeto não utiliza secrets personalizados em tempo de execução na aplicação pública.

As credenciais do workflow de deploy são fornecidas pelo próprio GitHub Actions por meio das permissões configuradas no workflow.

As integrações reais do workflow de enriquecimento de leads continuam dependentes de credenciais externas e não são armazenadas no repositório.

## Separação

A configuração diferencia o ambiente de desenvolvimento, utilizado para validação automatizada, do ambiente de produção, utilizado para publicação da aplicação.

Essa separação permite validar alterações antes de considerar a aplicação publicada como versão disponível ao usuário.
