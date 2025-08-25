# KKCompany_Music_Challenge
A competition for predicting the next five songs a user will listen to  

KKCompany舉辦的邀請制音樂預測比賽，參賽者必須根據資料集中每個使用者聽的前20首歌，預測他後5首會聽什麼歌  
細節與資料集在以下Kaggle連結:  
https://www.kaggle.com/competitions/datagame-2023/overview  
  
本組在比賽中獲得前27.8%的成績    
    
### 方法簡介
透過觀察得知許多人們會重複聆聽相同的歌曲，因此若在前20首中有同首歌重複聆聽，將優先預測他會聆聽相同歌曲，否則則透過相似度加上隨機抽選進行預測
