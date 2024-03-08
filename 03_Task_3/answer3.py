query_1 = """create table readers
(id serial primary key,
 name varchar(60),
 email varchar(60) unique,
 is_active boolean not null default True);"""

query_2 = """create table publishinghouses
(id serial primary key,
name varchar(60),
city varchar(20),
address varchar(120)
);"""

query_3 = """create table books(
    id serial primary key,
    title varchar(60),
    price decimal(5, 2),
    author varchar(60),
    publishing_house_id int references publishinghouses(id) on delete cascade
);"""

query_4 = """create table readersbooks (
    id serial primary key,
    reader_id int references readers(id) on delete cascade,
    book_id int references books(id) on delete cascade);
"""

## alternativne
query_4 = """create table readersbooks (
    reader_id int references readers(id) on delete cascade,
    book_id int references books(id) on delete cascade);
    primary_key (reader_id, book_id)
"""

query_5 = """select * from books where price > 10;"""

query_6 = """insert into publishinghouses 
(name, city, address) values
    ('Super Books', 'Wilderness', '120 Main Road.');
"""

query_7 = """delete from books where id = 12;"""

query_8 = """select * from readers left join readersbooks on readers.id = readersbooks.readers_id;"""

query_9 = """update readers set is_active = False where id = 2;"""

query_10 = """alter table readers add column date_of_birth date;"""
