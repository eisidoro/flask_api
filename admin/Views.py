from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView

from config import app_config, app_active

config = app_config[app_active]

class HomeView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render(
            'home_admin.html',
            data = {
                'username': 'Eduardo Isidoro'
            }
        )

class UserView(ModelView):
    column_exclude_list = ['password', 'recovery_code']
    form_excluded_columns = ['last_update', 'recovery_code']
    form_widget_args = {
        'password': {
            'type': 'password'
        }
    }
    can_set_page_size = True
    can_view_details = True
    column_searchable_list = ['username', 'email']
    column_filters = ['username', 'email', 'funcao']
    export_types = ['json', 'yaml', 'csv', 'xls', 'df']
    create_modal = True
    edit_modal = True

    column_labels = {
        'funcao': 'Função',
        'username': 'Nome de usuário',
        'email': 'E-mail',
        'date_created': 'Data de criação',
        'last_update': 'Última atualização',
        'active': 'Ativo',
        'password': 'Senha',
    }

    column_descriptions = {
        'funcao': 'Função no painel administrativo',
        'username': 'Nome de usuário no sistema',
        'email': 'E-mail do usuário no sistema',
        'date_created': 'Data de criação do usuário no sistema',
        'last_update': 'Última atualização desse usuário no sistema',
        'active': 'Estado ativo ou inativo no sistema',
        'password': 'Senha do usuário no sistema',
    }

    def on_model_change(self, form, User, is_created):
        if 'password' in form:
            if form.password.data is not None:
                User.set_password(form.password.data)
            else:
                del form.password