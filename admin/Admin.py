from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink

# models
from model.Role import Role
from model.User import User
from model.Category import Category
from model.Product import Product

# views
from admin.Views import UserView, HomeView

def start_views(app, db):
    admin = Admin(
        app,
        name = 'Meu Estoque',
        template_mode = 'bootstrap3',
        base_template = 'admin/base.html',
        index_view = HomeView()
    )
    

    admin.add_view(
        ModelView(Role, db.session, 'Cargos', category = 'Usuários')
    )
    admin.add_view(
        UserView(User, db.session, 'Usuários', category = 'Usuários')
    )
    admin.add_view(
        ModelView(Category, db.session, 'Categorias', category = 'Produtos')
    )
    admin.add_view(
        ModelView(Product, db.session, 'Produtos', category = 'Produtos')
    )

    admin.add_link(MenuLink(name='Sair', url='/logout'))

    