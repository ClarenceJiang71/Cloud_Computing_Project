create database if not exists customerDB;

-- use customer;

create table account
(
    emailID varchar(256) primary key,
    password varchar(256) not null
);

create table customer
(
    emailID varchar(256) not null primary key
        references account(emailID)
        on delete cascade,
    username varchar(256) not null,
    firstname varchar(256) not null,
    lastname varchar(256) not null,
    phone varchar(256) not null
);

create table membership
(
    emailID varchar(256) not null primary key
        references customer(emailID)
        on delete cascade,
    valid_by date not null
);

insert into customerDB.account(emailID, password) values
                                                      ("yw3912@columbia.edu", "000000"),
                                                      ("hello@gmail.com", "111111"),
                                                      ("hi@yahoo.com", "222222");

insert into customerDB.customer values
                                    ("yw3912@columbia.edu", "yw3912", "Yuyang", "Wang", "123-456-7890"),
                                    ("hello@gmail.com", "hello", "Harry", "Smith", "098-765-4321");

insert into customerDB.membership values("yw3912@columbia.edu", "2023-12-31");