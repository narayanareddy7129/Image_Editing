# Image Editor — Streamlit & OpenCV

An interactive, browser-based image editing application built with **Python**, **Streamlit**, and **OpenCV**.  
Upload any image, apply a stack of visual filters in real time, preview the result, and download the modified image — all without writing HTML or CSS.

---

## Features / Filters Implemented

| Filter | Control | Description |
|---|---|---|
| **Grayscale** | Toggle (checkbox) | Converts image to luminance (black & white) |
| **Brightness** | Slider (−100 → +100) | Linearly shifts pixel intensity |
| **Contrast** | Slider (0.5 → 3.0) | Scales pixel values around the midpoint |
| **Blur** | Slider (1 → 51, odd) | Gaussian blur — higher = more smoothing |
| **Sharpness** | Slider (0.0 → 3.0) | Unsharp mask — enhances edges |
| **Edge Detection** | Toggle + 2 sliders | Canny algorithm with adjustable thresholds |

> **Filters are stackable** — applied in sequence (grayscale → brightness/contrast → blur → sharpness → edge detection) every time a slider changes.

---

## Project Structure

```
image_editor/
├── app.py           # Main Streamlit application & UI layout
├── filters.py       # All OpenCV filter functions
├── utils.py         # Format conversion helpers (PIL ↔ NumPy ↔ bytes)
├── requirements.txt # Python dependencies
└── README.md        # This file
```

---

## Setup & Installation

### Prerequisites
- Python 3.9 or newer

### 1. Clone the repository

git clone https://github.com/<your-username>/image-editor.git
cd image-editor


### 2. Create a virtual environment (recommended)

python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows


### 3. Install dependencies

pip install -r requirements.txt


### 4. Run the app
streamlit run app.py


The app will open automatically at **http://localhost:8501**.

---

## Screenshot

> *(Add a screenshot of the running app here after your first run.)*  
> Example: `![App Screenshot](screenshot.png)`

---

## Demo Video

> https://www.youtube.com/watch?v=qbGNiZ1ztWA  


---

## How It Works

1. **Upload** a JPG or PNG image via the file uploader.  
2. **Adjust** any filter slider or toggle in the left sidebar.  
3. The app re-applies **all active filters in sequence** on the original image and updates the **side-by-side preview** instantly.  
4. **Download** the processed image as a PNG with one click.  
5. Use the **Reset All Filters** button to return every control to its default value.

---

## Tech Stack

| Library | Purpose |
|---|---|
| `streamlit` | Web UI — sliders, file uploader, layout |
| `opencv-python` | Image processing & filter operations |
| `numpy` | Image array manipulation |
| `Pillow` | PIL → NumPy conversion & PNG encoding |

---
