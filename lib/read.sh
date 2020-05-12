nly 1 parameter !
#读取预测结果文件给不及格学生发送警告消息
if [ $# != 1 ];then
	echo " Usage: .\read.sh filename!";
    exit
fi

# check the file !
if ! [ -f $1 ];then
    echo "file does not exist!"
    exit
elif ! [ -r $1 ];then
    echo "file can not be read !"
    exit
fi

# PRESS ANY KEY TO CONTITUE !
read -p "begin to read $1 "

# set IFS="\n" , read $1 file per line !
IFS="
"

# i is the line number
zero=0
for line in `cat $1`
do
    if test ${line##*,} -eq ${zero}
	then
	
		user=${line%%,*}
		echo “同学，你有不及格风险，你已经被警告” |write $user >/dev/null 2>&1
		echo "给$user发送警告成功"
	fi
    
done


