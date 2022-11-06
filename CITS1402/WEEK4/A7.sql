SELECT titles.title, people.name  FROM titles, people, ratings, castmembers WHERE (titles.title_id=ratings.title_id AND ratings.rating>= 9) AND castmembers.title_id=titles.title_id AND castmembers.person_id = people.person_id;