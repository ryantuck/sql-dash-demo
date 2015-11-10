-- generate some junk tables to mess around with

create table queries_master (
    id integer,
    query text
);

create table puppies (
    id integer,
    name text,
    breed text,
    is_male boolean
);

create table owners (
    id integer,
    name text,
    pet_id integer
);

insert into puppies
    values
    (1, 'ralph', 'corgi', true),
    (2, 'fiona', 'great dane', false),
    (3, 'bro', 'weiner dog', true),
    (4, 'spike', 'actually a cat', false);

insert into owners
    values
    (11, 'jimbo', 2),
    (22, 'kuz', 4),
    (33, 'michael analysis craig', 3),
    (44, 'stephen jobs', 1);

insert into queries_master
    values
    (1, 'select * from puppies'),
    (2, 'select * from owners'),
    (3, 'select * from puppies where is_male is false'),
    (4,
        'select 
            owners.name, 
            puppies.name,
            puppies.breed
        from owners 
        inner join puppies 
            on owners.pet_id = puppies.id'
        );


