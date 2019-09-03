"""
    https://python-redmine.com/installation.html
"""


if __name__ == '__main__':
    import os
    from redminelib import Redmine
    KEY = os.environ.get('KEY')
    print('ingresando a redmine usando {}'.format(KEY))
    redmine = Redmine('https://pedidos.econo.unlp.edu.ar', key=KEY)
    project = redmine.project.get('pcs')
    for iss in project.issues:
        f = list(filter(lambda i: i.name == 'MAC', iss.custom_fields))
        fields = { f.name: f.value if hasattr(f, 'value') and f.value.strip() != '' else None for f in iss.custom_fields}
        print("ID:#{} MAC: {}   IP: {}".format(iss.id, fields['MAC'], fields['IP']))
