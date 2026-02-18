import requests
import csv


def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()

        file = open("posts.csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(file)

        writer.writerow(["id", "title", "body"])

        for post in posts:
            writer.writerow([post["id"], post["title"], post["body"]])

        file.close()
