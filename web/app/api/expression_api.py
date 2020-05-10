import logging
import os

from flask import (
    current_app,
    flash,
    jsonify,
    render_template,
    request
)
from werkzeug.utils import secure_filename
from user_agents import parse
from flask_jwt_extended import jwt_optional, get_jwt_identity
from flask_limiter.util import get_remote_address

from web.app.services.api_wolfram.waAPI import compute_expression
from web.app.services.parser.const import asciimath_grammar
from web.app.services.parser.parser import ASCIIMath2Tex
from web.app import limiter, LIMIT

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)

@jwt_optional
@limiter.limit(LIMIT, exempt_when=lambda: get_jwt_identity() != None)
def submit_expression():
    logging.info("Identita': " + str(get_jwt_identity()) + " da IP: " + str(get_remote_address()))
    user_agent = parse(request.headers.get('User-Agent'))
    if(user_agent.is_pc):
        try:
            logging.info("Requests from Desktop")
            expression = request.form["symbolic_expression"]
            parsed = parse_2_latex(expression)
            response_obj = compute_expression(parsed)    
            return render_template(
                "show_results.html",
                query=expression,
                response_obj=response_obj
            )
        except Exception as e: 
            logging.info(e)
            return render_template(
                'math.html',
                alert=True,
                error='something goes wrong'
            )
    else:
        logging.info("Request from mobile")
        _json = request.get_json()
        expression = _json["symbolic_expression"]
        logging.info("Expression = " + expression)
        parsed = parse_2_latex(expression)
        response_obj = compute_expression(parsed).to_json()
        return jsonify({"results" : response_obj})

def parse_2_latex(expression):
    parser = ASCIIMath2Tex(
        asciimath_grammar, inplace=True, parser="lalr", lexer="contextual"
    )
    return parser.asciimath2tex(expression)

@jwt_optional
@limiter.limit(LIMIT, exempt_when=lambda: get_jwt_identity() != None)
def send_file():
    fileob = request.files["file2upload"]
    filename = secure_filename(fileob.filename)
    save_path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
    logging.info("Save path is = " + save_path)
    fileob.save(save_path)
    # open and close to update the access time.
    with open(save_path, "r") as f:
        pass
    flash("File uploaded succesfully!")
    return "200"


# GET NAMES OF UPLOADED FILES
@limiter.exempt
def get_filenames():
    logging.info("Current working location is = " + os.getcwd())

    filenames = os.listdir(current_app.config["UPLOAD_FOLDER"])

    def modify_time_sort(file_name):
        file_path = os.path.join(
            current_app.config["UPLOAD_FOLDER"], file_name
        )
        file_stats = os.stat(file_path)
        last_access_time = file_stats.st_atime
        return last_access_time

    filenames = sorted(filenames, key=modify_time_sort)
    return_dict = dict(filenames=filenames)
    return jsonify(return_dict)
