# 🚂 Guía de Despliegue en Railway

Railway es una plataforma moderna diseñada específicamente para aplicaciones como Django. Es mucho más simple que Vercel para proyectos Django.

---

## ✅ Ventajas de Railway sobre Vercel

- ✅ **PostgreSQL incluido gratis** (no necesitas Supabase)
- ✅ **Diseñado para Django** (no necesitas adaptadores complicados)
- ✅ **Despliegue automático** desde GitHub
- ✅ **Logs en tiempo real** fáciles de ver
- ✅ **Variables de entorno** simples de configurar
- ✅ **$5 de crédito gratis** cada mes

---

## 📋 Pasos para Desplegar

### 1. Crear Cuenta en Railway

1. Ve a [railway.app](https://railway.app)
2. Haz clic en **"Start a New Project"**
3. Inicia sesión con GitHub

### 2. Crear Nuevo Proyecto

1. Haz clic en **"New Project"**
2. Selecciona **"Deploy from GitHub repo"**
3. Busca y selecciona tu repositorio: `Jsaez-a113/proyecto-integrado`
4. Haz clic en **"Deploy Now"**

### 3. Agregar Base de Datos PostgreSQL

1. En tu proyecto, haz clic en **"+ New"**
2. Selecciona **"Database"** → **"Add PostgreSQL"**
3. Railway creará automáticamente la base de datos
4. La variable `DATABASE_URL` se configurará automáticamente

### 4. Configurar Variables de Entorno

En tu proyecto de Railway, ve a la pestaña **"Variables"** y agrega:

| Variable | Valor |
|----------|-------|
| `SECRET_KEY` | `fc5^^5^z&ah4czf00m3+q1!s(i3cb_4lvpeal=6*@t1y=s%fyd` |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `.railway.app` |
| `WHATSAPP_NUMBER` | `+56985661992` |

> [!NOTE]
> **NO necesitas configurar** `DATABASE_URL` - Railway lo hace automáticamente cuando agregas PostgreSQL.

### 5. Desplegar

1. Railway detectará automáticamente que es un proyecto Django
2. Usará el `Procfile` para saber cómo iniciar la aplicación
3. El despliegue tomará 2-3 minutos
4. ¡Listo! Tu sitio estará en línea

---

## 🔧 Archivos de Configuración Creados

### `Procfile`
```
web: gunicorn auka_terapias.wsgi --log-file -
```
Le dice a Railway cómo iniciar tu aplicación Django.

### `runtime.txt`
```
python-3.12
```
Especifica la versión de Python a usar.

### `railway.toml`
```toml
[deploy]
startCommand = "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn auka_terapias.wsgi"
```
Ejecuta migraciones y collectstatic automáticamente antes de iniciar.

---

## 📊 Después del Despliegue

### Crear Superusuario

Una vez desplegado, necesitas crear un superusuario:

1. Ve a tu proyecto en Railway
2. Haz clic en la pestaña **"Deployments"**
3. Selecciona el deployment activo
4. Haz clic en **"View Logs"**
5. En la parte superior, haz clic en el ícono de terminal
6. Ejecuta:
   ```bash
   python manage.py createsuperuser
   ```

### Acceder a tu Sitio

1. En Railway, ve a **"Settings"** → **"Domains"**
2. Railway te dará una URL como: `https://tu-proyecto.up.railway.app`
3. Visita esa URL para ver tu sitio
4. Accede al admin: `https://tu-proyecto.up.railway.app/admin`

---

## 🎯 Migración de Datos desde Supabase

Si quieres migrar los datos que ya tienes en Supabase a Railway:

### Opción 1: Exportar e Importar (Recomendado)

```bash
# 1. Exportar desde Supabase (local)
python manage.py dumpdata --natural-foreign --natural-primary > data.json

# 2. Cambiar DATABASE_URL a Railway
# 3. Importar a Railway
python manage.py loaddata data.json
```

### Opción 2: Usar Railway CLI

```bash
# Instalar Railway CLI
npm i -g @railway/cli

# Iniciar sesión
railway login

# Vincular proyecto
railway link

# Ejecutar comandos
railway run python manage.py migrate
railway run python manage.py createsuperuser
```

---

## ⚠️ Archivos Media

Al igual que con Vercel, Railway tiene almacenamiento efímero. Para archivos media persistentes, usa:

- **Cloudinary** (recomendado - gratis)
- **AWS S3**
- **Railway Volumes** (almacenamiento persistente de Railway)

---

## 💰 Costos

- **Plan Hobby**: $5 de crédito gratis cada mes
- **Uso típico de Django**: ~$3-4/mes
- **PostgreSQL**: Incluido en el plan
- **Suficiente para proyectos pequeños/medianos**

---

## 🆚 Railway vs Vercel

| Característica | Railway | Vercel |
|----------------|---------|--------|
| Django Support | ✅ Nativo | ⚠️ Complicado |
| PostgreSQL | ✅ Incluido | ❌ Externo |
| Configuración | ✅ Simple | ❌ Compleja |
| Logs | ✅ Fáciles | ⚠️ Limitados |
| Precio | $5/mes crédito | Gratis limitado |

---

## 🚀 Próximos Pasos

1. Sube los cambios a GitHub (ya están listos)
2. Ve a Railway y crea tu proyecto
3. Conecta tu repositorio
4. Agrega PostgreSQL
5. Configura variables de entorno
6. ¡Despliega!

---

¿Listo para desplegar? Los archivos ya están configurados y listos para subir a GitHub.
