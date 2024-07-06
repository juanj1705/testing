print("Hello git!\n");
# git -h
# git --help
print("Configuracion global de git en el equipo local");
# git config --global user.name "Nombre"
# git config --global user.email "email@gmail.com"
print("Cambio de nombre opcional de la rama master a main")
# git config --global init.defaultBranch main 

print("Crear carpeta .git en carpeta del proyecto");
# git init
print("Renombrar la rama si se desea")
# git branch -m main
print("Con las excepciones en la carpeta .gitignore");
# **/ignored.txt

print("Ver el estado actual del git para modificar");
# git status
print("Ver el historial del git para modificar");
# git log
print("Commandos por default con alias");
# git alias

print("Añadir fichero o ficheros");
# git add hellogit.py
# git add .
print("Captura de version");
# git commit -m "Version"