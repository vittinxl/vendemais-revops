# VendeMais — Enriquecimento e Qualificação de Leads

Projeto acadêmico de RevOps voltado à evolução de um fluxo de enriquecimento de leads B2B, com foco em segurança, privacidade, testes automatizados, observabilidade e entrega contínua.

## Aplicação pública

**Demonstração:** https://vittinxl.github.io/vendemais-revops/

A aplicação apresenta uma interface demonstrativa para qualificação de empresas. Os resultados exibidos são simulados e não representam consultas reais a um CRM ou a um modelo de inteligência artificial.

## Repositório

https://github.com/vittinxl/vendemais-revops

## Objetivos

- Documentar a arquitetura e as decisões técnicas.
- Reduzir a exposição de dados pessoais antes da preparação de prompts.
- Limitar o tamanho dos trechos de pesquisa enviados ao processamento.
- Testar a retenção e a exclusão de registros fictícios.
- Executar verificações automaticamente com GitHub Actions.
- Documentar riscos, limitações e melhorias necessárias para produção.

## Arquitetura do fluxo original

O fluxo de referência utiliza:

1. **HubSpot:** origem e destino de informações comerciais.
2. **Google Custom Search:** busca de informações públicas sobre empresas.
3. **OpenAI:** geração de informações estruturadas de enriquecimento.
4. **Airtable:** armazenamento dos resultados.

A integração real depende das credenciais e configurações dos respectivos serviços. A página pública deste projeto é uma demonstração estática independente dessas integrações.

## Segurança e privacidade

Foram adicionados ou documentados:

- Sanitização básica de e-mails e telefones comuns antes da montagem do prompt nos testes de lógica.
- Limitação dos trechos de pesquisa a 500 caracteres.
- Arquivo de exemplo de variáveis de ambiente (`.env.example`).
- Proteção para não versionar arquivos locais e segredos.
- Mapa de dados e considerações sobre LGPD e transferência internacional.
- Política de retenção e exclusão para arquivos JSON de demonstração.
- Testes automatizados para verificar o comportamento da sanitização e da retenção.

A sanitização por expressões regulares é limitada e não garante a remoção de todos os dados pessoais. A integração com sistemas reais exige validações adicionais.

## Retenção e exclusão

O script `ai-factory-vendemais-main/ai-factory-vendemais-main/tests/retention_cleanup.py` identifica registros vencidos em arquivos JSON locais. O prazo padrão é de 90 dias e a exclusão só é aplicada quando a opção `--apply` é informada.

Esse mecanismo não exclui automaticamente dados do HubSpot, Airtable ou de fornecedores externos.

## Testes automatizados

O projeto possui verificações para a estrutura dos workflows, a lógica de enriquecimento, a sanitização e a política de retenção.

Os testes são executados pelo GitHub Actions nos eventos configurados no workflow.

Para executar os testes de retenção a partir da pasta do projeto:

```bash
cd ai-factory-vendemais-main/ai-factory-vendemais-main/tests
python -m unittest test_retention_cleanup.py
```

## Observabilidade e métricas

Para uma implantação real, devem ser acompanhadas pelo menos estas cinco métricas:

| Métrica | Objetivo |
|---|---|
| Latência p50, p95 e p99 | Medir o tempo de processamento |
| Custo por execução | Acompanhar o gasto com os provedores |
| Taxa de erro | Identificar falhas no processamento |
| Volume de leads processados | Medir o uso do fluxo |
| Qualidade do enriquecimento | Avaliar a utilidade e a consistência dos resultados |

A página estática atual não coleta telemetria real de chamadas a LLM nem de integrações externas. Essas métricas dependem de instrumentação adicional no ambiente de execução. Nenhum valor de custo, latência ou qualidade é apresentado aqui como medição real.

## Dashboard e alertas

**Dashboard:** pendente de instrumentação de métricas reais.

O alerta de produção deverá ter prioridade, condição de disparo, destinatários e canal de notificação definidos. O fluxo demonstrativo não deve ser interpretado como um monitoramento real de chamadas a LLM ou de integrações externas.

## Deploy

A publicação da demonstração é realizada pelo GitHub Pages, com deploy automatizado por GitHub Actions quando há atualizações na branch `main`.

## Documentação técnica

A documentação do projeto está organizada em `ai-factory-vendemais-main/ai-factory-vendemais-main/docs/`, incluindo decisões técnicas, arquitetura, mapa de dados, testes de fumaça, evidências de rollback e política de retenção.

## Limitações conhecidas

- A interface pública apresenta resultados simulados.
- A sanitização implementada é básica e precisa de validação adicional para produção.
- A retenção atua apenas em arquivos JSON locais de demonstração.
- As métricas de produção e o alerta operacional dependem de instrumentação e configuração adicionais.
- A conformidade com a LGPD exige validação das bases legais, contratos, transferências internacionais e procedimentos de exclusão.

## Próximas melhorias

- Instrumentar latência, erros, volume e custos reais.
- Configurar alertas operacionais com condições e responsáveis definidos.
- Automatizar a retenção nos sistemas reais, após validação.
- Validar a sanitização com casos adicionais e dados representativos.
- Revisar a documentação e os controles antes de qualquer uso com dados pessoais reais.


## Painel de observabilidade

Acesse o [Dashboard de Observabilidade do VendeMais](https://vittinxl.github.io/vendemais-revops/dashboard.html).

O painel apresenta os cinco indicadores definidos para acompanhamento operacional: latência, custo por execução, taxa de erro, volume de leads processados e qualidade do enriquecimento.

**Limitação atual:** o painel é estático e ainda não recebe métricas reais da aplicação. Os indicadores indisponíveis estão identificados como N/D. O alerta configurado cobre falhas dos workflows do GitHub Actions por meio de notificações do GitHub e por e-mail.

Consulte também o [documento do alerta operacional](ai-factory-vendemais-main/ai-factory-vendemais-main/docs/alerta-operacional.md).

## Otimização mensurável

Foi implementada a sanitização de e-mails e telefones nos textos usados para construir o prompt enviado à IA, acompanhada de testes automatizados específicos.

A melhoria foi validada por testes funcionais. Ainda não existem medições de redução de latência ou custo em produção, pois a demonstração não possui instrumentação real.

Consulte a [documentação da otimização mensurável](ai-factory-vendemais-main/ai-factory-vendemais-main/docs/otimizacao-mensuravel.md) para ver a comparação antes/depois, as evidências e as limitações.
