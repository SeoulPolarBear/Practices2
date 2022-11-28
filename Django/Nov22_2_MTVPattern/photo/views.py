from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from photo.forms import PhotoForm

#View
#Template과 Model 사이를 이어주는 다리역할( = MVC 패턴의 C)

# 뷰를 만드는 방법은 다양한데,
# 대표적으로 함수형 뷰와 클래스형 뷰
# 함수형 !

# 기능 개발 순서로는
#    Model -> Template -> View -> URL 순으로 작성

# def photo_list(request):
    # return render(request,'photo/photo_list.html', {})
#렌더링 : 서버로부터 HTML 파일을 받아서 브라우저엣 뿌려지는 과정
#    웹에 보여질 수 있도록 가공해서 전달!


# objects.all()을 통해서 Photo 모델 데이터 전체를 가져옴
# render 마지막 파라미터에 있는 {}를 활용하면 템플릿으로 데이터를 보낼 수 있음
# {}안에 넣고자 하는 데이터를 데이터의 이름과 함께 전달하면 됨
# 이 부분이 Django에서 제공하는 ORM(Object Relational Mapping)
def photo_list(request):
    photos = Photo.objects.all()
    return render(request,'photo/photo_list.html', {'photos':photos})


def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request,'photo/photo_detail.html',{'photo':photo})

#get_object_or_404()는 모델로부터 데이터를 찾아보고 찾는 데이터가 없다면 404에러를 반환하는 함수
#pk(primary key)
#    : model에서 찍어낸 수많은 객체들을 구분할 수 있는 구분자
# 이때 우리는 따로 PK값을 주지 않고 아래와 같이 선언 함으로써 pk 값을 대신 사용하였다.
    # # __str__() 함수로 사진 제목과 번호 보여주기
    # def __str__(self):
        # return f'[{self.pk}] {self.title}'
        
def photo_post(request):
    #POST 방식 사용자가 입력을 다해서 제출을 눌렀을 경우 저장을 하는 부분
    if request.method == "POST":
        form=PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save(commit= False)
            photo.save()
            return redirect("photo_detail",pk=photo.pk)
    else:
        form = PhotoForm()# 포토 폼에 있는 것을 사용해서 input 대신에 form을 보여줄 수 있게 처리해준다.
    #GET 방식 사용자가 처음 들어왔을 때 즉, 입력을 해야 하는 경우
    return render(request, 'photo/photo_post.html', {'form':form})

# 수정 기능 photo_detail.html은 그대로 사용할 것
def photo_edit(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == "POST":
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save(commit = False)
            photo.save()
            return redirect('photo_detail', pk=photo.pk)
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'photo/photo_post.html',{'form':form})
# 등록할 때랑 코드는 비슷
# 추가로 PhotoForm의 instance를 photo로 설정해줘서 수정 대상이 될 데이터를 설정해줬음
# get 방식 요청이 들어와도 photo데이터를 폼에 담아 photo_post.html로 넘겨서 기존 데이터를 수정할 수 있게 함

#삭제하기
def photo_delete(request,pk):
    photo = Photo.objects.get(pk=pk)
    if request.method == "GET":
        photo.delete()
        return redirect('/', pk=photo.pk)
    








