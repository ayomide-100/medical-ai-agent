# Medica Image Diagnosis Agent

An AI-powered medical image analysis tool that leverages advanced computer vision and large language models to provide expert-level diagnostic insights for medical images. This agent combines the power of Google Gemini, real-time web research, and a user-friendly Streamlit interface to assist healthcare professionals and patients in understanding medical imaging results.

---

## Features

- **Multi-Modal AI Analysis:** Uses Google Gemini for sophisticated image and text understanding.
- **Medical Image Support:** Accepts X-ray, MRI, CT, Ultrasound, and other common formats (JPG, JPEG, PNG, DICOM).
- **Automated Research:** Integrates DuckDuckGo search to provide up-to-date medical literature and treatment protocols.
- **Structured Reporting:** Delivers findings in a clear, markdown-formatted report with sections for key findings, diagnosis, patient-friendly explanations, and research context.
- **Patient-Centric:** Explains results in accessible language, addressing common concerns and providing visual analogies.
- **Secure API Key Management:** API keys are managed securely via environment variables or Streamlit sidebar input.

---

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/med_ai_agent.git
   cd med_ai_agent
   ```

2. **Set up a virtual environment (recommended):**
   ```sh
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   # or
   source venv/bin/activate      # On macOS/Linux
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure your API key:**
   - Create a `.env` file in the root directory:
     ```
     GEMINI_API_KEY=your_google_gemini_api_key
     ```
   - Or enter your API key in the Streamlit sidebar at runtime.

---

## Usage

1. **Start the Streamlit app:**
   ```sh
   streamlit run main.py
   ```

2. **Upload a medical image:**  
   Supported formats: JPG, JPEG, PNG, DICOM.

3. **Analyze:**  
   Click "Analyze Image" to receive a detailed, structured report.

---

---

## File Structure

- [`main.py`](main.py): Streamlit app entry point.
- [`src/agent.py`](src/agent.py): Agent configuration and prompt template.
- [`requirements.txt`](requirements.txt): Python dependencies.
- [`test_images/`](test_images/): Sample images for testing.

---

## Security

- **API keys** are never hardcoded in the source. Use `.env` or the sidebar input.
- **Patient data** is not stored or transmitted beyond the analysis session.



## Disclaimer

_This tool is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for clinical decisions._