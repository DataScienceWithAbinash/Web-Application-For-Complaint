create table crform(
    id integer primary key autoincrement,
    refno integer,
    name text not null,
    email text not null,
    invoice_no integer not null,
    invoice_date date not null,
    product_name text not null,
    nature_of_complaint text not null,
    status text
);