import sys
import os
# Agregar la carpeta raiz al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from server import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
