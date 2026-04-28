"""
ParkGuard AI — Configuration
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Model ---
_model_dir = os.path.join(BASE_DIR, "model")

# Mise à jour avec tes nouveaux noms de fichiers
DETECTOR_MODEL_PATH = os.path.join(_model_dir, "yolov8n_plate.pt")
READER_MODEL_PATH = os.path.join(_model_dir, "PlateReaderyolo.pt")

CONFIDENCE_THRESHOLD = 0.4

# --- Database ---
DATABASE_PATH = os.path.join(BASE_DIR, "parking.db")

# --- Camera ---
CAMERA_INDEX = 0  # 0 = webcam par défaut
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

# --- Detection ---
DETECTION_INTERVAL_MS = 2000  # Intervalle de détection en ms

# --- Gate Signal Server ---
GATE_SERVER_PORT = 5555  # Port HTTP requis pour le script de la barrière