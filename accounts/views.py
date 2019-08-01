from django.shortcuts import render
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST) # 회원가입 정보가 서버로 전달되었다.
        # Post 방식으로 뷰를 호출했다는 것은 서버로 자료를 전달하는 상태라는 것이다.
        if user_form.is_valid(): # 유효성 검사 이상이 없으면 데이터베이스에 저장
            new_user = user_form.save(commit=False) # 폼 객체에 지정된 모델을 확인하고 이 모델을 객체로 만든다.
            # 이 때 옵션으로 commit=False를 지정했기 때문에 데이터베이스에 저장하는 것이 아니라 메모리 상에 객체만 만들어진다.
            new_user.set_password(user_form.cleaned_data['password']) # 비밀번호 지정 이러한 과정을 거쳐야 암호화된 상태로 저장
            new_user.save() # 실제 데이터베이스에 저장
            return render(request, 'registration/register_done.html', {'new_user':new_user})
    else: # request가 POST 가 아니라면 입력을 받는 화면을 보여줘야 한다.
            user_form = RegisterForm() # 비어있는 RegisterForm 객체를 만들고 register 템플릿을 렌더링해 보여준다.
    return render(request, 'registration/register.html',{'form':user_form})