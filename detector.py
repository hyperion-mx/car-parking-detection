"""
ParkGuard AI — License Plate Detector
Optimisé pour YOLOv8 (Détection) + YOLOv10 (OCR) pour plaques marocaines.
"""
import cv2
import numpy as np
import re
from config import DETECTOR_MODEL_PATH, READER_MODEL_PATH, CONFIDENCE_THRESHOLD

class PlateDetector:
    """Détecte et lit les plaques d'immatriculation via un double pipeline YOLO."""

    def __init__(self):
        self.detector_model = None
        self.reader_model = None
        self._loaded = False
        
        # Mapping des classes pour les lettres de série marocaines
        self.cls_to_letter_map = {
            '10': 'A', '11': 'B', '12': 'E', '13': 'D', '14': 'H'
        }

    def load(self):
        """Charge les deux modèles YOLO au démarrage."""
        if self._loaded:
            return True, "Déjà chargé."
        try:
            from ultralytics import YOLO
            self.detector_model = YOLO(DETECTOR_MODEL_PATH)
            self.reader_model = YOLO(READER_MODEL_PATH)
            self._loaded = True
            return True, "Modèles YOLO chargés avec succès."
        except Exception as e:
            return False, f"Échec du chargement : {e}"

    @property
    def is_loaded(self):
        return self._loaded

    def detect(self, frame):
        """Exécute la détection de plaque et l'OCR sur une image."""
        if not self._loaded:
            return []

        # 1. Détection de la zone de la plaque
        results = self.detector_model(frame, conf=CONFIDENCE_THRESHOLD, verbose=False)
        detections = []

        for result in results:
            if result.boxes is None:
                continue
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                conf = float(box.conf[0])

                # Découpage de la plaque
                plate_img = frame[y1:y2, x1:x2]
                
                # 2. Lecture des caractères via le second modèle YOLO
                plate_text = self._read_plate(plate_img)

                if plate_text:
                    detections.append({
                        "bbox": (x1, y1, x2, y2),
                        "confidence": conf,
                        "plate_text": plate_text,
                    })

        return detections

    def _read_plate(self, plate_img):
        """Extrait le texte d'une plaque découpée via le modèle Reader YOLO."""
        if plate_img is None or plate_img.size == 0:
            return ""

        try:
            # Inférence OCR
            results = self.reader_model(plate_img, verbose=False)[0]
            
            if not results.boxes:
                return ""

            char_boxes = results.boxes.data.cpu().numpy()
            chars_detected = []

            # Extraction et mapping des caractères détectés
            for char_box in char_boxes:
                x1, y1, x2, y2, conf, cls = char_box
                cls_name = str(results.names.get(int(cls)))
                text = self.cls_to_letter_map.get(cls_name, cls_name)
                chars_detected.append((x1, text))

            # Tri des caractères de gauche à droite selon leur position X
            chars_detected.sort(key=lambda x: x[0])
            full_text = "".join([c[1] for c in chars_detected])

            # Formatage propre : [Nombres]-[Lettre]-[Préfecture]
            match = re.match(r"^(\d+)([A-Z]+)(\d+)$", full_text)
            if match:
                return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
            
            return full_text

        except Exception:
            return ""

    def draw_detections(self, frame, detections):
        """Dessine les boîtes et le texte reconnu sur l'image."""
        annotated = frame.copy()
        for det in detections:
            x1, y1, x2, y2 = det["bbox"]
            text = det["plate_text"] or "???"
            conf = det["confidence"]

            cv2.rectangle(annotated, (x1, y1), (x2, y2), (0, 255, 100), 2)
            label = f"{text} ({conf:.0%})"
            (tw, th), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
            cv2.rectangle(annotated, (x1, y1 - th - 10), (x1 + tw + 6, y1), (0, 255, 100), -1)
            cv2.putText(annotated, label, (x1 + 3, y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

        return annotated