import streamlit as st
import requests

# Last.fm API Key
LASTFM_API_KEY = "dc42360d4141ba47bc72f36fcddc1a2b"

# Function to fetch tracks based on tags (moods/genres)
def get_lastfm_tracks(tag, limit=10):
    url = f"http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag={tag}&limit={limit}&api_key={LASTFM_API_KEY}&format=json"
    response = requests.get(url)
    data = response.json()
    if "tracks" in data and "track" in data["tracks"]:
        return [
            {
                "title": track["name"],
                "artist": track["artist"]["name"],
                "url": track["url"]
            }
            for track in data["tracks"]["track"]
        ]
    else:
        return None

# App title and description
st.title("Mood-Based Music Recommendation App 🎵")
st.write("Feeling a certain way? Let me recommend some music to match your mood!")

# Mood-to-Tag mapping
mood_to_tag = {
    "Happy": "happy",
    "Sad": "sad",
    "Energetic": "energetic",
    "Relaxed": "chill",
    "Romantic": "love"
}

# User selects their mood
st.subheader("How are you feeling today?")
mood = st.radio("Select your current mood:", list(mood_to_tag.keys()))

# Show recommendations
if st.button("Get Recommendations"):
    st.subheader(f"🎧 Songs for a {mood} mood:")
    tag = mood_to_tag[mood]
    recommendations = get_lastfm_tracks(tag)
    
    if recommendations:
        for song in recommendations:
            st.write(f"- **{song['title']}** by {song['artist']}")
            st.write(f"  [Listen on Last.fm]({song['url']})")
    else:
        st.write("No songs found for this mood. Try another one!")

# Footer
st.write("---")
st.caption("Made with ❤️ using Streamlit and Last.fm API")
