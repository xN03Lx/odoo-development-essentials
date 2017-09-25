{ 
    'name': 'To-Do Application', 
    'description': 'Manage your personal To-Do tasks.', 
    'author': 'Noel Toyo', 
    'depends': ['base'], 
    'application': True, 
    'data': [
    		'security/todo_access_rules.xml', 
    		'security/ir.model.access.csv', 
    		'views/todo_menu.xml',
    		'views/todo_view.xml'

    ],
}