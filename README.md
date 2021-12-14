Script que obtiene la lista de projectos de gitlabci y verifica si tienen o no la libreria log4j
como asi tambien los projectos de spv-commons-logging y spv-common-logger.

Genera como salida 3 archivos .csv con el id del proyecto y el nombre.

### Configuracion

En el archivo .python-gitlab.cfg se configura el token de la api para que permita read only.
"# log4j" 
