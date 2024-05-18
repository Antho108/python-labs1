# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"




# def censor(my_func): 
#     def new_wraper(msg): 
#         initial_result = my_func(msg)
#         removal_list = ["Shoot!", "fuck", "tg"]
       
#         for word in removal_list:
#             initial_result = initial_result.replace(word, "S****!")
    
#         return initial_result
#     return new_wraper


# @censor
# def sentence(msg): 
#     return msg 

# print(sentence("I bumped my toe! Shoot! tg fuck "))



## New Wrapper 


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