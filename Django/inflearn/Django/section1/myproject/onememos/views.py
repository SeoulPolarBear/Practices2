from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# requeset : UI에서 입력한 것을 받는 역할
# Response : UI에 돌려주는 역할

# render함수와 template파일의 관계
#   -웹사이트 개발 시 파이썬 코드와 데이터를 템프릿 파일로 만들어주는 함수.(쉡게말해 HTML로 변환해서 적용해주는 함수)
#   -결국 리턴은 HTML파일로 리턴.
#   -이렇게 HTML 파일로 리턴한 것을 -> 템플릿(Template) 또는 템플릿 파일.
#   -그러나 템플릿 파일이 HTML 파일은 아니다.
#   -이러한 템플릿 파일은 대부분의 프레임워크에서도 마찬가지인데 프레임워크 전용 파일의 개념.
#   -즉, 장고에서만 사용할 수 있는 문법(그래서 template 언어(문법, 태그)라고 불리기도 한다.) 등을 이러한 템플릿에 적용
#       -> 일반 HTML 파일 X
#   -당연히 템플릿도 규칙과 최소한의 문법(템플릿 태그라 불리우는 것들)이 존재.
#   -조건처리,반복처리 등이 가능 --> 얼핏 프로그래밍 언어처럼도 보이나 -> 언어라기보다는 템플릿 전용 언어이다.

#   -템플릿 폴더 만들기 규칙
#               - 첫 번째 : 프로젝트 루트 폴더에 templates폴더를 만들어서 사용 -> settings.py -> 템플릿 경로 추가하여 사용.
#                   -> settings.py에 Template라는 배열안데 dir에 추가하면 되는 형식 (번거롭다.)
#               - 두 번째 : 생성한 앱(APP)폴더 쪽 바로 하위에다가 -> templates폴더를 만들어서 사용 -> 앱별로 템플릿 사용이 가능. (이게 더 편하다.)
#               - 정리하면, 장고는 템플릿 폴더를 인식하는 방식이 여러가지이다.
#               - 서버 재시작.
#               - 즉, onememos앱의 경우 하위에 templates폴더 생성하면 별다른 설정없이 바로 템플릿 디렉토리 인식.
#               - 서버 재시작(py manage.py runserver)

def main(request):
    #return HttpResponse("Onememos~Hello, World~ ^.~")
    #return render(request,"템플릿 파일 경로")
    return render(request,"main.html")


#http://127.0.0.1:8000/onememos/createMemo/?memoContent=%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD(대한민국)
def createMemo(request):
# request객체는 사용자가 폼 페이지를 통해서 입력한 폼 데이터 값들을 받는다.
# requst.GET,request.POST,requst.COOKIE -> 사전형 데이터 GET, POST, COOKIE 정보들을 받는다.
    #memoContent = request.GET['memoContent'] # get, post,put,delete를 처리할 떄 이렇게 처리한다.
    memoContent = request.POST['memoContent']
    return HttpResponse("Create Memo=" + memoContent)
    
    
# 앞으로 공부할 내용
# 1. 뷰페이지 템플리 꾸미기(Form) -> 입력과 출력
# 2. 템플릿 파일의 목적(용도)
#   - 뷰페이지 처리 --> 템플릿 파일
#   - 개발과 디자인의 분리
#   - 개발자 코드 vs 디자이너 코드(HTML,CSS)
#   - 다른 프레임워크들에서도 보통 template이라는 폴더명을 만들어서 템플릿 폴더로 인식시켜서 사용.
#   - 아무튼 디자이너(뷰페이지 담당자) 입장에서는 템플릿 언어의 고유문법이나 태그들을 배워야 함

# 3. 관리자모드에서의 DB 조작
# 관리자모드에서의 DB조작 VS CMD 명령프롬프트에서의 DB조작(dbshell)
#           - 이 과정에서 오류가 발생하곤 한다 -> 이때 -> 어떻게 처리해줘야 하는지에 대해서 체크.
#           - sqlite tool설치가 안되서 나는 오류.
#           - https://www.sqlite.org/download.html여기서 관련 툴을 다운로드.
#           - sql-tools-win32-x86-....zip (1.8 ~ 2M)
#           - 앞축을 풀면 3개의 실행파일이 들어있는데 이중 sqlite3.exe실행파일을 생성한 프로젝트 루트 폴더에 넣어놓고
#           - sqlite DB에 접속하면 됩니다.
#           - 툴을 통해 DB의 테이블 정보 확인 및 테이블명 규칙성 확인 -> 실제 테이블명 확인.

# 4. 꾸민 폼 페이지에서 한 줄 메모 작성 -> DB에 입력 및 출력
    