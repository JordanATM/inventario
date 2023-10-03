from django.shortcuts import render, redirect
from .models import Producto
from django.db.models import Q
from django.contrib import messages
# Create your views here.

def home(request):
    productos = Producto.objects.all()
    return render(request,"gestionProductos.html", {"productos":productos})

def registrarProducto(request):
    nombre = request.POST['txtNombre']
    codigo = request.POST['txtCodigo']
    cantidad = request.POST['txtCantidad']

    producto = Producto.objects.create(nombre=nombre,codigo=codigo,cantidad=cantidad)
    # messages.success(request,'Producto añadido')
    return redirect("/")

def edicionProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    # messages.success(request,'Producto editado')
    return render(request, "edicionProducto.html", {"producto": producto})

def editarProducto(request):
    nombre = request.POST['txtNombre']
    codigo = request.POST['txtCodigo']
    cantidad = request.POST['txtCantidad']

    producto = Producto.objects.get(codigo=codigo)

    producto.nombre = nombre
    producto.codigo = codigo
    producto.cantidad = cantidad
    producto.save()

    # messages.success(request,'Producto editado')

    return redirect('/')

def eliminarProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    # messages.success(request,'Producto eliminado')
    return redirect('/')

def buscarProducto(request):
    if request.method == "POST":
        # Obtener el término de búsqueda del formulario
        query = request.POST.get("search_box")

        # Realizar la búsqueda de productos que coincidan con el término de búsqueda
        productos = Producto.objects.filter(Q(codigo__icontains=query) | Q(nombre__icontains=query))

        return render(request, "busquedaProducto.html", {"productos": productos, "query": query})

    return redirect("/")