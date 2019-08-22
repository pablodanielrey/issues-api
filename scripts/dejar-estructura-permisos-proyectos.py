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
            p.is_public = False
            if 'parent' not in p._decoded_attrs:
                pass
            else:
                p.inherit_members = True
            p.save()
        except Exception as a:
            print(p)
            print(a)