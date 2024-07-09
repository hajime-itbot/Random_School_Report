import random


def Performance_Generator(NumberOfStudent) : #任意の数の生徒の名前を生成する関数
    first_names = ["隆", "健太郎", "優生", "康太", "五郎", "玲於奈", "優香", "輪花", "良子", "益男" ,"孝則"]
    last_names = ["佐藤", "鈴木", "高橋", "田中", "渡辺", "伊藤", "山本", "中村", "小林", "加藤"]
    Name_list = {}

    for i in range (NumberOfStudent) : #各生徒と、それに対応するスコアの辞書を生成

        score = [] #三科目のスコアリスト

        for j in range(3) : #三科目のスコアを生成
            score.append(random.randint(0,100))

        Name_list[f"{random.choice(last_names)} {random.choice(first_names)}"] = score #｛任意の名前 : 三科目の得点のリスト｝
    
    return  Name_list



class School_Report :
    def __init__(self,name,score) : #生徒の基本情報
        self.name = name #名前
        self.score = score #点数
        self.Sum_score = sum(self.score) #合計点
        self.Ave_score = float(sum(self.score)/3) #平均点
    
    
    def Show(self) :
        print(f"名前 : {self.name}, 得点 : {self.score}, 合計点 : {self.Sum_score}, 平均点 : {self.Ave_score}\n") #成績表
    

try :
    Num = int(input("任意の生徒数を入力"))
    All_Average = 0 #全体の平均点
    Name_list = Performance_Generator(Num) #名前と得点の辞書

    for name , score in Name_list.items() : #任意の数の生徒のそれぞれの成績表を表示
        Sr = School_Report(name , score)
        Sr.Show()
        All_Average += Sr.Sum_score
    
    
    print("全体の合計点の平均点は{}".format(float(All_Average/Num))) #全体の合計点の平均を表示
        


except ValueError :
    print("数字を入力してください")














