# Otimização Mensurável — VendeMais

## 1. Objetivo

Melhorar a proteção de dados pessoais no processo de enriquecimento de empresas, evitando que e-mails e telefones identificáveis presentes nos resultados de pesquisa sejam incluídos no prompt enviado à IA.

## 2. Alteração implementada

Foi adicionada a função `sanitize_text()` ao código de enriquecimento. Ela identifica padrões comuns de e-mail e telefone brasileiro e os substitui por marcadores, antes da montagem do prompt.

Também foram adicionadas verificações automatizadas para conferir a sanitização e confirmar que os dados originais não aparecem no prompt de exemplo.

## 3. Comparação antes e depois

| Indicador | Antes | Depois |
|---|---|---|
| Sanitização de e-mails no prompt | Não implementada | Implementada |
| Sanitização de telefones no prompt | Não implementada | Implementada |
| Verificações automatizadas específicas | 0 | 4 verificações |
| Validação automatizada do comportamento | Não disponível para esses casos | Disponível |

As quatro verificações específicas verificam a substituição de e-mail, a substituição de telefone e a ausência dos dois valores originais no prompt construído.

## 4. Evidência de validação

O workflow de testes automatizados do GitHub Actions foi executado com sucesso após a implementação da sanitização.

A evidência pode ser consultada no histórico de [execuções dos testes](https://github.com/vittinxl/vendemais-revops/actions/workflows/tests.yml).

## 5. Resultado e limitações

A melhoria torna verificável uma proteção que antes não estava implementada e reduz o risco de exposição acidental de e-mails e telefones nos casos cobertos pelos testes.

A sanitização é baseada em padrões comuns e não garante a identificação de todos os dados pessoais. O código ainda precisa ser avaliado com outros formatos de telefone, identificadores e informações sensíveis.

Esta otimização mede a cobertura funcional dos testes de sanitização, não uma redução de latência ou custo em produção. A aplicação demonstrativa não possui instrumentação suficiente para afirmar ganhos de desempenho reais.
