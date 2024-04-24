from flask import Blueprint, render_template

cliente_route = Blueprint("cliente", __name__)


@cliente_route.route("/")
def lista_clientes():
    """listar os clientes"""
    return render_template("lista_clientes.html")


@cliente_route.route("/teste")
def lista_teste1():
    """listar os clientes"""
    return render_template("/teste/teste1.html")
