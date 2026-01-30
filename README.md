# Prescription-Reading-And-Alternated-Medicines-Prediction-Using-OCR-For-Medical-Store

## 📌 Project Overview

This project focuses on **automatically reading medical prescriptions using OCR (Optical Character Recognition)** and **predicting alternative medicines** for the identified drugs. It is designed to help medical stores, pharmacists, and healthcare systems reduce manual work, avoid misreading prescriptions, and quickly find substitute medicines when the prescribed one is unavailable.

The system extracts text from prescription images, processes medicine names, and suggests alternatives based on available data.

---

## 🎯 Features

* 📷 Upload prescription image
* 🔍 Extract text using OCR
* 💊 Identify medicine names from prescription
* 🔁 Predict alternative medicines
* ⚡ Fast and automated processing
* 🏥 Useful for medical stores and pharmacies

---

## 🛠️ Technologies Used

### 🔹 Programming Language

* **Python** – Core language for backend logic and processing

### 🔹 OCR & Image Processing

* **Tesseract OCR** – For extracting text from prescription images
* **OpenCV** – Image preprocessing for better OCR accuracy
* **Pillow (PIL)** – Image handling

### 🔹 Machine Learning / NLP

* **Scikit-learn** – For prediction and matching logic
* **Pandas** – Data handling and preprocessing
* **NumPy** – Numerical computations

### 🔹 Backend / API

* **Flask** – Web framework for building the application

### 🔹 Frontend (if applicable)

* **HTML**
* **CSS**
* **JavaScript**

### 🔹 Database (if used)

* **CSV / Local Dataset** for medicine and alternative mapping
  *(Can be replaced with MySQL / MongoDB in future)*

---

## 📂 Project Structure

```
Prescription-Reading-And-Alternated-Medicines-Prediction-Using-OCR/
│
├── static/                 # CSS, JS, Images
├── templates/              # HTML files
├── uploads/                # Uploaded prescription images
├── dataset/                # Medicine dataset
├── app.py                  # Main Flask app
├── ocr.py                  # OCR logic
├── prediction.py           # Alternative medicine logic
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
python app.py
```

### 4️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 🧪 Example Use Case

1. Upload a handwritten or printed prescription image
2. System extracts text using OCR
3. Medicine names are detected
4. Alternative medicines are suggested
5. Pharmacist can choose available option

---

## 🔮 Future Enhancements

* ✅ Deep learning-based OCR for higher accuracy
* ✅ Database integration (MySQL / MongoDB)
* ✅ Doctor handwriting recognition improvement
* ✅ Mobile app version
* ✅ Cloud deployment

---

## 👨‍💻 Author

Kolanu Padmakanth Reddy
AI / ML & Full Stack Developer

---

⭐ If you find this project useful, don’t forget to star the repository!
