from django.contrib.auth.models import User
from django import forms


class RegisterForm(forms.ModelForm):  # 회원가입 양식을 출력하기 위해 RegisterForm 이라는 클래스 생성
    password = forms.CharField(label='Password', widget=forms.PasswordInput)  # PasswordInput -- Input 태그 사용
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)  # 회원 가입 시 비밀번호 재입력

    class Meta:
        model = User  # model 설정
        fields = ['username', 'first_name', 'last_name', 'email']  # 입력받을 필드를 지정

    def clean_password2(self):  # clean_필드명 형태의 메서드이다.
        cd = self.cleaned_data  # clean_필드명 형태의 메서드에서 해당 필드의 값을 사용할 때는 꼭 cleaned_data에서 필드값을 찾아서 사용해야 한다.
        if cd['password'] != cd['password']:  # password와 password2가 같은지를 비교하는 코드 실행
            raise forms.ValidationError('Passwords not matched!')
        return cd['password2']
