def class_generate(class_name="NewClass", attributes={}, herency=()):
    return type(class_name, herency, attributes)

# Ejemplo de uso #1
def person_init(self, name):
    self.name = name

# definiendo el nombre  y los métodos que contendrá la clase
className = 'Person'
classMethods = {
    '__init__': person_init,
    'gretting': lambda self: 'Hi ' + self.name
}

# creando la definicón de la clase
Person = class_generate(className, classMethods)

person1 = Person('Harold')
person2 = Person('Benito')

print(person1.gretting())
print(person2.gretting())
