# Center the title-cased string within a width of 60 using * as the fill character.

string_1 = "Fill This."
result_1 = string_1.center(60 , "*")
print(result_1)


#################################################################

# Right justify the title-cased string within a width of 50 using - as the fill character.

string_2 = "Docker is super."
result_2 = string_2.rjust(50, "-")
print(result_2)

#################################################################

# Left justify the title-cased string within a width of 50 using # as the fill character.

string_3 = "Docker is great."
result_3 = string_3.ljust(50, "#")
print(result_3)