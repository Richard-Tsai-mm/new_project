import streamlit as st
import pandas as pd
from io import BytesIO

def convert_xlsx_to_u8(uploaded_file):
    # Read the Excel file
    df = pd.read_excel(uploaded_file, dtype=str)
    
    # Convert DataFrame to CSV format with UTF-8 encoding
    output = BytesIO()
    df.to_csv(output, encoding='utf-8', index=False, sep='|')
    output.seek(0)
    
    return output

# Streamlit UI
st.title("Excel to U8 Converter")

# File uploader placeholder
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"], key="file_uploader")

# File download placeholder
if uploaded_file is not None:
    st.success("File uploaded successfully!")
    
    converted_file = convert_xlsx_to_u8(uploaded_file)
    
    st.download_button(
        label="Download U8 File",
        data=converted_file,
        file_name="converted_file.U8",
        mime="text/plain",
        key="download_button"
    )
