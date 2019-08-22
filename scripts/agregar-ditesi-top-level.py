"""
    https://python-redmine.com/installation.html
"""

pablo = 8
ema = 5
ditesi = [9,7,200,78,11,14]
jefes = [pablo,ema]

rjefe = 3
rsoporte = 7


if __name__ == '__main__':
    import os
    from redminelib import Redmine
    KEY = os.environ.get('KEY')
    print(f'ingresando a redmine usando {KEY}')
    redmine = Redmine('https://pedidos.econo.unlp.edu.ar', key=KEY)

    for p in redmine.project.all(includes=['parent']):
        #print(p._decoded_attrs)
        try:
            if 'parent' not in p._decoded_attrs:
                ''' esto es un toplevel proyect '''
                for uid in ditesi:
                    redmine.project_membership.create(project_id=p.id, user_id=uid, role_ids=[rsoporte])
                for uid in jefes:
                    redmine.project_membership.create(project_id=p.id, user_id=uid, role_ids=[rjefe])

        except Exception as a:
            print(a)