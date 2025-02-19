import streamlit as st
import random

def main():
    st.set_page_config(
        page_title="Growth Mindset Hub",
        page_icon="🌟",
        layout="wide"
    )

    st.markdown("""
        <style>
            body {
                background-color: #B2BEB5; /* Ash Gray */
            }
            .stTitle {
                text-align: center;
                font-size: 2.5rem;
                font-weight: bold;
                color: #2c3e50;
            }
            .stHeader {
                color: #8e44ad;
                font-weight: bold;
                text-align: center;
            }
            .stMarkdown {
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='stTitle'>🌟 Unlock Your Full Potential</h1>", unsafe_allow_html=True)
    
    # Sidebar Navigation
    st.sidebar.header("Menu")
    page = st.sidebar.radio("Explore", ["Home", "Learn", "Reflect", "Track Progress"])

    if page == "Home":
        show_home()
    elif page == "Learn":
        show_learn()
    elif page == "Reflect":
        show_reflect()
    elif page == "Track Progress":
        show_track_progress()

def show_home():
    st.markdown("<h2 class='stHeader'>Welcome to Your Growth Journey</h2>", unsafe_allow_html=True)
    
    st.write("""
    A growth mindset helps you adapt, learn, and stay motivated. 
    This app is designed to guide you in developing a positive, unstoppable mindset.
    """)

    st.subheader("Core Principles of a Growth Mindset")
    cols = st.columns(3)
    
    with cols[0]:
        st.markdown("### 🎯 Face Challenges")
        st.write("See difficulties as chances to improve.")
    
    with cols[1]:
        st.markdown("### 💪 Keep Going")
        st.write("Hard work and persistence lead to success.")
    
    with cols[2]:
        st.markdown("### 📚 Learn from Feedback")
        st.write("Use advice and corrections to grow.")
    
    cols2 = st.columns(3)
    
    with cols2[0]:
        st.markdown("### 🌟 Stay Curious")
        st.write("Ask questions and explore new ideas.")
    
    with cols2[1]:
        st.markdown("### 🚀 Take Risks")
        st.write("Step outside your comfort zone and try new things.")
    
    with cols2[2]:
        st.markdown("### ❤️ Celebrate Progress")
        st.write("Recognize and enjoy your achievements.")

def show_learn():
    st.markdown("<h2 class='stHeader'>Discover the Growth Mindset</h2>", unsafe_allow_html=True)
    
    st.subheader("What is a Growth Mindset?")
    st.write("""
    A growth mindset means believing that skills and intelligence can improve with effort. 
    With patience and dedication, anyone can grow and succeed.
    """)
    
    if st.button("Show a Growth Tip"):        
        tips = [
            "Turn failures into lessons.",
            "Add 'yet' to challenges—'I can't do this yet!'.",
            "Small steps lead to big progress.",
            "Feedback is a guide, not a judgment.",
            "Try new things and embrace learning."
        ]
        st.info(random.choice(tips))

def show_reflect():
    st.markdown("<h2 class='stHeader'>Reflect on Your Progress</h2>", unsafe_allow_html=True)
    
    st.write("Thinking about your day helps you grow and improve.")
    
    with st.form("reflection_form"):
        date = st.date_input("Pick a Date")
        challenge = st.text_area("What challenge did you face today?")
        response = st.text_area("How did you handle it?")
        learning = st.text_area("What did you learn?")
        
        submitted = st.form_submit_button("Save Reflection")
        if submitted:
            st.success("Your thoughts are saved!")

def show_track_progress():
    st.markdown("<h2 class='stHeader'>Track Your Growth</h2>", unsafe_allow_html=True)
    
    st.subheader("How was your mindset today?")
    mindset_score = st.slider("Rate yourself from 1 to 10", 1, 10, 5)
    
    if mindset_score <= 3:
        st.warning("Every step counts! Keep going!")
    elif mindset_score <= 7:
        st.info("You're improving! Stay consistent.")
    else:
        st.success("Great mindset today! Keep it up!")

if __name__ == "__main__":
    main()
