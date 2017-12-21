%Author:Liujiangfan 
%Time  :2017.12
%@Github:LSayhi
%@SCHOOL OF ELECTRONIC ENGINEERING BUPT
%一个神经网络预测S参数的程序,亦可修改用于其它。
input_neural_num=3;%输入层特征数
output_neural_num=1;%输出层类别数
input_train=traininput(1:input_neural_num,:);%读入训练集输入
output_train=trainoutput(1:output_neural_num,:);%读入训练集输出
input_test=testinput(1:input_neural_num,:);%读入测试集输入
output_test=testoutput(1:output_neural_num,:);%读入测试集输出

[inputn,inputps]=mapminmax(input_train);%归一化训练集输入
[outputn,outputps]=mapminmax(output_train);%归一化训练集输出

net=newff(inputn,outputn,[5,10]);
%设置隐藏层层数和每层神经元数目，输入输出层由数据确定。
net.trainParam.epochs=1000;%最大迭代次数1000
net.trainParam.lr=0.1;%学习率0.1
net.trainParam.goal=0.001;%目标误差率

net=train(net,inputn,outputn);%训练设置好的神经网络模型

inputn_test=mapminmax('apply',input_test,inputps);
%测试集输入归一化（按训练集的归一化参数来，不是测试集按自己数据归一化）
an=sim(net,inputn_test);%将测试集输入导入模型net仿真
BPoutput=mapminmax('reverse',an,outputps);
%反归一化测试集输出（按训练集的参数反归一化）

figure(1);
plot(testinput(1,:),BPoutput(1,:),'.')%画出网络预测的S11幅值的图像
hold on;
plot(testinput(1,:),testoutput(1,:),'-')%画图HFSS仿真的S11幅值的图像
xlabel('frequency/GHz');ylabel('value/dB')
grid on;grid minor;
legend('预测magS11','仿真magS11');
title('Simulated S by HFSS and predicted S by neural network')

