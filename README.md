Parcial Corte III – Programación en el lenguaje Python – Electiva II – 8 Semestre

Cree un programa en Python donde implemente con POO en el siguiente esquema:

  1. Cree una clase llamada Persona que hará las veces de Super Clase, esta clase tendrá los siguientes
    Atributos:
      o Identificación, Tipo de Identificación, Nombre, Edad, Email, Dirección, Teléfono, RH
      
    Métodos:
      o Constructor (en donde se debe recibir como argumento los datos correspondientes a los atributos de esta clase y agregarlos a cada atributo).
      o Método especial STR que permita imprimir un mensaje con el siguiente formato:
        ▪ Tipo de Identificación – Identificación – Nombre (Edad), Email – Teléfono (RH).

  2. Cree una clase llamada Personas que tenga los siguientes Atributos:
    o Estudiantes y Profesores (ambos de tipo lista).
    
    Métodos:
      o Cree un método llamado AgregarEstudiante donde reciba como argumento un objeto Estudiante y adicione al atributo Estudiantes el argumento recibido.
      o Cree un método llamado AgregarProfesor donde reciba como argumento un objeto Profesor y adicione al atributo Profesores el argumento recibido.
      o Cree un método llamado VisualizarEstudiantes que recorra con un bucle el atributo Estudiantes e imprima los estudiantes apoyado del método especial STR de la Super Clase Persona.
      o Cree un método llamado VisualizarProfesores que recorra con un bucle el atributo Profesores e imprima los profesores apoyado del método especial STR de la Super Clase Persona.
      
  3. Cree una subclase llamada Estudiante que herede de la superclase Persona, y agregue los siguientes
    Atributos:
      o Código, Semestre, Facultad, Sede, Jornada
      
  4. Cree una subclase llamada Profesor que herede de la superclase Persona, y agregue los siguientes
    atributos:
      o Tipo de contrato, Salario, EPS

  Implemente en su programa el siguiente menú de consola:
  ***********************
  1. Agregar Estudiante
  2. Listar Estudiante
  3. Agregue Profesor
  4. Listar Profesor
  5. Salir
  ***********************
  Digite una opción:

El programa debe pedir que el usuario digite una opción, y según la opción digitada realizar las siguientes acciones:

Objeto Personas: Primero cree un objeto que instancie a la clase Personas.

  • Si el usuario digita la opción 1, entonces debe crear un objeto que instancie la clase Estudiante (enviando los argumentos requeridos) y complete los atributos adicionales propios del Estudiante; adicionalmente debe llevar el objeto creado al método AgregarEstudiante del objeto Personas.
  • Si el usuario digita la opción 2, deberá llamar el método VisualizarEstudiantes del objeto Personas.
  • Si el usuario digita la opción 3, entonces debe crear un objeto que instancie la clase Profesor (enviando los argumentos requeridos) y complete los atributos adicionales propios del Profesor; adicionalmente debe llevar el objeto creado al método AgregarProfesor del objeto Personas.
  • Si el usuario digita la opción 4, deberá llamar el método VisualizarProfesores del objeto Personas.
