import environ

root = environ.Path(__file__) - 2 # two folder back (/a/b/ - 2 = /)
env = environ.Env(DEBUG=(bool, False),) # set default values and casting
environ.Env.read_env() # reading .env file
