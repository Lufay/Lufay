#/bin/zsh

MYHOST=(
    'work@cq01-testing-ps7169.cq01'
    'root@cq01-testing-ps7169.cq01'
    'work@cp01-qa-bu-qa14-07.cp01'
    'root@cp01-qa-bu-qa14-07.cp01'
    'work@cp01-sys-rath4-c32-qa140.cp01'
    'root@cp01-sys-rath4-c32-qa140.cp01'
    'work@cp01-sys-rath4-c32-qa061.cp01'
    'root@cp01-sys-rath4-c32-qa061.cp01'
    'pangchao01@cq01-mazhe001-3.epc'
    'spider@cp01-cspub.epc'
    'work@cq01-testing-ps6208.cq01'
)

MYCOMMENT=(
    'home,sofa-jenkins'
    ''
    'itlg'
    ''
    'rock'
    ''
    'scholar'
    ''
    'ubm'
    'cspub'
    'xianzhi'
)

MYPASSWD=(
    'ps-testing!!!'
    'Root123@'
    'ps-testing!!!'
    'Lfr@123'
    'ps-testing!!!'
    'Root123@'
    'ps-testing!!!'
    'Root123@'
    'pangchao01@'
    'ps-testing!!!'
    'xianzhi@baidu.com'
)

DEFAULT=0
HLEN=${#MYHOST[@]}
PLEN=${#MYPASSWD[@]}
CLEN=${#MYCOMMENT[@]}
if [ $HLEN -ne $PLEN -o $HLEN -ne $CLEN ]; then
    echo "ERROR: HOST not match PASSWD!" >&2
    exit 1
fi
LEN=$HLEN

function login() {
    if [ ! -z "$2" ]; then
        with_token='
            expect "password:"
            send "liufei'$2'\n"'
    fi
    expect -c '
    spawn -noecho ssh liufei06@relay01.baidu.com'"$with_token"'
    expect "bash-baidu-ssl"
    send "ssh '${MYHOST[$1]}'\n"
    expect "password:"
    send "'${MYPASSWD[$1]}'\n"
    interact'
}

function list() {
    for((i=0;i<$LEN;i++))
    do
        echo -e $i". "${MYHOST[$i]}"\t\t"${MYCOMMENT[$i]}
    done
}

function passwd_map() {
    for((i=0;i<$LEN;i++))
    do
        echo -e $i". "${MYHOST[$i]}"\t\t"${MYPASSWD[$i]}
    done
}

while getopts "lvt:" arg
do
    case $arg in
        l)
            list
            exit
        ;;
        v)
            passwd_map
            exit
        ;;
        t)
            TOKEN=$OPTARG
        ;;
        ?)
            echo "Unknown argument!" >&2
            exit 1
        ;;
    esac
done

shift $[OPTIND-1]

if [ $# -eq 0 ]; then
    login $DEFAULT $TOKEN
elif [ $1 -ge 0 -a $1 -lt $LEN ]; then
    login $1 $TOKEN
else
    echo "Error: specify machine failed!" >&2
    echo "Machine list:" >&2
    list
    exit 1
fi
