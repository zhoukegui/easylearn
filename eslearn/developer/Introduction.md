# 开发背景
* 机器学习是fMRI未来的一个必然的重要的发展方向，目前形式来看，机器学习是唯一的一个能让fMRI转化到临床的方法。这些临床的应用包括疾病的早期预警、早期诊断、鉴别诊断、疗效预测。除了临床应用外也可以进行症状维度解码和神经机制研究等。
据我所知，大部分fMRI研究人员都有意向将机器学习应用于自己的领域，但是受制于编程和理论知识的缺乏，很难实现。

* 当前，世界上用于fMRI的机器学习软件，我知道的主要有sklearn, nilearn, pyMVPA, Pronto, coSMoMVPA。其中只有Pronto是基于图形界面的，但是Pronto的功能非常少而且方法老旧，不太适用现在的fMRI趋势。 从国家层面看，尽管中国有一些比较好的数据预处理软件，如dpabi, restplut, gretna等，中国现在还没有一款自己开发的机器学习软件包。这一现状体现了供求关系的极度不平衡，即有大量的想使用机器学习的科研人员，但没有国人自己开发并维护的机器学习软件包。试想有一款机器学习软件像dpabi，gretna软件一样方便用户使用，而且能零时差，零距离（微信、QQ等平台），零隔阂（中文或者英文）的把使用过程中出现的问题反映给开发者，然后开发者及时的给用户解决这个问题。通过，这样我们的软件能不断的更新、完善和扩展，也能最程度的让用户接受，并得到广泛的使用。

* 后期，随着软件趋于成熟，我们可以把我们的研究成果发布在软件平台，宣传我们的科研思想，寻找合作伙伴。

* 开发这个软件的目的是为了架起一座机器学习与fMRI的桥梁，连接的是一些成熟的机器学习方法和对编程不熟悉的医生、医学生以及相关科研人员。我们的目标是让不想自己写大量代码或者不太会写代码的人，能简单、方便、可靠且准确无误的将机器学习应用于自己的研究和临床领域。

# <font color=deeppink>如果您能参与，您能做的是什么</font>
* 如果您愿意加入我们，我希望老师能帮我们：
    * <font color=deeppink>在您的圈子里帮我们宣传这个软件</font>
    * <font color=deeppink>安排学生内部测试软件</font>

# 软件介绍
软件主要的功能是组合封装一些成熟的以及最新的机器学习算法，使之能直接应用到fMRI以及radiomics数据。  
#### 主要功能模块
* 数据加载模块  
    * nifti
    * img/hdr
    * cifti
    * dicom
    * text
    * excel
    * csv
    * npy
    * ...
* 特征工程模块
    * 包括特征预处理
    * 特征降维
    * 特征筛选
    * 样本不平衡处理  
* 机器学习模块 
    * 主要负责用户选择机器学习的类型、具体算法和参数
    * 例如选择分类模型，SVM算法以及C的寻优范围    
* 统计模块  
    * 例如置换检验
    * 二项分布建议
    * Pearson相关系数建议
    * 均方误差检验等
    * ...
* 可视化模块
    * 2D 脑可视化
    * 3D 脑可视化
    * 功能连接circos可视化
    * 功能连接矩阵可视化
    * ...

# 软件现状
现阶段，我已经把软件的框架搭建完成，图形界面已经开发了4/5。接下来的工作便是实现底层代码逻辑， 不过这一部分比较快。

# 团队
[current_team_members](./current_team_members.md)
[contributors_lis](./contributors_list.md)
