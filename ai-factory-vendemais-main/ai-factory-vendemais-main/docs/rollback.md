# Evidência de Rollback — VendeMais

## Objetivo

Validar a capacidade de restaurar uma versão anterior da aplicação após uma alteração publicada.

## Procedimento

1. Foi criada a release `v1.0.0`, representando a primeira versão funcional.
2. Após a release, foi realizada uma alteração no título da página.
3. O GitHub Actions publicou automaticamente a nova versão.
4. A alteração foi revertida por meio de um novo commit na branch `main`.
5. O GitHub Actions executou novamente o deploy.
6. A aplicação pública voltou a apresentar o título da versão anterior.

## Resultado

**Rollback realizado com sucesso.**

A aplicação retornou ao estado anterior após o commit de reversão e o novo deploy automático.

## Evidências

- Release de referência: `v1.0.0`
- Alteração posterior: `Update index.html`
- Commit de reversão: `revert: restaura versao v1.0.0`
- Deploy realizado pelo GitHub Actions
- URL pública: https://vittinxl.github.io/vendemais-revops/

## Conclusão

O processo demonstrou que uma alteração publicada pode ser revertida por meio de um novo commit e novamente disponibilizada pelo pipeline de deploy.
