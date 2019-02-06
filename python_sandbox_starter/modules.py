# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules
import datetime
import time
import camelcase

import validator

today = datetime.date.today()
print(today)
print(time.time())

camel = camelcase.CamelCase()
print(camel.hump("camelCASE"))

email = "testtest.com"
if validator.validate_email(email):
    print("email is good")
else:
    print("emal is fucked up")