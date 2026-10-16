"""
Fetch transcripts from YouTube videos.
Usage: python transcript.py
"""

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

# --- Configure here ---
VIDEO_IDS = [
    # "dQw4w9WgXcQ",  # replace with your video ID(s)
    "LvalonIuyjg"
]
LANGUAGES = ["fr"]          # preferred language codes, in priority order
# LANGUAGES = ["en"]          # preferred language codes, in priority order
PRINT_TIMESTAMPS = True     # set False to print plain text only
# ----------------------


def fetch(video_id: str) -> list[dict]:
    """Return transcript entries for a single video ID."""
    api = YouTubeTranscriptApi()
    return list(api.fetch(video_id, languages=LANGUAGES))


def format_entry(entry, timestamps: bool) -> str:
    text = entry.text.strip()
    if timestamps:
        start = entry.start
        m, s = divmod(int(start), 60)
        h, m = divmod(m, 60)
        ts = f"[{h:02d}:{m:02d}:{s:02d}]" if h else f"[{m:02d}:{s:02d}]"
        return f"{ts} {text}"
    return text


def main():
    for video_id in VIDEO_IDS:
        print(f"\n=== {video_id} ===")
        try:
            entries = fetch(video_id)
            for entry in entries:
                print(format_entry(entry, PRINT_TIMESTAMPS))
        except TranscriptsDisabled:
            print("  ERROR: transcripts are disabled for this video.")
        except NoTranscriptFound:
            print(f"  ERROR: no transcript found for languages {LANGUAGES}.")
        except Exception as e:
            print(f"  ERROR: {e}")


if __name__ == "__main__":
    main()
