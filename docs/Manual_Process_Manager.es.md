# Process Manager
  
Web service of Process Manager 

*Read this in other languages: [English](Manual_Process_Manager.md), [Español](Manual_Process_Manager.es.md), [Portugues](Manual_Process_Manager.pr.md).*
  
![banner](imgs/Banner_Process_manager.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



## Descripción de los comandos

### Abrir sesión
  
Abre una nueva sessión
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|contract|Contrato de la aplicación|84093009-1732-skl5-bd72-111f0ca3719d|
|Aplicación|Nombre de la aplicación|RPA POC|
|Secret|Secret de la aplicación|CiFeHmGiDaHhPjPcKmJcDCBDscAsbObLlLlBoBbObAaAbAMjkCbJiHoAdIgMhEfIc|
|Asignar resultado a variable|Variable donde se guardará el resultado|Variable|

### Abortar instancia
  
Aborta la instancia de un proceso
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Serial|Serial del proceso|84093009-1732-skl5-bd72-111f0ca3719d|
|Razón|Razón por la cual se aborta la instancia|Lorem ipsum dolor sit amet, consectetur adipiscing elit.|

### Iniciar Proceso
  
Inicia un Proceso
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Mnemonico|Mnemonico del proceso a iniciar|MnemoEx|
|Nombre|Nombre de la instancia del proceso que se va a crear|name|
|Asignar resultado a variable|Nombre de variable donde se guardará el resultado de la ejecución del proceso|Variable|

### Iniciar Proceso con atributos
  
Iniciar Proceso con atributos enviados por parámetro
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Mnemonico|Mnemonico del proceso a iniciar|MnemoEx|
|Nombre|Nombre de la instancia del proceso a iniciar|name|
|Atributo|Nombre y valor del atributo que se va a iniciar|name, value|
|Asignar resultado a variable|Nombre de variable donde se va a guardar el resultado|Variable|

### Asumir tarea
  
Asume la responsabilidad de una tarea
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Tarea|Nombre de la tarea a asumir|task name|
|Usuario|Usuario que asume la tarea|Usuario1|

### Terminar tarea
  
Finaliza una tarea
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Tarea|Nombre de la tarea a asumir|task name|
|Asignar resultado a variable|Nombre de variable donde se guardará el resultado de la tarea|Variable|

### Obtener atributos
  
Devuelve el valor (o valores) del atributo de un proceso
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Proceso|Nombre del proceso|SOMP-DIGT-00431|
|Nombre|Nombre del atributo|Serial: Name|
|Asignar resultado a variable|Nombre de variable donde se almacenará el atributo|Variable|

### Establecer atributo
  
Cambiar el valor de atributo de un proceso
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Proceso|ID del proceso|84093009-1732-skl5-bd72-111f0ca3719d|
|Nombre|Nombre del atributo|Serial:Name|
|Valor|Valor del atributo|value|

### Cerrar sesión
  
Cierra la sesión actual
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
| - | - | - |
