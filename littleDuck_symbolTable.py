class VarTable:
    def __init__(self):
        self.vars = {}

    def addVars(self, name, varType):
        if name in self.vars:
            raise ValueError("La variable {name} ya esta declarada.")
        self.vars[name] = varType

    def getVars(self, name):
        if name not in self.vars:
            raise ValueError("La variable {name} ya esta declarada.")
        return self.vars[name]

    def __str__(self):
        return f"VariableTable({self.variables})"     
    
class FuncDirectory:
    def __init__(self):
        self.funcs = {}