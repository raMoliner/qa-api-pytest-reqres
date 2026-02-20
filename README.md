![CI](https://github.com/raMoliner/qa-api-pytest-reqres/actions/workflows/ci.yml/badge.svg)
[![Allure Report](https://img.shields.io/badge/Allure-Report-brightgreen)](https://ramoliner.github.io/qa-api-pytest-reqres/)

# QA API Automation - JSONPlaceholder (Pytest + Requests + Allure)

Proyecto de automatización **API** con **Pytest** + **Requests**, reporting con **Allure** y publicación automática del reporte en **GitHub Pages**.

- **API under test:** https://jsonplaceholder.typicode.com
- **Allure Report (GitHub Pages):** https://ramoliner.github.io/qa-api-pytest-reqres/

> Nota técnica: inicialmente se evaluó ReqRes, pero en CI puede devolver 403 por protección anti-bot. JSONPlaceholder es estable para CI/CD.

---

## Stack
- Python + Pytest
- Requests
- Allure (pytest plugin + reporte HTML)
- GitHub Actions (CI + deploy a GitHub Pages)

---

## Qué cubre (Smoke)
- `GET /posts` (validaciones de status y estructura)
- `GET /posts/{id}`
- `POST /posts` (creación y validación de response)

---

## Estructura
```text
.
├─ api_clients/
├─ tests/
├─ artifacts/
│  ├─ allure-results/
│  └─ allure-report/
├─ pytest.ini
├─ requirements.txt
└─ .github/workflows/ci.yml
```

## Cómo ejecutar (local)
1) Crear venv e instalar dependencias

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2) Ejecutar todos los tests

```
pytest
```

3) Ejecutar solo smoke
```
pytest -m smoke
```

Allure (local)
Generar resultados y abrir reporte (servidor local)

```
pytest -m smoke --alluredir=artifacts/allure-results
allure serve artifacts/allure-results
```

Generar HTML estático
```
allure generate artifacts/allure-results -o artifacts/allure-report --clean
```
