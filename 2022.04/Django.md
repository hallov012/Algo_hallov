6. form 저장경로
6. orm 
6. models.py 가 변경되면 migtarion 필요 
6. MTV 디자인 패턴
6. .get : 2개 있거나 없으면 오류가 난다



#  1. Template, View, Routing

## Web framework

### Web

> * World Wide Web
> * 인터넷에 연결된 컴퓨터를 통해 정보를 공유할 수 있는 전 세계적인 정보 공간



### Static web page(정적 웹 페이지)

> * 서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지
>
> * 서버가 정적 웹 페이지에 대한 요청을 받은 경우
>
>   서버는 추가적인 처리 과정 없이 클라이언트에게 응답을 보냄
>
> * 모든 상황에서 모든 사용자에게 동일 정보 표시
>
> * 일반적으로 HTML, CSS, JavaScript로 작성
>
> * flat page 라고도 함



### Dinamic web page

> * 웹 페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 이후 클라이언트에게 응답을 보냄
>
> * 동적 웹 페이지는 방문자와 상호작용하기 때문에 페이지 내용은 그때그떄 다름
>
> * 서버 사이드 프로그래밍 언어(Python, Java, C++ 등) 사용,
>
>   파일을 처리하고 데이터베이스와의 상호작용이 이루어짐



### Framework

> * 프로그래밍에서 특정 운영 체제를 위한 응용 프로그램 표준 구조를 구현하는 클래스, 라이브러리 모임
>
> * 재사용할 수 있는 수많은 코드를 프레임워크로 통합함으로써
>
>   개발자가 새로운 애플리케이션을 위한 표준 코드를 다시 작성하지 않아도 같이 사용 가능하도록 도움
>
> * Application Framework 라고도 함



### Web framework

> * **웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적**
>
>   데이터베이스 연동, 템플릿 형태의 표준, 세션 관리, 코드 재사용 등의 기능 포함
>
> * 동적인 웹 페이지나, 웹 애플리케이션, 웹 서비스 개발 보조용으로 만들어지는 Application framework의 일종



### Django를 사용해야하는 이유

> * 검증된 python 언어 기반 web framework
> * 대규모 서비스에도 안정적이며 오랫동안 여러 기업들에 의해 사용됨



### Framework Architecture

> * MVC Design Pattern(model-view-controller)
>
> * 소프트웨어 공학에서 사용되는 디자인 패턴 중 하나
>
> * 사용자 인터페이스로부터 프로그램 로직을 분리하여 애플리케이션의 시각적 요소나 이면에서 실행되는 부분을
>
>   서로 영향 없이 쉽게 고칠 수 있는 애플리케이션을 만들 수 있음
>
> * Django는 **MTV Pattern**이라고 함



### MTV Pattern

> * Model (데이터)
>   * 응용프로그램의 데이터 구조를 정의, 데이터베이스의 기록을 관리(추가, 수정, 삭제)
>   
> * Template (보이는 것)
>   * 파일의 구조나 레이아웃 정의
>   * 실제 내용을 보여주는 데 사용(presentation)
>   
> * View (중간 관리자)
>   * HTTP 요청을 수신하고 응답을 반환
>   * Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
>   * template에게 응답의 서식 설정을 맡김
>   
> * MVC Pattern : Model, View, Controller
>
> * MTV Pattern : Model, Template, View
>
>   ![스크린샷 2022-03-20 오후 6.13.46](Django.assets/스크린샷 2022-03-20 오후 6.13.46.png)



## Django Intro

### [참고] LTS

> * Long Term Support (장기 지원 버전)
> * 일반적인 경우보다 장기간에 걸쳐 지원하도록 고안된 소프트웨어
> * 컴퓨터 소프트웨어의 제품 수명주기 관리 정책
> * 배포자는 LTS 확정을 통해 장기적이고 안정적인 지원을 보장함



### 프로젝트 구조

> * Init.py : Python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시
> * asgi.py
>   * Asynchronous Server Gateway Interface
>   * Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움
> * settings.py : 애플리케이션의 모든 설정을 포함
> * urls.py : 사이트 url과 적절한 views의 연결을 지정
> * wsgi.py
>   * Web Server Gateway Interface
>   * Django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움
> * manage.py : Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티



### 애플리케이션 구조

> * admin.py : 관리자용 페이지를 설정 하는 곳
> * apps.py : 앱의 정보가 작성된 곳
> * models.py : 앱에서 사용하는 Model을 정의하는 곳
> * tests.py : 프로젝트의 테스트 코드를 작성하는 곳
> * views.py : view 함수들이 정의 되는 곳



### Project

> * Application(앱)의 집합 
> * 프로젝트에는 여러 앱이 포함 될 수 있음
> * 앱은 여러 프로젝트에 있을 수 있음



### Application

> * 앱은 실제 요청을 처리하고 페이지를 보여주고 하는 등의 역할을 담당
> * 하나의 프로젝트는 여러 앱을 가짐
> * 일반적으로 앱은 하나의 역할 및 기능단위로 작성



<b>=> 프로젝트에서 앱을 사용하기 위해서는 반드시 (setting.py)INSTALLED_APPS에 추가해야 함</b> 

​	INSTALLED_APPS : Django installation에 활성화 된 모든 앱을 지정하는 문자열 목록



### 주의 사항

> * <b>반드시 생성 후 등록! </b>
> * INSTALLED_APPS에 먼저 작성(등록)하고 생성하려면 앱이 생성되지 않음
> * 장고가 권장하는 등록 사항 (권장사항임)
>   * Local => Third party => Django

```python
# 가상 공간 생성 및 활성화
python -m venv venv
source venv/bin/activate 
pip list
(비활성화 deactivate)

Control shift p -> python interpreter

pip install django==3.2.12
(pip install -r requirements.txt)

django-admin startproject mypjy .
# . 이 없으면 프로젝트 폴더를 만들고 그 안에 만든다
# . 이 있으면 그냥 현재 위치에 생성함

# app 생성하기
python manage.py startapp ( )

# app 등록하기
# setting의 INSTALLED_APPS 에 생성한 app 추가
from articles import views
# urls(프로젝트파일)에서 views(앱파일)을 불러올 수 있도록 import

# 장고 서버 켜보기
python manage.py runserver
```





## 요청과 응답

### urls (in project)

> * urls.py : HTTP 요청을 알맞은 view로 전달
> * views.py 
>   * HTTP 요청을 수신, HTTP 응답을 반환하는 함수 작성
>   * Model을 통해 요청에 맞는 필요 데이터에 접근
>   * Template에게 HTTP 응답 서식을 맡김
> * templates
>   * 실제 내용을 보여주는데 사용되는 파일
>   * 파일의 구조나 레이아웃을 정의 (ex. HTML)
>   * Template 파일 경로의 기본값은 **app 폴더 안의 templates 폴더**로 저장되어 있음



### 추가 설정(setting)

> * LANGUAGE_CODE
>
>   * 모든 사용자에게 제공되는 번역을 겨정
>   * 이 설정이 적용 되려면 USE_I18N 활성화 필요
>
> * TIME_ZONE
>
>   * 데이터베이스 연결 시간대를 나타내는 문자열 지정
>
>   * USE_TZ가 True이고 이 옵션이 설정된 경우 DB에서 날짜와 시간을 읽으면,
>
>     UTC 대신 새로 설정한 시간대의 인식 날짜&시간이 반환 됨
>
>   * USE_TZ이 False인 상태로 이 값을 설정하는 것은 error가 발생하므로 주의
>   
> * USE_I18N
>
>   * django의 변역 시스템을 활성화해야 하는지 여부를 지정
>
> * USE_L10N
>
>   * 데이터의 지역화 된 형식을 기본적으로 활성화할지 여부를 지정
>   * True일 경우 Django는 현재 locale의 형식을 사용해 숫자와 날짜 표시
>   
> * USE_TZ
>
>   * datetime가 기본적으로 시간대를 인식하는지 여부를 지정
>   * True일 경우 django는 내부적으로 시간대 인식 날짜/ 시간 사용



## Template

### Django Template

> * "데이터 표현을 제어하는 도구이자 표현에 관련된 로직"
> * 사용하는 built-in system (Django template language)



### Django Template Language (DTL)

> * Django template에서 사용하는 built-in tmaplate system
>
> * 조건, 반복, 변수, 치환, 필터 등의 기능을 제공
>
> * 단순히 python이 html에 포함 된 것이 아니며,
>
>   프로그래밍적 로직이 아니라 <b>프레젠테이션을 표현하기 위한 것</b>
>
> * Python 처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있으나,
>
>   이것은 해당 python 코드로 실행되는 것이 **아님** 



### DTL Syntax

1. **Variable**

> ```django
> {{ variable }}
> ```
>
> * Render()을 사용하여 views.py에서 정의한 변수를 template 파일로 넘겨 사용
>
> * 변수명은 영어, 숫자, 밑줄(_)의 조합으로 구성되나 밑줄로는 시작 할 수 없음
>
> * dot(.)을 사용해 변수 속성에 접근 가능
>
> * render()의 세번째 인자로 {'key': value}와 같이 딕셔너리 형태로 넘겨주며,
>
>   여기서 정의한 key에 해당하는 문자열이 template에서 사용가능한 변수명이 됨



2. **Fillers** 

> ```django
> {{ variable|filter }}
> ```
>
> * 표시 할 변수를 수정 할 때 사용
> * 60개의 built-in template filters 제공
> * chained가 가능하며 일부 필터는 인자를 받기도 함



3. **Tag**

> ```django
> {% tag %}
> ```
>
> * 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등,
>
>   변수보다 복잡한 일들을 수행
>
> * 일부 태그는 시작과 종료 태그 필요
>
>   * {% if %}{% endif%}
>
> * 약 24개의 built-in template tags 제공



4. **Comments**

> * 한줄 주석: {# ... #}
> * 여러 줄 주석: {% comment %} {% endcomment %}

* *코드 작성 순서는 URL -> VIEW -> TEMPLATE 순으로*



### Template inheritance (템플릿 상속)

> * 템플릿 상속은 기본적으로 코드의 재사용성에 초점을 맞춤
>
> * 템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함하고.
>
>   하위 템플릿이 재정의(override) 할 수 있는 블록을 정의하는
>
>   기본 "skeleton" 템플릿을 만들 수 있음



### Template inheritance -"tags"

```python
{% extends '' %}
```

> * 자식(하위)템플릿이 부모 템플릿을 확장한다는 것을 알림
> * 반드시 **템플릿 최상단**에 작성되어야 함

```python
{% block content %}{% endbolck %}
```

> * 하위 템플릿에서 재지정(overridden)할 수 있는 블록을 정의
> * 즉, 하위 템플릿이 채울 수 있는 공간
> * **app_name/templates 디렉토리 외 템플릿 추가 경로 설정 필요**
>   * settings.py -> TEMPLATES -> 'DIRS' = [BASE_DIR / 'templates']



### Template Tag -"include"

```python
{% include '' %}
```

> * 템플릿을 로드하고 현재 페이지로 렌더링
> * 템플릿 내에 다른 템플릿을 포함(including) 하는 방법



### Django template system (feat. Django 설계 철학)

> * "표현과 로직(view)을 분리"
>   * 템플릿 시스템은 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐이라고 생각해야 함
>   * 즉, 템플릿 시스템은 이러한 기본 목표를 넘어서는 기능을 지원하지 말아야 함
> * "중복을 배제"
>   * 대다수의 동적 웹사이트는 공통 header, footer, navbar 같은 사이트 공통 디자인을 가짐
>   * Django 템플릿 시스템은 이러한 요소를 한 곳에 저장하기 쉽게 하여 중복 코드를 없애야 함
>   * 이것이 템플릿 상속의 기초가 됨



## HTML Form

### HTML "form" element

> * 웹에서 사용자 정보를 입력하는 여러 방식(text, button, checkbox, file, hidden, image, password, radio, reset, submit)을 제공,
>
>   사용자로부터 할당된 데이터를 서버로 전송
>
> * 핵심 속성(attribute)
>
>   * **action**: 입력 데이터가 전송될 URL 지정
>   * **method**: 입력 데이터 전달 방식 지정



### HTML "input" element

> * 사용자로부터 데이터를 입력 받기 위해 사용
> * type 속성에 따라 동작 방식이 달라짐
> * 핵심 속성(attribute)
>   * **name**
>   * 중복 가능, 양식을 제출했을 때 name이라는 이름에 설정된 값을 넘겨서 값을 가져올 수 있음
>   * 주요 용도: GET/POST 방식으로 서버에 전달하는 파라미터(name=key, value=value)로 매핑
>   * GET 방식에서는 URL에서 **key=value&key=value**형식으로 데이터 전달



### HTML "label" element

> * 사용자 인터페이스 항목에 대한 설명(caption)을 나타냄
> * label을 input 요소와 연결하기
>   * input에 id 속성 부여
>   * label에는 input의 id와 동일한 값의 for 속성이 필요
> * label과 input 요소 연결의 주요 이점
>   * 시각적인 기능 뿐만 아니라 화면 리더기에서 label을 읽어 사용자가 입력해야 하는 text가 무엇인기 더 쉽게 이해할 수 있도록 돕는 프로그래밍적 이점 존재
>   * label을 클릭해 input에 초점을 맞추가나 활성화 시킬 수 있음



### HTML "for" attribute

> * For 속성의 값과 일치하는 id를 가진 문서의 첫 번째 요소를 제어
>   * 연결 된 요소가 labelable elements인 경우 이 요소에 대한 labeled control이 됨
> * "labelable elements"
>   * label 요소와 연결 할 수 있는 요소
>   * button, input(not hidden type), select, textarea...



### HTML "id" attribute

> * 전 문서에서 고유(must be unique)해야 하는 식별자를 정의
> * 사용 목적
>   * linking, scripting, styling 시 요소를 식별



### HTTP

> * HyperText Transfer Protocol
> * 웹에서 이루어지는 모든 데이터 교환의 기초
> * 주어진 리소스가 수행 할 작업을 나타내는 request methods를 정의
> * HTTP request method 종류 : GET, POST, PUT, DELETE, ...



### HTTP request method -"GET"

> * 서버로부터 **정보를 조회**하는 데 사용
> * 데이터를 가져올 때만 사용해야 함
> * 데이터를 서버로 전송할 때 body가 아닌 Query String Parameters를 통해 전송
> * 서버에 요청을 하여 HTML 문서 파일을 한장 받을 때 사용하는 요청의 방식



## URL

### Django URLs

> * Dispatcher(발송자, 운항 관리자) 로서의 URL
> * 웹 애플리케이션은 URL을 통한 클라이언트의 요청에서부터 시작 됨



### Variable Routing

> * URL 주소를 변수로 사용하는 것
> * URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음
> * 즉, 변수 값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음
> * example
>   * path('accounts/user/<<int:user_pk>>/, ...')
>     * accounts/user/1 -> 1번 user 관련 페이지
>     * accounts/user/2 -> 2번 user 관련 페이지



### URL Path converters

> * **str**
>   * '/'를 제외하고 비어있지 않은 모든 문자열과 매치
>   * 작성하지 않을 경우 기본 값
> * **int**: 0또는 양의 정수와 매치
> * **slug**
>   * ASCII 문자 또는 숫자, 하이픈 및 밑줄 문자로 구성된 모든 슬러그 문자열과 매치
> * uuid
> * path



### App URL mapping

> * app의 view 함수가 많아지면서 사용하는 path() 또한 많아지고,
>
>   app 또한 더 많이 작성되기 때문에 프로젝트의 urls.py에서 모두 관리하는 것은 프로젝트 유지보수에 좋지 않음
>
> * 이제는 **각 app에 urls.py를 작성**



### Including other URLconfs

> * **inclue()**
>
>   * 다른 URLconf(app1/urls.py)들을 참조할 수 있도록 도움
>
>   * 함수 include()를 만나게 되면, URL의 그 시점까지 일치하는 부분을 잘라내고,
>
>     남은 문자열 부분을 후속 처리를 위해 include된 URLconf로 전달
>
> * **django는 명시적 상대경로(from .module import ..)를 권장**



### Naming URL patterns

> * 이제는 링크에 url을 직접 작성하는 것이 아니라 path() 함수의 name 인자를 정의해 사용
> * Django Template Tag 중 하나인 url 태그를 사용해 path() 함수에 작성한 name 사용 가능
> * url 설정에 정의된 특정한 경로들의 의존성 제거 
>
> ```python
> path('index/', views.index, name='index')
> ```
>
> ```django
> <a href="{% url 'index' %}">메인 페이지</a>
> ```



### url template tag

> ```django
> {% url '' %}
> ```
>
> * 주어진 URL 패턴 이름 및 선택적 매개 변수와 일치하는 절대 경로 주소를 반환
> * 템플릿에 URL을 하드 코딩하지 않고도 DRY 원칙을 위반하지 않으면서 링크를 출력하는 방법



## namespace

### namespace(이름공간)

> * 객체를 구분할 수 있는 범위를 나타내는 말
>
>   일반적으로 하나의 이름 공간에서는 하나의 이름이 단 하나의 객체만을 가르킴
>
> * 변수명과 함수명이 겹치지 않게 정의하는 것이 어렵다
>
> * Django
>
>   * 서로 다른 app의 같은 이름을 가진 url name은 이름공간을 설정해서 구분
>
>   * Templates, static 등 django는 정해진 경로 하나로 모아서 보기 때문에
>
>     중간에 폴더를 임의로 만들어 주는 것으로 이름공간 설정



### URL namespace

> * URL namespace를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는
>
>   경우에도 이름이 지정된 URL을 고유하게 사용 할 수 있음
>
> * urls.py에 "app_name" attribute 값 작성
>
> * 참조는 ' : ' 를 사용



### Template namespace

> * django는 기본적으로 app_name/templates/ 경로에 있는 templates 파일만 찾을 수 있으며 INSTALLED_APPS에 작성한 순서로 검색 후 렌더링
> * 그래서 임의로 templates의 폴더 구조를 app_name/templates/app_name 형태로 변경해 임의로 이름 공간을 생성 후 변경된 추가 경로로 수정



## Static files

### 웹 서버와 정적 파일

> * 웹 서버는 특정 위치(URL)에 있는 자원(resource)을 요청(HTTP request) 받아서
>
>   제공(serving)하는 응답(HTTP response)을 처리하는 것을 기본 동작으로 함
>
> * 이는 자원과 접근 간으한 주소가 정적으로 연결된 관계
>
>   * ex) 사진 파일은 자원, 파일 경로는 웹 주소
>
> * 즉, 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원(static resource) 제공



### Static file

> * 정적 파일
>
> * 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
>
>   * 사용자의 요청에 따라 내용이 바뀌는 것이 아니라 요청한 것을 그대로 보여주는 파일
>
> * Ex) 웹서버는 일반적으로 이미지, 자바 스크립트 또는 CSS와 같은 
>
>   미리 추가된 파일(움직이지 않는)을 제공해야함
>
> * 파일 자체가 고정되어 있고, 서비스 중에도 추가되거나 변경되지 않고 고정되어 있음
>
> * Django에서는 이러한 파일을 "Static file" 이라 함
>
>   * django는 staticfiles 앱을 통해 정적 파일과 관련 된 기능 제공



### Static file 구성

> * **Django.contrib.staticfiles**가 INSTALLED_APPS에 포함되어 있는지 확인
> * settings.py에서 **STATIC_URL** 정의
> * 템플릿에서 **static 템플릿 태그**를 사용해 지정된 상대 경로에 대한 URL 빌드
>
> ```python
> {% load static %}
> <img scr="{% static 'my_app/example.jpg' %}" alt="my image"
> ```
>
> * 앱의 static 디렉토리에 정적 파일을 저장
>   * Ex) my_app/static/my_app/example.jpg



### Django template tag

> * **load**
>
>   * 사용자 정의 템플릿 태그 세트를 로드
>   * 로드하는 라이브러리, 패키지에 등록된 모든 태그와 필터를 불러옴
>
> * **static**
>
>   * STATIC_ROOT에 저장된 정적파일에 연결
>
>   ```django
>   {% load static %}
>   <img scr="{% static 'my_app/example.jpg' %}" alt="my image">
>   ```



### The staticfiles app

> * **STATICFIELS_DIRS**
>
>   * 'app/static/' 디랙토리 경로(기본경로)를 사용하는 것 외에
>
>     추가적인 정적 파일 경로 목록을 정의하는 리스트
>
>   * 추가 파일 디랙토리에 대한 전체 경로를 포함하는 문자열 목록으로 작성되어야 함
>
>   ```python
>   STATICFILES_DIR = [	
>     BASE_DIR / 'static',
>   ]
>   ```
>
> * **STATIC_URL**
>
>   * STATIC_ROOT에 있는 정적 파일을 참조할 때 사용할 URL
>
>     * 개발단계에서는 실제 정적 파일이 저장되어 있는 'app/static/' 경로(기본경로) 및
>
>       STATICFILES_DIRS에 정의된 추가 경로들을 탐색함
>
>   * 실제 파일/디렉토리가 아니며 URL로만 존재
>
>   * 비어있지 않은 값으로 설정한다면 반드시 '/'로 끝나야 함
>
>   ```python
>   STATIC_URL = '/static/'
>   ```
>
> * **STATIC_ROOT**
>
>   * collectstatic이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대경로
>   * django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아 넣는 경로
>   * 개발과정에서 settings.py의 DEBUG 값이 true로 설정되어 있으면 해당 값은 적용되지 않음
>     * 직접 작성하지 않으면 django 프로젝트에서는 settings.py에 작성되어 있지 않음
>   * 실 서비스환경(배포 환경)에서 django의 모든 정적파일을 다른 웹 서버가 직접 제공하기 위함
>
> * 참고
>
>   * STATIC_ROOT에 정적파일을 수집
>
>   ```python
>   # settings.py에 추가
>   STATIC_ROOT = BASE_DIR / 'staticfiles'
>   ```
>
>   ```bash
>   $ python manage.py collectstatic
>   ```





# 2. Model

## Model

### Model

> * 단일한 데이터에 대한 정보를 가짐
>   * 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들 포함
> * 저장된 데이터베이스의 구조(layout)
> * Django는 model을 통해 데이터에 접속하고 관리
> * 일반적으로 각각의 model은 하나의 데이터베이스 테이블에 매핑 됨



### Database

> * 데이터베이스(DB) : 체계화된 데이터의 모임
> * 쿼리(Query)
>   * 데이터를 조회하기 위한 명령어
>   * 조건에 맞는 데이터를 추출하거나 조작하는 명령어
>   * 'Quert를 날린다' => DB를 조작한다



### Database의 기본 구조

> * 스키마(Schema) : 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조(structure)
> * 테이블(Table)
>   * 열(컬럼/필드)와 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합
>   * SQL 데이터베이스에서는 테이블을 **관계**라고도 함
>   * 열(column) : 필드(feild) or 속성
>   * 행(row) : 레코드(record) or 튜플
> * 기본키(PK) 
>   * 각 행(레코드)의 고유값으로 Primary Key로 불림
>   * 반드시 설정해야하며, 데이터베이스 관리 및 관계 설정시 주요하게 활용 됨

* 웹 애플리케이션의 데이터를 **구조화**하고 **조작**하기 위한 도구



### ORM

> * Object-Relational-Mapping
>
> * 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에(Django - SQL) 데이터를
>
>   변환하는 프로그래밍 기술
>
> * OOP 프로그래밍에서 RDBMS를 연동할 때, 데이터베이스와 객체지향 프로그래밍 언어 간의
>
>   호환되지 않는 데이터를 변환하는 프로그래밍 기법
>
> * Django는 내장 Django ORM 사용



### ORM의 장점과 단점

> * 장점
>   * SQL을 잘 알지 못해도 DB 조작이 가능
>   * SQL의 절차적 접근이 아닌 객체 지향적 접근으로 인한 높은 생산성
> * 단점
>   * ORM 만으로 완전한 서비스를 구현하기 어려운 경우가 있음
> * *현대 웹 프레임워크의 요점은 웹 개발의 속도를 높이는 것 (**생산성**)*



**ORM을 사용하는 이유: DB를 객체(Object)로 사용하기 위해!!**



### model.py 작성

```python
# articles/models.py

class Articles(models.Model):
    title = models.CharField(max_length=0)
    content = models.TextField()
```

> * 각 모델은 Django.models.Model 클래스의 서브 클래스로 표현 됨
>   * django.db.models 모듈의 Model 클래스를 상속 받음
> * Models 모듈을 통해 어떤 타입의 DB 컬럼을 정의할 것인지 정의
>   * title과 content는 모델의 필드를 나타냄
>   * 각 필드는 클래스 속성으로 지정되어 있으며, 각 속성을 각 데이터베이스의 열에 매핑



### 사용 모델 필드

> * CharField(max_length=None, **options)
>
>   * 길이의 제한이 있는 문자열을 넣을 때 사용
>   * CharField의 max_length는 필수 인자
>   * **필드의 최대길이(문자)**, 데이터베이스 레벨과 django의 유효성 검사(값을 검증하는 것)에서 활용
>
> * TextField(**options)
>
>   * 글자의 수가 많을 때 사용
>
>   * max_length 옵션 작성시 자동양식 필드인 texterea 위젯에 반영은 되지만
>
>     모델과 데이터베이스 수준에는 적용되지 않음
>
>     * max_length 사용은 CharField에서 사용해야 함



## Migrations

### Migrations

> * "Django가 model에 생긴 변화를 반영하는 방법"
> * Migration 실행 및 DB 스키마를 다루기 위한 몇가지 명령어
>   * **makemigrations**
>   * **migrate**
>   * sqlmigrate
>   * showmigrations



### Migrations Commands

> ```python
> $ python manage.py (명령어)
> ```
>
> * makemigrations : model을 변경한 것에 기반한 새로운 마이그레이션(like 설계도)을 만들 때 사용
> * migrate
>   * 마이그레이션을 DB에 반영하기 위해 사용
>   * 설계도를 실제 DB에 반영하는 과정
>   * 모델에서의 변경 사항들과 Db의 스키마가 동기화를 이룸
> * sqlmigrate
>   * 마이그레이션에 대한 SQL 구문을 보기 위해 사용
>   * 마이그레이션이 SQL 문으로 어떻게 해석되어서 동작할지 미리 확인 가능
> * showmigrations
>   * 프로젝트 전체의 마이그레이션 상태를 확인하기 위해 사용
>   * 마이그레이션 파일들이 migrate 됐는지 안됐는지 여부를 확인 할 수 있음



## DateFiled's options

> * auto_now_add
>
>   * 최소 생성 일자
>
>   * django ORM이 최초 insert(테이블에 데이터 입력)시에만 현재 날짜와 시간으로 갱신
>
>     (테이블에 어떤 값을 최초로 넣을 때)
>
> * auto_now
>
>   * 최종 수정 일자
>   * django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신



### DateTimeField가 아닌 DateField의 options를 확인한 이유

> * DateTimeField는 Datefield와 동일한 추가 인자(extra argument)를 사용함
> * DateTimeField는 Datefield의 서브 클래스



### 반드시 기억해야 할 migration 3단계

> 1. models.py : model 변경사항 발생 시
> 2. $ python manage.py makemigrations : migration 파일 생성
> 3. $ python manage.py migrate : DB 반영(모델과 DB 동기화)



## Database API

### DB API

> * "DB를 조작하기 위한 도구"
>
> * Django가 기본적으로 ORM을 제공함에 따른 것으로 DB를 편하게 조작할 수 있도록 도움
>
> * model을 만들면 django는 객체를 만들고 읽고 수정하고 삭제 가능한
>
>   database-abstract API를 자동으로 만듦
>
> * database-abstract API 혹은 database-access API 라고 함
>
> * **Manager**
>
>   * Django 모델에 데이터베이스 query 작업이 제공되는 인터페이스
>   * 기본적으로 모든 django 모델 클래스에 objects라는 manager를 추가
>
> * **QuerySet**
>
>   * 데이터베이스로부터 전달받은 객체 목록
>   * queryset 안에 객체는 0개, 1개 혹은 여러개일 수 있음
>   * 데이터베이스로부터 조회, 필터, 정렬 등을 수행 할 수 있음 (유사 리스트)



### DB API 구문 - Making Queries

> * **Article.objects.all()**
>   * Article: class name
>   * Object: manager
>   * all(): QuerySet API



### Django Shell

> * 일반 python shell을 통해서는 장고 프로젝트 환경에 접근 불가능
> * 그래서 장고 프로젝트 설정이 load된 python shell을 활용해 DB API 구문 테스트 진행
> * 기본 Django shell 보다 더 많은 기능을 제공하는 shell_plus 사용해 진행
>   * Django-extensions 라이브러리의 기능 중 하나

```python
$ pip install ipython
$ pip install django-extensions

# settings.py
INSTALLED_APPS = [
  ...,
  'django_extensions',
  ...,
]

$ python manage.py shell_plus
```





## CRUD

* 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능인

​		Create, Read, Update, Delete를 묶어서 일컫는 말

### CREATE 관련 메서드

> * **save( )** method
>
>   * saving objests
>   * 객체를 데이터베이스에 저장
>   * 데이터 생성 시 save()를 호출하기 전에는 객체의 ID 값이 무엇인지 알 수 없음
>     * ID 값은 Django가 아니라 DB에서 계산되기 때문에
>   * 단순히 모델를 인스턴스화 하는 것은 DB에 영향을 미치지 않기 때문에 반드시 save!
>
> * str method
>
>   * 표준 파이썬 클래스의 메소드인 str()을 정의하여 각각의 objects가 사람이 읽을 수 있는
>
>     문자열을 반환 하도록 할 수 있음
>
>   * **작성 후 반드시 shell_plus 재시작 해야 함**
>
> ```python
> # 첫 번째 create 방법
> article.title = "첫 번째 제목"
> article.content = "첫 번째 내용"
> 
> # 두 번째 create 방법
>  article = Article(title="두 번째 제목", content="두 번째 내용")
> 
> ### 첫 번째와 두 번째는 save가 필수!
>   
> # 세 번째 create 방법
>  Article.objects.create(title="세 번째 제목", content="세 번째 내용")
> ```



### READ

> * QuerySet API method를 사용해 다양한 조회를 하는 것이 중요
>
> * QuerySet API method의 분류
>
>   * Methods that **return new query sets**
>   * Method that **do not return query sets**
>
> * **all()**: 현재 QuerySet의 복사본을 반환
>
> * **get()**
>
>   * 주어진 lookup 매개변수와 일치하는 객체를 반환
>
>   * 객체를 찾을 수 없으면 DoesNotExist 예외를 발생,
>
>     둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생 시킴
>
>   * 위와 같은 특징을 가지고 있기 때문에 pk와 같이 고유성을 보장하는 조회에서 사용
>
> * **filter()**: 주어진 lookup 매개변수와 일치하는 객체를 포함하는 새 QuerySet을 반환
>
> ```python
> >>Article.objects.all()
> ```



### UPDATE

> ```python
> # 수정하고 싶은 article을 불러옴
> article=Article.objects.get(pk=1)
> 
> # 값을 변경
> article.title = "첫 번째 제목 수정"
> article.content = "첫 번째 내용 수정"
> 
> # 저장
> article.save()
> ```



### DELETE

> * QuerySet의 모든 행에 대해 SQL 삭제 쿼리를 수행
> * 삭제된 객체 수와 객체 유형당 삭제 수가 포함된 딕셔너리 변환
>
> ```python
> # 삭제하고 싶은 article을 불러옴
> article=Article.objects.get(pk=1)
> 
> # 삭제
> article.delete()
> ```



### Field lookups

> * 조회 시 특정 검색 조건을 지정
> * QuerySet 메서드 **filter(), excluude()** 및 **get()**에 대한 키워드 인수로 지정됨
> * example
>   * Article.objects.filter(pk__**gt=2**)
>   * Article.objects.filter(content__**contains='ja'**)



## Admin Site

### Automatic admin interface

> * 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
> * Model class를 admin.py에 등록하고 관리
> * django.contrib.auth 모듈에서 제공됨
> * Record 생성 여부 확인에 매우 유용하며, 직접 record를 삽입할 수도 있음



### admin 생성

> ```python
> $ python manage.py createsuperuser
> ```
>
> * 관리자 계정 생성 후 서버를 실행한 다음 '/admin'으로 가서 관리자 페이지 로그인
>   * 계정만 만든 경우 Django 관리자 화면에서 아무 것도 보이지 않음
> * 내가 만든 Model을 보기 위해서는 admin.py에 작성하여 Django 서버에 등록
> * !주의! auth에 관련된 기본 테이블이 생성되지 않으면 관리자 계정을 생성할 수 없음



### admin 등록

> ```python
> # articles/admin.py
> from django.contib import admin
> from .models import Articel
> 
> # admin site에 register 하겠다
> admin.site.register(Article)
> ```
>
> * admin.py는 관리자 사이트에 Article 객체가 관리자 인터페이스를 가지고 있다는 것을 알려주기 위함
> * models.py에 정의한 __str__의 형태로 객체가 표현됨



### ModelAdmin options

> ```python
> # articles/admin.py
> from django.contib import admin
> from .models import Articel
> 
> class ArticleAdmin(admin.ModelAdmin):
>   list_display = ('pk', 'title', 'content', 'created_at', 'updateed_at')
>  
> admin.site.register(Article, ArticleAdmin)
> ```
>
> * **list_display**: models.py 정의한 각각의 속성(컬럼)들의 값(레코드)을 admin 페이지에 출력하도록 설정



## CRUD with views

### HTTP method

> * **GET**
>   * 특정 리소스를 가져오도록 요청할 때 사용
>   * 반드시 데이터를 가져올 때만 사용해야 함
>   * DB에 변화를 주지 않음
>   * CRUD에서 R역할 담당
> * **POST**
>   * 서버로 데이터를 전송할 때 사용
>   * 리소스를 생성/변경하기 위해 데이터를 HTTP body에 담아 전송
>   * 서버에 변경사항을 만듦
>   * CRUD에서 C/U/D 역학 담당



### 사이트 간 요청 위조(Cross-site request forgery)

> * 웹 애플리케이션 취약점 중 하나로 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여
>
>   특정 웹페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격법
>
> * Django는 CSRF에 대항하여 middleware과 template tag 제공
>
> * CSRF라고도 함



### CSRF 공격 방어

> * Security Token 사용 방식(CSRF Token)
>
>   * 사용자의 데이터에 임의의 난수 값을 부여해,  매 요청마다 난수값을 포함시켜 
>
>     전송시키도록 함
>
>   * 이후 서버에서 요청을 받을 때마다 전달된 token 값이 유효한지 검증
>
> * 일반적으로 데이터 변경이 가능한 POST, PATCH, DELETE Method 등에 적용(GET 제외)
>
> * Django는 CSRF token 템플릿 태그 제공
>
>   ```django
>   {% csrf_token %}
>   ```
>
>   * CSRF 보호에 사용
>   * Input type이 hidden으로 작성되며 value는  django에서 생성한 hash 값으로 설정됨
>   * 해당 캐그 없이 요청을 보낸다면 Djnago 서버는 403 forbidden을 응답



### CsrfViewMiddleware

> * CSRF 공격 관련 보안 설정은 settings.py에서 MIDDLEWARE에 작성 되어 있음
>
> * 실제로 요청 과정에서 urls.py 이전에 Middleware의 설정 사항들을 순차적으로 거치며
>
>   응답은 반대로 하단에서 상단으로 미들웨어를 적용시킴
>
> * Middleware
>
>   * 공통 서비스 및 기능을 애플리케이션에 제공하는 소프트웨어
>
>   * 데이터 관리, 애플리케이션 서비스, 메시징, 인증 밑 API 관리를 주로 미들웨어를 통해 처리
>
>   * 개발자들이 애플리케이션을 보다 효율적으로 구축할 수 있도록 지원하며,
>
>     애플리케이션, 데이터 및 사용자 사이를 연결하는 요소처럼 작동



### Django shortcut function - "redirect()"

> * 새 URL로 요청을 다시 보냄
> * 인자에 따라 HttpResponseRedirect를 반환
> * 브라우저는 현재 경로에 따라 전체 URL 자체를 재구성(reconstruct)
> * 사용가능한 인자
>   * model
>   * view name: viewname can be **URL pattern name** or callable **view object**
>   * absolute or relative URL



### DETAIL

> ```python
> # articles/urls.py
> path('<int:pk>/', views.detail, name='detail'),
> ```
>
> * 개별 게시글 상세 페이지
> * 글의 번호(pk)를 활용해서 각각의 페이지를 따로 구현해야 함
> * 무엇을 활용할 수 있을까? **Variable Routing**
>
> ```python
> # articles/views.py
> def detail(request, pk):
>   article = Article.objects.get(pk=pk)
>   context = {
>     'article': article,
>   }
>   return render(request, 'articles/datail.html', context)
> ```
>
> * 오른쪽 pk는 variable routing을 통해 받은 pk
> * 왼쪽 pk는 DB에 저장된 레코드의 pk(id)
>
> ```python
> def create(request):
>   ...
>   return redirect('articles:detail', article.pk)
> ```



### DELETE

> ```python
> # articles/views.py
> def delete(request, pk):
>   article = Article.objects.get(pk=pk)
>   if request.method == 'POST':
>     article.delete()
>     return redirect('articles:index')
>  	else:
>     return redirect('articles:detail', article.pk)
> ```
>
> * HTTP Method POST시에만 삭제될 수 있도록 조건 설정
