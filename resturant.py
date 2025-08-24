class food:
    # Topic refar list of speciacl topic uniqe for each class 
    def __int__(self, name , Cooking_Time , price ,Toping , size ):
        self.name = name
        self.Cooking_Time = Cooking_Time
        self.price  = price
        self.Toping = Toping
        self.size   = size

    def Total_Price(self):
        total_price = self.price
        if  self.size == 's':
            total_price = total_price*0.6
        elif self.size == 'M':
            total_price = total_price*0.8
        elif self.size == 'L':
            total_price = total_price
        if self.Toping == 0:
            return  total_price
        else:
            return total_price +10
    def Timing_Process(self):
         Tp =  self.Cooking_Time
         if  self.size == 's':
            total_price = total_price
         elif self.size == 'M':
            total_price = total_price+5
         elif self.size == 'L':
            total_price = total_price+10
         if self.Toping == 0:
            return   Tp 
    def GetName(self):
        return self.name
    
class main_dish(food):
     def __int__(self,name , Cooking_Time , price ,Toping , size ):
         super ().__init__(self, name , Cooking_Time , price ,Toping , size)

     list_of_Toping = ["none " ,"cheese" , "sauce", "extra beef"]
     def GetName(self):
         x = super ().GetName(self)+"size: "+self.size+"with "+main_dish.list_of_Toping[self.Toping]
         return x 
    

