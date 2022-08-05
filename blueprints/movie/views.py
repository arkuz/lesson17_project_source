import logging
from flask import Blueprint

logger = logging.getLogger(__name__)
movie_blueprint = Blueprint('movie_blueprint', __name__)
