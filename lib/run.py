#!/bin/python
# coding=<encoding name>
import pandas as pd 
import numpy as np 
from pandas import set_option 
from sklearn.externals import joblib
import datetime 
from dateutil import parser
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report 
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score
from datetime import timedelta 

#模型导入
model_DT = joblib.load('DT.model')
model_LR = joblib.load('LR.model')


#behavior_path = input('请输入学生行为数据路径：')
behavior_path = 'wtmp-users.csv'
behavior_path = open(behavior_path)

data = pd.read_csv(behavior_path, delimiter=',', header=None, names=['type','pid', 'tty', 'user', 'host', 'entry','timeval'])

behavior_path.close()#关闭流

data['entry'] = [parser.parse(i) for i in data['entry']]#时间格式纠正
#将type7和8的数据分别分出来
data_t7 = data[data.type == 7] 
data_t8 = data[data.type == 8] 
data_t8_merge = data_t8[['pid','entry']]#只抽取出类型8的pid和entry

data_merge = pd.merge(data_t7, data_t8_merge, on=['pid'])#同一进程号pid连接

data_merge['stay'] = data_merge.entry_y - data_merge.entry_x#猜测：计算学习时间

hours = timedelta(hours=2)#时间差为2小时
data_merge=data_merge.drop(data_merge[[i.days<0 for i in data_merge.stay]].index)#去除天数为负的数据
data_merge=data_merge.drop(data_merge[[i>hours for i in data_merge.stay]].index)#去除时间差大于2小时的数据

#去除重复值
pid = (data_merge.groupby(['pid']).size()>2)#pid值超过一次出现的
pid_true = pid[pid==True]#计下出现超过一次的pid
count = data_merge.groupby(['pid']).size().values#记录data_merge数据中各个pid出现的次数

data_result= data_merge.drop_duplicates(['entry_x','entry_y'])#去除entry_x和entry_y重复的的行
data_result = data_result.drop(['tty','type','timeval'],axis=True)#去除不需要的列
data_result = data_result.rename(columns={'entry_x':'entry','entry_y':'leave'})#列名重命名，进入时间与出去时间标明
data_result.user = data_result.user.astype('int64')#将user列属性转为整型


merge_score = data_result

#构造学习时段特征
def isWeekend(dayOfWeek): 
    return (dayOfWeek>4) 
def isWeekday(dayOfWeek): 
    return (not isWeekend(dayOfWeek)) 
def countWeekends(dates): 
    weekends = [ isWeekend(date.weekday()) for date in dates ] 
    return sum(weekends) 
def countWeekdays(dates): 
    weekdays = [ isWeekday(date.weekday()) for date in dates ] 
    return sum(weekdays)

def isDaytime(hour): 
    return (hour>9 and hour<17) 
def isNight(hour): 
    return (not isDaytime(hour)) 
def countDaytimes(dates): 
    daytimes = [ isDaytime(date.hour) for date in dates ] 
    return sum(daytimes) 
def countNights(dates): 
    nights = [ isNight(date.hour) for date in dates ] 
    return sum(nights)

#各个特征名初始化
users = []
logins = [] 
hosts = [] 
maxstays = []
meanstays = [] 
totalstays = []
weekends = [] 
weekdays = [] 
daytimes = [] 
nights = []

for user, groupScore in merge_score.groupby('user'): 
    users.append(user)
    
    logins.append(len(groupScore)) 
    hosts.append(np.unique(groupScore.host).size) 
    maxstays.append(max(groupScore.stay)) 
    meanstays.append(np.mean(groupScore.stay)) 
    totalstays.append(sum([stay.seconds for stay in groupScore.stay]))
    
    weekends.append(countWeekends(groupScore.entry)) 
    weekdays.append(countWeekdays(groupScore.entry)) 
    daytimes.append(countDaytimes(groupScore.entry)) 
    nights.append(countNights(groupScore.entry))
    
#重构特征数据
data = pd.DataFrame() 
data['user'] = np.array(users) 
data['logins'] = np.array(logins) 
data['hosts'] = np.array(hosts) 
data['maxstays'] = np.array(maxstays) 
data['meanstays'] = np.array(meanstays) 
data['totalstays'] = np.array(totalstays) 
data['weekends'] = np.array(weekends) 
data['weekdays'] = np.array(weekdays) 
data['daytimes'] = np.array(daytimes) 
data['nights'] = np.array(nights)

#各个占比
data['weekends_pct']= np.array(weekends)/(np.array(weekends)+np.array(weekdays)) 
data['weekdays_pct']= np.array(weekdays)/(np.array(weekends)+np.array(weekdays)) 
data['daytimes_pct']= np.array(daytimes)/(np.array(daytimes)+np.array(nights)) 
data['nights_pct']= np.array(nights)/(np.array(daytimes)+np.array(nights)) 
data['meanstay_pct']= np.array(meanstays)/np.array(totalstays)

#将最终成绩与上述构造特征合起来
merge_behavior = data

merge_behavior['meanstays'] = np.array([td.seconds for td in merge_behavior.meanstays])#平均学习时间，以秒计算
merge_behavior['maxstays'] = np.array([td.seconds for td in merge_behavior.maxstays]) #最久学习时间，以秒计算

data_behavior = merge_behavior.drop(['meanstay_pct'],axis=True) #去除无用列


X = data_behavior.iloc[:,1:]
pass_rate = model_LR.predict_proba(X)[:,1]
is_pass = model_DT.predict(X)

predict_result = pd.DataFrame()
predict_result['user'] = data_behavior['user']
#np.set_printoptions(precision = 2)
predict_result['pass_rate'] =np.around(pass_rate,decimals=2)
predict_result['is_pass'] = is_pass
predict_result.to_csv('predict_result.csv',encoding='utf-8',index=False)
print('预测结果已经输出至predict_result.csv')
