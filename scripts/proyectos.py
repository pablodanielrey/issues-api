
if __name__ == '__main__':
    from redminelib import Redmine
    redmine = Redmine('https://pedidos.econo.unlp.edu.ar', key='asdsdsad')
    for p in redmine.project.all():
        print(p)
