#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import ast
import pandas as pd
from math import factorial,e 
from numpy import sin, arcsin, arctan, cos, arccos , tan, sqrt , log as ln, tanh, cosh, sinh, log10 as log, arctanh, arccosh, arcsinh
from matplotlib import pyplot as plt
from tkinter import *
from tkinter import filedialog, messagebox, Scrollbar, Canvas, Frame, Text
from sklearn.linear_model import LogisticRegression, LinearRegression
π = np.pi
Exp = 10


class Calculator():
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculator")
        self.window.geometry("520x600")
        self.window.resizable(True,True);
        self.window.configure(background="snow")
        self.screen_text = StringVar()
        self.expression =""
        self.simple()
        self.window.mainloop()

    def simple(self):
        self.clear(self.window)
        self.column_config(5)
        self.screen1 = Entry(self.window,font=("comic",20,"bold"),width=25,borderwidth=1,textvariable=self.screen_text)
        self.buttom0 = Button(self.window,text="0",bg="DeepSkyBlue2",height=4,width=3,command=lambda :self.click(0)).grid(row=4,column=0,pady=5,padx=5,stick=E+W)
        self.buttom1 = Button(self.window,text="1",bg="DeepSkyBlue2",height=4,width=3,command=lambda :self.click(1)).grid(row=3,column=0,pady=5,padx=5,stick=E+W)
        self.buttom2 = Button(self.window,text="2",bg="DeepSkyBlue2",height=4,width=3,command=lambda :self.click(2)).grid(row=3,column=1,pady=5,padx=5,stick=E+W)
        self.buttom3 = Button(self.window,text="3",bg="DeepSkyBlue2",height=4,width=2,command=lambda :self.click(3)).grid(row=3,column=2,pady=5,padx=5,stick=E+W)
        self.buttom4 = Button(self.window,text="4",bg="DeepSkyBlue2",height=4,width=3,command=lambda :self.click(4)).grid(row=2,column=0,pady=5,padx=5,stick=E+W)
        self.buttom5 = Button(self.window,text="5",bg="DeepSkyBlue2",height=4,width=3,command=lambda :self.click(5)).grid(row=2,column=1,pady=5,padx=5,stick=E+W)
        self.buttom6 = Button(self.window,text="6",bg="DeepSkyBlue2",height=4,width=3,command=lambda :self.click(6)).grid(row=2,column=2,pady=5,padx=5,stick=E+W)
        self.buttom7 = Button(self.window,text="7",bg="DeepSkyBlue2",height=4,width=3,command=lambda :self.click(7)).grid(row=1,column=0,pady=5,padx=5,stick=E+W)
        self.buttom8 = Button(self.window,text="8",bg="DeepSkyBlue2",height=4,width=3,command=lambda :self.click(8)).grid(row=1,column=1,pady=5,padx=5,stick=E+W)
        self.buttom9 = Button(self.window,text="9",bg="DeepSkyBlue2",height=4,width=3,command=lambda :self.click(9)).grid(row=1,column=2,pady=5,padx=5,stick=E+W)
        self.buttomPoint = Button(self.window,text=".",bg="DeepSkyBlue2",height=4,width=3,command=lambda :self.click(".")).grid(row=4,column=1,pady=5,padx=5,stick=E+W)
        self.buttomPI = Button(self.window,text="π",bg="DeepSkyBlue2",height=4,width=3,command=lambda :self.click("π")).grid(row=4,column=2,pady=5,padx=5,stick=E+W)
        self.buttomAC = Button(self.window,text="AC",bg="DarkOrange3",height=4,width=3,command=lambda :self.clear_input()).grid(row=1,column=4,pady=5,padx=5,stick=E+W)
        self.buttomDEl = Button(self.window,text="DEL",bg="DarkOrange3",height=4,width=3,command=lambda:self.delete()).grid(row=1,column=3,pady=5,padx=5,stick=E+W)
        self.buttomSum = Button(self.window,text="+",bg="DarkOrange3",height=4,width=3,command=lambda:self.click("+")).grid(row=3,column=3,pady=5,padx=5,stick=E+W)
        self.buttomRes = Button(self.window,text="-",bg="DarkOrange3",height=4,width=3,command=lambda:self.click("-")).grid(row=3,column=4,pady=5,padx=5,stick=E+W)
        self.buttomMul = Button(self.window,text="*",bg="DarkOrange3",height=4,width=3,command=lambda:self.click("*")).grid(row=2,column=3,pady=5,padx=5,stick=E+W)
        self.buttomDiv = Button(self.window,text="/",bg="DarkOrange3",height=4,width=3,command=lambda:self.click("/")).grid(row=2,column=4,pady=5,padx=5,stick=E+W)
        self.buttomAns = Button(self.window,text="=",bg="DarkOrange3",height=4,width=3,command=lambda:self.term()).grid(row=5,column=2,pady=5,padx=5,stick=E+W)
        self.buttomPow = Button(self.window,text="^",bg="DarkOrange3",height=4,width=3,command=lambda:self.click("**")).grid(row=4,column=3,pady=5,padx=5,stick=E+W)
        self.buttomSqrt = Button(self.window,text="√",bg="DarkOrange3",height=4,width=3,command=lambda:self.click("sqrt(")).grid(row=4,column=4,pady=5,padx=5,stick=E+W)
        self.buttomEuler = Button(self.window,text="e",bg="DeepSkyBlue2",height=4,width=3,command=lambda:self.click("e")).grid(row=5,column=0,pady=5,padx=5,stick=E+W)
        self.buttomEXP = Button(self.window,text="E",bg="DarkOrange3",height=4,width=3,command=lambda:self.click("*Exp**")).grid(row=5,column=1,pady=5,padx=5,stick=E+W)
        self.buttom_Start_Parenthesis = Button(self.window,text="(",bg="DarkOrange3",height=4,width=3,command=lambda:self.click("(")).grid(row=5,column=3,pady=5,padx=5,stick=E+W)
        self.buttom_End_Parenthesis= Button(self.window,text=")",bg="DarkOrange3",height=4,width=3,command=lambda:self.click(")")).grid(row=5,column=4,pady=5,padx=5,stick=E+W)
        self.button_adv = Button(self.window,text="Advanced Options",bg="DarkOrange3",height=3,width=15,command=lambda:self.advanced()).grid(row=2, column=5,pady=5,padx=5,stick=E+W)
        self.button_cons = Button(self.window,text="Constants",bg="DarkOrange3",height=3,width=15,command=lambda:self.constants()).grid(row=3, column=5, pady=5,padx=5,stick=E+W)
        self.button_scien = Button(self.window,text="Scientific",bg="DarkOrange3",height=3,width=15,command=lambda:self.scientific()).grid(row=1, column=5, pady=5,padx=5,stick=E+W)
        self.screen1.grid(row=0,column=0,columnspan=5,padx=8,pady=5,stick=E+W)
       
        
       
    def column_config(self, n):
        for i in range(6):
            if i<=n :
                self.window.grid_columnconfigure(i, weight=1)
            else:
                self.window.grid_columnconfigure(i, weight=0) 
        
    def clear_input(self):
        self.expression = ""
        self.screen_text.set(" ")

        
    def delete(self):

        self.expression = self.expression[:(len(self.expression)-1)]
        self.screen_text.set(self.expression)
        
    def click(self,button_press):
        self.expression = self.screen1.get()

        self.expression += str(button_press)
        self.screen_text.set(self.expression)
        
    def term(self):
        self.expression = self.screen1.get()
        try:
            Term = str(eval(self.expression))
            self.expression = Term
        except ZeroDivisionError:
            Term = "math ERROR"
        except:
            Term = "syntax ERROR"
        self.screen_text.set(Term) 

    def to_classes(self,df):
        self.class_dict ={}
        self.from_class_dict={}
        y= []
        for i,x in enumerate(set(df.iloc[:,-1])):
            self.class_dict[x] = i
            self.from_class_dict[i] = x
        for x in df.iloc[:,-1]:
            y.append(self.class_dict[x])
        return np.array(y)
            
            
        
    def fill(self, df):
        X,y = [],[]
        for i in range(len(df.values)):
            a = df.loc[i].values.flatten().tolist()
            X.append(a[:len(a)-2])
            y.append(a[-1])
        return np.array(X), y
        
    def regression(self,reg):
        self.clear(self.window)
        self.column_config(3)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.advanced()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.label_regression = Label(self.window, text="type predict data").grid(row=1,column=0,stick=E+W)
        self.entry_regression = Entry(self.window,font=("comic",20,"bold"),width=25,borderwidth=1)
        self.entry_regression.grid(row=1,column=1,columnspan=2,stick=E+W)
        self.button_load = Button(self.window,text="Load csv",bg="firebrick2",height=3,width=15,command=lambda:self.load()).grid(row=2, column=1, pady=30,padx=10,stick=E+W)
        if reg:
            self.button_log_reg_show=Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.log_reg_show()).grid(row=2, column=2, pady=30,padx=10,stick=E+W)
        else:
            self.button_lin_reg_show=Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.lin_reg_show()).grid(row=2, column=2, pady=30,padx=10,stick=E+W)
    	
    def load(self):
    	self.file_path_regression = filedialog.askopenfilename()
    	
    def log_reg_show(self):
    	try:
	    	df = pd.read_csv(self.file_path_regression)
	    	X, y = self.fill(df)
	    	y = self.to_classes(df)
	    	
	    	clf = LogisticRegression(random_state=0).fit(X, y)
	    	regression_a= f"np.array([[{self.entry_regression.get()}]])"
	    	pred = eval(regression_a)
	    	regresion_label=Label(self.window,text=f"Predicted --> {self.from_class_dict[clf.predict(pred)[0]]}").grid(row=3, column=1, pady=30,padx=10)
    	except:
    		messagebox.showerror(title="Error",message="Couldn't load csv")

    def lin_reg_show(self):
    	try:
    		df = pd.read_csv(self.file_path_regression)
    		X, y= self.fill(df)
	    	try:
	    		y=np.array(y)
		    	clf = LinearRegression().fit(X, y)
		    	a= f"np.array([[{self.entry_regression.get()}]])"
		    	pred = eval((a))
		    	regresion_label=Label(self.window,text=f"Predicted --> {clf.predict(pred)[0]}").grid(row=3, column=0, pady=30,padx=10)
	    	except:
	    		messagebox.showerror(title="Error",message="Train data must be of type 'int' or 'float' ")
    	except:
    		messagebox.showerror(title="Error",message="Couldn't load csv")
    	
    	
    	
            
    def graph(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.advanced()).grid(row=4, column=2, pady=300,padx=10,stick=E+W)
        self.label_start = Label(self.window, text="Start").grid(row =0, column=0,stick=E+W)
        self.entry_start=Entry(self.window,font=("comic",20,"bold"),width=30,borderwidth=1)
        self.entry_start.grid(row=0,column=1,columnspan=3,stick=E+W)
        self.label_end= Label(self.window, text="End").grid(row =1, column=0,stick=E+W)
        self.entry_end=Entry(self.window,font=("comic",20,"bold"),width=30,borderwidth=1)
        self.entry_end.grid(row=1,column=1,columnspan=3,stick=E+W)
        self.label_function = Label(self.window,text="Fuction").grid(row=2,column=0,stick=E+W)
        self.entry_function = Entry(self.window,font=("comic",20,"bold"),width=30,borderwidth=1)
        self.entry_function.grid(row=2,column=1,columnspan=3,stick=E+W)
        self.button_graphs=Button(self.window,text="GRAPH",bg="firebrick2",height=3,width=15,command=lambda:self.plotting(self.entry_start.get(),self.entry_end.get(),self.entry_function.get())).grid(row=3, column=1, pady=30,padx=10,stick=E+W)
        
                
    def plotting(self,start,end,fuction):
        x = np.linspace((int)(start),(int)(end))
        plt.plot(x, ast.literal_eval(fuction))
        plt.xlabel('x axis')
        plt.ylabel('y axis')
        plt.axis('tight')
        plt.show()
        
    def stat(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.advanced()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_binomial=Button(self.window,text="binomial",bg="orange",height=3,width=15,command=lambda:self.dist_binomial()).grid(row=1, column=0, pady=30,padx=10,stick=E+W)
        self.button_hypergeometric=Button(self.window,text="hypergeometric",bg="orange",height=3,width=15,command=lambda:self.dist_hypergeometric()).grid(row=1, column=1, pady=30,padx=10,stick=E+W)
        self.button_poisson=Button(self.window,text="poisson",bg="orange",height=3,width=15,command=lambda:self.dist_poisson()).grid(row=2, column=0, pady=30,padx=10,stick=E+W)
        self.button_discrete=Button(self.window,text="discrete",bg="orange",height=3,width=15,command=lambda:self.dist_discrete()).grid(row=2, column=1, pady=30,padx=10,stick=E+W)

    def dist_binomial(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.stat()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.entry_binomial = Entry(self.window,font=("comic",20,"bold"),width=30,borderwidth=1)
        self.entry_binomial.grid(row=0,column=1,columnspan=3,stick=E+W)
        self.button_ok = Button(self.window,text="OK",bg="orange",height=3,width=15,command=lambda:self.binomial()).grid(row=2, column=0, pady=30,padx=10,stick=E+W)

    def binomial(self):
        temp = ast.literal_eval("["+self.entry_binomial.get()+"]")
        n, x, p = temp[0], temp[1], temp[2]
        self.result = factorial(n)/(factorial(n-x)*factorial(x))*(p**x)*(1-p)**(n-x)
        self.label_result = Label(self.window,text = f"x~B()= {self.result}").grid(row=3, column=1)

    def dist_hypergeometric(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.stat()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.label_inst = Label(self.window,text="x,N,k,n").grid(row=0,column=0)
        self.entry_hypergeometric = Entry(self.window,font=("comic",20,"bold"),width=30,borderwidth=1)
        self.entry_hypergeometric.grid(row=0,column=1,columnspan=3,stick=E+W)
        self.button_ok = Button(self.window,text="OK",bg="orange",height=3,width=15,command=lambda:self.hyper_geo()).grid(row=2, column=0, pady=30,padx=10,stick=E+W)

    def comb(self,x,y): 
        return factorial(x)/(factorial(x-y)*factorial(y)) 
   
    def poisson(self):
        temp = ast.literal_eval("["+self.entry_poisson.get()+"]")
        x,l = temp[0], temp[1] 
        result=(e**-l*l**x)/factorial(x) 
        label_result = Label(self.window,text = f"x~P()= {result}").grid(row=3, column=1)
    
    def hyper_geo(self):
        temp = ast.literal_eval("["+self.entry_hypergeometric.get()+"]")
        x,N,k,n = temp[0], temp[1], temp[2], temp[3] 
        result=(self.comb(k,x)*self.comb(N-k,n-x))/self.comb(N,n)
        label_result = Label(self.window,text = f"x~H()= {result}").grid(row=3, column=1)

    def var_discrete(self):
        temp = ast.literal_eval("["+self.entry_discrete.get()+"]")
        x,y = temp[0], temp[1] 
        E = sum([xi*yi for xi,yi in zip(x,y)]) 
        V = sum([(xi-E)**2 *yi for xi,yi in zip(x,y) ]) 
        label_result = Label(self.window,text = f"E= {E} V= {V}").grid(row=3,column=1)

    def dist_poisson(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.stat()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.label_inst = Label(self.window,text="x,l").grid(row=0,column=0)
        self.entry_poisson = Entry(self.window,font=("comic",20,"bold"),width=30,borderwidth=1)
        self.entry_poisson.grid(row=0,column=1,columnspan=3,stick=E+W)
        self.button_ok = Button(self.window,text="OK",bg="orange",height=3,width=15,command=lambda:self.poisson()).grid(row=2, column=0, pady=30,padx=10,stick=E+W)

    def dist_discrete(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.stat()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.label_inst = Label(self.window,text="x,y").grid(row=0,column=0)
        self.entry_discrete = Entry(self.window,font=("comic",20,"bold"),width=30,borderwidth=1)
        self.entry_discrete.grid(row=0,column=1,columnspan=3,stick=E+W)
        self.button_ok = Button(self.window,text="OK",bg="orange",height=3,width=15,command=lambda:self.var_discrete()).grid(row=2, column=0, pady=30,padx=10,stick=E+W)

    def circuits(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.advanced()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_resistance_eq=Button(self.window,text="equivalent resistance",bg="orange",height=3,width=15,command=lambda:self.resistance_equivalent()).grid(row=0, column=0, pady=30,padx=10,stick=E+W)
        self.button_vol_curr=Button(self.window,text="vol/curr divider",bg="orange",height=3,width=15,command=lambda:self.divisor()).grid(row=1, column=0, pady=30,padx=10,stick=E+W)
        self.button_capacitor_eq=Button(self.window,text="capacitor",bg="orange",height=3,width=15,command=lambda:self.capacitance()).grid(row=0, column=1, pady=30,padx=10,stick=E+W)
    
    def resistance_equivalent(self):
        self.clear(self.window)
        self.column_config(3)
        self.button_return=Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.circuits()).grid(row=5, column=1, pady=100,stick=E+W)
        self.parallel=Label(self.window, text="type resistances").grid(row =0, column=0,stick=E+W)
        self.entry_resistance1=Entry(self.window,font=("comic",20,"bold"),width=25,borderwidth=1)
        self.entry_resistance2=Entry(self.window,font=("comic",20,"bold"),width=25,borderwidth=1)
        self.entry_resistance1.grid(row=1,column=0,columnspan=2,pady=10,padx = 5,stick=E+W)
        self.entry_resistance2.grid(row=2,column=0,columnspan=2,pady=10, padx = 5,stick=E+W)
        self.button_parallel_resistance=Button(self.window,text="parallel",bg="firebrick2",height=3,width=15,command=lambda:self.equivalent_parallel()).grid(row=3, column=0,stick=E+W)
        self.button_serie_resistance=Button(self.window,text="serie",bg="yellow green",height=3,width=8,command= lambda:self.equivalent_serie()).grid(row=3, column=1,stick=E+W)
        

    def equivalent_parallel(self):
        self.result = 1/((1/(int)(self.entry_resistance1.get()))+(1/(int)(self.entry_resistance2.get())))
        self.label_result_parallel = Label(self.window, text = f"Req = {self.result}").grid(row=4, column=0,stick=E+W)

    def equivalent_serie(self):
        self.result = (int)(self.entry_resistance1.get())+(int)(self.entry_resistance2.get())
        self.label_result_parallel = Label(self.window, text = f"Req = {self.result}").grid(row=5, column=1,stick=E+W)

    def capacitance(self):
        self.clear(self.window)
        self.column_config(3)
        self.button_return=Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.circuits()).grid(row=6, column=1, pady=100,stick=E+W)
        self.parallel=Label(self.window, text="type capacitors").grid(row =0, column=0,stick=E+W)
        self.entry_resistance1=Entry(self.window,font=("comic",20,"bold"),width=25,borderwidth=1)
        self.entry_resistance2=Entry(self.window,font=("comic",20,"bold"),width=25,borderwidth=1)
        self.entry_resistance1.grid(row=1,column=0,columnspan=2,pady=10,padx = 5,stick=E+W)
        self.entry_resistance2.grid(row=2,column=0,columnspan=2,pady=10, padx = 5,stick=E+W)
        self.button_parallel_resistance=Button(self.window,text="parallel",bg="firebrick2",height=3,width=15,command=lambda:self.equivalent_serie()).grid(row=3, column=0,stick=E+W)
        self.button_serie_resistance=Button(self.window,text="serie",bg="yellow green",height=3,width=8,command= lambda:self.equivalent_parallel()).grid(row=3, column=1,stick=E+W)
        
    def divisor(self):
        self.clear(self.window)
        self.column_config(3)
        self.button_return=Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.circuits()).grid(row=6, column=1, pady=100,stick=E+W)
        self.label_vol_curr=Label(self.window, text="type voltage or current").grid(row =0, column=0,stick=E+W)
        self.label_resistance=Label(self.window, text="resistance").grid(row=1,column=0,stick=E+W)
        self.label_eq_resistance=Label(self.window, text="sum resistance").grid(row=2, column=0,stick=E+W)
        self.entry_vol_curr=Entry(self.window,font=("comic",20,"bold"),width=25,borderwidth=1)
        self.entry_resistance1=Entry(self.window,font=("comic",20,"bold"),width=25,borderwidth=1)
        self.entry_resistance2=Entry(self.window,font=("comic",20,"bold"),width=25,borderwidth=1)
        self.entry_vol_curr.grid(row=0,column=1,columnspan=2,pady=10,padx = 5,stick=E+W)
        self.entry_resistance1.grid(row=1,column=1,columnspan=2,pady=10, padx = 5,stick=E+W)
        self.entry_resistance2.grid(row=2,column=1,columnspan=2,pady=10, padx = 5,stick=E+W)
        self.button_divirsor=Button(self.window,text="OK",bg="firebrick2",height=3,width=15,command=lambda:self.divisor_vol_curr()).grid(row=3, column=0,stick=E+W)
        
    def divisor_vol_curr(self):
        self.result = (int(self.entry_resistance1.get())/(int(self.entry_resistance1.get())+int(self.entry_resistance2.get())))*int(self.entry_vol_curr.get())
        self.label_result_parallel = Label(self.window, text = f"result = {self.result}").grid(row=5, column=1,stick=E+W)

    def physics(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.advanced()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_mecanics=Button(self.window,text="equivalent resistance",bg="orange",height=3,width=15,command=lambda:self.mecanics()).grid(row=0, column=0, pady=30,padx=10,stick=E+W)
        self.button_electro=Button(self.window,text="vol/curr divider",bg="orange",height=3,width=15,command=lambda:self.electro()).grid(row=1, column=0, pady=30,padx=10,stick=E+W)

    def mecanics(self):
        self.clear(self.window)
        self.entry_move = Entry(self.window,font=("comic",20,"bold"),width=25,borderwidth=1)
        self.entry_move.grid(row=0,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.button_ok = Button(self.window,text="OK",bg="firebrick2",height=3,width=15,command=lambda:self.calculate_move()).grid(row=2, column=1,stick=E+W)

    def calculate_move(self):
        temp = ast.literal_eval("["+self.entry_move.get()+"]")
        xo, vo, t, a = temp[0], temp[1], temp[2], temp[3]
        result = xo + vo*t +((a*t**2)/2)
        label_result = Label(self.window,text = f"xf = {result}").grid(row=3,column=1)

         
        
    def linear_algebra(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.advanced()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_cross=Button(self.window,text="cross",bg="orange",height=3,width=15,command=lambda:self.do_cross()).grid(row=0, column=0, pady=30,padx=10,stick=E+W)
        self.button_transpose=Button(self.window,text="transpose",bg="orange",height=3,width=15,command=lambda:self.do_transpose()).grid(row=1, column=0, pady=30,padx=10,stick=E+W)
        self.button_determinant=Button(self.window,text="determinant",bg="orange",height=3,width=15,command=lambda:self.do_determinant()).grid(row=0, column=1, pady=30,padx=10,stick=E+W)
        self.button_determinant=Button(self.window,text="multiplication",bg="orange",height=3,width=15,command=lambda:self.do_mult_matrix()).grid(row=1, column=1, pady=30,padx=10,stick=E+W)

    def do_cross(self):
        self.clear(self.window)
        self.column_config(3)
        self.entry_vector1 = Entry(self.window,font=("comic",20,"bold"),width=25,borderwidth=1)
        self.entry_vector2 = Entry(self.window,font=("comic",20,"bold"),width=25,borderwidth=1)
        self.entry_vector1.grid(row=0,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.entry_vector2.grid(row=1,column=0,columnspan=2, stick=E+W,pady=10,padx=5) 
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.advanced()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_ok = Button(self.window,text="OK",bg="firebrick2",height=3,width=15,command=lambda:self.calculate_cross()).grid(row=2, column=1,stick=E+W)

    def calculate_cross(self):
        self.result = np.cross(np.array(ast.literal_eval(self.entry_vector1.get())),np.array(ast.literal_eval(self.entry_vector2.get())))
        self.label_result= Label(self.window,font=(40) ,text = f"cross = {self.result}").grid(row=3,column=0, columnspan=2)

    def do_determinant(self):
        self.clear(self.window)
        sself.column_config(3)
        self.entry_matrix = Entry(self.window,font=("comic",20,"bold"),width=25,borderwidth=1)
        self.entry_matrix.grid(row=0,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.linear_algebra()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_ok = Button(self.window,text="OK",bg="firebrick2",height=3,width=15,command=lambda:self.calculate_determinant()).grid(row=2, column=1,stick=E+W)

    def calculate_determinant(self):
        self.result= np.linalg.det(np.array(ast.literal_eval(self.entry_matrix.get())))
        self.label_result_det = Text(self.window, font=(20), width=25, height=25)
        self.label_result_det.insert("1.0",str(self.result))
        self.label_result_det.grid(row=3, column=0, columnspan=2)

    def do_transpose(self):
        self.clear(self.window)
        self.column_config(3)
        self.entry_matrix = Entry(self.window,font=("comic",20,"bold"),width=25,borderwidth=1)
        self.entry_matrix.grid(row=0,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.linear_algebra()).grid(row=4, column=1, pady=10,padx=10,stick=E+W)
        self.button_ok = Button(self.window,text="OK",bg="firebrick2",height=3,width=15,command=lambda:self.calculate_transpose()).grid(row=2, column=1,stick=E+W)

    def calculate_transpose(self):
        self.result= np.array(ast.literal_eval(self.entry_matrix.get())).T
        self.label_result_det = Text(self.window, font=(20), width=25, height=25)
        self.label_result_det.insert("1.0",(self.result))
        self.label_result_det.grid(row=3, column=0, columnspan=2)

    def do_mult_matrix(self):
        self.clear(self.window)
        self.column_config(3)
        self.entry_matrix1 = Entry(self.window,font=("comic",20,"bold"),width=25,borderwidth=1)
        self.entry_matrix2 = Entry(self.window,font=("comic",20,"bold"),width=25,borderwidth=1)
        self.entry_matrix1.grid(row=0,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.entry_matrix2.grid(row=1,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.linear_algebra()).grid(row=4, column=1, pady=10,padx=10,stick=E+W)
        self.button_ok = Button(self.window,text="OK",bg="firebrick2",height=3,width=15,command=lambda:self.calculate_mult_matrix()).grid(row=2, column=1,stick=E+W)

    def calculate_mult_matrix(self):
        self.result= np.dot(np.array(ast.literal_eval(self.entry_matrix1.get())),np.array(ast.literal_eval(self.entry_matrix2.get())))
        self.label_result_det = Text(self.window, font=(20), width=25, height=20)
        self.label_result_det.insert("1.0",(self.result))
        self.label_result_det.grid(row=3, column=0, columnspan=2)


    def scientific(self):
        self.clear(self.window)
        self.simple()
        self.button_simple = Button(self.window,text="Simple",bg="DarkOrange3",height=3,width=15,command=lambda:self.simple()).grid(row=1, column=5, pady=5,padx=5,stick=E+W)
        self.button_sin = Button(self.window,text="SIN",bg="honeydew3",height=4,width=3,command=lambda :self.click("sin(")).grid(row=6,column=0,pady=5,padx=5,stick=E+W)
        self.button_cos = Button(self.window,text="COS",bg="honeydew3",height=4,width=3,command=lambda :self.click("cos(")).grid(row=6,column=1,pady=5,padx=5,stick=E+W)
        self.buttom_tan = Button(self.window,text="TAN",bg="honeydew3",height=4,width=3,command=lambda :self.click("tan(")).grid(row=6,column=2,pady=5,padx=5,stick=E+W)
        self.buttom_arccos = Button(self.window,text="ARCCOS",bg="honeydew3",height=4,width=3,command=lambda :self.click("arccos(")).grid(row=6,column=3,pady=5,padx=5,stick=E+W)
        self.buttom_arcsin = Button(self.window,text="ARCSIN",bg="honeydew3",height=4,width=3,command=lambda :self.click("arcsin(")).grid(row=6,column=4,pady=5,padx=5,stick=E+W)
        self.buttom_arctan = Button(self.window,text="ARCTAN",bg="honeydew3",height=4,width=3,command=lambda :self.click("arctan(")).grid(row=7,column=0,pady=5,padx=5,stick=E+W)
        self.buttom_tanh = Button(self.window,text="TANH",bg="honeydew3",height=4,width=3,command=lambda :self.click("tanh(")).grid(row=7,column=1,pady=5,padx=5,stick=E+W)
        self.buttom_sinh = Button(self.window,text="SINH",bg="honeydew3",height=4,width=3,command=lambda :self.click("sinh(")).grid(row=7,column=2,pady=5,padx=5,stick=E+W)
        self.buttom_cosh = Button(self.window,text="COSH",bg="honeydew3",height=4,width=3,command=lambda :self.click("cosh(")).grid(row=7,column=3,pady=5,padx=5,stick=E+W)
        self.buttom_ln = Button(self.window,text="LN",bg="honeydew3",height=4,width=3,command=lambda :self.click("ln(")).grid(row=7,column=4,pady=5,padx=5,stick=E+W)
        self.buttom_log = Button(self.window,text="LOG",bg="honeydew3",height=4,width=3,command=lambda :self.click("log(")).grid(row=8,column=0,pady=5,padx=5,stick=E+W)
        self.buttom_arctanh = Button(self.window,text="ARCTANH",bg="honeydew3",height=4,width=3,command=lambda :self.click("arctanh(")).grid(row=8,column=1,pady=5,padx=5,stick=E+W)
        self.buttom_arcsinh = Button(self.window,text="ARCSINH",bg="honeydew3",height=4,width=3,command=lambda :self.click("arcsinh(")).grid(row=8,column=2,pady=5,padx=5,stick=E+W)
        self.buttom_arccosh = Button(self.window,text="ARCCOSH",bg="honeydew3",height=4,width=3,command=lambda :self.click("arccosh(")).grid(row=8,column=3,pady=5,padx=5,stick=E+W)
        self.buttom_abs = Button(self.window,text="ABS",bg="honeydew3",height=4,width=3,command=lambda :self.click("abs(")).grid(row=8,column=4,pady=5,padx=5,stick=E+W)
    
    def advanced(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.simple()).grid(row=5, column=1, pady=70,padx=50,stick=E+W)
        self.button_lin_reg = Button(self.window,text="Linear Regression",bg="LightSkyBlue2",height=3,width=15,command=lambda:self.regression(False)).grid(row=1, column=1, pady=30,padx=50,stick=E+W)
        self.button_log_reg = Button(self.window,text="Logistic Regression",bg="LightSkyBlue2",height=3,width=15,command=lambda :self.regression(True)).grid(row=1,column=0,pady=30,padx=50,stick=E+W)
        self.button_graphs = Button(self.window,text="Graphs",bg="LightSkyBlue2",height=3,width=15, command=lambda: self.graph()).grid(row=2,column=0, pady=30, padx=50,stick=E+W)
        self.button_stat = Button(self.window,text="Stat",bg="LightSkyBlue2", height=3, width=15, command=lambda: self.stat()).grid(row=2,column=1,pady=30,padx=50,stick=E+W)
        self.button_circuits = Button(self.window,text="Circuits",bg="LightSkyBlue2", height=3, width=15, command=lambda: self.circuits()).grid(row=3,column=0,pady=30,padx=50,stick=E+W)
        self.button_physics = Button(self.window,text="Physics",bg="LightSkyBlue2", height=3, width=15, command=lambda: self.physics()).grid(row=3,column=1,pady=30,padx=50,stick=E+W)
        self.button_linear = Button(self.window,text="linear algebra",bg="LightSkyBlue2", height=3, width=15, command=lambda: self.linear_algebra()).grid(row=4,column=0,pady=30,padx=50,stick=E+W)
    
    def constants(self):
        self.clear(self.window)
        self.scrollbar_constants = Scrollbar(self.window)
        self.canvas_constants = Canvas(self.window,bg="snow",yscrollcommand=self.scrollbar_constants.set)
        self.scrollbar_constants.config(command=self.canvas_constants.yview)
        self.scrollbar_constants.pack(side=RIGHT,fill=Y)
        self.window_constants = Frame(self.canvas_constants,bg="snow")
        self.canvas_constants.pack(side="left",fill="both",expand=True)
        self.canvas_constants.create_window(0,0,window=self.window_constants,anchor='nw')
        self.button_return = Button(self.window_constants,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.simple()).pack(side="bottom")
        self.title_constant = Label(self.window_constants,text="constants",font=("Soho",20),fg = "red",bg="snow").pack()
        self.speed_of_light_in_vacuum = Label(self.window_constants, text = "Speed of light in vacuum (c): 3x10⁸ m/s",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.speed_of_sound_in_air = Label(self.window_constants, text = "speed of sound in air (v): 343.2 m/s",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.permittivity_of_free_space = Label(self.window_constants, text = "permittivity of free space (μ0): 1.26x10⁻⁶ Wb/A*m",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.permittivity_of_vacuum = Label(self.window_constants, text = "permittivity of vacuum (ε0): 8.85x10⁻¹² C²/N*m²",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.avogadro_number = Label(self.window_constants, text = "avogadro's number (NA): 6.022x10²³ mol⁻¹",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.universal_gas_constant = Label(self.window_constants, text = "universal gas constant (R): 8.314472 J/mol*kg",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.atomic_mass_unit = Label(self.window_constants, text = "atomic mass unit (u): 1.6605x10-²⁷ kg",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.rest_energy_electron = Label(self.window_constants, text = "rest energy of the electron : 0.5109 MeV",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.electron_proton_charge = Label(self.window_constants, text = "electron/proton charge: ± 1.602x10⁻¹⁹ C",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.electron_mass = Label(self.window_constants, text = "electron mass: 9.1091x10⁻³¹ kg",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.proton_mass = Label(self.window_constants, text = "proton mass: 1.6750x10⁻²⁷ kg",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.neutron_mass = Label(self.window_constants, text = "neutron mass: 1.6750x10⁻²⁷ kg",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.euler_number = Label(self.window_constants, text = "Euler's number ≃ 2.718281828",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.coulomb_constant = Label(self.window_constants, text = "coulomb constant (k)= 9x10⁹ N*m²/C²",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.faraday_constant = Label(self.window_constants, text = "faraday constant (F)= 9.6496x10⁴ C/mol",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.planck_constant = Label(self.window_constants, text = "planck constant (h)= 6.63x10⁻³⁴ J*s",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.boltzmann_constant = Label(self.window_constants, text = "boltzmann constant (k)=1.38065x10⁻²³ J/K",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.boltz_stefan_constant = Label(self.window_constants, text = "stefan-boltzmann constant(σ) = 5.67x10⁻⁸ W/m²*K⁴",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.rydberg_constant = Label(self.window_constants, text = "rydberg constant (R) = 1.097x10⁷ m⁻¹",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.bohr_radius = Label(self.window_constants, text = "bohr radius (a0) = 5.29x10⁻¹¹ m",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.acceleration_gravity = Label(self.window_constants, text = "acceleration gravity (g) = 9.81 m/s²",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.gracitational_constant = Label(self.window_constants, text = "gracitational constant (G) = 6.6742x10⁻¹¹ N*m²/kg²",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.mass_earth = Label(self.window_constants, text = "mass Earth (Mt) = 5.972x10²⁴ kg",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.atmospheric_pressure = Label(self.window_constants, text = "atmospheric pressure (atm) = 1.01325x10⁵ Pa",font=("Soho",16),bg="snow",wraplength=520).pack()
        self.window.update()
        self.canvas_constants.config(scrollregion=self.canvas_constants.bbox("all"))

    def clear(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
calculator = Calculator()
calculator.window.mainloop()
#atribuciones Icons made by <a href="https://www.flaticon.com/authors/dinosoftlabs" title="DinosoftLabs">DinosoftLabs</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
