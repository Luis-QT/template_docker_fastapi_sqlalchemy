# Template Docker - FastAPI - SQLAlchemy

Este proyecto sirve como guía de inicio rápido para la construcción de sistemas que apliquen las tecnologías Docker, FastAPI, SQLAlchemy.

Para iniciar el proyecto solo básta con clonarlo, crear el archivo .env igual que en el ejemplo y ejecutar:

```
docker-compose up -d
```
Entrar a la documentación de APIs en http://localhost:8080/docs

La aplicación cuenta con:

- API Login - Generación de token JWT (admin, 123456)
- Ejemplo de API CRUD usuarios
- Ejemplo de tabla users
- Ejemplo de seeders (datos de prueba)
- Ejemplo de diccionario de traducciones
- API Master para refrescar la base de datos

Puede revisar secciones específicas en la documentación:

- [1. Construir la aplicación](/docs/1.%20Construir%20la%20aplicaci%C3%B3n.md)
- [2. Organización de carpetas y archivos](/docs/2.%20Organizaci%C3%B3n%20de%20carpetas.md)
