Pasos de GitHub:

Inicias la consola git y ejecutas los comandos:

Para clonar este proyecto si no lo tienes:
```
git clone https://github.com/fbonillo/proyecto_ddsi
```

Al añadir un archivo que no esté rastreado o al modificar un archivo. SI se quiere que git controle esta nueva versión, lo añadimos:
```
git add *
```

La * añade todos los archivos que no están rastreados, pero si quieres añadir uno en concreto, ejecuta git add archivo_concreto.html

Para confirmar los cambios, hacemos commit

```
git commit -m "Mensaje que quieras reflejar"
```

Para hacer efectivos los cambios en remoto en el servidor de GitHub:
```
git push
```

Si los archivos del repositario del servidor remoto están adelantados a tu versión actual en tu directorio:
```
git pull
```

Y puede que haya que hacer MERGE si hay datos que no están actualizados tanto en tu repositorio local como en el remoto. Seguir de lo que te indique git. Si no es un merge que involucre mismos archivos modificados, entonces salte de la pantalla de vim/nano que te haya salido al hacer push, y luego haz git pull
