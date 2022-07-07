#!/bin/bash
PROJECT_PATH="$HOME/base/dev/clients/arpartners/code"
VENV_NAME="venv_arpartners"
DJANGO_DIR="django_arpartners"

guake -r "runserver" -e "cd $PROJECT_PATH/$DJANGO_DIR"
guake -e "source $PROJECT_PATH/$VENV_NAME/bin/activate"
guake -e "clear"
guake -e "python manage.py runserver localhost:8080"

guake -n "node-sass" -r "node-sass" -e "cd $PROJECT_PATH"
guake -e "npm run dev"

guake -n "heroku" -r "heroku" -e "cd $PROJECT_PATH"
guake -e "source $PROJECT_PATH/$VENV_NAME/bin/activate"
guake -e "clear"

guake -n "bash" -r "bash" -e "cd $PROJECT_PATH"
guake -e "source $PROJECT_PATH/$VENV_NAME/bin/activate"
guake -e "clear"

guake -s 0

# execute a command
# -e "some command" 

# rename current shell
# -r "shell name" 

# create a new shell-tab
# -n "arbitray name" 

# select shell number
# -s INTEGER

