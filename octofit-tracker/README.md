# OctoFit Tracker (scaffold)

Estructura mínima del proyecto OctoFit Tracker.

Estructura creada:

```
octofit-tracker/
├── backend/
│   └── requirements.txt
└── frontend/
```

Configuración recomendada (desde el host, sin cambiar de directorio):

```bash
# Crear el entorno virtual para el backend
python3 -m venv octofit-tracker/backend/venv

# Activar el entorno (bash)
source octofit-tracker/backend/venv/bin/activate

# Instalar dependencias del backend
pip install -r octofit-tracker/backend/requirements.txt
```

Puertos relevantes (no cambiar):

- `8000` (Django)
- `3000` (frontend)
- `27017` (MongoDB, privado)

Notas:

- Usa siempre el ORM de Django para crear estructuras y datos, no scripts directos en MongoDB.
- Sigue las instrucciones en `.github/instructions/` del repositorio para más detalles.
