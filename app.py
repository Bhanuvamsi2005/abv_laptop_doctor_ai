# # #
# # #
# # # from flask import Flask, render_template, request, session, redirect, url_for
# # # from nlp.nlp_processor import extract_issue
# # # from rag.rag_engine import generate_solution
# # #
# # # app = Flask(__name__)
# # # app.secret_key = "hackathon_secret_key"
# # #
# # #
# # # @app.route("/", methods=["GET", "POST"])
# # # def index():
# # #     if "chat_history" not in session:
# # #         session["chat_history"] = []
# # #
# # #     if "last_issue" not in session:
# # #         session["last_issue"] = None
# # #
# # #     if request.method == "POST":
# # #         user_message = request.form["message"]
# # #
# # #         structured_issue = extract_issue(user_message)
# # #
# # #         bot_response, detected_issue = generate_solution(
# # #             company="Unknown",
# # #             model="Unknown",
# # #             user_problem=user_message,
# # #             structured_issue=structured_issue,
# # #             last_issue=session["last_issue"]
# # #         )
# # #
# # #         session["last_issue"] = detected_issue
# # #
# # #         session["chat_history"].append({
# # #             "user": user_message,
# # #             "bot": bot_response
# # #         })
# # #
# # #         session.modified = True
# # #
# # #     return render_template(
# # #         "index.html",
# # #         chat_history=session["chat_history"]
# # #     )
# # #
# # #
# # # # ✅ CLEAR HISTORY ROUTE
# # # @app.route("/clear")
# # # def clear_chat():
# # #     session["chat_history"] = []
# # #     session["last_issue"] = None
# # #     session.modified = True
# # #
# # #     return redirect(url_for("index"))
# # #
# # #
# # # if __name__ == "__main__":
# # #     app.run(debug=True)
# #
# # from flask import Flask, render_template, request, session, redirect
# # from nlp.nlp_processor import extract_issue
# # from rag.rag_engine import generate_solution
# # from database import init_db, save_feedback
# #
# # app = Flask(__name__)
# # app.secret_key = "hackathon_secret_key"
# #
# #
# # @app.route("/", methods=["GET", "POST"])
# # def index():
# #
# #     if "chat_history" not in session:
# #         session["chat_history"] = []
# #
# #     if request.method == "POST":
# #         user_message = request.form["message"]
# #
# #         structured_issue = extract_issue(user_message)
# #
# #         bot_response, detected_issue = generate_solution(
# #             company="Unknown",
# #             model="Unknown",
# #             user_problem=user_message,
# #             structured_issue=structured_issue
# #         )
# #
# #         session["chat_history"].append({
# #             "user": user_message,
# #             "bot": bot_response
# #         })
# #
# #         session.modified = True
# #
# #     return render_template("index.html", chat_history=session["chat_history"])
# #
# #
# # # ✅ Feedback Form Submission 🚀🔥
# # @app.route("/submit_feedback", methods=["POST"])
# # def submit_feedback():
# #     name = request.form["name"]
# #     email = request.form["email"]
# #     feedback_text = request.form["feedback"]
# #
# #     save_feedback(name, email, feedback_text)
# #
# #     return redirect("/")
# #
# #
# # # ✅ Clear Chat
# # @app.route("/clear")
# # def clear():
# #     session.clear()
# #     return redirect("/")
# #
# #
# # if __name__ == "__main__":
# #     init_db()
# #     app.run(debug=True)
#
# from flask import Flask, render_template, request, session, redirect
# from nlp.nlp_processor import extract_issue
# from rag.rag_engine import generate_solution
# from database import init_db, save_feedback, save_chat, load_chat_history
#
# app = Flask(__name__)
# app.secret_key = "hackathon_secret_key"
#
#
# @app.route("/", methods=["GET", "POST"])
# def index():
#
#     if "chat_history" not in session:
#         session["chat_history"] = []
#
#     if request.method == "POST":
#         user_message = request.form["message"]
#
#         structured_issue = extract_issue(user_message)
#
#         bot_response, detected_issue = generate_solution(
#             company="Unknown",
#             model="Unknown",
#             user_problem=user_message,
#             structured_issue=structured_issue
#         )
#
#         session["chat_history"].append({
#             "user": user_message,
#             "bot": bot_response
#         })
#
#         # ✅ SAVE TO DATABASE 🚀🔥
#         save_chat(user_message, bot_response)
#
#         session.modified = True
#
#     return render_template("index.html", chat_history=session["chat_history"])
#
#
# # ✅ SEE HISTORY SCREEN 🚀🔥🔥🔥
# @app.route("/history")
# def history():
#
#     chats = load_chat_history()
#
#     formatted = []
#
#     for chat in chats:
#         formatted.append({
#             "user": chat[0],
#             "bot": chat[1]
#         })
#
#     return render_template("history.html", chats=formatted)
#
#
# @app.route("/submit_feedback", methods=["POST"])
# def submit_feedback():
#     name = request.form["name"]
#     email = request.form["email"]
#     feedback_text = request.form["feedback"]
#
#     save_feedback(name, email, feedback_text)
#
#     return redirect("/")
#
#
# @app.route("/clear")
# def clear():
#     session.clear()
#     return redirect("/")
#
#
# if __name__ == "__main__":
#     init_db()
#     app.run(debug=True)

import re
from flask import Flask, render_template, request, session, redirect
from nlp.nlp_processor import extract_issue
from rag.rag_engine import generate_solution
from database import *

app = Flask(__name__)
app.secret_key = "hackathon_secret_key"


def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


@app.route("/second")
def home():
    if "user" not in session:
        return redirect("/signin")
    return redirect("/chat")
@app.route("/")
def pre_home():
    return render_template("pre_home.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if not is_valid_email(email):
            return render_template("signup.html", error="Invalid Email")

        if password != confirm_password:
            return render_template("signup.html", error="Passwords Do Not Match")

        if create_user(name, email, password):
            return redirect("/signin")
        else:
            return render_template("signup.html", error="Email Already Exists")

    return render_template("signup.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if validate_user(email, password):
            session["user"] = email
            return redirect("/chat")

        return render_template("signin.html", error="Invalid Credentials")

    return render_template("signin.html")


@app.route("/chat", methods=["GET", "POST"])
def chat():

    if "user" not in session:
        return redirect("/signin")

    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":
        user_message = request.form.get("message")

        structured_issue = extract_issue(user_message)

        bot_response, detected_issue = generate_solution(
            company="Unknown",
            model="Unknown",
            user_problem=user_message,
            structured_issue=structured_issue
        )

        session["chat_history"].append({
            "user": user_message,
            "bot": bot_response
        })

        save_chat(session["user"], user_message, bot_response)

    return render_template("index.html", chat_history=session["chat_history"])


@app.route("/history")
def history():

    if "user" not in session:
        return redirect("/signin")

    chats = load_chat_history(session["user"])
    formatted = [{"user": c[0], "bot": c[1]} for c in chats]

    return render_template("history.html", chats=formatted)


@app.route("/submit_feedback", methods=["POST"])
def submit_feedback():
    save_feedback(
        request.form["name"],
        request.form["email"],
        request.form["feedback"]
    )
    return redirect("/chat")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/signin")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)