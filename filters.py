from flask import Blueprint
import jinja2
from datetime import datetime

blueprint = Blueprint('filters', __name__)

@jinja2.contextfilter
@blueprint.app_template_filter()
def get_time(_, epoch):
    epoch = long(epoch)
    dt = datetime.fromtimestamp(epoch/1e3)
    readable_time = dt.strftime('%B %d, %Y %I:%M%p')
    return readable_time