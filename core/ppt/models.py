from django.db import models
from datetime import datetime
from core.ppt.choices import gender_choices
from django.forms import model_to_dict


# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    birthday = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    sexo = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


class Sale(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.names

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']




class Pais(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
        db_table = 'pais'
        ordering = ['id']


class Depeartamento(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        db_table = 'departamento'
        ordering = ['id']


class Ciudad(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    departamento = models.ForeignKey(Depeartamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        db_table = 'ciudad'
        ordering = ['id']


class Comuna(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'
        db_table = 'comuna'
        ordering = ['id']


class Barrio(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Barrio'
        verbose_name_plural = 'Barrios'
        db_table = 'barrio'
        ordering = ['id']


class Profesion(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Profesion'
        verbose_name_plural = 'Profesiones'
        db_table = 'profesion'
        ordering = ['id']


class Hobby(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Hobby'
        verbose_name_plural = 'Hobbies'
        db_table = 'hobby'
        ordering = ['id']


class Cargo(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        db_table = 'cargo'
        ordering = ['id']


class Lider(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Lider'
        verbose_name_plural = 'Lideres'
        db_table = 'lider'
        ordering = ['id']

class Etnia(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Etnia'
        verbose_name_plural = 'Etnias'
        db_table = 'etnia'
        ordering = ['id']

class Puesto(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    direccion = models.CharField(max_length=50, verbose_name='Direccion')
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Puesto'
        verbose_name_plural = 'Puestos'
        db_table = 'puesto'
        ordering = ['id']


class Elector(models.Model):
    names = models.CharField(max_length=50, verbose_name='Nombre')
    cedula = models.CharField(max_length=10, unique=True, verbose_name='Cedula')
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Depeartamento, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=50, verbose_name='Direccion')
    fecha_nacimiento = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    date_registro = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    genero = models.CharField(max_length=10)
    hijos = models.CharField(max_length=10)
    profesion = models.ForeignKey(Profesion, on_delete=models.CASCADE)
    ocupacion = models.CharField(max_length=50, verbose_name='Ocupacion')
    etnia = models.ForeignKey(Etnia, on_delete=models.CASCADE)
    lider = models.ForeignKey(Lider, on_delete=models.CASCADE)
    fijo = models.CharField(max_length=10, unique=False, verbose_name='Telefono Fijo')
    celular = models.CharField(max_length=10, unique=True, verbose_name='Telefono Celular')
    email = models.EmailField(max_length=50, verbose_name='Email')
    facebook = models.CharField(max_length=50, verbose_name='Facebook')
    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE)
    ciudad_v = models.CharField(max_length=50, verbose_name='Ciudad Votacion')
    #ciudad_v = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    mesa = models.CharField(max_length=4, unique=False, verbose_name='Mesa')
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)
    validacion1 = models.CharField(max_length=10)
    validacion2 = models.CharField(max_length=10)
    validacion3 = models.CharField(max_length=10)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Elector'
        verbose_name_plural = 'Electores'
        db_table = 'elector'
        ordering = ['id']
