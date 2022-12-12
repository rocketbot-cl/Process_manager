# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
    GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar("result", "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
   sudo pip install <package> -t .

"""
import os, sys
base_path = tmp_global_obj["basepath"] # os.getcwd()
cur_path = base_path + os.sep+ 'modules' + os.sep + 'Process_Manager' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
   sys.path.append(cur_path)

try:
    global process_manager

    class ProcessManager:
        
        def __init__(self):
            from suds.client import Client
            self.WSDL =  "https://latam.interact.com.br/sa/ws/bpm?wsdl"
            self.client = Client(self.WSDL)
            self.service = self.client.service
            self.session = ""
            self.close_session = self.service.closeSession
            
        def open_session(self, contract, service, application, secret):
            print(self.ping())
            self.session = self.service.openSession(contract=contract, service=service, application=application, secret=secret)
            return self.session            

        def ping(self, message=None):
            if message is None:
                message= "Conectado!"
            return self.service.ping(message)
        
        def get_attribute(self, name, process=None):
            print(name, process)
            if process is not None:
                attributes =  self.service.getAttributeValues(
                    session=self.session,
                    process=process,
                    which=name)
                return [att.value for att in attributes]
            return self.service.getAttributeValue(
                session = self.session,
                name = name
            )
        
        def set_attribute(self, name, value, process=None):
            session = self.session
            if process is not None:
                return self.service.setAttributeValues(
                    session=session, 
                    process=process,
                    attribute={"name": name, "value": value})
            return self.service.setAttributeValue(
                session=session, 
                name=name, 
                value=value)

    module = GetParams("module")

    if module == "open_session":
        contract = GetParams("contract")
        application = GetParams("application")
        secret = GetParams("secret")
        result = GetParams("result")

        process_manager = ProcessManager()
        res = process_manager.open_session(
            contract=contract, 
            service="ws.bpm", 
            application=application, 
            secret=secret)

        if result:
            SetVar(result, res)

    if module == "close_session":
        # session = GetParams("session")
        session = process_manager.session
        if session:
            process_manager.close_session(session)
        
    if module == "abort_instance":
        serial = GetParams("serial")
        reason = GetParams("reason")
        session = process_manager.session
        process_manager.service.abortInstance(session=session, serial=serial, reason=reason)
    
    if module == "start_process":
        mnemonic = GetParams("mnemonic")
        name = GetParams("name")
        result = GetParams("result")

        session = process_manager.session
        res = process_manager.service.startProcess(
            session=session, 
            mnemonic=mnemonic, 
            name=name)
        if result:
            SetVar(result, res)

    if module == "start_process_attribute":
        mnemonic = GetParams("mnemonic")
        name = GetParams("name")
        attribute = GetParams("attribute")
        result = GetParams("result")

        session = process_manager.session
        att_name = eval(attribute)[0]
        att_value = eval(attribute)[1]

        res = process_manager.service.startProcessWithAttributes(
            session=session, 
            mnemonic=mnemonic, 
            attribute = {"name":att_name, "value": att_value}
            )
        if result:
            SetVar(result, res)

    if module == "assume_task":
        task = GetParams("task")
        user = GetParams("user")
        session = process_manager.session
        process_manager.service.assumeTask(session=session, task=task, user=user)

    if module == "finish_task":
        task = GetParams("task")
        result = GetParams("result")
        session = process_manager.session
        res = process_manager.service.finishTask(session=session, task=task)
        
        if result:
            SetVar(result, res)

    if module == "get_attribute":
        process = GetParams("process")
        name = GetParams("name")
        result = GetParams("result")

        if name.startswith("["):
            name = eval(name)

        session = process_manager.session
        process = process if process != "" else None
        res = process_manager.get_attribute(name, process)

        if result:
            SetVar(result, res)
    
    if module == "set_attribute":
        process = GetParams("process")
        name = GetParams("name")
        value = GetParams("value")

        session = process_manager.session
        process = process if process != "" else None
        print(name, process)
        res = process_manager.set_attribute(name, value, process)
        print(res)

except Exception as e:
    PrintException()
    raise e

data = {}
data.update([[value[0], 0] for value in {variable}])
for array in variable:
    data[value] += array[1]
        