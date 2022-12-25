create database if not exists coms6156_sprint1_microservice2;

use coms6156_sprint1_microservice2;

create table product
(
    product_name varchar(255) null,
    price        varchar(255) null,
    productID    varchar(255) not null
        primary key
);

create table shop
(
    name    varchar(255) null,
    email   varchar(255) null,
    phone   varchar(20)  null,
    shopID  varchar(255) not null
        primary key,
    address varchar(255) null
);

create table order_table
(
    shopID    varchar(255) not null,
    productID varchar(255) null,
    date      datetime     null,
    num       int          null,
    orderID   varchar(255) not null
        primary key,
    constraint order_table_ibfk_1
        foreign key (productID) references product (productID)
            on update cascade on delete cascade,
    constraint order_table_ibfk_2
        foreign key (shopID) references shop (shopID)
            on update cascade on delete cascade
);



insert into shop (name, email, phone, shopID)
values ('Cu Store','CUstore@columbial.edu','123456789','1');



insert into product (product_name, price, productID)
values ('Purified Water', '1.0', '1');



insert into order_table (orderID, shopID, productID, date, num)
values ('1', '1', '1', '2022-11-15', '1');
