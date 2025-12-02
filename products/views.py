from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from .models import Product, Review, ContenidoQuienesSomos, ContenidoServiciosTerapeuticos, FotoBienvenida, ServicioTerapeutico
from datetime import datetime
import json


def home(request):
    """Vista para la página de inicio"""
    productos_destacados = Product.objects.filter(destacado=True, oculto=False)[:3]
    foto_bienvenida = FotoBienvenida.load()
    
    context = {
        'productos_destacados': productos_destacados,
        'foto_bienvenida': foto_bienvenida,
    }
    return render(request, 'products/home.html', context)


def catalogo(request):
    """Vista para el catálogo de productos"""
    productos = Product.objects.filter(oculto=False)
    
    # Filtros
    categoria = request.GET.get('categoria')
    if categoria:
        productos = productos.filter(categorizacion=categoria)
    
    # Ordenamiento
    orden = request.GET.get('orden', 'relevancia')
    if orden == 'precio_asc':
        productos = productos.order_by('precio')
    elif orden == 'precio_desc':
        productos = productos.order_by('-precio')
    else:  # relevancia (por fecha de creación)
        productos = productos.order_by('-created')
    
    # Paginación
    paginator = Paginator(productos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'categoria_actual': categoria,
        'orden_actual': orden,
    }
    return render(request, 'products/catalogo.html', context)


def product_detail(request, product_id):
    """Vista para el detalle de un producto"""
    product = get_object_or_404(Product, id=product_id, oculto=False)
    reviews = Review.objects.filter(product=product)
    
    if request.method == 'POST' and request.user.is_authenticated:
        rating = int(request.POST.get('rating'))
        comment = request.POST.get('comment')
        Review.objects.create(
            product=product,
            user=request.user,
            rating=rating,
            comment=comment
        )
        from django.contrib import messages
        messages.success(request, 'Tu reseña ha sido publicada exitosamente.')
        return redirect('product_detail', product_id=product_id)
    
    context = {
        'product': product,
        'reviews': reviews,
    }
    return render(request, 'products/product_detail.html', context)


def quienes_somos(request):
    """Vista para la página 'Quienes Somos'"""
    contenido = ContenidoQuienesSomos.load()
    valores_presentacion = []
    if contenido.valores:
        for valor in contenido.valores:
            if isinstance(valor, dict):
                titulo = valor.get('titulo', '')
                descripcion = valor.get('descripcion', '')
            elif isinstance(valor, str):
                partes = valor.split(':', 1)
                titulo = partes[0].strip()
                descripcion = partes[1].strip() if len(partes) > 1 else ''
            else:
                titulo = ''
                descripcion = ''
            if titulo or descripcion:
                valores_presentacion.append({
                    'titulo': titulo,
                    'descripcion': descripcion,
                })
    context_defaults = [
        {'titulo': '100% Natural', 'descripcion': 'Todos nuestros productos son completamente naturales'},
        {'titulo': 'Cultivado con Amor', 'descripcion': 'Cada planta es cuidada personalmente'},
        {'titulo': 'Calidad Garantizada', 'descripcion': 'Procesos artesanales y tradicionales'},
        {'titulo': 'Atención Personalizada', 'descripcion': 'Cuidamos de cada cliente'},
    ]
    if not valores_presentacion:
        valores_presentacion = context_defaults
    context = {
        'contenido': contenido,
        'valores_presentacion': valores_presentacion,
    }
    return render(request, 'products/quienes_somos.html', context)


def servicios_terapeuticos(request):
    """Vista para la página 'Servicios Terapéuticos'"""
    contenido = ContenidoServiciosTerapeuticos.load()
    servicios = ServicioTerapeutico.objects.filter(activo=True)
    context = {
        'contenido': contenido,
        'servicios': servicios,
    }
    return render(request, 'products/servicios_terapeuticos.html', context)


# ============ VISTAS DE ADMINISTRACIÓN ============

@staff_member_required
def admin_panel(request):
    """Panel principal de administración"""
    return render(request, 'products/admin_panel.html')


@staff_member_required
def admin_productos(request):
    """Vista para administrar productos"""
    productos = Product.objects.all().order_by('-created')
    context = {
        'productos': productos,
    }
    return render(request, 'products/admin_productos.html', context)


@staff_member_required
def admin_producto_editar(request, product_id=None):
    """Vista para crear o editar un producto"""
    if product_id:
        producto = get_object_or_404(Product, id=product_id)
    else:
        producto = None
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        beneficios = request.POST.get('beneficios')
        description = request.POST.get('description')
        categorizacion = request.POST.get('categorizacion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        destacado = request.POST.get('destacado') == 'on'
        oculto = request.POST.get('oculto') == 'on'
        sin_stock = request.POST.get('sin_stock') == 'on'
        
        if producto:
            producto.nombre = nombre
            producto.beneficios = beneficios
            producto.description = description
            producto.categorizacion = categorizacion
            # Solo actualizar precio si se proporciona un valor
            if precio:
                producto.precio = precio
            producto.stock = stock
            producto.destacado = destacado
            producto.oculto = oculto
            producto.sin_stock = sin_stock
        else:
            producto = Product(
                nombre=nombre,
                beneficios=beneficios,
                description=description,
                categorizacion=categorizacion,
                precio=precio,
                stock=stock,
                destacado=destacado,
                oculto=oculto,
                sin_stock=sin_stock
            )
        
        # Manejar imagen
        if 'img' in request.FILES:
            producto.img = request.FILES['img']
        
        producto.save()
        messages.success(request, f'Producto {"actualizado" if product_id else "creado"} exitosamente.')
        return redirect('admin_productos')
    
    context = {
        'producto': producto,
    }
    return render(request, 'products/admin_producto_editar.html', context)


@staff_member_required
def admin_producto_eliminar(request, product_id):
    """Vista para eliminar un producto"""
    producto = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        nombre = producto.nombre
        producto.delete()
        messages.success(request, f'Producto "{nombre}" eliminado exitosamente.')
        return redirect('admin_productos')
    context = {
        'producto': producto,
    }
    return render(request, 'products/admin_producto_eliminar.html', context)


@staff_member_required
def admin_contenido_quienes_somos(request):
    """Vista para editar el contenido de Quienes Somos"""
    contenido = ContenidoQuienesSomos.load()
    
    if request.method == 'POST':
        contenido.titulo = request.POST.get('titulo')
        contenido.titulo_icono = request.POST.get('titulo_icono', 'fas fa-leaf')
        contenido.titulo_icono_color = request.POST.get('titulo_icono_color', '#198754')
        contenido.historia_titulo = request.POST.get('historia_titulo')
        contenido.historia_icono = request.POST.get('historia_icono', 'fas fa-seedling')
        contenido.historia_icono_color = request.POST.get('historia_icono_color', '#0d6efd')
        contenido.historia_texto = request.POST.get('historia_texto')
        contenido.mision_titulo = request.POST.get('mision_titulo')
        contenido.mision_icono = request.POST.get('mision_icono', 'fas fa-heart')
        contenido.mision_icono_color = request.POST.get('mision_icono_color', '#dc3545')
        contenido.mision_texto = request.POST.get('mision_texto')
        contenido.valores_titulo = request.POST.get('valores_titulo')
        contenido.valores_icono = request.POST.get('valores_icono', 'fas fa-certificate')
        contenido.valores_icono_color = request.POST.get('valores_icono_color', '#0d6efd')
        
        # Manejar imagen
        if 'imagen_archivo' in request.FILES:
            contenido.imagen_archivo = request.FILES['imagen_archivo']
        elif request.POST.get('imagen_url'):
            contenido.imagen_url = request.POST.get('imagen_url')
        
        # Manejar valores detallados
        titulos = request.POST.getlist('valor_titulo[]')
        descripciones = request.POST.getlist('valor_descripcion[]')
        valores_lista = []
        for titulo, descripcion in zip(titulos, descripciones):
            titulo = titulo.strip()
            descripcion = descripcion.strip()
            if titulo or descripcion:
                valores_lista.append({
                    'titulo': titulo,
                    'descripcion': descripcion,
                })
        contenido.valores = valores_lista
        
        contenido.save()
        messages.success(request, 'Contenido de Quienes Somos actualizado exitosamente.')
        return redirect('admin_contenido_quienes_somos')
    
    # Preparar valores para el formulario
    valores_form = []
    if contenido.valores:
        for valor in contenido.valores:
            if isinstance(valor, dict):
                valores_form.append({
                    'titulo': valor.get('titulo', ''),
                    'descripcion': valor.get('descripcion', ''),
                })
            elif isinstance(valor, str):
                partes = valor.split(':', 1)
                titulo = partes[0].strip()
                descripcion = partes[1].strip() if len(partes) > 1 else ''
                valores_form.append({
                    'titulo': titulo,
                    'descripcion': descripcion,
                })
    else:
        valores_form = [
            {'titulo': '100% Natural', 'descripcion': 'Todos nuestros productos son completamente naturales'},
            {'titulo': 'Cultivado con Amor', 'descripcion': 'Cada planta es cuidada personalmente'},
            {'titulo': 'Calidad Garantizada', 'descripcion': 'Procesos artesanales y tradicionales'},
            {'titulo': 'Atención Personalizada', 'descripcion': 'Cuidamos de cada cliente'},
        ]
    
    context = {
        'contenido': contenido,
        'valores_form': valores_form,
    }
    return render(request, 'products/admin_contenido_quienes_somos.html', context)


@staff_member_required
def admin_contenido_servicios(request):
    """Vista para editar el contenido general de Servicios Terapéuticos"""
    contenido = ContenidoServiciosTerapeuticos.load()
    
    if request.method == 'POST':
        contenido.titulo = request.POST.get('titulo')
        contenido.subtitulo = request.POST.get('subtitulo')
        contenido.mensaje_agenda_titulo = request.POST.get('mensaje_agenda_titulo')
        contenido.mensaje_agenda_texto = request.POST.get('mensaje_agenda_texto')
        contenido.save()
        messages.success(request, 'Contenido de Servicios Terapéuticos actualizado exitosamente.')
        return redirect('admin_contenido_servicios')
    
    context = {
        'contenido': contenido,
    }
    return render(request, 'products/admin_contenido_servicios.html', context)


@staff_member_required
def admin_servicios_lista(request):
    """Vista para listar todos los servicios terapéuticos"""
    servicios = ServicioTerapeutico.objects.all().order_by('orden', 'created')
    context = {
        'servicios': servicios,
    }
    return render(request, 'products/admin_servicios_lista.html', context)


@staff_member_required
def admin_servicio_editar(request, servicio_id=None):
    """Vista para crear o editar un servicio terapéutico"""
    if servicio_id:
        servicio = get_object_or_404(ServicioTerapeutico, id=servicio_id)
    else:
        servicio = None
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        icono = request.POST.get('icono', 'fas fa-spa')
        color_icono = request.POST.get('color_icono', '#667eea')
        orden = request.POST.get('orden', 0)
        activo = request.POST.get('activo') == 'on'
        
        # Manejar items (lista de características)
        items_texto = request.POST.get('items_texto', '')
        items_lista = []
        if items_texto:
            items_lista = [item.strip() for item in items_texto.split('\n') if item.strip()]
        
        if servicio:
            servicio.titulo = titulo
            servicio.descripcion = descripcion
            servicio.icono = icono
            servicio.color_icono = color_icono
            servicio.orden = int(orden) if orden else 0
            servicio.activo = activo
            servicio.items = items_lista
        else:
            servicio = ServicioTerapeutico(
                titulo=titulo,
                descripcion=descripcion,
                icono=icono,
                color_icono=color_icono,
                orden=int(orden) if orden else 0,
                activo=activo,
                items=items_lista
            )
        
        servicio.save()
        messages.success(request, f'Servicio {"actualizado" if servicio_id else "creado"} exitosamente.')
        return redirect('admin_servicios_lista')
    
    # Preparar items para el textarea
    items_texto = '\n'.join(servicio.items) if servicio and servicio.items else ''
    
    context = {
        'servicio': servicio,
        'items_texto': items_texto,
    }
    return render(request, 'products/admin_servicio_editar.html', context)


@staff_member_required
def admin_servicio_eliminar(request, servicio_id):
    """Vista para eliminar un servicio terapéutico"""
    servicio = get_object_or_404(ServicioTerapeutico, id=servicio_id)
    if request.method == 'POST':
        titulo = servicio.titulo
        servicio.delete()
        messages.success(request, f'Servicio "{titulo}" eliminado exitosamente.')
        return redirect('admin_servicios_lista')
    context = {
        'servicio': servicio,
    }
    return render(request, 'products/admin_servicio_eliminar.html', context)


@staff_member_required
def admin_foto_bienvenida(request):
    """Vista para editar la foto de bienvenida del home"""
    foto_bienvenida = FotoBienvenida.load()
    
    if request.method == 'POST':
        foto_bienvenida.titulo = request.POST.get('titulo')
        foto_bienvenida.texto = request.POST.get('texto')
        
        # Manejar imagen
        if 'imagen_archivo' in request.FILES:
            foto_bienvenida.imagen_archivo = request.FILES['imagen_archivo']
        elif request.POST.get('imagen_url'):
            foto_bienvenida.imagen_url = request.POST.get('imagen_url')
        
        foto_bienvenida.save()
        messages.success(request, 'Foto de bienvenida actualizada exitosamente.')
        return redirect('admin_foto_bienvenida')
    
    context = {
        'foto_bienvenida': foto_bienvenida,
    }
    return render(request, 'products/admin_foto_bienvenida.html', context)


@staff_member_required
def admin_pedidos(request):
    """Vista para ver los pedidos pendientes"""
    from cart.models import Order, OrderItem
    from accounts.models import UserProfile
    
    # Filtrar por estado si se proporciona
    status_filter = request.GET.get('status', 'pending')
    if status_filter == 'all':
        pedidos = Order.objects.all().order_by('-created')
    else:
        pedidos = Order.objects.filter(status=status_filter).order_by('-created')
    
    # Obtener información de perfiles de usuario
    pedidos_con_info = []
    for pedido in pedidos:
        try:
            profile = UserProfile.objects.get(user=pedido.user)
            telefono = profile.phone
        except UserProfile.DoesNotExist:
            telefono = 'No registrado'
        
        pedidos_con_info.append({
            'pedido': pedido,
            'telefono': telefono,
            'items': OrderItem.objects.filter(order=pedido)
        })
    
    context = {
        'pedidos_con_info': pedidos_con_info,
        'status_actual': status_filter,
    }
    return render(request, 'products/admin_pedidos.html', context)


@staff_member_required
def admin_pedido_actualizar(request, order_id):
    """Vista para actualizar el estado de un pedido"""
    from cart.models import Order
    
    pedido = get_object_or_404(Order, id=order_id)
    
    if request.method == 'POST':
        nuevo_status = request.POST.get('status')
        if nuevo_status in dict(Order.STATUS_CHOICES):
            pedido.status = nuevo_status
            pedido.save()
            messages.success(request, f'Estado del pedido #{pedido.id} actualizado a {pedido.get_status_display()}.')
        return redirect('admin_pedidos')
    
    return redirect('admin_pedidos')

