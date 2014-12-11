#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint

detail_blueprint = Blueprint('detail', __name__, template_folder='templates')

@detail_blueprint.route('/detail')
def detail():
    return 'detail'
        
