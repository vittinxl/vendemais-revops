# C4 Nível 1 — Diagrama de Contexto

## Objetivo

Este diagrama apresenta uma visão geral do sistema de enriquecimento de leads da VendeMais e suas principais integrações externas.

```mermaid
C4Context
    title VendeMais — Contexto do Sistema

    Person(revops, "Equipe RevOps", "Responsável por acompanhar e administrar o processo")

    System(vendemais, "Sistema de Enriquecimento de Leads", "Automação responsável por pesquisar, analisar e registrar informações de empresas")

    System_Ext(hubspot, "HubSpot", "CRM utilizado para gerenciamento dos negócios e leads")
    System_Ext(google, "Google Search", "Serviço utilizado para pesquisa de informações sobre empresas")
    System_Ext(openai, "OpenAI", "Serviço de inteligência artificial utilizado para analisar os resultados")
    System_Ext(airtable, "Airtable", "Base utilizada para armazenar os dados enriquecidos")

    Rel(revops, vendemais, "Administra e acompanha")
    Rel(hubspot, vendemais, "Fornece negócios")
    Rel(vendemais, google, "Pesquisa informações")
    Rel(vendemais, openai, "Envia resultados para análise")
    Rel(vendemais, airtable, "Armazena dados enriquecidos")
    Rel(vendemais, hubspot, "Atualiza informações")
