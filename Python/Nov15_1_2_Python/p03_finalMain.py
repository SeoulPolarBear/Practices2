from p03_final import BeStop, writeFileStudent, getStudentbyName, getLectureHall,\
    insertStudent, menu

if __name__ == "__main__":
    num = 999
    while BeStop(num):
        num = menu()
        if num == 1:
            insertStudent()
        elif num == 2:
            getLectureHall()
        elif num == 3:
            getStudentbyName()
        elif num == 4:
            writeFileStudent()
        elif num == 0:
            print("프로그램을 종료 합니다.")
        else:
            print("다시 입력하세요")
            
  
            
            
