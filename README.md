# proyectopython

En este repositorio subiremos el código del proyecto de programación que vamos a hacer en python: conecta4

## iniciar git

1.Nos movemos la directorio (carpeta) donde queremos clonar (descargar) el repositorio

CONSEJO: El directorio donde guardemos los repositorios, que no tengan caracteres especiales: espacios, acentos, mayusculas...etc

En este ejemplo, crearemos una carpeta llamada GIT en la raiz del pc.

```bash
mkdir c:\git
cd c:\git
```

2.Clonamos el repositorio de github. Nos pedira usuario y contraseña

```bash
git clone https://github.com/victoriapenasmiro/proyectopython
```

3.Accedemos a la carpeta y verificamos que haya ido todo bien

```bash
cd proyectopython
git status
```

Si todo ha ido bien, la consola devolvera:

```bash
srodriguez@MacBook-Pro-de-Sebastian proyectopython % git status
On branch master
Your branch is up to date with 'origin/master'.
```

### Borrar repositorio GIT

Para borrar un repositorio git, basta que borremos el directorio (carpeta) donde alojamos dicho repositorio

```bash
rd c:\git /S /Q
````
