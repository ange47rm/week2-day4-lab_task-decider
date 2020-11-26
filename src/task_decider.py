def get_preffered_option(task_1, task_2):
    if task_1.description == 'Wash the dishes' and task_2.description  == 'Cook the dinner':
        return task_1.description
    elif task_2.description == 'Wash the dishes' and task_1.description  == 'Cook the dinner':
        return task_2.description

    elif task_1.description == 'Cook the dinner' and task_2.description == 'Clean the windows':
        return task_1.description
    elif task_2.description == 'Cook the dinner' and task_1.description == 'Clean the windows':
        return task_2.description

    elif  task_1.description == 'Clean the windows' and task_2.description == 'Wash the dishes':
        return task_1.description
    elif  task_2.description == 'Clean the windows' and task_1.description == 'Wash the dishes':
        return task_2.description