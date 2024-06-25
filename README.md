<h1 align="center">Problemas del Juez Patito 🔨🦆</h1>

![](./assets/banner.png)

<p align="center">
    <a href="https://www.python.org/">
        <img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/>
    </a>
    <a href="https://jv.umsa.bo/oj/problemset.php">
        <img alt="Python" src="https://img.shields.io/badge/Juez Patito-4285F4.svg?style=for-the-badge&logo=microsoftedge&logoColor=white"/>
    </a>
</p>

Este repositorio contiene la solución a los problemas del juez patito, una plataforma de problemas de la *Universidad Mayor de San Andrés*. Los problemas están resueltos únicamente en Python pero se dejan explicaciones detalladas de los problemas para que puedan ser resueltos en otros lenguajes de programación.

> [!CAUTION]
> Este repositorio únicamente es para guardar mis soluciones, no se recomienda copiar y pegar el código, **es mejor intentar resolver los problemas por ti mismo**.

> [!NOTE]
> No se encuentran todos los problemas de la plataforma, eventualmente se irán añadiendo más problemas conforme los vaya resolviendo o vayan saliendo nuevos problemas.

### 📚 Contenid

- [🎯 Objetivos](#-objetivos)
- [📁 Estructura de archivos](#-estructura-de-archivos)
- [📄 Formato de archivos](#-formato-de-archivos)


## 🎯 Objetivos

- [ ] Resolver 100 problemas
- [ ] Resolver 200 problemas
- [ ] Resolver 400 problemas
- [ ] Resolver 800 problemas
- [ ] Resolver 1200 problemas
- [ ] Resolver TODOS los problemas
- [x] Crear una base de datos con los problemas y soluciones
- [ ] Crear un CLI para interactuar con el proyecto
- [ ] Crear una página web estática para mostrar las soluciones


## 📁 Estructura de archivos

Los problemas están organizados en carpetas, **cada carpeta contiene al menos 200 problemas** que indican el rango de `[id]` de problemas. Además, cada archivo está separado por `_` que representan los espacios en blanco del nombre del problema.

```bash
├── 1000-1200
│   ├── [id]_[Nombre del problema].py
│   ├── [id]_[Nombre del problema].py
│   ├── ...
├── 1201-1401
│   ├── [id]_[Nombre del problema].py
│   ├── [id]_[Nombre del problema].py
│   ├── ...
├── 1402-1602
│   ├── [id]_[Nombre del problema].py
│   ├── [id]_[Nombre del problema].py
├── ...
│
```

## 📄 Formato de archivos

En cada archivo Python se encuentra la solución de los problemas en código, además de comentarios los cuales son utilizados para guardarse en una base de datos y poder ser consultados en el futuro.

> [!NOTE]
> Los comentarios multilineas son contenido markdown potenciado con plugins de remark, por lo que no se verán correctamente en un editor de texto plano.

```python
# [id]
# [Nombre del problema]
# [Link del problema]
# tag1 tag2 tag3-con-espacios

"""description
El contenido de la descripción del problema
con imagenes o algun contexto necesario para
poder resolver el problema
"""

"""steps
En aquí se describe los pasos algoritmicos
que se sigue para poder resolver el problemas

1. leer datos en la variable `N`
2. hacer algo con `N`
3. ...
"""

print("Hola mundo")
```