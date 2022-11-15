-- coffee table
-- 커피이름/ 가격/ 원두

create table nov11_coffee(
	c_no number(3) primary key,
	c_name varchar2(10 char) not null,
	c_price number(5) not null,
	c_bean varchar2(10 char) not null
);

create sequence nov11_coffee_seq;

select * from nov11_coffee;

select num, c_price from
(select rownum as num ,c_price from 
(select c_price from nov11_coffee order by c_price))
where num between 1 and 3;

create table nov14_weather(
	w_no number(3) primary key,
	w_hour varchar2(2 char) not null,
	w_temp varchar2(4 char) not null,
	w_tmx varchar2(6 char) not null,
	w_tmn varchar2(6 char) not null
);
drop table nov14_weather;

create sequence nov14_weather_seq;
drop sequence nov14_weather_seq;

select * from nov14_weather;
------------------------------------------------------
create table nov15_seoulAir(
	sa_no number(2) primary key,
	sa_MSRSTE_NM varchar2(3 char) not null,
	sa_PM10 varchar2(4 char) not null,
	sa_PM25 varchar2(4 char) not null,
);

create sequence nov15_seoulAir_seq;

