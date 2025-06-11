from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm, ComentarioForm
from .models import Producto, Categoria
from django.db.models import Q

# Lista de productos con búsqueda opcional
def lista_productos(request):
    query = request.GET.get("q")
    categoria_id = request.GET.get("categoria")

    productos = Producto.objects.all()
    categorias = Categoria.objects.all()

    if query:
        productos = productos.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query)
        )

    if categoria_id and categoria_id.isdigit():
        productos = productos.filter(categoria_id=categoria_id)

    context = {
        "productos": productos.order_by("-fecha_creacion"),
        "categorias": categorias,
        "categoria_id": categoria_id,
        "query": query,
    }
    return render(request, "productos/lista.html", context)

# Detalle del producto + comentarios
def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    comentarios = producto.comentarios.all()

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.producto = producto
            comentario.save()
            return redirect('detalle_producto', producto_id=producto.id)
    else:
        form = ComentarioForm()

    return render(request, 'productos/detalle.html', {
        'producto': producto,
        'comentarios': comentarios,
        'form': form
    })

# Crear producto (para administradores)
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()

    return render(request, 'productos/crear.html', {
        'form': form
    })
