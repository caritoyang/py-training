# Whenever we are importing any module, that module executable code will run automatically
import PyModule

# Calling module function by using ModuleName
PyModule.testingPythonModuleFunction()
PyModule.sum(20,50)

x=PyModule.mul(2,3)
print(x)

# We need to create object of class written in any module
obj=PyModule.A()
obj.testing()
