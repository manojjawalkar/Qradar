# Copyright 2020 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Blueprint, render_template
from ipaddress import IPv4Network
import json
from qpylib import qpylib

# pylint: disable=invalid-name
viewsbp = Blueprint('views', __name__, url_prefix='/')


# An endpoint that populates a dropdown with Ariel database names using REST api call.
@viewsbp.route('/getArielDBList')
def get_ariel_databases():
    try:
        ariel_databases = qpylib.REST('get', '/api/ariel/databases')
        options = {}
        for db_name in ariel_databases.json():
            options[db_name] = db_name
            qpylib.log("Ariel DB name: " + db_name)
        item = {
            'id': 'ArielDBs',
            'title': 'Ariel DB names',
            'HTML': render_template('ariel.html', options=options)
        }
        return json.dumps(item)
    except Exception as ex:
        qpylib.log(
            'Error calling REST api GET /api/ariel/databases: ' + str(ex),
            'ERROR')
        raise

@viewsbp.route('/network_search')
def admin_screen():
    try:
        networks = qpylib.REST('get', '/api/config/network_hierarchy/networks')
        options = {}
        for network in networks.json():
            qpylib.log("Networks ="+ str(network))
            net_name = network['name']
            net_cidr = network['cidr']
            net_group = network['group']

        qpylib.log("Name="+ net_name)
        qpylib.log("cidr="+ net_cidr)
        qpylib.log("group="+ net_group)
        qpylib.log(type(net_name))
        qpylib.log(type(net_cidr))
        qpylib.log(type(net_group))

        y = IPv4Network(net_cidr)
        qpylib.log("--- printing IPv4 addr ---")
        qpylib.log(y)
        z = IPv4Network('0.0.0.14')
        qpylib.log(y.overlaps(z))



        return render_template("network_search.html", title="Admin Me!")
    except Exception as ex:
        qpylib.log("This is an exception"+str(ex),'ERROR')
        raise
