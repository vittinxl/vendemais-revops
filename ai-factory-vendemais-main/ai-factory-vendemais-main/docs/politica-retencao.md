# Política de Retenção e Exclusão de Dados — VendeMais

## 1. Objetivo

Definir critérios para retenção e exclusão de dados utilizados no processo de enriquecimento de leads, reduzindo o armazenamento desnecessário e apoiando os princípios de necessidade e segurança da LGPD.

## 2. Prazo de retenção proposto

Para a demonstração técnica, foi adotado um prazo configurável de **90 dias** para os registros que possuem a data de enriquecimento (`enriched_at`).

Esse prazo é uma configuração inicial do projeto acadêmico, e não uma determinação legal universal. Em um ambiente real, o período deve ser validado conforme a finalidade do tratamento, as obrigações legais e a política aprovada pela organização.

## 3. Funcionamento do mecanismo

O script `tests/retention_cleanup.py` implementa o mecanismo de retenção em arquivos JSON locais.

O procedimento:

1. Lê uma lista de registros em formato JSON.
2. Identifica registros cuja data `enriched_at` ultrapassa o prazo configurado.
3. Mantém registros recentes e registros cuja data não pôde ser validada.
4. Por padrão, apenas informa quantos registros estão vencidos, sem alterar o arquivo.
5. Executa a exclusão somente quando a opção `--apply` é informada.

## 4. Execução

Na pasta `tests`, o modo de simulação pode ser executado com:

```bash
python retention_cleanup.py retention_sample.json --dias 90
```

Para aplicar a exclusão no arquivo de demonstração:

```bash
python retention_cleanup.py retention_sample.json --dias 90 --apply
```

**Atenção:** a segunda execução altera o arquivo informado. Os comandos devem ser testados apenas com dados fictícios ou cópias de teste.

## 5. Testes automatizados

O arquivo `tests/test_retention_cleanup.py` verifica:

- Se a simulação identifica registros vencidos sem modificar o arquivo.
- Se a opção de aplicação remove registros antigos e preserva registros recentes.

Esses testes são executados pelo GitHub Actions durante as atualizações do repositório.

## 6. Limitações atuais

O mecanismo implementado é uma demonstração funcional em arquivos JSON locais. Ele ainda não:

- Exclui registros diretamente do HubSpot ou Airtable.
- Executa automaticamente em uma agenda (cron).
- Propaga exclusões para cópias mantidas por fornecedores externos.
- Define sozinho a base legal ou o prazo adequado para cada categoria de dado.

Essas funcionalidades precisam ser avaliadas e implementadas antes de utilizar o mecanismo para tratar dados reais em produção.

## 7. Procedimento recomendado para produção

Antes da implantação real, a organização deverá:

1. Aprovar os prazos de retenção por categoria de dado.
2. Identificar todos os sistemas que armazenam os registros.
3. Implementar a exclusão ou anonimização nos sistemas envolvidos.
4. Automatizar a execução por um agendador confiável.
5. Registrar os resultados da rotina sem expor dados pessoais.
6. Testar a exclusão e os procedimentos de recuperação.
7. Validar os procedimentos com os responsáveis por privacidade e segurança.

## 8. Conclusão

O projeto possui um mecanismo executável e testado para demonstrar a identificação e a exclusão de registros vencidos. A integração com os sistemas externos e a automação agendada permanecem como melhorias necessárias para uma utilização real.
