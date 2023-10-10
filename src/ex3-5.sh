#!/bin/sh
echo "프로그램을 시작합니다."
mf(){
    echo "함수안으로 들어 왔음."
    ls $1
}

mf $1
echo "프로그램을 종료합니다."

exit 0