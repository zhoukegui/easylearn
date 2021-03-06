# -*- coding: utf-8 -*-
""" This module is used to train a classification model from given training dataset, then test it using unseen validation dataset.

This module uses grid search or random search strategy combined with pipeline to perform training.
Created on Fri Apr 12 16:25:57 2019
@author: Li Chao
Email:lichao19870617@gmail.com
"""


import sys
import os
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import make_scorer
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA, NMF
from sklearn.feature_selection import SelectKBest, f_classif, RFE
from joblib import Memory
from shutil import rmtree
import nibabel as nib

from eslearn.model_evaluation.el_evaluation_model_performances import eval_performance
from eslearn.feature_engineering.feature_preprocessing.el_preprocessing import Preprocessing
from eslearn.utils.lc_niiProcessor import NiiProcessor


class SvcForGivenTrAndTe():
    """
    Training model on given training data.
    Then apply this mode to another testing data.
    Last, evaluate the performance
    If you encounter any problem, please contact lichao19870617@gmail.com
    """
    def __init__(self,
                # =====================================================================
                # All inputs are follows
                patients_path=r'D:\workstation_b\xiaowei\ToLC\training\BD_label1',  # 训练组病人
                hc_path=r'D:\workstation_b\xiaowei\ToLC\training\MDD__label0',  # 训练组正常人
                val_path=r'D:\workstation_b\xiaowei\ToLC\testing',  # 验证集数据
                val_label=r'D:\workstation_b\xiaowei\ToLC\testing_label.txt',  # 验证数据的label文件
                suffix='.nii',  # 特征文件的尾缀
                mask=r'G:\Softer_DataProcessing\spm12\spm12\tpm\Reslice3_TPM_greaterThan0.2.nii',  # mask
                path_out=r'D:\workstation_b\xiaowei\ToLC',
                n_jobs=1,  # 并行处理使用的线程数目
                
                # 以下参数可以调试
                data_preprocess_method='MinMaxScaler', # OR 'StandardScaler'
                data_preprocess_level='group',  # OR 'subject'
                mask_threshold=0.1,
                search_strategy='random',  # OR 'grid', if your choose 'grid', then the running time is significantly greater than 'random'
                k=5,  # 网格搜索最佳参数时，用几折交叉验证
                n_iter_of_randomedsearch=10,  # When you used randomedSearchCV ('random'), how many iterations to perform random search.
                max_components=0.99,  # PCA参数：最大成分数目
                min_components=0.3,  # PCA参数：最小成分数目
                number_pc=5,      # number_pc=10 PCA参数：参数寻优的候选成分范围内的数目
                
                feature_selection_step=10,  #feature_selection_step=10 特征选择范围内的间隔，间隔越小搜索的特征组合越多
                range_C = np.logspace(-2, 10, 5),  #  np.logspace(-2, 10, 5)代码参与模型搜索的模型包括：支持向量机和逻辑回归，两者超参数C的搜索范围，必须时正数
                range_gamma = np.logspace(-9, 3, 5),  # np.logspace(-9, 3, 5) 代码参与模型搜索的模型包括：支持向量机和逻辑回归，两者超参数gamma的搜索范围
                # =====================================================================
                ):
        
        super().__init__()
        self.patients_path = patients_path
        self.hc_path = hc_path
        self.val_path = val_path
        self.val_label = val_label
        self.suffix = suffix
        self.mask = mask
        self.path_out=path_out
        self.n_jobs = n_jobs

        self.data_preprocess_method=data_preprocess_method
        self.data_preprocess_level=data_preprocess_level
        self.mask_threshold = mask_threshold
        self.search_strategy=search_strategy
        self.k = k
        self.n_iter_of_randomedsearch=n_iter_of_randomedsearch
        self.max_components = max_components
        self.min_components = min_components
        self.number_pc = number_pc
        self.feature_selection_step = feature_selection_step
        self.range_C = range_C
        self.range_gamma = range_gamma

        print("SvcForGivenTrAndTe initiated")
        
    def _load_data_infolder(self):
        """load training data and validation data and generate label for training data"""
        print("loading...")
        # train data
        data1, _ = NiiProcessor().read_multi_nii(self.patients_path, self.suffix)
        data1 = np.squeeze(np.array([np.array(data1).reshape(1,-1) for data1 in data1]))
        data2,_ = NiiProcessor().read_multi_nii(self.hc_path, self.suffix)
        data2 = np.squeeze(np.array([np.array(data2).reshape(1,-1) for data2 in data2]))
        data = np.vstack([data1,data2])
        
        # validation data
        data_validation,self.name_val=NiiProcessor().read_multi_nii(self.val_path, self.suffix)
        data_validation=np.squeeze(np.array([np.array(data_validation).reshape(1,-1) for data_validation in data_validation]))
        
        # data in mask
        mask, self.mask_obj = NiiProcessor().read_sigle_nii(self.mask)
        self.mask_orig = mask>=self.mask_threshold
        self.mask_1d = np.array(self.mask_orig).reshape(-1,)
        
        self.data_train = data[:,self.mask_1d]
        self.data_validation = data_validation[:,self.mask_1d]
        
        # label_tr
        self.label_tr=np.hstack([np.ones([len(data1),]),np.ones([len(data2),]) - 1])
        print("loaded")
        return self

    def pipeline_grid(self, x_train, y_train):
        # Make pipeline

        location = 'cachedir'
        memory = Memory(location=location, verbose=10)
        pipe = Pipeline(steps=[
                ('reduce_dim', 'passthrough'),
                ('feature_selection', 'passthrough'),
                ('estimator', 'passthrough'),
            ], 
            memory=memory
        )

        # Feature reduction parameters
        range_dimreduction = np.linspace(self.min_components, self.max_components, self.number_pc).reshape(self.number_pc,)
        
        # Feature selection parameters
        print("Identifing components after PCA...\n")
        pca = PCA(n_components=self.min_components)
        pca.fit(X=x_train)
        min_number_anova = pca.n_components_
        pca = PCA(n_components=self.max_components)
        pca.fit(X=x_train)
        max_number_anova = pca.n_components_
        range_feature_selection = np.arange(min_number_anova, max_number_anova, self.feature_selection_step)
        
        # Set parameters of gridCV
        print("Setting parameters of gridCV...\n")
        param_grid = [
            {   'reduce_dim':[PCA(iterated_power=7)],
                'reduce_dim__n_components': range_dimreduction,
                'feature_selection':[RFE(estimator=SVC())],
                'feature_selection__n_features_to_select': range_feature_selection,
                'estimator':[SVC()],
                'estimator__kernel': ['rbf', 'linear'],
                'estimator__C': self.range_C,
                'estimator__gamma': self.range_gamma,
                
            }, 
            {   'reduce_dim':[PCA(iterated_power=7)],
                'reduce_dim__n_components': range_dimreduction,
                'feature_selection':[SelectKBest(f_classif)],
                'feature_selection__k': range_feature_selection,
                'estimator':[LogisticRegression()],
                'estimator__penalty': ['l1', 'l2'],
            }, 
        ]
        
        iteration_num = (
            len(range_dimreduction) * len(range_feature_selection) * 2 * len(self.range_C) * len(self.range_gamma) + 
            len(range_dimreduction) * len(range_feature_selection) * 2
        )
        
        # Train
        cv = StratifiedKFold(n_splits=self.k)
        if self.search_strategy == 'grid':
            grid = GridSearchCV(
                pipe, n_jobs=self.n_jobs, param_grid=param_grid, cv=cv, 
                scoring = make_scorer(accuracy_score), refit=True
            )
            print(f"GridSearchCV fitting (about {iteration_num} times iteration)...\n")

        elif self.search_strategy == 'random':
            model = RandomizedSearchCV(
                pipe, n_jobs=self.n_jobs, param_distributions=param_grid, cv=cv, 
                scoring = make_scorer(accuracy_score), refit=True, n_iter=self.n_iter_of_randomedsearch,
            )
        
            print(f"RandomizedSearchCV fitting (about {iteration_num} times iteration)...\n")
        else:
            print(f"Please specify which search strategy!\n")
            return

        model.fit(x_train, y_train)

        # Delete the temporary cache before exiting
        memory.clear(warn=False)
        rmtree(location)

        # In[9]:
        return model

    def tr_te_ev(self):
        """训练，测试，评估
        """
        
        # scale
        prep = Preprocessing(data_preprocess_method='StandardScaler', data_preprocess_level='group')
        data_train, data_validation = prep.data_preprocess(self.data_train, self.data_validation)

        #%% training
        print("training...\nYou need to wait for a while...")
        grid = self.pipeline_grid(data_train, self.label_tr)
        
        pred_train = grid.predict(data_train)
        #TODO: different estimator has different method to get decision
        try:
            dec_train = grid.predict_proba(data_train)[:,1]
        except AttributeError:
            dec_train = grid.decision_function(data_train)

        # fetch orignal weight
        estimator = grid.best_estimator_
        clf = estimator['estimator']
        pca_model = estimator['reduce_dim']
        select_model = estimator['feature_selection']
        
        weight = np.zeros(np.size(select_model.get_support()))
        #TODO: different estimator has different method to get coef.
        # Besides, some estimator have no coef, e.g., rbf svm
        try:
            weight[select_model.get_support()] = clf.coef_[0]
            weight = pca_model.inverse_transform(weight)
            self.weight_3d = np.zeros(self.mask_orig.shape)
            self.weight_3d[self.mask_orig] = weight
            self._weight2nii()
        except AttributeError:
             self.weight_3d = None
             
        # testing
        print("testing...")
        self.predict = grid.predict(data_validation)
        #TODO: different estimator has different method to get decision
        try:
            self.decision = grid.predict_proba(data_validation)
        except AttributeError:
            self.decision = grid.decision_function(data_validation)

        # eval performances
        acc, sens, spec, auc = eval_performance(
            self.label_tr,pred_train,dec_train, 
            accuracy_kfold=None, sensitivity_kfold=None, specificity_kfold=None, AUC_kfold=None,
            verbose=1, is_showfig=False,
        )
        performances_train = [acc, sens, spec, auc]
        print(f"Training performances: {acc, sens, spec, auc}")

        self.val_label=np.loadtxt(self.val_label)
        acc, sens, spec, auc = eval_performance(
            self.val_label,self.predict,self.decision, 
            accuracy_kfold=None, sensitivity_kfold=None, specificity_kfold=None, AUC_kfold=None,
            verbose=1, is_showfig=False,
        )
        performances_val = [acc, sens, spec, auc]
        print(f"Validation performances: {acc, sens, spec, auc}")
        
        # Save performances
        all_per = np.vstack([np.array(performances_train), np.array(performances_val)])
        all_per[np.isnan(all_per)] = 0
        np.savetxt(os.path.join(self.path_out, 'performances.txt'), all_per, fmt="%f", delimiter=",")

    def _weight2nii(self, dimension_nii_data=(61, 73, 61)):
        """Transfer weight matrix to nii file

        I used the mask file as reference to generate the nii file
        """

        # save to nii
        weight_nii = nib.Nifti1Image(self.weight_3d, affine=self.mask_obj.affine)
        weight_nii.to_filename(os.path.join(self.path_out, 'weight.nii'))
    
    def main(self):
        self._load_data_infolder()
        self.tr_te_ev()
    
if __name__=="__main__":
    svc=SvcForGivenTrAndTe()
    svc.main()
    print("Done!\n")
