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
        #print(p._decoded_attrs)
        try:
            if 'parent' not in p._decoded_attrs:
                print('obtieniendo los miembros de proyecto: {}'.format(p.name))
                memberships = redmine.project_membership.filter(project_id=p.id)
                for m in memberships:
                    print(m._decoded_attrs)
                    print(m)
            else:
                print('obteniendo los miembros de proyecto: {}'.format(p.name))
                memberships = redmine.project_membership.filter(project_id=p.id)
                for m in memberships:
                    print(m._decoded_attrs)
                    print(m)

        except Exception as a:
            pass