from distutils.command import clean
from email import utils
import json
import time
from urllib import response
import requests
from .utils import ServiceEnums, log_error, log_info, convert_time


class RedditAPI:

    def __init__(self):
        log_info(ServiceEnums.REDDIT, "Initializing reddit API")

        self.url = "https://www.reddit.com/r/yorku/top.json?count=6"
        # Custom cache code
        self.cached_data = []
        self.cache_time = 0
        self.cache_duration = 60 * 60 * 2
        self.cache_time = time.time()

        self.get_data(cache_enabled=False)

        log_info(ServiceEnums.REDDIT, "Initializing reddit API complete")

    def clean_data(self, d):
        """
        This cleans up the data from the reddit API
        """
        fall_back_thumbnail = d.get("thumbnail") if d.get(
            "thumbnail") != "self" else None

        preview = d.get("preview", {}).get("images", [{}])[
            0].get("source", {}).get("url")

        return {
            "title": d.get("title"),
            "description": d.get("selftext") if d.get("selftext") != "" else None,
            "image": preview if preview else fall_back_thumbnail,
            "url": d.get("url"),
            "author": d.get("author"),
            "create_at": convert_time(d.get("created_utc")),
        }

    def get_data_from_api(self):
        """
        This makes requests to the reddit API and caches the data.
        """
        posts = []

        log_info(ServiceEnums.REDDIT, "Getting data from reddit API")

        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        response = requests.get(self.url, timeout=10, headers=header)
        data = response.json()
        # cleaning up the data and adding it to the posts list
        log_info(ServiceEnums.REDDIT, "Cleaning up data from reddit API")
        for post in data.get("data", {}).get("children") or []:
            d = post.get("data")
            clean_data = None
            try:
                clean_data = self.clean_data(d)
            except Exception as e:
                log_error(ServiceEnums.REDDIT, f"Error cleaning data: {e}")

            if clean_data:
                posts.append(clean_data)

        log_info(ServiceEnums.REDDIT,
                 "Cleaning up data from reddit API complete")

        # updating the cache
        self.cached_data = posts
        self.cache_time = time.time()

        return posts

    def get_data(self, cache_enabled=True):
        if cache_enabled and (time.time() - self.cache_time < self.cache_duration) and self.cached_data != []:
            log_info(ServiceEnums.REDDIT, "Using cached data")
            return self.cached_data

        log_info(ServiceEnums.REDDIT, "Getting data from API")
        self.cached_data = self.get_data_from_api()
        self.cache_time = time.time()
        return self.cached_data
