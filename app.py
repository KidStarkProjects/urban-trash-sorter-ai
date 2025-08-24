import gradio as gr
from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import requests

# 1. Muat Model dan Processor dari Hugging Face
model_name = "google/vit-base-patch16-224"
processor = ViTImageProcessor.from_pretrained(model_name)
model = ViTForImageClassification.from_pretrained(model_name)

# 2. Tentukan Label Klasifikasi Sampah
trash_mapping = {
    "water bottle": "Plastik PET (Daur ulang)",
    "plastic bottle": "Plastik PET (Daur ulang)",
    "plastic bag": "Plastik HDPE (Daur ulang)",
    "bottle cap": "Plastik (Daur ulang)",
    "soda can": "Aluminium (Daur ulang)",
    "glass bottle": "Kaca (Daur ulang)",
    "paper towel": "Kertas (Kompos/Dibuang)",
    "cardboard box": "Kardus (Daur ulang)",
    "banana": "Sampah Organik (Kompos)",
    "apple": "Sampah Organik (Kompos)",
    "fruit": "Sampah Organik (Kompos)",
}

def predict_trash(image):
    """
    Fungsi ini menerima gambar dan mengembalikan hasil klasifikasi sampah.
    """
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    predicted_label = model.config.id2label[predicted_class_idx]
    
    classification = "Tidak diketahui"
    if predicted_label.lower() in trash_mapping:
        classification = trash_mapping[predicted_label.lower()]
    else:
        classification = predicted_label
        
    result_text = f"Objek yang terdeteksi: **{predicted_label}**"
    suggestion_text = f"Rekomendasi penanganan: **{classification}**"

    return result_text, suggestion_text

# 3. Buat Antarmuka Gradio dengan Opsi Kamera
title = "Smart Urban Trash Sorter"
description = "Unggah atau ambil foto sampah, dan AI akan mengklasifikasikan jenisnya serta memberikan rekomendasi daur ulang. Inovasi sederhana untuk urban living."
examples = [
    ["https://ibb.co.com/VPvWJFX"],
    ["https://ibb.co.com/qMs9QNv7"]
]

demo = gr.Interface(
    fn=predict_trash,
    # Untuk mengaktifkan fitur kamera
    inputs=gr.Image(type="pil", label="Unggah atau ambil foto sampah", sources=["upload", "webcam"]),
    outputs=[gr.Textbox(label="Hasil Klasifikasi"), gr.Textbox(label="Rekomendasi")],
    title=title,
    description=description,
    examples=examples,
    allow_flagging="auto",
)

# Luncurkan aplikasi Gradio
if __name__ == "__main__":
    demo.launch(share=True)