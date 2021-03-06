# 목차
- [유투브 링크](https://youtu.be/j4O1nrworMU)
- [목차](#목차)
- [목적](#목적)
- [목표](#목표)
- [준비](#준비)
- [실행](#실행)
- [삭제](#삭제)
- [테라폼 스크립트 상세설명](#테라폼-스크립트-상세설명)
- [참고자료](#참고자료)

<br>

# 목적
* 테라폼으로 EC2 인스턴스와 AMI를 생성한다.

<br>

# 목표
* 테라폼으로 EC2 인스턴스를 생성할 수 있다.
* EC2인스턴스 원격접속을 위해 공개키 인증방식을 적용할 수 있다.
* 테라폼으로 EC2 인스턴스 user-data를 설정할 수 있다.
* 테라폼으로 AMI를 생성할 수 있다. 

<br>

# 준비
* 테라폼 설치
* aws 접속 정보를 환경변수로 설정
```sh
export AWS_ACCESS_KEY_ID="<AWS_ACCESS_KEY_ID>"
export AWS_SECRET_ACCESS_KEY="<AWS_SECRET_ACCESS_KEY>"
export AWS_DEFAULT_REGION="ap-northeast-2"
```
* ssh 키쌍 생성
```
ssh-keygen -t rsa -b 4096 -N "" -f test
```

<br>

# 실행
```sh
terraform init
terraform apply
```

<br>

# 삭제
```sh
terraform destroy
```

<br>

# 테라폼 스크립트 상세설명
* pdf참고 챕터2-AMI생성 챕터 참고: [pdf링크](../terraform-aws.pdf)

<br>

# 참고자료
* [블로그-provisioner](https://blog.outsider.ne.kr/1342)
* [terraform 공식문서-connection](https://www.terraform.io/docs/language/resources/provisioners/connection.html)
* [terraform 공식문서-provisioners](https://www.terraform.io/docs/language/resources/provisioners/syntax.html)
* [terrafrom 공식문서-aws_instance](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance)
* [블로그-apache2 권한설정](https://stackoverflow.com/questions/50378664/permission-denied-inside-var-www-html-when-creating-a-website-and-its-files-wi/50379288)
* [블로그-apache2 권한설정](https://itreport.tistory.com/630)
* [aws ubuntu AMI untill](https://stackoverflow.com/questions/42279763/why-does-terraform-apt-get-fail-intermittently)
* [ubuntu ami finder](https://cloud-images.ubuntu.com/locator/ec2/)
* [terraform 공식문서-aws_ami_from_instance](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ami_from_instance)