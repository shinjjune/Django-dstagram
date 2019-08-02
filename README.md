# DJANGO

#### dstagram
이번 프로젝트는 인스타그램 카피 서비스입니다. 인스타그램의 모든 기능을 구현하지 않지만 구현할 수 있는 범위 내에서 비슷하게 구현을 해보면서 
이미지 파일에 관한 설정, 서버 셋팅, 파일 다루기에 대해서 중점적으로 배워보겠습니다.


* 기능

웹 서비스의 기능과 디자인을 살펴보겠습니다. 이번 장에서도 부트스트랩을 사용해서 디자인을 입히겠습니다.
상단 메뉴바에는 홈 링크, 환영 메시지, 업로드 링크, 로그인(로그아웃), 회원가입 링크를 출력합니다.
메인 페이지는 사진목록을 출력하며 댓글 시스템도 사용하겠습니다.
뷰단위로 기능을 살펴 보자


### 댓글기능 구현하기

##### DISQUS 가입하기

https://disqus.com

$pip install django-disqus

<settings.py 에 등록>

'disqus',

'django.contrib.sites'


$python manage.py migrate   => sites 앱을 위한 데이터베이스를 설정

<settings.py 에 추가>

DISQUS_WEBSITE_SHORTNAME = 'dstagram-django'

SITE_ID =1


url : 127.0.0.1:8000/detail/1/

### cf) 권한 제한하기
---> 데코레이터(decorator)와 믹스인(mixin)



