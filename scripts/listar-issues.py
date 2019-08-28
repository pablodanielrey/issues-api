"""
    https://python-redmine.com/installation.html
"""


if __name__ == '__main__':

    import os
    KEY = os.environ.get('KEY')

    from redminelib import Redmine
    print('ingresando a redmine usando {}'.format(KEY))
    redmine = Redmine('https://pedidos.econo.unlp.edu.ar', key=KEY)

    for pedido in redmine.issue.all():
        print(dir(pedido))
        #print(f"Id: {u.id}, Nombre: {u.firstname} {u.lastname}, Usuario: {u.login}")
