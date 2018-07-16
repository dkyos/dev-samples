#!/usr/bin/env python

import airflow
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser
user = PasswordUser(models.User())
user.username = 'admin'
user.email = 'dkyun77@gmail.com'
user._set_password = 'password'
session = settings.Session()
session.add(user)
session.commit()
session.close()
exit()
