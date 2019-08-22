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
        try:
            if p.parent is None:
                print(f'obtieniendo los miembros de proyecto: {p.id}')
                memberships = redmine.project_membership.filter(project_id=p.id)
                for m in memberships:
                    print(m)
        except Exception as a:
            pass