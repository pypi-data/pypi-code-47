import requests
from .start_up import URLS, AUTH


async def check_response(resp, topic=None):
    status = resp.status_code
    if status != 200:
        print(f"{topic or ''}request not successful: {status} - {resp.reason}")
    return resp


async def get_blog_posts():
    resp = requests.get(URLS["BLOGS"], headers=AUTH)
    if await check_response(resp, topic="get_blogs"):
        return resp.json()


async def show_blog_posts():
    """
    lists blog posts
    """
    posts = await get_blog_posts()
    print(f"  > showing {len(posts)} blog posts:")
    for blog_post in posts:
        print(f"{blog_post}")


async def post_blog_entry(blog_text):
    resp = requests.post(URLS["BLOGS"], headers=AUTH, json={"text": blog_text})
    if await check_response(resp, topic="post_blog_entry"):
        return resp.json()
