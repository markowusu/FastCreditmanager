import os 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'creditmanagement.settings')

# import django and setup()
import django
django.setup()

#  import random, faker, and the models 

import random
from creditApp.models import  User_table
from  faker import Faker # this is a convention

#  instance of faker

fakegen = Faker()

credit= [
        2000,100,5000,450,230,673,333,989,7000,123
    ]

def populate(N=5):
    for counter in range(N):
        fake_email = fakegen.safe_email()
        fake_name = fakegen.first_name()
        fake_num = random.choice(credit)
        
        usr_entry = User_table.objects.get_or_create( username=fake_name, email=fake_email,currentCredit=fake_num)[0]

if __name__ == '__main__':
    print("Populating.../")
    populate(10)
    print("Population Done!")        