%DNN电感建模
%Author:Liujiangfan 
%Time  :2018.5
%Github:https://github.com/LSayhi
%Addres:SCHOOL OF ELECTRONIC ENGINEERING at BUPT,Beijing ,China


%说明
%输入数据依次为频率（标准化/60G），电感内径（/29.6um），电感线宽(/5.1um)
%输出数据依次为S11模值，S21模值，S11相位（弧度制），S21相位（弧度制）
%输入输出若不标准化则可能导致模型不收敛或收敛变慢

%定义
num_inputlayer=3;%输入参数个数
num_outputlayer=4;%输出参数个数

input_train = traininput(1:num_inputlayer,:);%读入训练集输入
output_train= trainoutput(1:num_outputlayer,:);%读入训练集输出
input_test  = testinput(1:num_inputlayer,:);%读入测试集输入
output_test = testoutput(1:num_outputlayer,:);%读入测试集输出

[inputn,inputps]=mapminmax(input_train);%归一化训练集输入
[outputn,outputps]=mapminmax(output_train);%归一化训练集输出

net=newff(inputn,outputn,[10,10]);
%{'tansig','tansig','purelin'}，激活函数
%设置隐藏层层数和每层神经元数目，输入输出层由数据确定。

net.trainParam.epochs=10000;%最大迭代次数1000
net.trainParam.lr=0.01;%学习率0.1
net.trainParam.goal=0.000001;%目标误差率
% net.divideParam.trainRatio = 60/100;  
% net.divideParam.valRatio = 30/100;  
% net.divideParam.testRatio = 10/100; 
%net.divideFcn = '';
net=train(net,inputn,outputn);%训练设置好的神经网络模型

inputn_test=mapminmax('apply',input_test,inputps);
%测试集输入归一化（按训练集的归一化参数来，不是测试集按自己数据归一化）
an=sim(net,inputn_test);%将测试集输入导入模型net仿真
BPoutput=mapminmax('reverse',an,outputps);
%反归一化测试集输出（按训练集的参数反归一化）


%画直角坐标图
figure(1);
plot(testinput(1,:),BPoutput([1,3],:),'.')%预测S11的幅值和相位
hold on;
plot(testinput(1,:),output_test([1,3],:),'-')%仿真的S11幅值和相位
legend('预测S11mag','预测S11deg','仿真S11mag','仿真S11deg')
title('Simulated S by HFSS and predicted S by neural network')

figure(2);
plot(testinput(1,:),BPoutput([2,4],:),'.')%预测S21的幅值和相位
hold on;
plot(testinput(1,:),output_test([2,4],:),'-')%仿真的S21幅值和相位
legend('预测S21mag','预测S21deg','仿真S21mag','仿真S21deg')
title('Simulated S by HFSS and predicted S by neural network')

%画极坐标图
figure(3);
polar(BPoutput(1,:),BPoutput(3,:),'.');%S11仿真
hold on;
polar(output_test(1,:),output_test(3,:),'-');%S11预测
legend('仿真S11','预测S11')
title('Simulated S by HFSS and predicted S by neural network')

figure(4);
polar(BPoutput(2,:),BPoutput(4,:),'.');%S21仿真
hold on;
polar(output_test(2,:),output_test(4,:),'-');%S21预测
legend('仿真S21','预测S21')
title('Simulated S by HFSS and predicted S by neural network')
