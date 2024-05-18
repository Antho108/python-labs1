# Create a virtual environment and edit the activation script to add
# the following information:
# 
# - ENVIRONMENT="development"
# - SECRET="i ate your sweets"
# 
# Then write the necessary code to access and print the values of these
# two environment variables in this script.

# ENVIRONMENT="development"
# SECRET="i ate your sweets"


# export ENVIRONMENT="development"
# export SECRET="i ate your sweets"

# deactivate () {
#     unset SECRET
#     unset ENVIRONNMENT        
#     # Lots of other code
# }

import os



secret = os.environ['MY_SUPER_SECRET_SECRET']
print(secret)

print(os.environ)


# Returns `None` if key doesn't exist
print(os.environ.get('KEY_THAT_MIGHT_EXIST'))

# Returns `default_value` if key doesn't exist
print(os.environ.get('KEY_THAT_MIGHT_EXIST', default_value))

# Returns `default_value` if key doesn't exist
print(os.getenv('KEY_THAT_MIGHT_EXIST', default_value))