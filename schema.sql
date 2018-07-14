create table dogs (
    id integer primary key,
    name text not null,
    age integer not null,
    sex text not null,
    energy integer not null,
    farm_id integer not null
);

create table farms (
    id integer primary key,
    name text not null
);

insert into farms (name) values ('brads doggie farm');
insert into farms (name) values ('farmville');

insert into dogs (name, age, sex, energy, farm_id) values ('fido', 3, 'm', 100, 1);
insert into dogs (name, age, sex, energy, farm_id) values ('rido', 5, 'f', 100, 1);
insert into dogs (name, age, sex, energy, farm_id) values ('bido', 7, 'f', 95, 2);
