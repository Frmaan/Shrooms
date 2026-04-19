import json
import os
import random

from flask import Blueprint, render_template, request

bp = Blueprint("main", __name__, static_folder="static")


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/quiz", methods=["GET", "POST"])
def quiz():
    json_path = os.path.join(bp.static_folder, "data", "mushrooms.json")
    with open(json_path, "r") as f:
        mushrooms = json.load(f)

    mushroom = random.choice(mushrooms)
    correct_name = mushroom["common_name"]

    all_names = [m["common_name"] for m in mushrooms]
    wrong_name = random.choice([n for n in all_names if n != correct_name])
    options = [correct_name, wrong_name]
    random.shuffle(options)

    is_correct = None

    if request.method == "POST":
        user_answer = request.form["answer"]
        is_correct = user_answer == correct_name

    return render_template(
        "quiz.html", mushroom=mushroom, options=options, is_correct=is_correct
    )
