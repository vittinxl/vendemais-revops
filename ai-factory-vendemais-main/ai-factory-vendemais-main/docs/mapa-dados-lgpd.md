# Mapa de Dados e LGPD — VendeMais

## 1. Objetivo

Documentar o fluxo de dados do processo de enriquecimento de leads da VendeMais, identificar riscos relacionados à privacidade e registrar medidas recomendadas para adequação à Lei Geral de Proteção de Dados Pessoais (LGPD).

## 2. Fluxo de dados

1. O HubSpot recebe e armazena informações comerciais sobre leads e empresas.
2. O Google Custom Search é utilizado para buscar informações públicas relacionadas à empresa.
3. Os resultados da pesquisa são enviados ao serviço de IA para gerar dados estruturados de enriquecimento.
4. Os resultados são registrados no Airtable.
5. Os campos de enriquecimento podem ser enviados de volta ao HubSpot.

## 3. Categorias de dados

| Categoria | Exemplos | Finalidade |
|---|---|---|
| Dados de identificação comercial | Nome da empresa e identificador do negócio | Identificar e relacionar registros |
| Dados profissionais | Nome, cargo e contato profissional, caso estejam presentes no CRM ou nos resultados | Apoiar o processo comercial |
| Dados de enriquecimento | Segmento, stack tecnológica e sinais de compra | Qualificar leads |
| Dados de avaliação | ICP Score e pontos de abordagem comercial | Apoiar a priorização de oportunidades |
| Dados técnicos | Data de processamento e estado da execução | Auditoria e monitoramento |

Os dados efetivamente tratados devem ser confirmados por meio da inspeção das configurações e dos registros reais do fluxo.

## 4. Sistemas envolvidos

| Sistema | Papel no fluxo | Ponto de atenção |
|---|---|---|
| HubSpot | CRM e origem/destino dos dados | Controlar acesso e finalidade de uso |
| Google Custom Search | Pesquisa de informações públicas | Avaliar os dados enviados na consulta |
| Serviço de IA (OpenAI) | Processamento e geração de resultados | Minimizar dados e avaliar condições de tratamento |
| Airtable | Armazenamento dos resultados | Definir acesso, retenção e exclusão |
| GitHub | Versionamento de código e documentação | Nunca armazenar credenciais reais |

## 5. Base legal

A base legal adequada deve ser definida e documentada pelo controlador dos dados, considerando a finalidade específica, a necessidade do tratamento, a relação com os titulares e as circunstâncias da operação.

O legítimo interesse pode ser avaliado quando aplicável, mediante análise de finalidade, necessidade, balanceamento dos direitos dos titulares e salvaguardas. Não deve ser considerado automaticamente válido para todos os dados ou finalidades.

Quando houver dados pessoais, a equipe responsável deverá documentar a base legal escolhida e disponibilizar informações adequadas aos titulares.

## 6. Transferência internacional

O fluxo pode envolver o envio de dados a provedores cujos serviços ou infraestrutura estejam fora do Brasil.

Antes da utilização em produção, devem ser verificados os locais de processamento, os contratos aplicáveis, as configurações de retenção e os mecanismos jurídicos exigidos pela LGPD para eventual transferência internacional.

## 7. Minimização e sanitização

Antes de enviar conteúdo ao serviço de IA:

- Remover dados pessoais que não sejam necessários para a finalidade.
- Priorizar informações sobre a empresa em vez de informações sobre pessoas.
- Limitar o tamanho dos resultados de pesquisa.
- Evitar enviar e-mails, telefones, identificadores pessoais ou dados sensíveis sem necessidade e autorização apropriada.
- Validar e estruturar a resposta antes de armazená-la.

A sanitização deve ocorrer antes da chamada ao serviço externo, e não apenas depois de receber a resposta.

## 8. Retenção e exclusão

A empresa deverá definir um prazo de retenção compatível com a finalidade comercial e com as obrigações legais aplicáveis.

Recomendações:

- Definir prazos para registros de enriquecimento e resultados brutos de pesquisa.
- Evitar armazenar resultados brutos por mais tempo do que o necessário.
- Implementar um procedimento para corrigir ou excluir dados quando aplicável.
- Avaliar a propagação de solicitações de exclusão entre HubSpot, Airtable e demais fornecedores.
- Registrar a execução das exclusões sem manter cópias desnecessárias dos dados removidos.

Os prazos definitivos devem ser aprovados pelo responsável pela proteção de dados da organização.

## 9. Segurança e controle de acesso

- Utilizar credenciais corporativas e com privilégios mínimos.
- Guardar segredos em mecanismos apropriados de gerenciamento de credenciais.
- Não versionar arquivos `.env` nem chaves de API.
- Restringir o acesso aos sistemas e às bases de dados.
- Evitar incluir dados pessoais ou segredos em logs.
- Avaliar contratos e configurações de segurança dos fornecedores.

## 10. Pendências para produção

- [ ] Confirmar as categorias de dados efetivamente tratadas.
- [ ] Registrar a base legal aprovada para cada finalidade.
- [ ] Validar contratos e transferências internacionais.
- [ ] Definir e aprovar os prazos de retenção.
- [ ] Implementar e testar a sanitização antes do envio à IA.
- [ ] Validar os procedimentos de correção e exclusão.
- [ ] Revisar permissões e credenciais dos fornecedores.

## 11. Conclusão

Este documento identifica os principais fluxos, riscos e controles recomendados para o enriquecimento de leads. Ele constitui um registro técnico inicial, não uma certificação de conformidade com a LGPD. A entrada em produção depende da validação das pendências pelas áreas responsáveis.
