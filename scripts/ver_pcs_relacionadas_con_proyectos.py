
import os
import redminelib

KEY=os.environ.get('KEY')
r = redminelib.Redmine('https://pedidos.econo.unlp.edu.ar', key=KEY)

r.project()