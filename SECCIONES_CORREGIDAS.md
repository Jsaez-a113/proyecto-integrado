# Secciones Corregidas para el Informe - Auka Terapias

Este documento contiene las secciones corregidas listas para copiar y pegar en tu informe, reemplazando las versiones originales.

---

## 📋 SECCIÓN III.6.1.1 - Modelo Lógico (CORREGIDO)

### REEMPLAZAR: Sección III.6.1.1 completa

**Entidades Principales:**

**PRODUCTO**
- id_producto (PK, INT, AUTO_INCREMENT)
- nombre (VARCHAR(200), NOT NULL)
- beneficios (TEXT, NOT NULL)
- descripcion (TEXT, NOT NULL)
- categorizacion (VARCHAR(20), NOT NULL) [medicinal/cosmético]
- precio (DECIMAL(10,2), NOT NULL)
- img (VARCHAR(500), NOT NULL) [URL]
- stock (INT, NOT NULL)
- destacado (BOOLEAN, DEFAULT FALSE)
- created (DATETIME, AUTO_NOW_ADD)
- updated (DATETIME, AUTO_NOW)

**USUARIO** (Modelo estándar Django User)
- id_usuario (PK, INT, AUTO_INCREMENT)
- username (VARCHAR(150), UNIQUE, NOT NULL)
- email (VARCHAR(254), UNIQUE)
- password (VARCHAR(128), NOT NULL) [hasheada]
- first_name (VARCHAR(150))
- last_name (VARCHAR(150))
- is_active (BOOLEAN, DEFAULT TRUE)
- is_staff (BOOLEAN, DEFAULT FALSE)
- is_superuser (BOOLEAN, DEFAULT FALSE)
- date_joined (DATETIME, AUTO_NOW_ADD)
- last_login (DATETIME)

**USER_PROFILE** (Extensión del modelo User)
- id_profile (PK, INT, AUTO_INCREMENT)
- user (FK → USUARIO, UNIQUE, ONE_TO_ONE)
- phone (VARCHAR(20), NULL)
- address (TEXT, NULL)

**RESEÑA**
- id_reseña (PK, INT, AUTO_INCREMENT)
- id_producto (FK → PRODUCTO)
- id_usuario (FK → USUARIO)
- comentario (TEXT, NOT NULL)
- calificacion (INT, 1-5, NOT NULL)
- fecha (DATETIME, AUTO_NOW_ADD)

**Nota:** Las reseñas se publican automáticamente sin moderación. El administrador puede eliminarlas desde el panel si es necesario.

**CART_ITEM** (Carrito de Compras)
- id_cart_item (PK, INT, AUTO_INCREMENT)
- id_usuario (FK → USUARIO, NOT NULL)
- id_producto (FK → PRODUCTO, NOT NULL)
- cantidad (INT, NOT NULL, DEFAULT 1)
- created (DATETIME, AUTO_NOW_ADD)
- **Restricción UNIQUE:** (id_usuario, id_producto)

**PEDIDO**
- id_pedido (PK, INT, AUTO_INCREMENT)
- id_usuario (FK → USUARIO)
- fecha (DATETIME, AUTO_NOW_ADD)
- total (DECIMAL(10,2), NOT NULL)
- estado (VARCHAR(20), NOT NULL) [pending, confirmed, completed, cancelled]
- updated (DATETIME, AUTO_NOW)

**DETALLE_PEDIDO**
- id_detalle (PK, INT, AUTO_INCREMENT)
- id_pedido (FK → PEDIDO)
- product_name (VARCHAR(200), NOT NULL) [snapshot del nombre al momento de la orden]
- product_price (DECIMAL(10,2), NOT NULL) [snapshot del precio al momento de la orden]
- cantidad (INT, NOT NULL)

**Nota:** DETALLE_PEDIDO no tiene Foreign Key a PRODUCTO porque guarda un snapshot (instantánea) del producto al momento de crear la orden. Esto permite preservar el historial incluso si el producto se elimina o cambia de precio posteriormente.

**Relaciones:**
- USUARIO 1:1 USER_PROFILE
- USUARIO 1:N RESEÑA
- PRODUCTO 1:N RESEÑA
- USUARIO 1:N CART_ITEM
- PRODUCTO 1:N CART_ITEM
- USUARIO 1:N PEDIDO
- PEDIDO 1:N DETALLE_PEDIDO

**Nota sobre Servicios Terapéuticos:** Los servicios terapéuticos (masajes) están implementados como contenido estático en el template HTML. No requieren modelo de base de datos ya que la información es fija y no requiere gestión dinámica.

---

## 📋 ANEXO B - Diccionario de Datos (CORREGIDO)

### REEMPLAZAR: Anexo B completo

**Tabla: PRODUCTO**

| Campo | Tipo | Longitud | Null | Default | Descripción |
|-------|------|----------|------|---------|-------------|
| id_producto | INTEGER | - | NO | AUTO | Identificador único |
| nombre | VARCHAR | 200 | NO | - | Nombre del producto |
| beneficios | TEXT | - | NO | - | Beneficios del producto |
| descripcion | TEXT | - | NO | - | Descripción detallada |
| categorizacion | VARCHAR | 20 | NO | - | 'medicinal' o 'cosmético' |
| precio | DECIMAL | 10,2 | NO | - | Precio en CLP |
| img | VARCHAR | 500 | NO | - | URL imagen remota |
| stock | INTEGER | - | NO | - | Unidades disponibles (sin default) |
| destacado | BOOLEAN | - | NO | FALSE | Mostrar en Home |
| created | DATETIME | - | NO | NOW() | Fecha creación |
| updated | DATETIME | - | NO | NOW() | Fecha actualización |

**Tabla: USUARIO** (Modelo estándar Django)

| Campo | Tipo | Longitud | Null | Default | Descripción |
|-------|------|----------|------|---------|-------------|
| id_usuario | INTEGER | - | NO | AUTO | Identificador único |
| username | VARCHAR | 150 | NO | - | Nombre de usuario (único) |
| email | VARCHAR | 254 | SI | NULL | Email del usuario |
| password | VARCHAR | 128 | NO | - | Contraseña hasheada |
| first_name | VARCHAR | 150 | SI | NULL | Nombre |
| last_name | VARCHAR | 150 | SI | NULL | Apellido |
| is_active | BOOLEAN | - | NO | TRUE | Usuario activo |
| is_staff | BOOLEAN | - | NO | FALSE | Acceso admin Django |
| is_superuser | BOOLEAN | - | NO | FALSE | Permisos admin |
| date_joined | DATETIME | - | NO | NOW() | Fecha de registro |
| last_login | DATETIME | - | SI | NULL | Último acceso |

**Tabla: USER_PROFILE**

| Campo | Tipo | Longitud | Null | Default | Descripción |
|-------|------|----------|------|---------|-------------|
| id_profile | INTEGER | - | NO | AUTO | Identificador único |
| user_id | INTEGER | - | NO | - | FK a USUARIO (UNIQUE, ONE_TO_ONE) |
| phone | VARCHAR | 20 | SI | NULL | Teléfono de contacto |
| address | TEXT | - | SI | NULL | Dirección |

**Tabla: RESEÑA**

| Campo | Tipo | Longitud | Null | Default | Descripción |
|-------|------|----------|------|---------|-------------|
| id_resena | INTEGER | - | NO | AUTO | Identificador único |
| product_id | INTEGER | - | NO | - | FK a PRODUCTO |
| user_id | INTEGER | - | NO | - | FK a USUARIO |
| comentario | TEXT | - | NO | - | Texto de la reseña |
| calificacion | INTEGER | - | NO | - | Valor entre 1 y 5 |
| fecha | DATETIME | - | NO | NOW() | Fecha publicación |

**Nota:** Las reseñas se publican automáticamente sin moderación previa. El administrador puede eliminarlas desde el panel Django Admin si es necesario.

**Tabla: CART_ITEM**

| Campo | Tipo | Longitud | Null | Default | Descripción |
|-------|------|----------|------|---------|-------------|
| id_cart_item | INTEGER | - | NO | AUTO | Identificador único |
| user_id | INTEGER | - | NO | - | FK a USUARIO |
| product_id | INTEGER | - | NO | - | FK a PRODUCTO |
| cantidad | INTEGER | - | NO | 1 | Unidades en carrito |
| created | DATETIME | - | NO | NOW() | Fecha creación |

**Restricción:** UNIQUE (user_id, product_id) - Un usuario solo puede tener un registro por producto en el carrito.

**Tabla: PEDIDO**

| Campo | Tipo | Longitud | Null | Default | Descripción |
|-------|------|----------|------|---------|-------------|
| id_pedido | INTEGER | - | NO | AUTO | Identificador único |
| user_id | INTEGER | - | NO | - | FK a USUARIO |
| fecha | DATETIME | - | NO | NOW() | Fecha del pedido |
| total | DECIMAL | 10,2 | NO | - | Monto total CLP |
| estado | VARCHAR | 20 | NO | 'pending' | Estado: pending, confirmed, completed, cancelled |
| updated | DATETIME | - | NO | NOW() | Fecha última actualización |

**Tabla: DETALLE_PEDIDO**

| Campo | Tipo | Longitud | Null | Default | Descripción |
|-------|------|----------|------|---------|-------------|
| id_detalle | INTEGER | - | NO | AUTO | Identificador único |
| order_id | INTEGER | - | NO | - | FK a PEDIDO |
| product_name | VARCHAR | 200 | NO | - | Nombre del producto (snapshot) |
| product_price | DECIMAL | 10,2 | NO | - | Precio al momento de la orden (snapshot) |
| cantidad | INTEGER | - | NO | - | Unidades compradas |

**Nota Importante:** Esta tabla NO tiene Foreign Key a PRODUCTO. Guarda un snapshot (instantánea) del producto al momento de crear la orden. Esto permite:
- Preservar el historial aunque el producto se elimine
- Mantener el precio original aunque el producto cambie de precio
- Generar reportes históricos precisos

---

## 📋 SECCIÓN III.6.3.3 - Guía de Estilos (CORREGIDO)

### REEMPLAZAR: Sección III.6.3.3 completa

**Paleta de Colores:**

**Colores Primarios:**
- **Gradiente Principal:** #667eea (Violeta) a #764ba2 (Morado Oscuro)
  - Uso: Header, navbar, botones principales, fondos destacados
  - Implementación: `background: linear-gradient(135deg, #667eea 0%, #764ba2 100%)`

**Colores de Acento:**
- **Rojo/Coral:** #ff6b6b
  - Uso: Iconos destacados, badges de carrito, elementos de atención
- **Naranja:** #FF6F00 (opcional para CTAs)
  - Uso: Call-to-action secundarios, precios destacados

**Colores Neutros:**
- **Gris Oscuro:** #212121
  - Uso: Texto principal
- **Gris Medio:** #757575
  - Uso: Texto secundario, placeholders
- **Gris Claro:** #F5F5F5
  - Uso: Fondos, separadores
- **Blanco:** #FFFFFF
  - Uso: Fondo de cards, contenedores

**Colores de Estado:**
- **Éxito:** #4CAF50 (Verde)
- **Error:** #F44336 (Rojo)
- **Advertencia:** #FF9800 (Naranja)
- **Información:** #2196F3 (Azul)

**Tipografía:**

**Fuente Principal: Poppins**
- `font-family: 'Poppins', sans-serif;`
- Pesos disponibles: 300 (Light), 400 (Regular), 500 (Medium), 600 (SemiBold), 700 (Bold)
- Uso: Todo el sitio (títulos, cuerpo, navegación, formularios)
- Importación: Google Fonts CDN

**Jerarquía Tipográfica:**
- **H1:** 48px / Poppins Bold / Line-height 1.2
- **H2:** 36px / Poppins SemiBold / Line-height 1.3
- **H3:** 28px / Poppins Medium / Line-height 1.4
- **H4:** 22px / Poppins Medium / Line-height 1.4
- **Body:** 16px / Poppins Regular / Line-height 1.6
- **Small:** 14px / Poppins Regular / Line-height 1.5
- **Caption:** 12px / Poppins Light / Line-height 1.4

**Componentes UI:**

**Botones:**
```css
/* Botón Primario */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
color: #FFFFFF;
padding: 10px 25px;
border-radius: 25px;
border: none;
font-weight: 500;
transition: all 0.3s;
box-shadow: 0 2px 10px rgba(0,0,0,0.1);

/* Hover */
transform: translateY(-2px);
box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
```

**Cards de Producto:**
```css
background: #FFFFFF;
border: none;
border-radius: 15px;
overflow: hidden;
box-shadow: 0 2px 10px rgba(0,0,0,0.1);
transition: transform 0.3s, box-shadow 0.3s;

/* Hover */
transform: translateY(-5px);
box-shadow: 0 5px 20px rgba(0,0,0,0.2);
```

**Inputs:**
```css
border: 2px solid #E0E0E0;
border-radius: 8px;
padding: 10px;
font-size: 16px;
font-family: 'Poppins', sans-serif;

/* Focus */
border-color: #667eea;
outline: none;
box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
```

**Iconografía:**
- Biblioteca: Font Awesome 6.4.0 (CDN)
- Iconos principales: shopping-cart, user, search, instagram, whatsapp, star, leaf
- Tamaños: 16px (pequeño), 24px (medio), 32px (grande), 48px (extra grande)

**Responsividad:**
- Móvil: < 768px (1 columna)
- Tablet: 768px - 1024px (2 columnas)
- Desktop: > 1024px (3-4 columnas)

---

## 📋 RF-006: Sistema de Reseñas (CORREGIDO)

### REEMPLAZAR: RF-006 en Sección III.1

**RF-006: Sistema de Reseñas**
- Usuarios registrados pueden escribir reseñas en productos
- Reseñas deben mostrar nombre de usuario, fecha, calificación (1-5 estrellas) y comentario
- Las reseñas se publican automáticamente sin moderación previa
- El administrador puede visualizar y eliminar reseñas desde el panel Django Admin
- Cada usuario puede escribir una reseña por producto

---

## 📋 RF-011: Panel Administrativo (CORREGIDO)

### REEMPLAZAR: RF-011 en Sección III.1

**RF-011: Panel Administrativo**
- Interfaz Django Admin estándar para gestión de productos, usuarios y pedidos
- CRUD completo de productos (crear, leer, actualizar, eliminar)
- Gestión de productos destacados para Home mediante campo booleano
- Visualización de pedidos con estado y detalles
- Gestión de usuarios registrados
- Visualización y eliminación de reseñas
- Acceso restringido mediante autenticación de superusuario

**Nota:** No incluye dashboard personalizado con estadísticas. Se utiliza el panel administrativo estándar de Django con personalizaciones mínimas en la visualización de modelos.

---

## 📋 ANEXO C - Guía de Estilos Completa (CORREGIDO)

### REEMPLAZAR: Anexo C completo

**PALETA DE COLORES**

**Colores Primarios:**
- **Gradiente Principal:** #667eea (Violeta) → #764ba2 (Morado Oscuro)
  - RGB: (102, 126, 234) → (118, 75, 162)
  - Uso: Headers, navbar, botones principales, fondos destacados
  - Implementación CSS: `background: linear-gradient(135deg, #667eea 0%, #764ba2 100%)`

**Colores de Acento:**
- **Rojo/Coral:** #ff6b6b (RGB: 255, 107, 107)
  - Uso: Iconos destacados, badges de carrito, elementos de atención
- **Naranja:** #FF6F00 (RGB: 255, 111, 0)
  - Uso: Call-to-action secundarios, precios destacados

**Colores Neutros:**
- **Gris Oscuro:** #212121 (RGB: 33, 33, 33)
  - Uso: Texto principal
- **Gris Medio:** #757575 (RGB: 117, 117, 117)
  - Uso: Texto secundario, placeholders
- **Gris Claro:** #F5F5F5 (RGB: 245, 245, 245)
  - Uso: Fondos, separadores
- **Blanco:** #FFFFFF (RGB: 255, 255, 255)
  - Uso: Fondo de cards, contenedores

**Colores de Estado:**
- **Éxito:** #4CAF50 (Verde)
- **Error:** #F44336 (Rojo)
- **Advertencia:** #FF9800 (Naranja)
- **Información:** #2196F3 (Azul)

**TIPOGRAFÍA**

**Fuente Principal: Poppins**
```css
font-family: 'Poppins', sans-serif;
```
- Pesos disponibles: 300 (Light), 400 (Regular), 500 (Medium), 600 (SemiBold), 700 (Bold)
- Uso: Todo el sitio (títulos, cuerpo, navegación, formularios)
- Importación: Google Fonts CDN
- URL: `https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap`

**Jerarquía Tipográfica:**
- **H1:** 48px / Poppins Bold / Line-height 1.2
- **H2:** 36px / Poppins SemiBold / Line-height 1.3
- **H3:** 28px / Poppins Medium / Line-height 1.4
- **H4:** 22px / Poppins Medium / Line-height 1.4
- **Body:** 16px / Poppins Regular / Line-height 1.6
- **Small:** 14px / Poppins Regular / Line-height 1.5
- **Caption:** 12px / Poppins Light / Line-height 1.4

**COMPONENTES UI**

**Botones:**
```css
/* Botón Primario */
.btn-primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: #FFFFFF;
    padding: 10px 25px;
    border-radius: 25px;
    border: none;
    font-weight: 500;
    font-family: 'Poppins', sans-serif;
    transition: all 0.3s;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}
```

**Cards de Producto:**
```css
.product-card {
    background: #FFFFFF;
    border: none;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    transition: transform 0.3s, box-shadow 0.3s;
}

.product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 5px 20px rgba(0,0,0,0.2);
}
```

**Inputs:**
```css
.form-control {
    border: 2px solid #E0E0E0;
    border-radius: 8px;
    padding: 10px;
    font-size: 16px;
    font-family: 'Poppins', sans-serif;
}

.form-control:focus {
    border-color: #667eea;
    outline: none;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}
```

**ICONOGRAFÍA**
- Biblioteca: Font Awesome 6.4.0 (CDN)
- Iconos principales: shopping-cart, user, search, instagram, whatsapp, star, leaf, snowflake, sun, seedling
- Tamaños: 16px (pequeño), 24px (medio), 32px (grande), 48px (extra grande)
- Color por defecto: Hereda del contexto (generalmente #FFFFFF en navbar)

**ESPACIADO**
Sistema de espaciado base: 8px (Bootstrap estándar)
- xs: 4px
- sm: 8px
- md: 16px
- lg: 24px
- xl: 32px
- 2xl: 48px

**RESPONSIVE BREAKPOINTS**
```css
/* Mobile First */
@media (min-width: 576px) { /* Small devices */ }
@media (min-width: 768px) { /* Tablets */ }
@media (min-width: 992px) { /* Desktops */ }
@media (min-width: 1200px) { /* Large desktops */ }
```

**ANIMACIONES**
Transiciones estándar: `transition: all 0.3s ease;`

Efectos Hover:
- Cards: elevación suave (translateY)
- Botones: cambio de color + sombra
- Links: cambio de color
- Imágenes: zoom sutil (scale 1.05)

---

## 📋 ANEXO G - Manual Técnico - Estructura (CORREGIDO)

### REEMPLAZAR: Sección 3 del Anexo G

**3. Estructura del Proyecto**

```
auka_terapias/
├── manage.py
├── requirements.txt
├── .env (variables de entorno)
├── .gitignore
├── auka_terapias/          # Configuración del proyecto
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── products/                # App de productos
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py           # Product, Review
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── accounts/                # App de usuarios
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py           # UserProfile
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── migrations/
├── cart/                    # App del carrito
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py           # CartItem, Order, OrderItem
│   ├── views.py
│   ├── urls.py
│   ├── context_processors.py
│   └── migrations/
├── templates/              # Templates HTML
│   ├── base.html
│   ├── products/
│   │   ├── home.html
│   │   ├── catalogo.html
│   │   ├── product_detail.html
│   │   ├── quienes_somos.html
│   │   └── servicios_terapeuticos.html
│   ├── accounts/
│   │   ├── login.html
│   │   ├── register.html
│   │   └── profile.html
│   └── cart/
│       └── cart.html
├── static/                  # Archivos estáticos
│   └── .gitkeep
├── media/                   # Archivos subidos por usuarios
│   └── .gitkeep
└── db.sqlite3              # Base de datos SQLite
```

**Nota:** Los nombres de las apps son en inglés: `products`, `accounts`, `cart` (no en español).

---

## 📋 RF-005: Carrito de Compras (ACLARACIÓN)

### ACTUALIZAR: RF-005 en Sección III.1

**RF-005: Carrito de Compras**
- Usuarios **registrados y autenticados** pueden agregar productos al carrito
- El carrito persiste en base de datos (no es sesión temporal)
- El sistema debe permitir agregar/eliminar productos del carrito
- El sistema debe permitir actualizar cantidades de productos en el carrito
- Debe mostrar resumen con productos y total
- Debe generar mensaje de WhatsApp con formato: "Hola, quiero concretar la compra de estos productos: [lista de productos]"
- Debe redirigir a WhatsApp del administrador con mensaje pre-cargado
- Al enviar pedido por WhatsApp, se crea un registro de Order en la base de datos

**Restricción:** El carrito requiere autenticación. No hay funcionalidad de carrito para usuarios anónimos.

---

## 📋 URLS CORRECTAS (VERIFICACIÓN)

### ACTUALIZAR: Cualquier mención a URLs en el informe

**URLs Públicas:**
- `/` - Home
- `/catalogo/` - Catálogo de productos
- `/producto/<id>/` - Detalle de producto
- `/quienes-somos/` - Quiénes Somos
- `/servicios-terapeuticos/` - Servicios Terapéuticos

**URLs de Autenticación:**
- `/accounts/register/` - Registro de usuario
- `/accounts/login/` - Inicio de sesión
- `/accounts/logout/` - Cerrar sesión
- `/accounts/profile/` - Perfil de usuario

**URLs del Carrito:**
- `/cart/` - Ver carrito
- `/cart/add/<product_id>/` - Agregar al carrito
- `/cart/remove/<item_id>/` - Eliminar del carrito
- `/cart/update/<item_id>/` - Actualizar cantidad
- `/cart/send-whatsapp/` - Enviar pedido por WhatsApp

**URLs de Administración:**
- `/admin/` - Panel Django Admin

---

## 📝 CHECKLIST DE REEMPLAZOS

Marca cada sección cuando la reemplaces:

- [ ] Sección III.6.1.1 - Modelo Lógico
- [ ] Anexo B - Diccionario de Datos Completo
- [ ] Sección III.6.3.3 - Guía de Estilos
- [ ] RF-006 - Sistema de Reseñas
- [ ] RF-011 - Panel Administrativo
- [ ] RF-005 - Carrito de Compras (aclaración)
- [ ] Anexo C - Guía de Estilos Completa
- [ ] Anexo G - Sección 3 (Estructura del Proyecto)
- [ ] Verificar todas las URLs mencionadas
- [ ] Eliminar menciones a SERVICIO_TERAPEUTICO como modelo
- [ ] Eliminar menciones a campo `aprobada` en RESEÑA
- [ ] Actualizar todos los colores mencionados
- [ ] Actualizar tipografía a Poppins

---

## 🎯 NOTAS FINALES

1. **Servicios Terapéuticos:** No es un modelo, es contenido estático. Si necesitas mencionarlo, di "contenido estático en template HTML" o "no requiere modelo de base de datos".

2. **Colores:** El diseño usa gradientes morados, no verdes. Esto es importante para la coherencia visual.

3. **Carrito:** Siempre menciona que requiere autenticación. Es un punto importante de seguridad y funcionalidad.

4. **OrderItem:** Explica claramente por qué no tiene FK a Product (snapshot para preservar historial).

5. **Reseñas:** Aclara que se publican automáticamente. Si quieres mencionar moderación, di "el admin puede eliminar reseñas inapropiadas".

---

**¡Listo!** Con estas correcciones, tu informe estará 100% alineado con el código implementado. 🎉

