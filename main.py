import os
from PIL import Image as PILImage
from agno.media import Image as AgnoImage
import streamlit as st
from src import agent
from src.agent import med_agent, prompt
from dotenv import load_dotenv
load_dotenv()

if "GEMINI_API_KEY" not in st.session_state:
    st.session_state.GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") 


with st.sidebar:
    st.title("Configuration")

    if not st.session_state.GEMINI_API_KEY:
        api_key = st.text_input("Enter your API key: ", type= "password")

        st.caption("Get your api key from google studios")

        if api_key:
            st.session_state.GEMINI_API_KEY = api_key
            st.success("API Key Saved")
            st.rerun()
    else: 
        st.success("API KEY configured")
        


    st.info("AI-powered medical image analysis using advanced computer vision and expertise")

med_agent if st.session_state.GEMINI_API_KEY else None

st.title("Medica Image Diagnosis Agent")
st.write("Upload medical image for analysis")

upload_container = st.container()
image_container = st.container()
analysis_container = st.container()

with upload_container:
    uploaded_file = st.file_uploader(
        "Upload Medical Image", 
        type=["jpg", "jpeg", "png", "dicom"], 
        help="Supported formats: JPG, JPEG, PNG, DICOM"
        )

if uploaded_file is not None:
    with image_container:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2: 
            image = PILImage.open(uploaded_file)
            width, height = image.size
            aspect_ratio = width / height
            new_width = 500
            new_height = int(new_width / aspect_ratio)
            resized_image = image.resize((new_width, new_height))
            
            
            st.image(
                resized_image, caption="Uploaded Image", 
                use_column_width=True
            )

            analyze_button = st.button(
                "Analze Image", 
                type= "primary", 
                use_container_width=True
            )


    with analysis_container:
        if analyze_button:
            with st.spinner("Analyzing image......Please wait"):
                try: 
                    temp_path = "temp_resized_image.png"
                    resized_image.save(temp_path)

                    agno_image = AgnoImage(filepath=temp_path)

                    response = med_agent.run(prompt, images = [agno_image])
                    st.markdown("### Analysis Results")
                    st.markdown("---")
                    st.markdown(response.content)
                    st.markdown("---")
                    st.caption("" \
                    "Analysis complete, Subject to confirmation from a Medical Professional")
                except Exception as e:
                    st.error(f"Analysis error: {e}")
else:

    st.info("You forgot to upload an image to start the analysis")