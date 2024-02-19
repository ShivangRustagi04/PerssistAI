import streamlit as st
from streamlit_player import st_player

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
        'video_path1': "C:\\Users\\shiva\\OneDrive\\Desktop\\ShivangRustagi_Submission\\sample 1.mp4",
        'video_path2': "C:\\Users\\shiva\\OneDrive\\Desktop\\ShivangRustagi_Submission\\sample 2.mp4",
        'video_path3': "C:\\Users\\shiva\\OneDrive\\Desktop\\ShivangRustagi_Submission\\sample 3.mp4",
    }

    # Use st_player for each video
    player1 = st_player(video_options['video_path1'])
    player2 = st_player(video_options['video_path2'])
    player3 = st_player(video_options['video_path3'])

    # Display video players
    st.write(player1)
    st.write(player2)
    st.write(player3)

    # User selects a video
    selected_video = st.selectbox("Select a video", list(video_options.keys()))

    # Display the selected video using iframe
    video_embed_code = f'<iframe src="{video_options[selected_video]}" width="100%" height="500" frameborder="0" allowfullscreen></iframe>'
    st.markdown(f'<div class="video-container">{video_embed_code}</div>', unsafe_allow_html=True)

    # End main container
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
