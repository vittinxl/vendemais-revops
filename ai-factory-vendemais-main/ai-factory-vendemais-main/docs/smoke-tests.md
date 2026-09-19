# Smoke Tests — VendeMais

## Objetivo

Validar rapidamente se a aplicação publicada está acessível e se as principais interações da interface estão funcionando.

## Ambiente

- Ambiente: Produção
- Plataforma: GitHub Pages
- Aplicação: VendeMais
- URL: https://vittinxl.github.io/vendemais-revops/

## Teste 1 — Enriquecimento de lead

**Entrada:** `TOTVS`

**Ação:** informar o nome da empresa e clicar em "Enriquecer Lead".

**Resultado esperado:** o sistema apresenta os dados de enriquecimento e o ICP Score.

**Resultado obtido:** PASSOU.

---

## Teste 2 — Campo obrigatório

**Entrada:** campo de empresa vazio.

**Ação:** clicar em "Enriquecer Lead" sem informar uma empresa.

**Resultado esperado:** o sistema informa que o nome da empresa deve ser preenchido.

**Resultado obtido:** PASSOU.

Mensagem apresentada:

> Digite o nome de uma empresa.

---

## Teste 3 — Novo lead

**Entrada:** `Microsoft`

**Ação:** informar o nome da empresa e clicar em "Enriquecer Lead".

**Resultado esperado:** o resultado apresentado deve identificar a empresa informada.

**Resultado obtido:** PASSOU.

A aplicação apresentou `Microsoft` como empresa no resultado.

---

## Conclusão

Os três smoke tests realizados no ambiente de produção foram concluídos com sucesso.
