##
## Renan DUBOIS, 2022
## MAKEFILE
## File description:
## Makefile for a test task
## For the Veeam company
##

SRC =  	main.py

NAME = main

all: $(NAME)

$(NAME):
	cp $(SRC) $(NAME) 
	chmod 777 $(NAME)

clean:
	rm -rf;

fclean: clean;
	rm -rf $(NAME);

re: fclean
	@make $(NAME) --no-print-directory

.PHONY: all clean
