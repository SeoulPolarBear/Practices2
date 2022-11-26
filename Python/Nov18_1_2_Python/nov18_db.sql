create table nov18_map(
m_id number(3) primary key,
m_place_name varchar2(30 char) not null,
m_phone varchar2(14 char) not null,
m_longitude number(9,6) not null,
m_latitude number(9,6) not null
);

create sequence nov18_map_seq;

select * from NOV18_MAP;

--NVL 함수 : null일 때, 지정한 값으로 대체하는 함수
--NVL(값, (값이)null일 때 대체값)
select nvl(null, "-"), nvl('null', '-') from dual;

--NVL2 함수 : null의 여부에 따라서 지정한 값으로 대체하는 함수
--NVL2(값, 값이 있을 때 대체값,없을 때 대체값)
select nvl2(null, "A", "B"), nvl('null', "A", "B") from dual;


drop table NOV18_MAP;