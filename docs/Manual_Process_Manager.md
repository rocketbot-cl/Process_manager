# Process Manager
  
Process Manager is the BPMS module that allows you to manage the survey, modeling, simulation, design, automation and improvement of business processes of the Suite SA platform.  

*Read this in other languages: [English](Manual_Process_Manager.md), [Español](Manual_Process_Manager.es.md), [Português](Manual_Process_Manager.pr.md).*
  
![banner](imgs/Banner_Process_manager.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



## Description of the commands

### Open Session
  
Open a new session
|Parameters|Description|example|
| --- | --- | --- |
|Server URL|Process Manager server URL|https://example.interact.com/sa/ws/bpm|
|Contract|Application contract|84093009-1732-skl5-bd72-111f0ca3719d|
|Service|Application service|ws.bpm|
|Application|Application name|RPA POC|
|Secret|Application secret|CiFeHmGiDaHhPjPcKmJcDCBDscAsbObLlLlBoBbObAaAbAMjkCbJiHoAdIgMhEfIc|
|Task|Application secret|PROCESS SERIAL: TASK NEMOTECNIC|
|User|Application user|User|
|Assign result to variable |Variable where the result will be saved|Variable|

### Abort instance
  
Abort the instance of a process
|Parameters|Description|example|
| --- | --- | --- |
|Serial|Process serial|84093009-1732-skl5-bd72-111f0ca3719d|
|Reason|Reason why the instance is aborted|Lorem ipsum dolor sit amet, consectetur adipiscing elit.|

### Start Process
  
Starts a Process
|Parameters|Description|example|
| --- | --- | --- |
|Mnemonic|Mnemonic of the process to start|MnemoEx|
|Name|Name of the process instance to create|name|
|Assign result to variable |Variable name where the result of the process execution will be saved|Variable|

### Start Process with attributes
  
Starts a Process with attributes sent by parameter
|Parameters|Description|example|
| --- | --- | --- |
|Mnemonic|Mnemonic of the process to start|MnemoEx|
|Name|Name of the process instance to start|name|
|Name and value of the attribute|Name and value of the attribute to start|{"name": "value"}|
|Assign result to variable |Variable name where the result will be saved|Variable|

### Assume task
  
Take responsibility for a task.
|Parameters|Description|example|
| --- | --- | --- |
|Task|Task name to assume|task name|
|User|User that assumes the task|User1|

### Finish task
  
Finish a task
|Parameters|Description|example|
| --- | --- | --- |
|Task|Task name to assume|task name|
|Assign result to variable |Variable name where the task result will be saved|Variable|

### Get attribute
  
Returns the value (or values) of the attribute of a process
|Parameters|Description|example|
| --- | --- | --- |
|Process|Process name|SOMP-DIGT-00431|
|Name|Attribute name|Serial: Name|
|Assign result to variable |Variable name where the attribute will be stored|Variable|

### Set attribute
  
Change the attribute value of a process
|Parameters|Description|example|
| --- | --- | --- |
|Process|Process ID|84093009-1732-skl5-bd72-111f0ca3719d|
|Name|Attribute name|Serial:Name|
|Value|Attribute value|value|

### Close Session
  
Close the current session
|Parameters|Description|example|
| --- | --- | --- |
