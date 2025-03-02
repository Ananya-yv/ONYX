import streamlit as st

# Custom CSS for setting the background image
page_bg_img = """
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1635776063328-153b13e3c245?q=80&w=3132&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    
}
section[data-testid="stSidebar"] {
    background-color: #231d84 !important;  /* Replace with any color */
    color: #e4cffc
}


header[data-testid="stHeader"] {
    background: rgba(0, 0, 0, 0) !important;  /* Fully transparent */
}

header[data-testid="stHeader"] * {
    color: #10002b !important;  /* Ensures text inside the header changes color */
}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Page Content
st.markdown("<h1 style='text-align: center; color: #10002b; font-family: Luminari'>O N Y X</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #10002b'>S P A M  &nbsp D E T E C T O R</h2>", unsafe_allow_html=True)
st.sidebar.title("About the Model:")
st.sidebar.text("This Spam Classifier model uses SBERT (Sentence-BERT) to generate text embeddings.\n\n Predictions are done using SVM (Support Vector Machine) Classifier")
expander = st.sidebar.expander("Model Metrics:")
expander.write('''
    Accuracy: &nbsp; 99.01%
''')
expander.image("Screenshot 2025-03-02 213026.png")

st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    <style>
        .sidebar-link a {
            text-decoration: none;
            font-weight: bold;
            color: #d1c3f6;
        }
        .sidebar-link a:hover {
            color: #a295ea;
        }
    </style>
    <div class="sidebar-link">
        <a href="https://github.com/Ananya-yv/ONYX-Spam-Classifier" target="_blank"><h3> View Code on GitHub</h3></a>
    </div>
    """,
    unsafe_allow_html=True
)

footer = """
<style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #211b83;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    .footer a {
        color: #a295ea;
        text-decoration: none;
        font-weight: bold;
    }
    .footer a:hover {
        color: #d1c3f6;
    }
</style>
<div class="footer">
    <p>Developed by Ananya | © 2025 All Rights Reserved</p>
    <p>
        <a href="https://github.com/Ananya-yv" target="_blank">GitHub</a> | 
        <a href="www.linkedin.com/in/venkata-ananya-yerrapragada-29299b2b8" target="_blank">LinkedIn</a>
    </p>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)

import pickle

# Load the encoder model
with open("models/enc_model.pkl", "rb") as f:
    encoder = pickle.load(f)

# Load the SVM classification model
with open("models\svm_model.pkl", "rb") as f:
    classifier = pickle.load(f)

st.markdown(
    """
    <style>
    textarea {
        background-color: #aa9bf1  !important;  /* Light gray background */
        color: #181260  !important;  /* Dark purple text */
        font-size: 16px !important;  /* Adjust text size */
        border-radius: 10px !important; /* Rounded corners */
        padding: 10px !important; /* Extra spacing */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Custom CSS for button styling
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color:  #251f87!important;  /* Custom button color */
        color: white !important;  /* Text color */
        border-radius: 10px !important; /* Rounded corners */
        padding: 10px 20px !important; /* Button size */
        font-size: 18px !important; /* Font size */
        font-weight: bold !important;
        border: none !important;
        
            
    }

    div.stButton > button:first-child:hover {
        background-color: #5a4dbc !important;  /* Darker shade on hover */
        color: #d1c3f6 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<p style='color: #10002b; font-size: 20px; font-weight: bold;'>🔍 Drop your suspicious text here:</p>", unsafe_allow_html=True)
text = st.text_area("")


st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
# Custom CSS to make the background of messages more opaque
st.markdown("""
    <style>
    div.stAlert {
        background-color: #f8f9fa !important;  /* Light green for success */
        border-radius: 10px;
        color: 
        
    }
    
    </style>
    """, unsafe_allow_html=True)

if st.button("Predict"):
    if text.strip():
        # Encode the input text
        encoded_text = encoder.encode([text])  # Assuming encoder has an 'encode' method
        
        # Predict using the SVM classifier
        prediction = classifier.predict(encoded_text)[0]  # Get the first prediction
        
        # Display result
        if prediction == 1:
            st.markdown("<div style='padding: 15px; border-radius: 10px; background-color: #ffcccc; color: #721c24; font-weight: bold; text-align: center;'>🚨 Uh-Oh! This message is <span style='font-size: 18px;'>SPAM!</span> 🚨</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='padding: 15px; border-radius: 10px; background-color: #d4edda; color: #155724; font-weight: bold; text-align: center;'>✅<span style='font-size: 18px;'>No Spam</span> detected! The Message is Safe ✅</div>", unsafe_allow_html=True)


    else:
        st.markdown("<div style='padding: 15px; border-radius: 10px; background-color: #ffbf69; color: #155724; font-weight: bold; text-align: center;'>⚠️ Please enter a message to classify.</div>", unsafe_allow_html=True)


