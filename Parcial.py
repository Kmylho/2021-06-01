print("Realizado por Andres Piratova, Claudia Moreno & Walter Cuprita")

menu =  """
    ***********************
        1. Agregar Estudiante
        2. Listar Estudiante
        3. Agregue Profesor
        4. Listar Profesor
        5. Salir
    ***********************
    """

personas = []
estudiantes = []
profesores = []

class Persona:
    def __init__(self,Identificacion,Tipo_de_Identificación,Nombre,Edad,Email,Direccion,Telefono,RH):
        self.Identificacion=Identificacion
        self.Tipo_de_Identificación=Tipo_de_Identificación
        self.Nombre=Nombre
        self.Edad=Edad
        self.Email=Email
        self.Direccion=Direccion
        self.Telefono=Telefono
        self.RH=RH

    def __str__(self):
        return """
            Tipo_de_Identificación\t()
            Identificacion\t()
            Nombre\t()
            Edad\t()
            Email\t()
            Telefono\t()
            RH\t()
            """.format(self.Tipo_de_Identificación,self.Identificacion,self.Nombre,self.Edad,self.Email,self.Telefono,self.RH)

class Estudiante(Persona):
    def __init__(self,Codigo, Semestre, Facultad, Sede, Jornada):
        self.Codigo=Codigo
        self.Semestre=Semestre
        self.Facultad=Facultad
        self.Sede=Sede
        self.Jornada=Jornada
    
    def AgregarEstudiante(self, Identificacion,Tipo_de_Identificación,Nombre,Edad,Email,Direccion,Telefono,RH):
        super().__init__(Identificacion,Tipo_de_Identificación,Nombre,Edad,Email,Direccion,Telefono,RH)
    
    def __str__(self):
        return """
            Codigo:\t{}
            Semestre:\t{}
            Facultad:\t{}
            Sede:\t{}
            Jornada:\t{}
            """.format(self.Codigo,self.Semestre,self.Facultad,self.Sede,self.Jornada)

def VisualizarEstudiantes():
    for Estudiante in estudiantes:
        print(Estudiante)

class Profesor(Persona):
    def __init__(self, Tipo_de_contrato, Salario, EPS):
        self.Tipo_de_contrato=Tipo_de_contrato
        self.Salario=Salario
        self.EPS=EPS

    def AgregarProfesor(self, Identificacion,Tipo_de_Identificación,Nombre,Edad,Email,Direccion,Telefono,RH):
        super().__init__(Identificacion,Tipo_de_Identificación,Nombre,Edad,Email,Direccion,Telefono,RH)

    def __str__(self):
        return """
            Tipo_de_contrato:\t{}
            Salario:\t{}
            EPS:\t{}
            """.format(self.Tipo_de_contrato,self.Salario,self.EPS,self)

def VisualizarProfesores():
    for Profesor in profesores:
        print(Profesor)

ejecutando = True
while ejecutando == True:
    print(menu)
    letraCapturada = str(input("Digite una opción: ")).lower()
    if (letraCapturada == "1" or letraCapturada == "2" or letraCapturada == "3" or letraCapturada == "4" or letraCapturada == "5"):
        if(letraCapturada == "1"):
            Codigo = str(input("Ingrese el Codigo: "))
            Semestre = str(input("Ingrese el Semestre: "))
            Facultad = str(input("Ingrese el Facultad: "))
            Sede = str(input("Ingrese el Sede: "))
            Jornada = str(input("Ingrese el Jornada: "))
            Identificacion = str(input("Ingrese el Identificacion: "))
            Tipo_de_Identificación = str(input("Ingrese el Tipo de Identificación: "))
            Nombre = str(input("Ingrese el Nombre: "))
            NombreTemp = Nombre
            Edad = str(input("Ingrese el Edad: "))
            Email = str(input("Ingrese el Email: "))
            Direccion = str(input("Ingrese el Direccion: "))
            Telefono = str(input("Ingrese el Telefono: "))
            RH = str(input("Ingrese el RH: "))
            Nombre = Estudiante(Codigo, Semestre, Facultad, Sede, Jornada)
            Nombre.AgregarEstudiante(Identificacion, Tipo_de_Identificación, NombreTemp, Edad, Email, Direccion, Telefono, RH)
            estudiantes.append(Nombre)

        if(letraCapturada == "2"):
            VisualizarEstudiantes()

        if(letraCapturada == "3"):
            Tipo_de_contrato = str(input("Ingrese el Tipo de contrato: "))
            Salario = str(input("Ingrese el Salario: "))
            EPS = str(input("Ingrese la EPS: "))
            Identificacion = str(input("Ingrese el Identificacion: "))
            Tipo_de_Identificación = str(input("Ingrese el Tipo de Identificación: "))
            Nombre = str(input("Ingrese el Nombre: "))
            NombreTemp = Nombre
            Edad = str(input("Ingrese el Edad: "))
            Email = str(input("Ingrese el Email: "))
            Direccion = str(input("Ingrese el Direccion: "))
            Telefono = str(input("Ingrese el Telefono: "))
            RH = str(input("Ingrese el RH: "))
            Nombre = Profesor(Tipo_de_contrato, Salario, EPS)
            Nombre.AgregarProfesor(Identificacion, Tipo_de_Identificación, NombreTemp, Edad, Email, Direccion, Telefono, RH)
            profesores.append(Nombre)

        if(letraCapturada == "4"):
            VisualizarProfesores()

        if(letraCapturada == "5"):
            ejecutando = False
            
        