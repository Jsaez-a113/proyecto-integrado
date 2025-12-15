# Guía de Despliegue en Vercel - Auka Terapias

Esta guía te ayudará a desplegar tu proyecto Django en Vercel usando Supabase como base de datos PostgreSQL.

## Requisitos Previos

1. **Cuenta en Vercel**: Crea una cuenta gratuita en [vercel.com](https://vercel.com)
2. **Cuenta en Supabase**: Crea una cuenta gratuita en [supabase.com](https://supabase.com)
3. **Git**: Tu proyecto debe estar en un repositorio Git (GitHub, GitLab, o Bitbucket)

---

## Paso 1: Configurar Supabase

### 1.1 Crear Proyecto en Supabase

1. Inicia sesión en [Supabase](https://supabase.com)
2. Haz clic en "New Project"
3. Completa los datos:
   - **Name**: auka-terapias (o el nombre que prefieras)
   - **Database Password**: Crea una contraseña segura (¡guárdala!)
   - **Region**: Selecciona la región más cercana (South America - São Paulo)
4. Haz clic en "Create new project"
5. Espera unos minutos mientras se crea el proyecto

### 1.2 Obtener la URL de Conexión

1. En tu proyecto de Supabase, ve a **Settings** → **Database**
2. En la sección "Connection string", selecciona **URI**
3. Copia la cadena de conexión que se ve así:
   ```
   postgresql://postgres:[YOUR-PASSWORD]@db.xxxxxxxxxxxxx.supabase.co:5432/postgres
   ```
4. Reemplaza `[YOUR-PASSWORD]` con la contraseña que creaste
5. **Guarda esta URL**, la necesitarás para Vercel

> [!IMPORTANT]
> La URL de conexión contiene tu contraseña. Nunca la compartas públicamente ni la subas a Git.

---

## Paso 2: Preparar tu Repositorio Git

### 2.1 Inicializar Git (si no lo has hecho)

```bash
git init
git add .
git commit -m "Preparar proyecto para Vercel"
```

### 2.2 Subir a GitHub

1. Crea un nuevo repositorio en [GitHub](https://github.com/new)
2. **NO** marques "Initialize with README"
3. Copia los comandos que GitHub te muestra y ejecútalos:

```bash
git remote add origin https://github.com/tu-usuario/tu-repositorio.git
git branch -M main
git push -u origin main
```

### 2.3 Actualizar .gitignore

Asegúrate de que tu `.gitignore` incluya:

```
*.pyc
__pycache__/
db.sqlite3
.env
staticfiles/
media/
*.log
```

---

## Paso 3: Desplegar en Vercel

### 3.1 Importar Proyecto

1. Inicia sesión en [Vercel](https://vercel.com)
2. Haz clic en "Add New..." → "Project"
3. Selecciona tu repositorio de GitHub
4. Haz clic en "Import"

### 3.2 Configurar Variables de Entorno

En la sección "Environment Variables", agrega las siguientes variables:

| Name | Value | Ejemplo |
|------|-------|---------|
| `SECRET_KEY` | Una clave secreta segura | `django-insecure-abc123...` |
| `DEBUG` | `False` | `False` |
| `ALLOWED_HOSTS` | Tu dominio de Vercel | `.vercel.app` |
| `DATABASE_URL` | URL de Supabase | `postgresql://postgres:...` |
| `WHATSAPP_NUMBER` | Tu número de WhatsApp | `+56985661992` |

> [!TIP]
> Para generar una SECRET_KEY segura, puedes usar:
> ```python
> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```

### 3.3 Configurar Build Settings

Vercel debería detectar automáticamente la configuración desde `vercel.json`. Verifica que:

- **Framework Preset**: Other
- **Build Command**: `bash build.sh`
- **Output Directory**: `staticfiles`

### 3.4 Desplegar

1. Haz clic en "Deploy"
2. Espera a que termine el proceso (puede tomar 2-5 minutos)
3. Una vez completado, verás un mensaje de éxito con la URL de tu sitio

---

## Paso 4: Migrar la Base de Datos

Después del primer despliegue, necesitas ejecutar las migraciones:

### 4.1 Usando Vercel CLI (Recomendado)

1. Instala Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Inicia sesión:
   ```bash
   vercel login
   ```

3. Vincula tu proyecto:
   ```bash
   vercel link
   ```

4. Ejecuta las migraciones:
   ```bash
   vercel env pull .env.production
   python manage.py migrate
   ```

### 4.2 Usando Supabase SQL Editor (Alternativa)

Si prefieres, puedes ejecutar las migraciones localmente apuntando a Supabase:

1. Crea un archivo `.env` local con:
   ```
   DATABASE_URL=postgresql://postgres:[PASSWORD]@db.xxxxx.supabase.co:5432/postgres
   ```

2. Ejecuta las migraciones:
   ```bash
   python manage.py migrate
   ```

3. Crea un superusuario:
   ```bash
   python manage.py createsuperuser
   ```

---

## Paso 5: Configurar Archivos Media (Opcional)

> [!WARNING]
> Vercel tiene un sistema de archivos de solo lectura. Los archivos subidos por usuarios (imágenes de productos) no persistirán entre despliegues.

### Opciones para Archivos Media:

#### Opción A: Cloudinary (Recomendado - Gratis)

1. Crea cuenta en [Cloudinary](https://cloudinary.com)
2. Instala el paquete:
   ```bash
   pip install cloudinary django-cloudinary-storage
   ```
3. Agrega a `requirements.txt`:
   ```
   cloudinary>=1.36.0
   django-cloudinary-storage>=0.3.0
   ```
4. Configura en `settings.py`:
   ```python
   INSTALLED_APPS = [
       # ...
       'cloudinary_storage',
       'cloudinary',
       # ...
   ]
   
   CLOUDINARY_STORAGE = {
       'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME'),
       'API_KEY': config('CLOUDINARY_API_KEY'),
       'API_SECRET': config('CLOUDINARY_API_SECRET')
   }
   
   DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
   ```

#### Opción B: Vercel Blob

1. Instala el paquete:
   ```bash
   pip install vercel-blob
   ```
2. Sigue la [documentación de Vercel Blob](https://vercel.com/docs/storage/vercel-blob)

---

## Paso 6: Verificar el Despliegue

1. Visita la URL de tu proyecto en Vercel
2. Verifica que el sitio carga correctamente
3. Prueba el acceso al admin: `https://tu-proyecto.vercel.app/admin`
4. Verifica que los archivos estáticos se cargan correctamente

---

## Comandos Útiles

### Ver logs en tiempo real
```bash
vercel logs
```

### Redesplegar
```bash
vercel --prod
```

### Ver variables de entorno
```bash
vercel env ls
```

### Agregar variable de entorno
```bash
vercel env add SECRET_KEY
```

---

## Solución de Problemas

### Error: "Application Error"

1. Revisa los logs en Vercel Dashboard → Deployments → [tu deployment] → Logs
2. Verifica que todas las variables de entorno estén configuradas
3. Asegúrate de que `DATABASE_URL` sea correcta

### Error: "Static files not loading"

1. Verifica que `whitenoise` esté en `requirements.txt`
2. Ejecuta `python manage.py collectstatic` localmente para verificar
3. Revisa que `STATIC_ROOT` esté configurado correctamente

### Error: "Database connection failed"

1. Verifica que la URL de Supabase sea correcta
2. Asegúrate de haber reemplazado `[YOUR-PASSWORD]` con tu contraseña real
3. Verifica que el proyecto de Supabase esté activo

### Error: "Module not found"

1. Asegúrate de que todas las dependencias estén en `requirements.txt`
2. Verifica que las versiones sean compatibles
3. Intenta redesplegar

---

## Actualizaciones Futuras

Cada vez que hagas cambios en tu código:

1. Haz commit de los cambios:
   ```bash
   git add .
   git commit -m "Descripción de los cambios"
   ```

2. Sube a GitHub:
   ```bash
   git push
   ```

3. Vercel desplegará automáticamente los cambios

---

## Dominio Personalizado (Opcional)

1. En Vercel Dashboard, ve a tu proyecto
2. Ve a Settings → Domains
3. Agrega tu dominio personalizado
4. Sigue las instrucciones para configurar el DNS
5. Actualiza `ALLOWED_HOSTS` en las variables de entorno para incluir tu dominio

---

## Notas Importantes

> [!CAUTION]
> - Nunca subas archivos `.env` a Git
> - Mantén tu `SECRET_KEY` segura
> - Usa contraseñas fuertes para Supabase
> - Haz backups regulares de tu base de datos

> [!TIP]
> - El plan gratuito de Vercel permite 100GB de ancho de banda
> - Supabase gratuito incluye 500MB de base de datos
> - Cloudinary gratuito ofrece 25GB de almacenamiento

---

## Recursos Adicionales

- [Documentación de Vercel](https://vercel.com/docs)
- [Documentación de Supabase](https://supabase.com/docs)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)

---

¡Felicidades! Tu proyecto Django ahora está desplegado en Vercel 🎉
