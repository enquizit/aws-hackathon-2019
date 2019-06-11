from sls_forum.model.model import User, Post, Comment, Author
import random
import string


def rnd_str(n):
    return "".join([random.choice(string.ascii_letters) for _ in range(n)])


username_list = [
    "Sam",
    "Mercy",
    "Mouse",
    "Rita",
    "Shobila",
    "John",
    "Doe",
    "Bill",
    "Eliza",
    "Karre",
    "Doyle",
]

user_list = [
    User(username=username, email=username + "@email.com", password_digest=rnd_str(12))
    for username in username_list
]
user_list.append(User(_id="7d4da959-2310-40c1-8d62-56163ec67adb", username="Alice", email="alice@email.com", password_digest=rnd_str(12)))

User.smart_insert(user_list)

title_list = [
    "Using ruby-saml without Rails",
    "Open VSTO oulook add-in Persistent data using Office add-in Javascript API (office.js)",
    "How to fix my jquery ajax login form that keeps redirecting to the action page?",
    "How do I average by specific columns",
    "Is there a way to configure an EKS service to use HTTPS?",
    "The problem with CORS headers for the server on Go",
    "Here is the config for our current EKS service",
]

post_list = list()
for title in title_list:
    user = random.choice(user_list)
    post = Post(
        title=title, content="Hello AWS Hackathon",
        author=Author(
            _id=user._id,
            username=user.username
        )
    )
    post_list.append(post)

Post.smart_insert(post_list)