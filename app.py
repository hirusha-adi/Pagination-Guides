
from flask import redirect, render_template, Flask, url_for
from flask_paginate import Pagination

app = Flask(__name__)


@app.route("/test")
@app.route("/test/")
def current_function_name_no_args():
    # Return with default `page` as `1` if no `page` is given
    return redirect(url_for('current_function_name', page=1))


@app.route("/test/<page>")
def current_function_name(page):
    # Current Page
    current_page = int(page)

    # a list
    list_all = [i for i in range(10)]

    # Length of the list
    list_length = len(list_all)

    # Elements Per Page
    per_page = 3

    # Possible Maximum Page
    max_possible_page = (list_length // per_page)+1

    # Default to max value if a larger is entered
    if current_page > max_possible_page:
        current_page = max_possible_page

    # Instantating `flask_paginate.Pagination`
    pagination = Pagination(
        per_page=per_page,
        page=current_page,
        total=list_length,
        href=str(url_for('current_function_name', page=1))[:-1] + "{0}"

    )

    min_index = (current_page*per_page) - \
        per_page  # Index to start with per page
    max_index = (min_index + per_page)  # Index to end the page

    # Slicing the list with min index and max index per page
    final_list = list_all[min_index:max_index]

    return render_template(
        "index.html",
        pagination=pagination,
        final_list=final_list
    )


if __name__ == "__main__":
    app.run("0.0.0.0", port=8080, debug=True)
