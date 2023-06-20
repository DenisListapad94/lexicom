INSTALL 
1. Git: https://git-scm.com/downloads
2. Docker: https://www.docker.com/products/docker-desktop/


SETUP

1. Create directory for project $ mkdir my_project
2. Clone this repository into your directory my_project $ git clone  https://github.com/DenisListapad94/lexicom.git
3. Run docker on your computer
4. Create docker compose image $ docker compose build
5. Run docker compose container $ docker compose up

SQL 

Solving second tasks using postgresql. Both solutions are provided with a subquery and different postgresql functions

UPDATE full_names
SET status = (
	SELECT status 
	FROM short_names 
	WHERE short_names.name = split_part(full_names.name, '.', 1));


UPDATE full_names
SET status = (
  SELECT status
  FROM short_names
  WHERE regexp_count(full_names.name,  short_names.name,1) = 1
);