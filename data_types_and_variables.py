# You have rented some movies for your kids: The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

rental_fee = 3 
little_mermaid_days = 3
brother_bear_days = 5
hercules_days = 1

print ("The rental fee for all movies are",(rental_fee * (little_mermaid_days + brother_bear_days + hercules_days)),"dollars.")


# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
# they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

google = 400
amazon = 380
facebook = 350
g_hr = 6
a_hr = 4
fb_hr = 10

print ("The payment received for this weeks work was",(google * g_hr)+(amazon *a_hr)+(facebook * fb_hr),"dollars.")


# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

class_full = False
class_open = True
class_schdl = True
curr_schdl = class_schdl and class_open

print ("Student is able to enroll in class =",curr_schdl)


# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.

apply_offer_if_over_two_items = True
offer_not_expired = True
offer_expired = False
prem_member = True
non_member = False
apply_offer = (apply_offer_if_over_two_items or prem_member) and offer_not_expired

print (apply_offer)


# Create a variable that holds a boolean value for each of the following conditions:
# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace

username = 'codeup'
password = 'notastrongpassword'

password_min_5_char = len(password) >= 5
username_max_20_char = len(username) <= 20
pw_not_same_as_un = username != password
password_no_whitespaces = password == password.strip()
username_no_whitespaces = username == username.strip()
good_username_and_password = (password_min_5_char 
    and username_max_20_char
    and pw_not_same_as_un 
    and password_no_whitespaces 
    and username_no_whitespaces)
    
print (good_username_and_password)