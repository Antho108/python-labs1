# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".


def mot_offensant(mots_interdits): 
    def decorators_bg(initial_func):
        def wrap_toto(*args): 
             initial_result = initial_func(*args)
             for word in mots_interdits:
                 initial_result = initial_result.replace(word, '*' * len(word))
             return initial_result
        return wrap_toto
    return decorators_bg





@mot_offensant(['Shoot', 'Crazy'])
def new_msg(msg): 
    return msg 


print(new_msg("salut et si on Shoot! "))