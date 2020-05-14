# Django AWS Image Rekongnition

Proyecto de Inteligencia Artificial; utilizando herramientas de Amazon Web Services, el software es capáz de identificar objetos dentro de una imagen.

![Farmers Market Finder Demo](gifs/1.gif)

## Cómo comenzar ?

Necesitamos un entorno virtual basado Python 3.7
Con el entorno activo, instalamos las librerías.

```
 $: pip install -r librerias.txt
```

## Configuración AWS

Para que la magia funcione, debes tener configuro el acceso de usuario IAM en tu cuenta de AWS.
Se configura simplemente así:
```
 $: aws configure
```

## Levantar el proyecto

El comando de siempre
```
 $: python manage.py runserver 0:80
```

## Autor

* **Franco Díaz** - *Python Developer* - [@fraediaz](https://github.com/fraediaz)
