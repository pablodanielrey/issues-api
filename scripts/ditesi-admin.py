"""
    https://python-redmine.com/installation.html
"""

pablo = 8
ema = 5
ditesi = [9,7,200,78,11,14]
jefes = [pablo,ema]


if __name__ == '__main__':
    import os
    from redminelib import Redmine
    KEY = os.environ.get('KEY')
    print(f'ingresando a redmine usando {KEY}')
    redmine = Redmine('https://pedidos.econo.unlp.edu.ar', key=KEY)

    for u in redmine.user.all():
        if u.id in ditesi:
            print(u)
            print(u._decoded_attrs)
            u.admin = False
            u.save()
