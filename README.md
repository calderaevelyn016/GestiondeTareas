# Gestion De Tareas

## Descripción de la aplicación

Gestor de Tareas es una aplicación web desarrollada con Flask como backend y Bootstrap 5 como frontend.  
Permite administrar tareas de forma simple e intuitiva, incluyendo la creación, visualización, actualización de estado y eliminación de tareas, todo con una interfaz moderna y responsive.

La aplicación no utiliza una base de datos real, ya que las tareas se manejan en memoria, lo cual la hace ideal para fines educativos y demostrativos.

---

## Características y funcionalidades

- Crear nuevas tareas con título obligatorio y descripción opcional  
- Muestra una lista de todas las tareas en tarjetas 
- Marca las tareas como completadas o pendientes  
- Elimina tareas confirmadas  
- Visualización clara del estado de cada tarea
- Panel de estadísticas con total de tareas, tareas completadas y tareas pendientes  
- Mensajes (éxito, error y advertencia) usando alertas  
- Diseño responsive compatible con dispositivos móviles y desktop  

---

## Tecnologías utilizadas

- Python 3.x  
- Flask  
- Bootstrap 5 (vía CDN)  
- Bootstrap Icons (vía CDN)  
- HTML5  
- JavaScript  

---

## Instrucciones de instalación

Para ejecutar el proyecto localmente, primero se debe clonar el repositorio desde GitHub y acceder a la carpeta del proyecto.   
Luego se debe crear un entorno virtual de Python y activarlo según el sistema operativo: "python -m venv venv" y "venv\Scripts\activate" en windows.  
Una vez activado el entorno virtual, se instalan las dependencias necesarias utilizando el archivo requirements.txt.  
Finalmente, se ejecuta el archivo principal de la aplicación y se accede desde el navegador web utilizando la dirección local del servidor: python app.py.

---

## Estructura del proyecto

El proyecto está organizado de la siguiente manera:

- app.py: archivo principal de la aplicación Flask donde se definen las rutas y la lógica del sistema  
- requirements.txt: archivo que contiene las dependencias necesarias para ejecutar el proyecto  
- README.md: documentación del proyecto  

Carpetas principales:

- templates: Plantillas HTML de la aplicación  
  - base.html: layout principal con la barra de navegación
  - index.html: vista principal donde se muestran las tareas  
- static: carpeta para archivos estáticos ( vacía por restricción)  
- screenshots: carpeta de las capturas de pantalla de la aplicación funcionando  

---

## Capturas de pantalla

![Vista principal](<img width="1361" height="497" alt="image" src="https://github.com/user-attachments/assets/ca7b8eda-0a8b-4529-97b7-df0936e0d44f" />
)
)
![Agregar tarea](<img width="1050" height="283" alt="image" src="https://github.com/user-attachments/assets/b6571a48-ba31-43b9-925d-2311edad3b78" />
)
)
![Vista Responsive](<img width="985" height="699" alt="image" src="https://github.com/user-attachments/assets/80a4e74b-6c01-475d-8b3c-2a7ad108786d" />
)
)


## Instrucciones de uso

Al ingresar a la aplicación, el usuario puede visualizar la lista de tareas existentes.  
Para agregar una nueva tarea, se completa el formulario con el título obligatorio y una descripción opcional.  
Cada tarea se muestra en una tarjeta donde se puede ver su estado, fecha de creación y acciones disponibles.  
El usuario puede marcar las tareas como completadas o pendientes y también eliminarlas con confirmación previa.  
El panel de estadísticas se actualiza automáticamente según las acciones realizadas.

---

## Posibles mejoras futuras

- Agregar una base de datos  
- Inicio de Sesion  
- Editar tareas existentes  
- Filtros de tareas  
- Búsqueda de tareas  

---

