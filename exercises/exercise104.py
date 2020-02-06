# check for rating for this movie:
  ## universal -> everyone can watch
  ## pg --> General viewing, but some scenes may be unsuitable for young children
  ## 12 -->  Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.
  ## 15 --> No one younger than 15 may see a 15 film in a cinema.
  ## 18 --> No one younger than 18 may see an 18 film in a cinema.

age = input('How old are you?    ').strip()
int_age = int(age)
with_adult = input('You are with someone older than 18. True or False   ').strip().capitalize()


# if int_age < 12 and with_adult == False:
#     print("You can only watch U and PG movies")
if int_age < 12 and eval(with_adult) == True:
    print("You can watch U, PG and 12A movies")
elif 15 > int_age >= 12:
    print("You can watch U, PG and 12A movies")
elif 18 > int_age >= 15:
    (print("You can watch U, PG, 12A and 15 movies"))
elif int_age >= 18:
    print("You can watch any movie")
else:
    print("You can watch only U and PG movies")