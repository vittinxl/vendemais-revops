# Alerta Operacional — VendeMais

## Objetivo
Detectar falhas nos processos automatizados de validação e publicação do projeto, permitindo que o responsável tome conhecimento do problema e investigue a causa.

## Alerta configurado
Foi habilitada a preferência de notificações do GitHub Actions para receber notificações no GitHub e por e-mail quando um workflow falhar, utilizando a opção **Failed workflows only**.

## Eventos monitorados
- Falha no workflow de testes (`tests.yml`).
- Falha no workflow de publicação do GitHub Pages (`deploy.yml`).

## Procedimento de resposta
1. Abrir a notificação recebida.
2. Acessar os detalhes da execução que falhou.
3. Consultar os logs para identificar a etapa com erro.
4. Corrigir o problema e executar novamente o workflow.
5. Confirmar que a execução terminou com sucesso.

## Limitação
Este alerta monitora falhas dos workflows do GitHub Actions. Ele não monitora diretamente latência, custos de chamadas de IA, qualidade dos enriquecimentos ou disponibilidade de integrações externas. Esses indicadores dependem de instrumentação adicional.

## Evidência
A configuração pode ser conferida em **GitHub → Settings → Notifications → System → Actions**, na opção **Failed workflows only**.
