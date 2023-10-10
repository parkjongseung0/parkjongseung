#!/bin/sh
echo "리눅스가 재밌나요? (yes / no)"
read answer

case $answer in
    yes | y | Y | Yes | YES | yy | yyy | yyyy | yesyesyes | 네)
        echo "yes";;
    no | n | N | No | NO | nn | nnn | nono | nonono | 아니 | 아니요)
        echo "no";;
    *)
        echo "yes or no로 입력해 주세요."
        exit 1;;
esac

exit 0