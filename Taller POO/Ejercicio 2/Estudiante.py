class Estudiante:

    def __init__(self, Id, Nombre, Programa, Semestre, Email, Institucion, Telefono):
        self._Id = Id
        self._Nombre = Nombre
        self._Programa = Programa
        self._Semestre = Semestre
        self._Email = Email
        self._Institucion = Institucion
        self._Telefono = Telefono
    
    @property
    def Id(self):
        return self._Id

    @property
    def Nombre(self):
        return self._Nombre

    @property
    def Programa(self):
        return self._Programa

    @property
    def Semestre(self):
        return self._Semestre

    @property
    def Institucion(self):
        return self._Institucion

    @property
    def Email(self):
        return self._Email

    @property
    def Telefono(self):
        return self._Telefono

    @Nombre.setter
    def Nombre(self, Nombre):
        self._Nombre = Nombre

    @Cargo.setter
    def Cargo(self, Cargo):
        self._Cargo = Cargo

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @Telefono.setter
    def Telefono(self, Telefono):
        self._Telefono = Telefono

    @Programa.setter
    def Programa(self, Programa):
        self._Programa = Programa

    @Semestre.setter
    def Semestre(self, Semestre):
        self._Semestre = Semestre

    @Institucion.setter
    def Institucion(self, Institucion):
        self._Institucion = Institucion