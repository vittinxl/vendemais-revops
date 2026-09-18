# C4 Nível 2 — Diagrama de Containers

## Objetivo

Este diagrama detalha os principais componentes envolvidos no processo de enriquecimento de leads.

```mermaid
C4Container
    title VendeMais — Containers da Solução

    Person(revops, "Equipe RevOps", "Administra e acompanha a automação")

    System_Boundary(vendemais, "Sistema VendeMais") {
        Container(make, "Make.com", "Plataforma de automação", "Orquestra o processo de enriquecimento")
        Container(blueprint, "Blueprint versionado", "JSON + GitHub", "Representa a configuração do workflow")
        Container(tests, "Testes automatizados", "Python", "Valida a estrutura dos workflows e parte da lógica")
    }

    System_Ext(hubspot, "HubSpot", "CRM")
    System_Ext(google, "Google Search", "Pesquisa")
    System_Ext(openai, "OpenAI", "IA")
    System_Ext(airtable, "Airtable", "Armazenamento")

    Rel(revops, make, "Administra")
    Rel(blueprint, make, "Define configuração")
    Rel(tests, blueprint, "Valida")
    Rel(make, hubspot, "Lê e atualiza negócios")
    Rel(make, google, "Realiza pesquisas")
    Rel(make, openai, "Envia dados para análise")
    Rel(make, airtable, "Grava dados enriquecidos")
