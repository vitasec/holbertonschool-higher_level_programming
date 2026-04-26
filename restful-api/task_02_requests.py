#!/usr/bin/python3

import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    r = requests.get(URL)
    print(f"Status Code: {r.status_code}")
    posts = r.json()
    for post in posts:
        print(post["title"])


def fetch_and_save_posts():
    r = requests.get(URL)
    if r.status_code == 200:
        posts = r.json()
        
        sturctured_posts = [
            {
                 "id": post.get("id"),
                 "title": post.get("title"),
                 "body": post.get("body"),
             }
            for post in posts
        ]

        with open("posts.csv", "w", newline="") as f:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(f, fieldnames)

            writer.writeheader()
            writer.writerows(sturctured_posts)
    else:
        print("failed")
