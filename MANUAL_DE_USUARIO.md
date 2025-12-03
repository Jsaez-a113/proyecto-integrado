# Manual de Usuario - Auka Terapias
## Sistema de E-commerce para Productos Naturales

---

## 1. Introducción

### 1.1 Descripción del Software

**Auka Terapias** es una plataforma web de comercio electrónico desarrollada con Django, diseñada específicamente para la venta de productos medicinales y cosméticos 100% naturales. El sistema permite a los usuarios explorar un catálogo de productos, realizar compras mediante un carrito de compras integrado con WhatsApp, y gestionar su perfil de usuario.

Para los administradores, el sistema ofrece un panel completo de administración que permite gestionar productos, contenido de páginas informativas, servicios terapéuticos, pedidos y más, todo desde una interfaz web intuitiva y moderna.

### 1.2 Propósito del Manual

Este manual está diseñado para servir como:
- **Guía de usuario**: Para clientes que desean utilizar la plataforma para realizar compras
- **Manual de administración**: Para personal administrativo que gestiona el contenido y productos
- **Documento de autocapacitación**: Para nuevos usuarios que desean aprender a utilizar el sistema de manera independiente

El manual está estructurado de forma clara y sencilla, con explicaciones paso a paso e imágenes descriptivas de cada funcionalidad.

---

## 2. Requisitos del Sistema

### 2.1 Requisitos de Hardware

**Mínimos:**
- Procesador: Intel Core i3 o equivalente (2.0 GHz o superior)
- Memoria RAM: 4 GB
- Espacio en disco: 500 MB libres
- Conexión a Internet: Banda ancha (mínimo 1 Mbps)

**Recomendados:**
- Procesador: Intel Core i5 o superior
- Memoria RAM: 8 GB o más
- Espacio en disco: 1 GB libres
- Conexión a Internet: Banda ancha (5 Mbps o superior)

### 2.2 Requisitos de Software

**Cliente (Navegador Web):**
- Navegador web moderno compatible con HTML5 y CSS3:
  - Google Chrome (versión 90 o superior) - **Recomendado**
  - Mozilla Firefox (versión 88 o superior)
  - Microsoft Edge (versión 90 o superior)
  - Safari (versión 14 o superior) - Solo macOS/iOS
- JavaScript habilitado
- Cookies habilitadas

**Servidor (Para instalación local):**
- Python 3.10 o superior
- Django 5.x
- SQLite (incluido con Python)
- Pillow 10.0.0 o superior (para manejo de imágenes)

### 2.3 Plataformas Soportadas

El sistema es una aplicación web que funciona en cualquier plataforma que tenga un navegador web compatible:

- **Windows**: Windows 10, Windows 11
- **macOS**: macOS 10.15 (Catalina) o superior
- **Linux**: Cualquier distribución moderna con navegador web
- **Dispositivos móviles**: 
  - iOS 12 o superior (iPhone/iPad)
  - Android 8.0 (Oreo) o superior

**Nota**: El sistema es responsive y se adapta automáticamente a diferentes tamaños de pantalla.

---

## 3. Instalación

### 3.1 Instalación para Usuarios Finales

Como usuario final, **NO necesitas instalar nada**. El sistema es una aplicación web que se accede a través de un navegador. Simplemente:

1. Abre tu navegador web preferido
2. Ingresa la URL proporcionada por el administrador del sistema
3. ¡Listo! Ya puedes comenzar a usar el sistema

### 3.2 Instalación para Administradores/Desarrolladores

Si necesitas instalar el sistema en un servidor local o de producción, sigue estos pasos:

#### Paso 1: Verificar Python

Abre una terminal o línea de comandos y verifica que Python esté instalado:

```bash
python --version
# Debe mostrar: Python 3.10.x o superior
```

Si no tienes Python instalado, descárgalo desde [python.org](https://www.python.org/downloads/)

#### Paso 2: Navegar al Directorio del Proyecto

```bash
cd "ruta/al/proyecto/integrado"
```

#### Paso 3: Crear Entorno Virtual (Recomendado)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Paso 4: Instalar Dependencias

```bash
pip install -r requirements.txt
```

Esto instalará:
- Django 5.x
- Pillow (para manejo de imágenes)

#### Paso 5: Aplicar Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

#### Paso 6: Crear Superusuario (Administrador)

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para crear un usuario administrador:
- Username: (elige un nombre de usuario)
- Email: (opcional pero recomendado)
- Password: (ingresa una contraseña segura)

#### Paso 7: Ejecutar el Servidor

```bash
python manage.py runserver
```

El sistema estará disponible en:
- **Sitio principal**: http://127.0.0.1:8000/
- **Panel de administración**: http://127.0.0.1:8000/admin/

#### Paso 8: Acceder al Sistema

Abre tu navegador y visita las URLs indicadas arriba.

---

## 4. Arquitectura del Software

### 4.1 Resumen de Funcionalidades

El sistema **Auka Terapias** está diseñado con una arquitectura modular basada en Django, dividida en las siguientes aplicaciones principales:

#### 4.1.1 Módulo de Productos (`products`)
- Gestión de catálogo de productos
- Sistema de reseñas y calificaciones
- Contenido editable de páginas informativas
- Gestión de servicios terapéuticos
- Foto de bienvenida del home

#### 4.1.2 Módulo de Usuarios (`accounts`)
- Sistema de registro e inicio de sesión
- Perfiles de usuario
- Historial de compras

#### 4.1.3 Módulo de Carrito (`cart`)
- Carrito de compras
- Gestión de órdenes
- Integración con WhatsApp

### 4.2 Requerimientos Funcionales

#### Para Usuarios (Clientes):

1. **Navegación y Exploración**
   - Ver página de inicio con productos destacados
   - Explorar catálogo completo de productos
   - Filtrar productos por categoría (Medicinal/Cosmético)
   - Ordenar productos por precio o relevancia
   - Ver detalles completos de cada producto

2. **Autenticación**
   - Registrarse en el sistema
   - Iniciar sesión
   - Cerrar sesión
   - Recuperar contraseña (si está implementado)

3. **Carrito de Compras**
   - Añadir productos al carrito
   - Ver carrito con productos seleccionados
   - Modificar cantidades
   - Eliminar productos del carrito
   - Enviar pedido por WhatsApp

4. **Reseñas**
   - Ver reseñas de otros usuarios
   - Publicar reseñas con calificación (1-5 estrellas)

5. **Perfil de Usuario**
   - Ver historial de pedidos
   - Ver estado de pedidos

#### Para Administradores:

1. **Gestión de Productos**
   - Crear nuevos productos
   - Editar productos existentes
   - Eliminar productos
   - Marcar productos como destacados
   - Ocultar/mostrar productos
   - Gestionar stock

2. **Gestión de Contenido**
   - Editar contenido de "Quienes Somos"
   - Editar contenido de "Servicios Terapéuticos"
   - Gestionar bloques de servicios terapéuticos
   - Editar foto de bienvenida del home
   - Seleccionar iconos y colores para secciones

3. **Gestión de Pedidos**
   - Ver lista de pedidos
   - Ver detalles de cada pedido
   - Actualizar estado de pedidos (Pendiente, Confirmado, Completado, Cancelado)
   - Ver información del cliente

4. **Panel de Administración**
   - Acceso centralizado a todas las funciones administrativas
   - Interfaz intuitiva con tarjetas de acceso rápido

### 4.3 Estructura de Datos

#### Modelos Principales:

1. **Product**: Almacena información de productos
   - nombre, beneficios, descripción
   - categorización (medicinal/cosmético)
   - precio, stock, imagen
   - destacado, oculto, sin_stock

2. **Review**: Reseñas de productos
   - producto, usuario, rating, comentario

3. **CartItem**: Items en el carrito
   - usuario, producto, cantidad

4. **Order**: Órdenes de compra
   - usuario, total, estado, fecha

5. **OrderItem**: Items de una orden
   - orden, nombre_producto, precio, cantidad

6. **ServicioTerapeutico**: Servicios terapéuticos
   - título, descripción, icono, color_icono
   - items (características), orden, activo

7. **ContenidoQuienesSomos**: Contenido editable de "Quienes Somos"
   - título, iconos y colores configurables
   - historia, misión, valores

8. **FotoBienvenida**: Foto de bienvenida del home
   - título, texto, imagen

---

## 5. Items del Software - Pantalla por Pantalla

### 5.1 Página de Inicio (Home)

**URL**: `/` o `http://127.0.0.1:8000/`

**Descripción**: Esta es la primera página que ven los usuarios al acceder al sitio.

**Elementos principales:**

1. **Barra de Navegación Superior**
   - **Logo "Auka Terapias"**: Enlace que lleva al home
   - **Menú de Navegación**:
     - Inicio: Vuelve a la página principal
     - Catálogo: Muestra todos los productos
     - Quienes Somos: Información sobre el emprendimiento
     - Servicios Terapéuticos: Información sobre masajes y terapias
   - **Icono de Carrito**: Muestra cantidad de items y lleva al carrito (solo si hay sesión iniciada)
   - **Botones de Usuario**:
     - "Registrarse": Si no hay sesión iniciada
     - "Iniciar Sesión": Si no hay sesión iniciada
     - Nombre de usuario + "Cerrar Sesión": Si hay sesión iniciada

2. **Sección de Bienvenida**
   - **Foto de Bienvenida**: Imagen configurable por el administrador
   - **Título**: Texto configurable (ej: "Bienvenido a Auka Terapias")
   - **Texto descriptivo**: Mensaje configurable

3. **Productos Destacados**
   - Muestra hasta 3 productos marcados como "destacados"
   - Cada producto muestra:
     - Imagen del producto
     - Nombre
     - Precio
     - Botón "Ver Detalles"

4. **Pie de Página (Footer)**
   - Enlaces a redes sociales (Instagram, WhatsApp)
   - Información de contacto
   - Copyright

**Funcionalidades:**
- Navegación a otras secciones del sitio
- Acceso rápido a productos destacados
- Acceso al carrito de compras

---

### 5.2 Página de Catálogo

**URL**: `/catalogo/`

**Descripción**: Muestra todos los productos disponibles en el sistema con opciones de filtrado y ordenamiento.

**Elementos principales:**

1. **Barra de Navegación** (igual que en Home)

2. **Título de la Página**
   - "Catálogo de Productos"

3. **Filtros y Ordenamiento**
   - **Filtro por Categoría**:
     - Botón "Todos": Muestra todos los productos
     - Botón "Medicinal": Solo productos medicinales
     - Botón "Cosmético": Solo productos cosméticos
   - **Ordenamiento**:
     - "Relevancia": Orden por fecha de creación (más recientes primero)
     - "Precio: Menor a Mayor"
     - "Precio: Mayor a Menor"

4. **Grid de Productos**
   - Muestra 10 productos por página
   - Cada tarjeta de producto contiene:
     - Imagen del producto
     - Nombre del producto
     - Precio
     - Botón "Ver Detalles"

5. **Paginación**
   - Números de página en la parte inferior
   - Botones "Anterior" y "Siguiente"

**Funcionalidades:**
- Filtrar productos por categoría
- Ordenar productos por diferentes criterios
- Navegar entre páginas de productos
- Acceder al detalle de cada producto

---

### 5.3 Detalle de Producto

**URL**: `/producto/<id>/`

**Descripción**: Muestra información completa de un producto individual.

**Elementos principales:**

1. **Barra de Navegación** (igual que en otras páginas)

2. **Información del Producto**
   - **Imagen del Producto**: Imagen grande del producto
   - **Nombre del Producto**: Título destacado
   - **Precio**: Precio en formato de moneda
   - **Categoría**: Badge indicando "Medicinal" o "Cosmético"
   - **Stock**: Indicador de disponibilidad
   - **Beneficios**: Lista de beneficios del producto
   - **Descripción**: Descripción completa del producto

3. **Botones de Acción**
   - **"Añadir al Carrito"**: Solo visible si hay sesión iniciada
     - Añade el producto al carrito y redirige a la página del carrito
   - **"Iniciar Sesión para Comprar"**: Solo visible si NO hay sesión iniciada

4. **Sección de Reseñas**
   - **Título**: "Reseñas de Clientes"
   - **Lista de Reseñas**: Muestra todas las reseñas del producto
     - Cada reseña muestra:
       - Nombre de usuario
       - Calificación (estrellas de 1 a 5)
       - Comentario
       - Fecha de publicación
   - **Formulario de Nueva Reseña** (solo si hay sesión iniciada):
     - Selector de calificación (1-5 estrellas)
     - Campo de texto para comentario
     - Botón "Publicar Reseña"

**Funcionalidades:**
- Ver información completa del producto
- Añadir producto al carrito (requiere sesión)
- Ver reseñas de otros usuarios
- Publicar reseñas propias (requiere sesión)

---

### 5.4 Página "Quienes Somos"

**URL**: `/quienes-somos/`

**Descripción**: Página informativa sobre el emprendimiento Auka Terapias.

**Elementos principales:**

1. **Barra de Navegación** (igual que en otras páginas)

2. **Título Principal**
   - Título configurable con icono y color personalizable

3. **Imagen Principal**
   - Imagen circular del emprendimiento (si está configurada)

4. **Sección "Nuestra Historia"**
   - Título con icono y color personalizable
   - Texto descriptivo editable

5. **Sección "Nuestra Misión"**
   - Título con icono y color personalizable
   - Texto descriptivo editable

6. **Sección "Nuestros Valores"**
   - Título con icono y color personalizable
   - Lista de valores con formato:
     - **Título del valor**: Descripción del valor
     - Cada valor tiene un checkmark verde

7. **Botones de Acción**
   - "Ver Productos": Lleva al catálogo
   - "Nuestros Servicios": Lleva a la página de servicios

**Funcionalidades:**
- Información sobre el emprendimiento
- Navegación a otras secciones

---

### 5.5 Página "Servicios Terapéuticos"

**URL**: `/servicios-terapeuticos/`

**Descripción**: Muestra información sobre los servicios de masajes y terapias ofrecidos.

**Elementos principales:**

1. **Barra de Navegación** (igual que en otras páginas)

2. **Encabezado**
   - Título principal configurable
   - Subtítulo descriptivo

3. **Bloques de Servicios**
   - Grid de tarjetas, cada una representa un servicio terapéutico
   - Cada tarjeta muestra:
     - **Icono**: Icono personalizable con color configurable
     - **Título del Servicio**
     - **Descripción**: Texto descriptivo del servicio
     - **Características**: Lista de items (ej: "Duración: 60 minutos")

4. **Sección "Agenda Tu Sesión"**
   - Tarjeta destacada con fondo de color
   - Título y texto configurable
   - **Botón "Contactar por WhatsApp"**: Abre WhatsApp con mensaje pre-escrito

**Funcionalidades:**
- Ver información de servicios terapéuticos
- Contactar por WhatsApp para agendar sesión

---

### 5.6 Carrito de Compras

**URL**: `/cart/`

**Descripción**: Muestra todos los productos añadidos al carrito del usuario.

**Requisito**: Debe haber sesión iniciada.

**Elementos principales:**

1. **Barra de Navegación** (igual que en otras páginas)

2. **Título**: "Mi Carrito"

3. **Lista de Productos en el Carrito**
   - Cada item muestra:
     - Imagen del producto
     - Nombre del producto
     - Precio unitario
     - **Selector de Cantidad**: Input numérico para modificar cantidad
     - **Subtotal**: Precio × Cantidad
     - **Botón "Eliminar"**: Remueve el producto del carrito

4. **Resumen del Carrito**
   - **Total de Items**: Cantidad total de productos
   - **Total a Pagar**: Suma de todos los subtotales
   - **Botón "Enviar por WhatsApp"**: 
     - Crea una orden en el sistema
     - Genera mensaje con los productos
     - Abre WhatsApp con el mensaje pre-escrito
     - Limpia el carrito

5. **Mensaje de Carrito Vacío**
   - Se muestra si no hay productos en el carrito
   - Incluye botón "Ver Catálogo"

**Funcionalidades:**
- Ver productos en el carrito
- Modificar cantidades
- Eliminar productos
- Enviar pedido por WhatsApp
- Ver total a pagar

---

### 5.7 Registro de Usuario

**URL**: `/accounts/register/`

**Descripción**: Permite crear una nueva cuenta en el sistema.

**Elementos principales:**

1. **Barra de Navegación** (igual que en otras páginas)

2. **Título**: "Registrarse"

3. **Formulario de Registro**
   - **Nombre de Usuario**: Campo de texto (requerido)
   - **Email**: Campo de email (opcional)
   - **Contraseña**: Campo de contraseña (requerido)
   - **Confirmar Contraseña**: Campo de contraseña (requerido)
   - **Botón "Registrarse"**: Envía el formulario

4. **Enlace a Inicio de Sesión**
   - "¿Ya tienes cuenta? Inicia sesión aquí"

**Funcionalidades:**
- Crear nueva cuenta de usuario
- Validación de formulario
- Redirección automática al login después del registro

---

### 5.8 Inicio de Sesión

**URL**: `/accounts/login/`

**Descripción**: Permite a los usuarios iniciar sesión en el sistema.

**Elementos principales:**

1. **Barra de Navegación** (igual que en otras páginas)

2. **Título**: "Iniciar Sesión"

3. **Formulario de Login**
   - **Nombre de Usuario**: Campo de texto (requerido)
   - **Contraseña**: Campo de contraseña (requerido)
   - **Botón "Iniciar Sesión"**: Envía el formulario

4. **Enlace a Registro**
   - "¿No tienes cuenta? Regístrate aquí"

**Funcionalidades:**
- Autenticación de usuarios
- Redirección después del login
- Manejo de errores de autenticación

---

### 5.9 Perfil de Usuario

**URL**: `/accounts/profile/`

**Descripción**: Muestra el perfil del usuario y su historial de pedidos.

**Requisito**: Debe haber sesión iniciada.

**Elementos principales:**

1. **Barra de Navegación** (igual que en otras páginas)

2. **Título**: "Mi Perfil"

3. **Información del Usuario**
   - Nombre de usuario
   - Email (si está disponible)

4. **Historial de Pedidos**
   - Tabla con las siguientes columnas:
     - **ID de Orden**: Número de orden
     - **Fecha**: Fecha de creación
     - **Total**: Monto total de la orden
     - **Estado**: Badge con el estado actual
       - "Pendiente" (amarillo)
       - "Confirmado" (azul)
       - "Completado" (verde)
       - "Cancelado" (rojo)
   - Si no hay pedidos, muestra mensaje: "No tienes pedidos aún"

**Funcionalidades:**
- Ver información del perfil
- Ver historial completo de pedidos
- Ver estado de cada pedido

---

### 5.10 Panel de Administración - Página Principal

**URL**: `/admin-panel/`

**Descripción**: Panel central de administración con acceso a todas las funciones administrativas.

**Requisito**: Debe ser usuario staff (administrador).

**Elementos principales:**

1. **Barra de Navegación** (igual que en otras páginas)

2. **Título**: "Panel de Administración"

3. **Tarjetas de Acceso Rápido** (Grid de 3 columnas):

   **a) Tarjeta "Productos"**
   - Icono: Caja (box)
   - Título: "Productos"
   - Descripción: "Administra tus productos: añadir, modificar, eliminar, destacar, ocultar, etc."
   - Botón: "Gestionar Productos" (azul/primary)

   **b) Tarjeta "Contenido"**
   - Icono: Archivo (file-alt)
   - Título: "Contenido"
   - Descripción: "Edita el contenido de las páginas Quienes Somos y Servicios Terapéuticos."
   - Botones:
     - "Quienes Somos" (verde/success)
     - "Servicios Terapéuticos (General)" (verde/success)
     - "Gestionar Bloques de Servicios" (verde outline)

   **c) Tarjeta "Foto de Bienvenida"**
   - Icono: Imagen (image)
   - Título: "Foto de Bienvenida"
   - Descripción: "Edita la foto y texto de bienvenida en la página de inicio."
   - Botón: "Editar Foto de Bienvenida" (azul/info)

4. **Segunda Fila - Tarjeta "Pedidos"**
   - Icono: Carrito de compras (shopping-cart)
   - Título: "Pedidos"
   - Descripción: "Gestiona los pedidos de los clientes: ver información del usuario, productos pedidos y actualizar estados."
   - Botón: "Ver Pedidos" (amarillo/warning)
   - **Nota**: Esta tarjeta está centrada debajo de "Contenido"

5. **Botón "Volver al Inicio"**
   - En la parte inferior, centrado

**Funcionalidades:**
- Acceso centralizado a todas las funciones administrativas
- Navegación rápida a cada módulo

---

### 5.11 Administración - Gestión de Productos

**URL**: `/admin-panel/productos/`

**Descripción**: Lista todos los productos del sistema con opciones de gestión.

**Requisito**: Debe ser usuario staff.

**Elementos principales:**

1. **Barra de Navegación** (igual que en otras páginas)

2. **Encabezado**
   - Título: "Administrar Productos"
   - Botón "Nuevo Producto" (verde, a la derecha)

3. **Tabla de Productos**
   - Columnas:
     - **ID**: Número de identificación
     - **Imagen**: Miniatura del producto
     - **Nombre**: Nombre del producto
     - **Categoría**: Badge (Medicinal/Cosmético)
     - **Precio**: Precio formateado
     - **Stock**: Cantidad disponible
     - **Destacado**: Badge "Sí" o "No"
     - **Oculto**: Badge "Sí" o "No"
     - **Acciones**: Botones "Editar" y "Eliminar"

4. **Botones de Acción por Producto**
   - **"Editar"** (azul/primary): Lleva al formulario de edición
   - **"Eliminar"** (rojo/danger): Muestra confirmación antes de eliminar

5. **Mensaje si no hay productos**
   - "No hay productos registrados. Crea el primero."

6. **Botón "Volver al Panel"** (parte inferior)

**Funcionalidades:**
- Ver lista completa de productos
- Crear nuevo producto
- Editar producto existente
- Eliminar producto
- Ver estado de productos (destacado, oculto)

---

### 5.12 Administración - Crear/Editar Producto

**URL**: `/admin-panel/productos/nuevo/` o `/admin-panel/productos/<id>/editar/`

**Descripción**: Formulario para crear o editar un producto.

**Requisito**: Debe ser usuario staff.

**Elementos principales:**

1. **Barra de Navegación** (igual que en otras páginas)

2. **Título del Formulario**
   - "Nuevo Producto" o "Editar Producto"

3. **Formulario de Producto**
   - **Nombre del Producto***: Campo de texto (requerido)
   - **Beneficios***: Textarea (requerido)
   - **Descripción***: Textarea (requerido)
   - **Categorización***: Select (Medicinal/Cosmético) (requerido)
   - **Precio***: Campo numérico (requerido)
   - **Imagen**: 
     - Input de archivo para subir imagen
     - O campo de URL para imagen remota
   - **Stock***: Campo numérico (requerido)
   - **Checkboxes**:
     - ☐ Destacado: Marcar para mostrar en productos destacados
     - ☐ Oculto: Marcar para ocultar del catálogo
     - ☐ Sin Stock: Marcar si el producto está sin stock

4. **Botones de Acción**
   - **"Cancelar"** (gris): Vuelve a la lista de productos
   - **"Guardar"** (verde): Guarda los cambios

**Funcionalidades:**
- Crear nuevo producto
- Editar producto existente
- Subir imagen o usar URL
- Configurar opciones del producto

---

### 5.13 Administración - Eliminar Producto

**URL**: `/admin-panel/productos/<id>/eliminar/`

**Descripción**: Página de confirmación para eliminar un producto.

**Requisito**: Debe ser usuario staff.

**Elementos principales:**

1. **Barra de Navegación** (igual que en otras páginas)

2. **Mensaje de Confirmación**
   - Título: "¿Estás seguro?"
   - Texto: "¿Estás seguro de que deseas eliminar el producto '[Nombre del Producto]'?"
   - Advertencia: "Esta acción no se puede deshacer."

3. **Información del Producto**
   - Muestra detalles del producto a eliminar

4. **Botones de Acción**
   - **"Cancelar"** (gris): Vuelve a la lista sin eliminar
   - **"Eliminar"** (rojo): Confirma y elimina el producto

**Funcionalidades:**
- Confirmar eliminación de producto
- Cancelar eliminación

---

### 5.14 Administración - Editar Contenido "Quienes Somos"

**URL**: `/admin-panel/contenido/quienes-somos/`

**Descripción**: Permite editar todo el contenido de la página "Quienes Somos".

**Requisito**: Debe ser usuario staff.

**Elementos principales:**

1. **Barra de Navegación** (igual que en otras páginas)

2. **Título**: "Editar Contenido: Quienes Somos"

3. **Sección: Título Principal**
   - **Título Principal**: Campo de texto
   - **Icono del Título**: 
     - Preview del icono actual
     - Botón "Seleccionar Icono" (abre modal)
     - Selector de color para el icono
   - **Imagen Principal**: 
     - Input de archivo para subir imagen
     - O campo de URL para imagen remota

4. **Sección: Nuestra Historia**
   - **Título**: Campo de texto
   - **Icono**: Botón para seleccionar icono con selector de color
   - **Texto**: Textarea para el contenido

5. **Sección: Nuestra Misión**
   - **Título**: Campo de texto
   - **Icono**: Botón para seleccionar icono con selector de color
   - **Texto**: Textarea para el contenido

6. **Sección: Nuestros Valores**
   - **Título**: Campo de texto
   - **Icono**: Botón para seleccionar icono con selector de color
   - **Gestor de Valores**:
     - Lista de valores existentes
     - Cada valor tiene:
       - Campo "Título del Valor"
       - Campo "Descripción"
       - Botón "Eliminar"
     - Botón "Añadir Valor": Añade un nuevo valor a la lista

7. **Modal de Selección de Iconos**
   - Campo de búsqueda de iconos
   - Selector de color (picker + input hexadecimal)
   - Grid de iconos disponibles
   - Al hacer clic en un icono, se selecciona y cierra el modal

8. **Botones de Acción**
   - **"Cancelar"**: Vuelve al panel
   - **"Guardar Cambios"** (verde): Guarda todas las modificaciones

**Funcionalidades:**
- Editar título principal con icono y color
- Editar secciones (Historia, Misión, Valores) con iconos y colores personalizables
- Gestionar lista de valores (añadir, editar, eliminar)
- Subir imagen o usar URL
- Seleccionar iconos de Font Awesome con colores personalizados

---

### 5.15 Administración - Editar Contenido "Servicios Terapéuticos"

**URL**: `/admin-panel/contenido/servicios/`

**Descripción**: Permite editar el contenido general de la página "Servicios Terapéuticos".

**Requisito**: Debe ser usuario staff.

**Elementos principales:**

1. **Barra de Navegación** (igual que en otras páginas)

2. **Título**: "Editar Contenido: Servicios Terapéuticos"

3. **Formulario de Contenido**
   - **Título Principal**: Campo de texto
   - **Subtítulo**: Campo de texto
   - **Título del Mensaje de Agenda**: Campo de texto
   - **Texto del Mensaje de Agenda**: Textarea

4. **Botones de Acción**
   - **"Cancelar"**: Vuelve al panel
   - **"Guardar Cambios"** (verde): Guarda las modificaciones

**Funcionalidades:**
- Editar contenido general de la página de servicios
- Configurar mensaje de agenda

---

### 5.16 Administración - Gestionar Bloques de Servicios

**URL**: `/admin-panel/servicios/`

**Descripción**: Lista todos los bloques de servicios terapéuticos individuales.

**Requisito**: Debe ser usuario staff.

**Elementos principales:**

1. **Barra de Navegación** (igual que en otras páginas)

2. **Encabezado**
   - Título: "Administrar Servicios Terapéuticos"
   - Botón "Nuevo Servicio" (verde, a la derecha)

3. **Mensaje Informativo**
   - Explica que aquí se gestionan los bloques de servicios
   - Enlace para editar el contenido general

4. **Tabla de Servicios**
   - Columnas:
     - **Orden**: Número de orden de visualización
     - **Icono**: Icono del servicio con color
     - **Título**: Título del servicio
     - **Descripción**: Descripción truncada
     - **Items**: Badge con cantidad de características
     - **Estado**: Badge "Activo" o "Inactivo"
     - **Acciones**: Botones "Editar" y "Eliminar" (centrados)

5. **Botones de Acción por Servicio**
   - **"Editar"** (azul/primary): Lleva al formulario de edición
   - **"Eliminar"** (rojo/danger): Muestra confirmación

6. **Mensaje si no hay servicios**
   - "No hay servicios registrados. Crea el primero."

7. **Botón "Volver al Panel"** (parte inferior)

**Funcionalidades:**
- Ver lista de servicios terapéuticos
- Crear nuevo servicio
- Editar servicio existente
- Eliminar servicio
- Ver estado de servicios

---

### 5.17 Administración - Crear/Editar Servicio Terapéutico

**URL**: `/admin-panel/servicios/nuevo/` o `/admin-panel/servicios/<id>/editar/`

**Descripción**: Formulario para crear o editar un servicio terapéutico.

**Requisito**: Debe ser usuario staff.

**Elementos principales:**

1. **Barra de Navegación** (igual que en otras páginas)

2. **Título del Formulario**
   - "Nuevo Servicio" o "Editar Servicio"

3. **Formulario de Servicio**
   - **Título del Servicio***: Campo de texto (requerido)
   - **Descripción***: Textarea (requerido)
   - **Icono**: 
     - Preview del icono actual con color
     - Botón "Seleccionar Icono" (abre modal)
     - Selector de color para el icono
   - **Orden de Visualización**: Campo numérico (menor número aparece primero)
   - **Características del Servicio**: Textarea
     - Una característica por línea
     - Ejemplo: "Duración: 60 minutos"
   - **Checkbox**:
     - ☐ Servicio Activo: Marcar para mostrar en la página

4. **Modal de Selección de Iconos**
   - Campo de búsqueda de iconos
   - Selector de color (picker + input hexadecimal)
   - Grid de iconos disponibles con preview del color seleccionado
   - Al hacer clic en un icono, se selecciona y cierra el modal

5. **Botones de Acción**
   - **"Cancelar"** (gris): Vuelve a la lista
   - **"Guardar"** (verde): Guarda los cambios

**Funcionalidades:**
- Crear nuevo servicio terapéutico
- Editar servicio existente
- Seleccionar icono con color personalizado
- Configurar orden de visualización
- Añadir características del servicio
- Activar/desactivar servicio

---

### 5.18 Administración - Eliminar Servicio Terapéutico

**URL**: `/admin-panel/servicios/<id>/eliminar/`

**Descripción**: Página de confirmación para eliminar un servicio terapéutico.

**Requisito**: Debe ser usuario staff.

**Elementos principales:**

1. **Barra de Navegación** (igual que en otras páginas)

2. **Mensaje de Confirmación**
   - Título: "¿Estás seguro?"
   - Texto: "¿Estás seguro de que deseas eliminar el servicio '[Título del Servicio]'?"
   - Advertencia: "Esta acción no se puede deshacer."

3. **Información del Servicio**
   - Muestra detalles del servicio a eliminar

4. **Botones de Acción**
   - **"Cancelar"** (gris): Vuelve a la lista sin eliminar
   - **"Eliminar"** (rojo): Confirma y elimina el servicio

**Funcionalidades:**
- Confirmar eliminación de servicio
- Cancelar eliminación

---

### 5.19 Administración - Editar Foto de Bienvenida

**URL**: `/admin-panel/foto-bienvenida/`

**Descripción**: Permite editar la foto y texto de bienvenida que aparece en el home.

**Requisito**: Debe ser usuario staff.

**Elementos principales:**

1. **Barra de Navegación** (igual que en otras páginas)

2. **Título**: "Editar Foto de Bienvenida"

3. **Formulario**
   - **Título**: Campo de texto
   - **Texto**: Textarea
   - **Imagen**: 
     - Input de archivo para subir imagen
     - O campo de URL para imagen remota
   - Preview de la imagen actual (si existe)

4. **Botones de Acción**
   - **"Cancelar"**: Vuelve al panel
   - **"Guardar Cambios"** (verde): Guarda las modificaciones

**Funcionalidades:**
- Editar título y texto de bienvenida
- Cambiar imagen de bienvenida (subir archivo o usar URL)

---

### 5.20 Administración - Gestión de Pedidos

**URL**: `/admin-panel/pedidos/`

**Descripción**: Lista todos los pedidos realizados por los clientes.

**Requisito**: Debe ser usuario staff.

**Elementos principales:**

1. **Barra de Navegación** (igual que en otras páginas)

2. **Título**: "Gestión de Pedidos"

3. **Tabla de Pedidos**
   - Columnas:
     - **ID de Orden**: Número de orden
     - **Cliente**: Nombre de usuario del cliente
     - **Fecha**: Fecha de creación
     - **Total**: Monto total formateado
     - **Estado**: Badge con estado actual
       - "Pendiente" (amarillo)
       - "Confirmado" (azul)
       - "Completado" (verde)
       - "Cancelado" (rojo)
     - **Acciones**: Botón "Ver Detalles"

4. **Botón "Ver Detalles"** por pedido
   - Lleva a la página de detalles del pedido

5. **Mensaje si no hay pedidos**
   - "No hay pedidos registrados."

6. **Botón "Volver al Panel"** (parte inferior)

**Funcionalidades:**
- Ver lista completa de pedidos
- Ver información de cada pedido
- Filtrar por estado (si está implementado)

---

### 5.21 Administración - Detalles de Pedido

**URL**: `/admin-panel/pedidos/<id>/actualizar/`

**Descripción**: Muestra detalles completos de un pedido y permite actualizar su estado.

**Requisito**: Debe ser usuario staff.

**Elementos principales:**

1. **Barra de Navegación** (igual que en otras páginas)

2. **Título**: "Detalles del Pedido #<ID>"

3. **Información del Cliente**
   - Nombre de usuario
   - Email (si está disponible)

4. **Información del Pedido**
   - **ID de Orden**: Número de orden
   - **Fecha de Creación**: Fecha y hora
   - **Estado Actual**: Badge con estado

5. **Lista de Productos**
   - Tabla con:
     - Nombre del producto
     - Precio unitario
     - Cantidad
     - Subtotal

6. **Resumen**
   - **Total de Items**: Cantidad total
   - **Total a Pagar**: Monto total

7. **Actualizar Estado**
   - Select con opciones:
     - Pendiente
     - Confirmado
     - Completado
     - Cancelado
   - Botón "Actualizar Estado" (verde)

8. **Botones de Acción**
   - **"Volver a Pedidos"**: Vuelve a la lista
   - **"Actualizar Estado"**: Guarda el nuevo estado

**Funcionalidades:**
- Ver información completa del pedido
- Ver productos incluidos en el pedido
- Actualizar estado del pedido
- Ver información del cliente

---

## 6. Consejos y Mejores Prácticas

### 6.1 Para Usuarios (Clientes)

1. **Registro**: Crea una cuenta para poder realizar compras y ver tu historial
2. **Carrito**: Revisa tu carrito antes de enviar por WhatsApp
3. **Reseñas**: Comparte tu experiencia con otros usuarios
4. **Contacto**: Usa WhatsApp para consultas o para concretar compras

### 6.2 Para Administradores

1. **Productos Destacados**: Marca como destacados los productos más importantes (máximo 3 para el home)
2. **Stock**: Mantén el stock actualizado para evitar problemas
3. **Imágenes**: Usa imágenes de buena calidad para los productos
4. **Contenido**: Mantén el contenido de las páginas informativas actualizado
5. **Pedidos**: Revisa y actualiza el estado de los pedidos regularmente
6. **Iconos y Colores**: Usa iconos y colores consistentes para mantener la identidad visual

---

## 7. Solución de Problemas Comunes

### 7.1 No puedo iniciar sesión
- Verifica que el nombre de usuario y contraseña sean correctos
- Asegúrate de que las cookies estén habilitadas
- Intenta limpiar la caché del navegador

### 7.2 No puedo añadir productos al carrito
- Asegúrate de haber iniciado sesión
- Verifica que el producto tenga stock disponible
- Recarga la página e intenta nuevamente

### 7.3 El botón de WhatsApp no funciona
- Verifica que tengas WhatsApp instalado en tu dispositivo
- Asegúrate de tener conexión a Internet
- Intenta desde un dispositivo móvil si estás en computadora

### 7.4 No veo mis pedidos en el perfil
- Verifica que hayas completado al menos un pedido
- Asegúrate de estar en la cuenta correcta
- Contacta al administrador si el problema persiste

### 7.5 No puedo acceder al panel de administración
- Verifica que tu cuenta tenga permisos de staff
- Contacta al administrador principal para obtener acceso
- Asegúrate de estar iniciado sesión

---

## 8. Glosario de Términos

- **Producto Destacado**: Producto que aparece en la página de inicio
- **Producto Oculto**: Producto que no se muestra en el catálogo público
- **Orden/Pedido**: Solicitud de compra realizada por un cliente
- **Estado de Pedido**: Estado actual de un pedido (Pendiente, Confirmado, Completado, Cancelado)
- **Carrito**: Lista temporal de productos que el usuario desea comprar
- **Staff**: Usuario con permisos de administración
- **Icono**: Símbolo visual usado para representar secciones o servicios
- **Badge**: Etiqueta pequeña que muestra información (ej: estado, categoría)

---

## 9. Contacto y Soporte

Para más información o asistencia:

- **WhatsApp**: +56 9 8566 1992
- **Instagram**: [@auka_terapias](https://www.instagram.com/auka_terapias/?hl=es)

---

**Versión del Manual**: 1.0  
**Fecha de Actualización**: 2025  
**Desarrollado para**: Auka Terapias

---

*Este manual está diseñado para ser una guía completa y didáctica. Si encuentras algún error o tienes sugerencias de mejora, por favor contacta al equipo de desarrollo.*


