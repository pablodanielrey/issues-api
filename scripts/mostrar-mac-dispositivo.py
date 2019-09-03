"""
    https://python-redmine.com/installation.html
"""


if __name__ == '__main__':

    import os
    KEY = os.environ.get('KEY')

    from redminelib import Redmine

    print('ingresando a redmine usando {}'.format(KEY))
    redmine = Redmine('https://pedidos.econo.unlp.edu.ar', key=KEY)
    
    dispositivo = redmine.issue.get(8049)
    print(f"{dispositivo.tracker.name} #{dispositivo.id} {dispositivo.subject}")
    if not dispositivo.custom_fields.get(11).value.strip():
        print(f"{dispositivo.custom_fields.get(11).name}: no establecido")
    else:
        print(f"{dispositivo.custom_fields.get(11).name}: {dispositivo.custom_fields.get(11).value}") 
    if not dispositivo.custom_fields.get(12).value.strip():
        print(f"{dispositivo.custom_fields.get(12).name}: no establecido")
    else:
        print(f"{dispositivo.custom_fields.get(12).name}: {dispositivo.custom_fields.get(12).value}")