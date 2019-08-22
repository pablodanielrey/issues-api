"""
    https://python-redmine.com/installation.html
"""


if __name__ == '__main__':
    import os
    from redminelib import Redmine
    KEY = os.environ.get('KEY')
    print(f'ingresando a redmine usando {KEY}')
    redmine = Redmine('https://pedidos.econo.unlp.edu.ar', key=KEY)
    for p in redmine.project.all():
        print(p)
