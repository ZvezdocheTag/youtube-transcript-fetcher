# YouTube Transcript Fetcher

Fetches transcripts from YouTube videos using [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/).

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install youtube-transcript-api
```

## Usage

Edit `transcript.py` and set your video IDs:

```python
VIDEO_IDS = [
    "dQw4w9WgXcQ",   # the part after ?v= in the YouTube URL
    "another_id",
]
LANGUAGES = ["en"]       # language priority order, e.g. ["en", "de"]
PRINT_TIMESTAMPS = True  # False = plain text only
```

Then run:

```bash
python transcript.py
```

### Output example

```
=== dQw4w9WgXcQ ===
[00:13] Never gonna give you up
[00:15] Never gonna let you down
...
```

Each entry has three fields you can use in code:

| Field      | Type  | Description                          |
|------------|-------|--------------------------------------|
| `text`     | str   | Transcript line                      |
| `start`    | float | Start time in seconds                |
| `duration` | float | Duration of that line in seconds     |

## Limitations

| Limitation | Detail |
|---|---|
| No API key needed | But YouTube may rate-limit or block IPs that make too many requests |
| Transcripts must exist | The video owner or YouTube must have added captions; auto-generated counts |
| Age-restricted / private videos | Will fail — the library cannot authenticate as a user |
| `TranscriptsDisabled` | Owner explicitly turned off transcripts |
| `NoTranscriptFound` | No transcript exists for the requested language(s) |
| Language codes | Use BCP-47 codes: `en`, `fr`, `de`, `ja`, etc. Pass multiple for fallback order |
| Unofficial API | YouTube does not publish a transcript API; this library reverse-engineers it and may break on YouTube changes |
