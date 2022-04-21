# Copyright 2022
# author Manoj Jawalkar


from flask import Blueprint, render_template, request
from ipaddress import IPv4Network, AddressValueError, NetmaskValueError
from qpylib import qpylib

# pylint: disable=invalid-name
viewsbp = Blueprint('views', __name__, url_prefix='/')

@viewsbp.route('/network_search', methods=['GET','POST'])
def network_search():
    base_url = qpylib.get_app_base_url()
    if request.method == 'GET':
        return render_template("network_search.html", base_url=base_url)
    else:
        base_url = qpylib.get_app_base_url()
        found = []
        ip = request.form["ip"]
        try:
            target_net = IPv4Network(ip)
        except (AddressValueError, NetmaskValueError, ValueError) as e:
            return render_template("network_search.html", base_url=base_url, ip_addr_exception=e)
        qpylib.log("target_net =" + str(target_net))
        networks = qpylib.REST('get', '/api/config/network_hierarchy/networks')
        for network in networks.json():
            net_cidr = network['cidr']
            matches_net = IPv4Network(net_cidr)
            if target_net.overlaps(matches_net):
                qpylib.log("Target matched with one of the networks =" + net_cidr)
                found.append(network)
        return render_template("network_search.html", ip=ip, found=found, base_url=base_url)

