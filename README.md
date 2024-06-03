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

## 📁 Estructura de archivos

Los problemas están organizados en carpetas, cada carpeta contiene al menos 200 problemas que indican el rango de `[id]` de problemas. Además, cada archivo está separado por `_` que representan los espacios en blanco del nombre del problema.

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

## 📄 Estrucutra en los archivos

Cada problema tiene una estructura similar, habrán excepciones pero en general se seguirá la siguiente estructura

- **[id]**: Identificador del problema
- **[Nombre del problema]**: Nombre del problema
- **[Link]**: Link del problema
- **Pasos**: Serie de comentarios que explican los pasos a seguir para resolver el problema
- **Código**: Código de la solución

```python
# [id]
# [Nombre del problema]
# [Link del problema]

"""
#[...tags]

El contenido de la descripción del problema

1. Paso 1
2. Paso 2
3. Paso 3
"""

print("Hola mundo")
```