# helper.py mein add karo
import requests
import re
import sys
from urllib.parse import urlparse, parse_qs

def convert_mpd_to_m3u8(mpd_url, quality="720"):
    """
    Convert master.mpd URL to m3u8 URL using vid.py logic
    """
    try:
        parsed_url = urlparse(mpd_url)
        base_url = parsed_url.scheme + "://" + parsed_url.netloc
        path_parts = parsed_url.path.split("/")
        video_id = path_parts[1]
        query_string = parsed_url.query
        
        # Construct m3u8 URL
        m3u8_url = f"{base_url}/{video_id}/hls/{quality}/main.m3u8?{query_string}"
        
        # Download and modify m3u8 content
        response = requests.get(m3u8_url)
        if response.status_code != 200:
            raise Exception(f"Failed to download m3u8 file: {response.status_code}")
        
        content = response.text

        # Replace EXT-X-KEY URI
        new_key_uri = f"{base_url}/{video_id}/hls/enc.key?{query_string}"
        content = re.sub(r'URI=".*?"', f'URI="{new_key_uri}"', content)

        # Replace TS chunk paths
        def replace_ts(match):
            ts_file = match.group(1)
            return f"{base_url}/{video_id}/hls/{quality}/{ts_file}?{query_string}"

        content = re.sub(r'(\d+\.ts)', replace_ts, content)
        
        return content, m3u8_url
        
    except Exception as e:
        raise Exception(f"MPD to M3U8 conversion failed: {str(e)}")