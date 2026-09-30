import streamlit as st
st.set_page_config(page_title="AI Smart Agriculture", page_icon="🌱")

st.title("🌱 AI-POWERED SMART AGRICULTURE PLATFORM")
st.write("By V. LAVANYA- 20624u48027 | Kamban College")

menu = st.sidebar.selectbox("Select", ["Crop Recommendation", "Smart Irrigation", "Disease Detection"])

if menu == "Crop Recommendation":
    st.header("🌾 Crop Recommendation")
    n = st.number_input("Nitrogen", 0, 100, 50)
    p = st.number_input("Phosphorus", 0, 100, 50)
    k = st.number_input("Potassium", 0, 100, 50)
    temp = st.number_input("Temperature", 0.0, 50.0, 25.0)
    if st.button("Recommend Crop"):
        st.success("Recommended Crop: **Rice** - Suitable for your soil! 🌾")

elif menu == "Smart Irrigation":
    st.header("💧 Smart Irrigation")
    moisture = st.slider("Soil Moisture %", 0, 100, 40)
    if moisture < 30:
        st.error("Water Needed! Motor ON")
    else:
        st.success("Moisture OK! Motor OFF")

else:
    st.header("🍃 Disease Detection")
    file = st.file_uploader("Upload Leaf Image", type=["jpg","png"])
    if file:
        st.image(file)
        st.warning("Prediction: Healthy Leaf (Sample) - Use AI model here")
