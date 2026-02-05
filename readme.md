# 🥋 The Coding Dojo: Algorithmic Katas

Este repositorio es mi espacio personal de entrenamiento. Aquí no solo resuelvo problemas, sino que practico la **maestría del código** a través de *Katas*: ejercicios diseñados para perfeccionar la lógica, la sintaxis y el pensamiento algorítmico mediante la repetición y el refinamiento.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![LeetCode](https://img.shields.io/badge/-LeetCode-FFA116?style=for-the-badge&logo=LeetCode&logoColor=black)
---

## 📂 Estructura del Dojo

He organizado el entorno para que sea minimalista y eficiente. Cada ejercicio (Kata) reside en la carpeta `katas/`, identificada por su ID de LeetCode.

```text
.
├── katas/                # El corazón del dojo (Python + Pytest)
│   ├── 1.py              # Two Sum
│   ├── 20.py             # Valid Parentheses
│   ├── 26.py             # Remove Duplicates from Sorted Array
│   ├── 28.py             # Find the Index of the First Occurrence in a String
│   ├── 70.py             # Climbing Stairs
│   └── ...
├── utils/                # Utilidades de apoyo (Loggers, etc.)
├── create.sh             # El "Sensei": automatización de Katas
└── README.md             # El manifiesto del Dojo
```

---

## 🧪 Laboratorio de Pruebas (Testing)

En este Dojo, una solución solo se considera "dominada" cuando supera todos los casos de prueba de forma elegante.

### 🐍 Python con Pytest
Utilizo tests parametrizados para una validación exhaustiva:
```python
@pytest.mark.parametrize("input, expected", [
    (["flower","flow","flight"], "fl"),
    (["dog","racecar","car"], ""),
])
def test_solution(input, expected):
    assert Solution().longestCommonPrefix(input) == expected
```

---

## 🛠️ El "Sensei" (Automatización)

Para mantener el enfoque en la lógica y no en la configuración, utilizo un script en Bash para generar el *boilerplate* de mis Katas.

### Uso:
1. **Permisos de ejecución:** `chmod +x create.sh`
2. **Generar nueva Kata:**

```bash
./sensei.sh -m "9. Palindrome Number"
./sensei.sh -m "125 Valid Palindrome"
```

3. **Ejecutar la Kata:**

```bash
./sensei.sh -m 9
```

El script genera esqueletos automáticos con:
- ✅ **Estructura de tests** lista para completar.
- ✅ **Logging estandarizado** con `utils.log`.

---

## 🥋 Filosofía de Entrenamiento

1. **Claridad sobre Velocidad:** El código debe ser legible antes que ingenioso.
2. **Refactorización Continua:** Una Kata no termina al pasar el test, sino cuando el código es lo más simple posible.

---
*“No temo al hombre que ha practicado 10,000 patadas una vez, sino al que ha practicado una patada 10,000 veces.”* – Bruce Lee
