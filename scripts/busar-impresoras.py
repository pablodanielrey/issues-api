"""
    https://python-redmine.com/installation.html
"""


if __name__ == '__main__':
    import os
    from redminelib import Redmine
    KEY = os.environ.get('KEY')
    print('ingresando a redmine usando {}'.format(KEY))
    redmine = Redmine('https://pedidos.econo.unlp.edu.ar', key=KEY)

    for p in redmine.project.all(includes=['parent']):
        if 'mpr' in p.name:
            print(p.id)
            print(p)