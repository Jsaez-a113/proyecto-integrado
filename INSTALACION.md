# 📋 Guía Paso a Paso de Instalación

Esta guía te llevará paso a paso desde cero hasta tener el proyecto funcionando.

## Prerrequisitos

Asegúrate de tener Python 3.10 o superior instalado. Puedes verificar con:

```bash
python --version
```

O en algunos sistemas:

```bash
python3 --version
```

## Paso 1: Navegar al Directorio del Proyecto

```bash
cd "C:\Users\Jostin\Downloads\proyecto integrado"
```

## Paso 2: Crear Entorno Virtual (Recomendado)

Crear un entorno virtual aísla las dependencias del proyecto:

```bash
# Windows
python -m venv venv

# Activar el entorno virtual (Windows)
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

Cuando el entorno virtual esté activado, verás `(venv)` al inicio de tu línea de comandos.

## Paso 3: Instalar Dependencias

Con el entorno virtual activado, instala las dependencias:

```bash
pip install -r requirements.txt
```

Esto instalará:
- Django 5.x
- Pillow (para manejo de imágenes)

## Paso 4: Aplicar Migraciones

Las migraciones crean las tablas en la base de datos:

```bash
python manage.py makemigrations
python manage.py migrate
```

Esto creará:
- Tabla de usuarios
- Tabla de productos
- Tabla de reseñas
- Tabla de carrito
- Tabla de órdenes
- Y todas las tablas necesarias

## Paso 5: Crear Superusuario (Administrador)

Crea un usuario administrador para acceder al panel de administración:

```bash
python manage.py createsuperuser
```

Te pedirá:
- Username: (elige un nombre de usuario)
- Email address: (opcional, pero recomendado)
- Password: (ingresa una contraseña segura)
- Password (again): (confirma la contraseña)

**Ejemplo:**
```
Username: admin
Email address: admin@auka.com
Password: ********
Password (again): ********
```

## Paso 6: Ejecutar el Servidor

Inicia el servidor de desarrollo:

```bash
python manage.py runserver
```

Verás un mensaje como:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

## Paso 7: Acceder al Sitio

Abre tu navegador y visita:

- **Sitio principal:** http://127.0.0.1:8000/
- **Panel de administración:** http://127.0.0.1:8000/admin/

## Paso 8: Agregar Productos (Opcional)

1. Ve a http://127.0.0.1:8000/admin/
2. Inicia sesión con el superusuario que creaste
3. En la sección "Products", haz clic en "Products"
4. Haz clic en "Add Product" (arriba a la derecha)
5. Llena el formulario:
   - **Nombre:** Ej: "Aceite de Lavanda"
   - **Beneficios:** Ej: "Relajante, ayuda a dormir mejor"
   - **Description:** Descripción completa del producto
   - **Categorizacion:** Selecciona "Medicinal" o "Cosmético"
   - **Precio:** Ej: 15000
   - **Img:** URL de una imagen (ej: "https://images.unsplash.com/photo-...")
   - **Stock:** Ej: 50
   - **Destacado:** Marca si quieres que aparezca en productos destacados
6. Haz clic en "Save"

## Paso 9: Crear Cuenta de Usuario

1. Ve a http://127.0.0.1:8000/
2. Haz clic en "Registrarse" en el menú
3. Completa el formulario
4. Inicia sesión con tu nueva cuenta

## ✅ Verificación

Para verificar que todo funciona:

1. ✅ El sitio carga en http://127.0.0.1:8000/
2. ✅ Puedes ver el catálogo
3. ✅ Puedes registrarte e iniciar sesión
4. ✅ Puedes añadir productos al carrito
5. ✅ El panel de administración funciona

## 🛑 Detener el Servidor

Para detener el servidor, presiona `CTRL + C` en la terminal.

## 🔄 Para Ejecutar Nuevamente

Cada vez que quieras trabajar en el proyecto:

1. Activa el entorno virtual:
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

2. Ejecuta el servidor:
   ```bash
   python manage.py runserver
   ```

## 📝 Notas Importantes

- **No cierres la terminal** mientras el servidor esté corriendo
- El servidor se recarga automáticamente cuando haces cambios en el código
- La base de datos SQLite se crea automáticamente en `db.sqlite3`
- Los productos necesitan URLs de imágenes remotas (no archivos locales)

## 🐛 Problemas Comunes

### Error: "python no se reconoce como comando"
- Usa `python3` en lugar de `python`
- O asegúrate de que Python esté en tu PATH

### Error: "No module named 'django'"
```bash
pip install -r requirements.txt
```

### Error: "TemplateDoesNotExist"
- Verifica que la carpeta `templates/` exista en la raíz del proyecto
- Verifica que `TEMPLATES` en `settings.py` tenga `'DIRS': [BASE_DIR / 'templates']`

### Error: "Port already in use"
El puerto 8000 está ocupado. Usa otro puerto:
```bash
python manage.py runserver 8001
```

## 📞 Siguiente Paso

Una vez que tengas el sitio funcionando, consulta el `README.md` para más información sobre cómo usar el sitio.

---

¡Listo! Tu sitio web de Auka Terapias está funcionando. 🎉

