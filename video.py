import streamlit as st

def main():
    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .main-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
            background-color: #f0f0f0;
        }
        .header {
            font-size: 36px;
            font-weight: bold;
            color: #4CAF50;
            margin-bottom: 20px;
        }
        .description {
            font-size: 18px;
            color: #333;
            margin-bottom: 30px;
            text-align: center;
        }
        .video-container {
            width: 80%;
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Main container with styling
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    # Custom header
    st.markdown('<div class="header">Creative Video Showcase</div>', unsafe_allow_html=True)

    # Description
    st.markdown('<div class="description">Welcome to our creative video showcase. Choose a video and enjoy!</div>', unsafe_allow_html=True)

    # Video options
    video_options = {
        "Video 1": "https://youtu.be/1fzGzhcoks0?si=3ZUAVmtjCUcLDgWf",
        "Video 2": "https://youtu.be/RHigHuA4J98?si=QOFBs1Gux7W03o5s",
        "Video 3": "https://youtu.be/LFcXFF4rI5o?si=35tMySCH7Lm6YDfV",
    }

    # User selects a video
    selected_video = st.selectbox("Select a video", list(video_options.keys()))

    # Display the selected video using st.video
    st.video(video_options[selected_video], format="video/mp4", start_time=0)

    # End main container
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
