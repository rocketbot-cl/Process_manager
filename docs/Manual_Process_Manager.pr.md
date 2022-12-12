# Process Manager
  
Web service of Process Manager  

*Read this in other languages: [English](Manual_Process_Manager.md), [Español](Manual_Process_Manager.es.md), [Portugues](Manual_Process_Manager.pr.md).*
  
![banner](imgs/Banner_Process_manager.png)
## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot  



## Descrição do comando

### Abrir Sessão
  
Abra uma nova sessão
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|contrato|Contrato do aplicativo|84093009-1732-skl5-bd72-111f0ca3719d|
|Aplicativo|Nome do aplicativo|RPA POC|
|Secret|Secret do aplicativo|CiFeHmGiDaHhPjPcKmJcDCBDscAsbObLlLlBoBbObAaAbAMjkCbJiHoAdIgMhEfIc|
|Atribuir resultado à variável|Variável onde o resultado será salvo|Variável|

### Abortar instância
  
Aborta a instância de um processo
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Serial|Serial do processo|84093009-1732-skl5-bd72-111f0ca3719d|
|Razão|Razão pela qual a instância é abortada|Lorem ipsum dolor sit amet, consectetur adipiscing elit.|

### Iniciar o processo
  
Inicia um processo
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Mnemônico|Mnemônico do processo a iniciar|MnemoEx|
|Nome|Nome da instância do processo a criar|nome|
|Atribuir resultado à variável|Nome da variável onde o resultado da execução do processo será salvo|Variável|

### Inicia um processo com atributos
  
Inicia um processo com atributos enviados por parâmetro
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Mnemônico|Mnemônico do processo a iniciar|MnemoEx|
|Nome|Nome da instância do processo a iniciar|nome|
|Atributo|Nome e valor do atributo que será iniciado|nome, valor|
|Atribuir resultado à variável|Nome da variável onde o resultado será salvo|Variável|

### Assumir a tarefa
  
Assuma a responsabilidade por uma tarefa.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Tarefa|Nome da tarefa a assumir|task name|
|Usuário|Usuário que assume a tarefa|Usuário1|

### Terminar tarefa
  
Conclua uma tarefa
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Tarefa|Nome da tarefa a assumir|task name|
|Atribuir resultado à variável|Nome da variável onde o resultado da tarefa será salvo|Variável|

### Obter atributo
  
Retorna o valor (ou valores) do atributo de um processo
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Processo|Nome do processo|SOMP-DIGT-00431|
|Nome|Nome do atributo|Serial: Name|
|Atribuir resultado à variável|Nome da variável onde o atributo será armazenado|Variável|

### Definir atributo
  
Altere o valor do atributo de um processo
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Processo|ID do processo|84093009-1732-skl5-bd72-111f0ca3719d|
|Nome|Nome do atributo|Serial:Nome|
|valor|Valor do atributo|value|

### Fechar Sessão
  
Fecha a sessão atual
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
| - | - | - |
