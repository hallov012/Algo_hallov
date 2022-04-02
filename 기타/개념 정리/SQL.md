## Database

### 데이터베이스(DB)

> * DB는 **체계화된 데이터**의 모임
>
> * 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
>
> * 논리적으로 연관된 (하나 이상의) 자료의 모음,
>
>   그 내용을 고도로 구조화 함으로써 검색, 갱신의 효율화를 꾀한 것
>
> * 즉, **몇 개의 자료 파일을 조직적으로 통합**하여
>
>   **자료 항목의 중복을 없애고 자료를 구조화하여 기억**시켜 놓은 **자료의 집합체**



### 데이터베이스로 얻는 장점들

> * 데이터 중복 최소화
> * 데이터 무결성(정확한 정보 보장)
> * 데이터 일관성
> * 데이터 독립성(물리적/ 논리적)
> * 데이터 표준화
> * 데이터 보안 유지



## RDB

### 관계형 데이터베이스(DB)

> * Relational Database
> * 키와 값들의 간단한 관계를 표 형태로 정리한 데이터베이스
> * 관계형 모델에 기반



### 관계형 데이터베이스 용어 정리

> * 스키마(schema): 데이터베이스에서 자료의 구조, 표현 방법, 관계 등 
>
>   전반적인 **명세를 기술**한 것 
>
> * 테이블(table): 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합
>
> * 열(column): 각 열에는 고유한 데이터 형식이 지정됨
>
> * 행(row): 실제 데이터가 저장되는 형태
>
> * 기본 키(Primary Key): 각 행(레코드)의 고유 값
>
>   * 반드시 설정해야 하며, 데이터베이스 관리 및 관계 설정 시 주요하게 활용 됨



## RDBMS

### 관계형 데이터베이스 관리 시스템 (RDBMS)

> * Relational Database Management System
> * 관계형 모델을 기반으로 하는 데이터베이스 관리시스템
> * example
>   * MySQL, SQLite, PostgreSQL, ORACLE, MS SQL



### SQLite

> 서버 형태가 아닌 파일 형식으로 응용프로그렘에 넣어 사용하는 **비교적 가벼운  데이터베이스**
>
> 구글 안드로이드 운영체제에 기본적으로 탑재, 임베디드 소프트웨어에서도 많이 활용
>
> 로컬에서 간단한 DB 구성 가능, 오픈소스 프로젝트이기 때문에 자유롭게 사용 가능



### SQLite Data Type

> * NULL
> * INTEGER: 크기에 따라 0, 1, 2, 3, 4, 6 또는 8바이트에 저장된 부호 있는 정수
> * REAL: 8바이트 부동 소수점 숫자로 저장된 부동 소수점 값
> * TEXT
> * BLOB: 입력된 그대로 정확히 저장된 데이터(별다른 타입 없이 그대로 저장)



### SQLite Type Affinity

> << Type Affinity : 특정 컬럼에 저장하도록 권장하는 데이터 타입>>
>
> * INTEGER
> * TEXT
> * BLOB
> * REAL
> * NUMERIC



## SQL

### SQL (Structured Quert Language)

> * 관계형 데이터베이스 관리시스템의 **데이터 관리**를 위해 설계된 **특수 목적으로 프로그래밍 언어**
> * 데이터베이스 스키마 생성 및 수정
> * 자료의 검색 및 관리
> * 데이터베이스 객체 접근 조정 관리



### SQL 분류

> * DDL(Data Definition Language) = 데이터 정의 언어
>   * 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어
>   * example
>     * CREATE, DROP, ALTER
> * DML(Data Manipulation Language) = 데이터 조작 언어
>   * 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어
>   * example
>     * INSERT, SELECT, UPDATE, DELETE
> * DCL(Data Control Language) = 데이터 제어 언어
>   * 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어
>   * example
>     * GRANT, REVOKE, COMMIT, ROLLBACK



### SQL Keywords - Data Manipulation Language

> * INSERT: 새로운 데이터 삽입(추가)
> * SELECTL: 저장되어있는 데이터 조회
> * UPDATE: 저장되어있는 데이터 갱신
> * DELETE: 저장되어있는 데이터 삭제



## 테이블 생성 및 삭제

```python
# 데이터베이스 생성하기
$ sqlite3 ().sqlite3
sqlite> .database

# csv 파일을 table로 만들기
sqlite> .mode csv
sqlite> .import (csv파일 이름).csv (table 이름)
sqlite> .tables

# SELECT
sqlite> SELECT * FROM examples;

# (Optional) 터미널 view 변경하기
sqlite> .headers on  	# 제목 출력
sqlite> .mode column	# 줄 맞춤
```



### 테이블 생성 및 삭제 statement

> * CREATE TABL: 데이터베이스에서 테이블 생성
>
>   ```python
>   # 테이블 생성 및 확인하기
>   CREATE TABLE (table 이름) (
>   id INTEGER PRIMARY KEY,
>   name TEXT
>   );
>   sqlite> .tables
>   
>   # 특정 테이블의 schema 조회
>   sqlite> .schema classmates
>   ```
>
> * DROP TABLE: 데이터베이스에서 테이블 제거
>
>   ```python
>   DROP TABLE classmates;
>   ```



## CRUD

## CREATE

### INSERT

> * "Insert a single row into a table"
> * 테이블에 단일 행 삽입
>
> ```python
> INSERT INTO 테이블이름 (컬럼1, 컬럼2, ...) VALUES (값1, 값2, ...);
> ```
>
> * 모든 열에 데이터가 있는 경우 column을 명시하지 않아도 됨
>
> * SQLite는 따로 **PRIMARY KEY 속성의 컬럼을 작성하지 않으면**
>
>   값이 자동으로 증가하는 PK옵션을 가진 **rowid 컬럼을 정의**



## READ

### SELECT satement

> * SELECT
>   * "query data from a table"
>   * 테이블에서 데이터를 조회
>   * SELECT 문은 SQLite에서 가장 복잡한 문이며 다양한 절(clause)와 함께 사용
>     * ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY, ...



### SELECT와 함께 사용하는 clause

> * LIMIT
>   * "constrain the number of rows returned by a query"
>   * 쿼리에서 반환되는 행 수를 제한
>   * 특정 행부터 시작해서 조회하기 위해 **OFFSET** 키워드와 함께 사용하기도 함
> * WHERE
>   * "specify the search condition for rows returned by the query"
>   * 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정
> * DISTINCT
>   * "remove duplicate rows in the result set"
>   * 조회 결과에서 중복 행을 제거
>   * DISTINCT 절은 SELECT 키워드 바로 뒤에 작성해야 함
>
> ```python
> # 모든 컬럼 값이 아닌 특정 컬럼만 조회하기
> SELECT 컬럼1, 컬럼2, ... FROM 테이블이름;
> 
> # LIMIT 
> SELECT 컬럼1, 컬럼2, ... FROM 테이블이름 LIMIT 숫자;
> 
> # OFFSET
> SELECT 컬럼1, 컬럼2, ... FROM 테이블이름 LIMIT 숫자 OFFSET 숫자;
> 
> # WHERE
> SELECT 컬럼1, 컬럼2, ... FROM 테이블이름 WHERE 조건;
> 
> # DISTINCT
> SELECT DISTINCT 컬럼 FROM 테이블이름;
> ```



### [참고] OFFSET

> * 동일 오브젝트 안에서 오브젝트 처음부터 주어진 요소나 지점까지 변위차(위치 변화량)을 
>
>   나타내는 정수형
>
> * example
>
>   * 문자열 'abcdef'에서 문자 'c'는 시작점 'a'에서 2의 OFFSET을 지님
>   * SELECT * FROM MY_TABLE LIMIT 10 **OFFSET 5**
>     * '6번째 행부터 10개 행을 조회'
>     * 0부터 시작함



## DELETE

