import streamlit as st
import zxcvbn
import random
import string
import pyperclip

# Configure Streamlit Page
st.set_page_config(page_title="🔐 Advanced Password Strength Meter", page_icon="🔒", layout="centered")

# Custom CSS for Stunning UI
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: white;
        }
        .stProgress > div > div > div {
            border-radius: 10px;
        }
        .password-box {
            font-size: 18px;
            border-radius: 10px;
            padding: 10px;
            width: 100%;
        }
        .strength-bar {
            border-radius: 10px;
            height: 20px;
        }
        .copy-btn {
            background-color: #2ECC71;
            color: white;
            border-radius: 5px;
            padding: 5px;
            font-weight: bold;
            cursor: pointer;
            text-align: center;
            display: inline-block;
            width: 100px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Input
st.title("🔐 Ultimate Password Strength Meter")

# Show/Hide Password Toggle
show_password = st.checkbox("👁 Show Password")
if show_password:
    password = st.text_input("Enter your password:", type="default")  # Show password as plain text
else:
    password = st.text_input("Enter your password:", type="password")  # Hide password


if password:
    # Analyze password strength
    analysis = zxcvbn.zxcvbn(password)
    strength_score = analysis['score']  # Score ranges from 0 (weak) to 4 (strong)
    feedback = analysis['feedback']['suggestions']
    time_to_crack = analysis['crack_times_display']['offline_fast_hashing_1e10_per_second']

    # Define strength levels
    strength_levels = ["❌ Very Weak", "⚠️ Weak", "🟡 Fair", "🟢 Strong", "✅ Very Strong"]
    strength_colors = ["#FF4B4B", "#FF944B", "#FFC107", "#4CAF50", "#2ECC71"]

    # Display Strength Score
    st.markdown(f"### Strength: **{strength_levels[strength_score]}**")
    st.progress((strength_score + 1) * 20)  # Convert to percentage
    st.markdown(f"<div style='background-color: {strength_colors[strength_score]}; height: 10px; border-radius: 10px;'></div>", unsafe_allow_html=True)

    # Estimated Crack Time
    st.markdown(f"⏳ **Time to Crack Password:** `{time_to_crack}`")

    # Feedback and Suggestions
    if feedback:
        st.warning("⚠️ Suggestions to Improve:")
        for tip in feedback:
            st.write(f"- {tip}")

    # Password Tips
    st.info("💡 Tips for a Stronger Password:")
    st.write("- Use at least **12 characters**.")
    st.write("- Include **uppercase, lowercase, numbers, and special characters**.")
    st.write("- Avoid **common words or patterns** (e.g., 'password123').")
    st.write("- Do not reuse old passwords.")

# Generate Strong Password
st.subheader("🔑 Need a Strong Password?")
def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

generated_password = generate_password()

if st.button("🎲 Generate Strong Password"):
    st.success(f"🔐 **Generated Password:** `{generated_password}`")

    # Copy to Clipboard (Manually)
    pyperclip.copy(generated_password)
    st.markdown("✅ Password copied to clipboard!")

# Footer
st.markdown("---")
st.markdown("🔒 **Secure your online accounts with strong passwords!**")

# Run the app with: streamlit run app.py
