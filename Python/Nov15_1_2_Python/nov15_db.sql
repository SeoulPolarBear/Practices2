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
	sa_MSRSTE_NM varchar2(10 char) not null,
	sa_PM10 number(4,1) not null,
	sa_PM25 number(4,1) not null
);
drop table nov15_seoulAir;
create sequence nov15_seoulAir_seq;
drop sequence nov15_seoulAir_seq;
select * from nov15_seoulAir;

alter table nov15_seoulAir modify column sa_MSRSTE_NM varchar2(10 char) not null;
-------------------------------------------------------------------------------------
--학생 : 이름, 생일, 몇 강의장, 중간, 기말
create table nov15_student(
s_no number(5) primary key,
s_name varchar2(5 char) not null,
s_birthday date not null,
s_lh_no number(2) not null,
s_mid_exam number(3) not null,
s_final_exam number(3) not null,
CONSTRAINT fk_nov15_student FOREIGN KEY(s_lh_no)
    REFERENCES nov15_lecture_hall(lh_no) ON DELETE CASCADE
);

create sequence nov15_student_seq;
drop sequence nov15_student_seq;


--------------------------------------------------------------------------------------
--강의장 : 몇 강의장, 강의장 위치
-- 1강의장 : 7층 복도 오른쪽 / 2강의장 : 5층 복도 왼쪽 끝
-- 3강의장 : 7층 복도 왼쪽 첫번째 / 4강의장 : 8층 왼쪽 / 5강의장 : 6층 오른쪽

create table nov15_lecture_hall(
lh_no number(2) primary key,
lh_location varchar2(20char) not null
);
create sequence nov15_lecture_hall_seq;
drop sequence nov15_lecture_hall_seq;

insert into nov15_lecture_hall values(nov15_lecture_hall_seq.nextval,'7층 복도 오른쪽');
insert into nov15_lecture_hall values(nov15_lecture_hall_seq.nextval,'5층 복도 왼쪽 끝');
insert into nov15_lecture_hall values(nov15_lecture_hall_seq.nextval,'7층 복도 왼쪽 첫번째');
insert into nov15_lecture_hall values(nov15_lecture_hall_seq.nextval,'8층 왼쪽');
insert into nov15_lecture_hall values(nov15_lecture_hall_seq.nextval,'6층 오른쪽');

select * from nov15_lecture_hall;
select * from nov15_student;














