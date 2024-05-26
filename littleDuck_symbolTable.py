class FuncDirectory:
    def __init__(self):
        self.funcs = {}

    def addFunc(self, name, type):
        if name in self.funcs:
            raise Exception(f"Function '{name}' already defined")
        self.funcs[name] = {
            'type': type,
            'parameters': [],
            'variables': {}
        }

    def addParam(self, funcName, paramName, paramType):
        if funcName not in self.funcs:
            raise Exception(f"Function '{funcName}' not defined")
        self.funcs[funcName]['parameters'].append((paramName, paramType))

    def addVar(self, funcName, varName, varType):
        if funcName not in self.funcs:
            raise Exception(f"Function '{funcName}' not defined")
        if varName in self.funcs[funcName]['variables']:
            raise Exception(f"Variable '{varName}' already defined in function '{funcName}'")
        self.funcs[funcName]['variables'][varName] = varType

class VarTable:
    def __init__(self):
        self.variables = {}

    def addVar(self, name, varType):
        if name in self.variables:
            raise Exception(f"Variable '{name}' already defined")
        self.variables[name] = varType