# Project 1

Este proyecto 1 consiste en un sitio web enfocado a la promoción y venta de libros online utilizando la API de 
Google Books. Esta página WEB consiste en:

1. HOME
Consiste en una interfaz de inicio y ambiente con portada de imagen del sitio WEB. Contiene también características heredadas del archivo layout_flask como nombre del sitio, eslógan, banner y barra de navegación.

2. Register
Para poder tener acceso a los servicios del sitio es necesario inscribirse como cliente (usuario del sitio). Para ello se pide nombre, apellido, email, contraseña y verificación de la contraseña.

3. Sing In
También conocido como Log In. Es la interfaz de entrada al sitio utilizando el email y la contraseña. 

4. Index
Además de las características heredadas descritas en el numeral HOME, este contiene la barra de búsqueda y pestañas de acceso al resto de secciones del sitio WEB, incluido el botón de salida LOGOUT. Aquí se puede ver un mosaico de obras en promoción.

5. Offers
Aquí se ofrecen las ofertas literarias recomendadas por el sitio WEB.

6. Novelties
Las novedades literarias del año se pueden visualizar aquí.

7. Best Sellers.
Esta sección recoge las puntuaciones con máximo rating.

8. Help
Es nuestra sección de ayuda para nuestros clientes.

Hay algunos archivos que son el motor de arranque de este sitio, los llamados backend; dichos archivos son:

a. application.py
Contiene la programación ejecutable principal. Está escrita en lenguaje Python

b. helpers.py
Ejecutable de ayuda para brindar algunos mensajes de apology.

c. import.py
Ejecutable auxiliar para poder subir a la base de datos PostgreSQL un listado de 5000 volúmenes con sus datos principales.

d. api.py
Realiza la conexión del sitio con los servicios API de Google Books

e. estilos.scss
Contiene el códex fons de estilos de CSS, el cual brinda mejoras estéticas a la interfaz del sitio.

Sin extender la descripción, estos son los elementos principales de los que consta este Proyecto 1. Bienvenido a
nuestro sitio WEB.

