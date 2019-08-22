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
            memberships = redmine.project_membership.filter(project_id=p.id)
            for m in memberships:
                print(m._decoded_attrs)
                print(m)
                m.delete()

        except Exception as a:
            pass