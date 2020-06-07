#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import ast
import pandas as pd
import sympy as sp
from scipy.integrate import quad
from math import factorial,e 
from numpy import sin, arcsin, arctan, cos, arccos , tan, sqrt , log as ln, tanh, cosh, sinh, log10 as log, arctanh, arccosh, arcsinh
from matplotlib import pyplot as plt
from tkinter import *
from tkinter import filedialog, messagebox, Scrollbar, Canvas, Frame, Text, PhotoImage
from sklearn.linear_model import LogisticRegression, LinearRegression
import re
π = np.pi
Exp = 10
G_constant =6.67408*(10**-11)
k_constant = 8.9875517923*(10**9)

class Calculator():
    def __init__(self,debug = False):
        self.window = Tk()
        self.debug = debug
        self.window.iconphoto(False,PhotoImage(file='calculator.png'))
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
        self.screen1 = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1,textvariable=self.screen_text)
        self.button0 = Button(self.window,text="0",bg="DeepSkyBlue2",height=4,width=3,command=lambda :self.click(0)).grid(row=4,column=0,pady=5,padx=5,stick=E+W)
        self.button1 = Button(self.window,text="1",bg="DeepSkyBlue2",height=4,width=3,command=lambda :self.click(1)).grid(row=3,column=0,pady=5,padx=5,stick=E+W)
        self.button2 = Button(self.window,text="2",bg="DeepSkyBlue2",height=4,width=3,command=lambda :self.click(2)).grid(row=3,column=1,pady=5,padx=5,stick=E+W)
        self.button3 = Button(self.window,text="3",bg="DeepSkyBlue2",height=4,width=2,command=lambda :self.click(3)).grid(row=3,column=2,pady=5,padx=5,stick=E+W)
        self.button4 = Button(self.window,text="4",bg="DeepSkyBlue2",height=4,width=3,command=lambda :self.click(4)).grid(row=2,column=0,pady=5,padx=5,stick=E+W)
        self.button5 = Button(self.window,text="5",bg="DeepSkyBlue2",height=4,width=3,command=lambda :self.click(5)).grid(row=2,column=1,pady=5,padx=5,stick=E+W)
        self.button6 = Button(self.window,text="6",bg="DeepSkyBlue2",height=4,width=3,command=lambda :self.click(6)).grid(row=2,column=2,pady=5,padx=5,stick=E+W)
        self.button7 = Button(self.window,text="7",bg="DeepSkyBlue2",height=4,width=3,command=lambda :self.click(7)).grid(row=1,column=0,pady=5,padx=5,stick=E+W)
        self.button8 = Button(self.window,text="8",bg="DeepSkyBlue2",height=4,width=3,command=lambda :self.click(8)).grid(row=1,column=1,pady=5,padx=5,stick=E+W)
        self.button9 = Button(self.window,text="9",bg="DeepSkyBlue2",height=4,width=3,command=lambda :self.click(9)).grid(row=1,column=2,pady=5,padx=5,stick=E+W)
        self.buttonPoint = Button(self.window,text=".",bg="DeepSkyBlue2",height=4,width=3,command=lambda :self.click(".")).grid(row=4,column=1,pady=5,padx=5,stick=E+W)
        self.buttonPI = Button(self.window,text="π",bg="DeepSkyBlue2",height=4,width=3,command=lambda :self.click("π")).grid(row=4,column=2,pady=5,padx=5,stick=E+W)
        self.buttonAC = Button(self.window,text="AC",bg="DarkOrange3",height=4,width=3,command=lambda :self.clear_input()).grid(row=1,column=4,pady=5,padx=5,stick=E+W)
        self.buttonDEl = Button(self.window,text="DEL",bg="DarkOrange3",height=4,width=3,command=lambda:self.delete()).grid(row=1,column=3,pady=5,padx=5,stick=E+W)
        self.buttonSum = Button(self.window,text="+",bg="DarkOrange3",height=4,width=3,command=lambda:self.click("+")).grid(row=3,column=3,pady=5,padx=5,stick=E+W)
        self.buttonRes = Button(self.window,text="-",bg="DarkOrange3",height=4,width=3,command=lambda:self.click("-")).grid(row=3,column=4,pady=5,padx=5,stick=E+W)
        self.buttonMul = Button(self.window,text="*",bg="DarkOrange3",height=4,width=3,command=lambda:self.click("*")).grid(row=2,column=3,pady=5,padx=5,stick=E+W)
        self.buttonDiv = Button(self.window,text="/",bg="DarkOrange3",height=4,width=3,command=lambda:self.click("/")).grid(row=2,column=4,pady=5,padx=5,stick=E+W)
        self.buttonAns = Button(self.window,text="=",bg="DarkOrange3",height=4,width=3,command=lambda:self.term()).grid(row=5,column=2,pady=5,padx=5,stick=E+W)
        self.buttonPow = Button(self.window,text="^",bg="DarkOrange3",height=4,width=3,command=lambda:self.click("**")).grid(row=4,column=3,pady=5,padx=5,stick=E+W)
        self.buttonSqrt = Button(self.window,text="√",bg="DarkOrange3",height=4,width=3,command=lambda:self.click("sqrt(")).grid(row=4,column=4,pady=5,padx=5,stick=E+W)
        self.buttonEuler = Button(self.window,text="e",bg="DeepSkyBlue2",height=4,width=3,command=lambda:self.click("e")).grid(row=5,column=0,pady=5,padx=5,stick=E+W)
        self.buttonEXP = Button(self.window,text="E",bg="DarkOrange3",height=4,width=3,command=lambda:self.click("*Exp**")).grid(row=5,column=1,pady=5,padx=5,stick=E+W)
        self.button_Start_Parenthesis = Button(self.window,text="(",bg="DarkOrange3",height=4,width=3,command=lambda:self.click("(")).grid(row=5,column=3,pady=5,padx=5,stick=E+W)
        self.button_End_Parenthesis= Button(self.window,text=")",bg="DarkOrange3",height=4,width=3,command=lambda:self.click(")")).grid(row=5,column=4,pady=5,padx=5,stick=E+W)
        self.button_adv = Button(self.window,text="Advanced Options",bg="DarkOrange3",height=3,width=15,command=lambda:self.advanced()).grid(row=2, column=5,pady=5,padx=5,stick=E+W)
        self.button_cons = Button(self.window,text="Constants",bg="DarkOrange3",height=3,width=15,command=lambda:self.constants()).grid(row=3, column=5, pady=5,padx=5,stick=E+W)
        self.button_scien = Button(self.window,text="Scientific",bg="DarkOrange3",height=3,width=15,command=lambda:self.scientific()).grid(row=1, column=5, pady=5,padx=5,stick=E+W)
        self.screen1.grid(row=0,column=0,columnspan=5,padx=8,pady=5,stick=E+W)
   
    def replace(self,match):
        return self.np_to_sp_dict[match.group(0)]
        
    def np_to_sp(self,string):
        temp = string
        lsym= "/ ( ) * + - **"
        for i in lsym:
            temp.replace(i, " "+i+" ")
        self.np_to_sp_dict= {"sin":"sp.sin",
                          "arcsin":"sp.asin",
                          "arctan":"sp.atan",
                          "cos":"sp.cos",
                          "arccos":"sp.acos",
                          "tan":"sp.tan",
                          "sqrt":"sp.sqrt",
                          "ln":"sp.log",
                          "tanh":"sp.tanh",
                          "cosh":"sp.cosh",
                          "sinh":"sp.sinh",
                          "log":"sp.log",
                          "arctanh":"sp.atanh",
                          "arccosh":"sp.acosh",
                          "arcsinh":"sp.asinh"}
        temp = re.sub('|'.join(r'\b%s\b' % re.escape(s) for s in self.np_to_sp_dict), 
                            self.replace, temp) 
        return temp


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


    def comb(self,x,y): 
        return factorial(x)/(factorial(x-y)*factorial(y)) 

    def equations_help(self, info):
        messagebox.showinfo(title="help",message=f"use comma like separator, vars in this order = {info}")
        
    def regression(self,reg):
        self.clear(self.window)
        self.column_config(3)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.advanced()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("[v1,v2,v3], and you need load to csv")).grid(row=4, column=0, pady=300,padx=10,stick=E+W)
        self.label_regression = Label(self.window, text="type predict data").grid(row=1,column=0,stick=E+W)
        self.entry_regression = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_regression.grid(row=1,column=1,columnspan=2,stick=E+W)
        self.button_load = Button(self.window,text="Load csv",bg="firebrick2",height=3,width=15,command=lambda:self.load()).grid(row=2, column=1, pady=30,padx=10,stick=E+W)
        self.regresion_label=Label(self.window,text="", font=("Centaur",20),bg="snow")
        self.regresion_label.grid(row=3, column=0,columnspan=3, pady=30,padx=10)
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
	    	self.regresion_label.config(text=f"Predicted --> {self.from_class_dict[clf.predict(pred)[0]]}")
    	except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
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
                self.regresion_label.config(text=f"Predicted --> {clf.predict(pred)[0]}")
            except Exception as Err:
                if self.debug:
                    messagebox.showerror(title="Error",message=Err)
                else:
                    messagebox.showerror(title="Error",message="Train data must be of type 'int' or 'float' ")
    	except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="Couldn't load csv")
    	
    	
    	
            
    def graph(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.advanced()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("function of x")).grid(row=4, column=0, pady=70,padx=10,stick=E+W)
        self.label_start = Label(self.window, text="Start").grid(row =0, column=0,stick=E+W)
        self.entry_start=Entry(self.window,font=("Centaur",20),width=30,borderwidth=1)
        self.entry_start.grid(row=0,column=1,columnspan=3,stick=E+W)
        self.label_end= Label(self.window, text="End").grid(row =1, column=0,stick=E+W)
        self.entry_end=Entry(self.window,font=("Centaur",20),width=30,borderwidth=1)
        self.entry_end.grid(row=1,column=1,columnspan=3,stick=E+W)
        self.label_function = Label(self.window,text="Fuction").grid(row=2,column=0,stick=E+W)
        self.entry_function = Entry(self.window,font=("Centaur",20),width=30,borderwidth=1)
        self.entry_function.grid(row=2,column=1,columnspan=3,stick=E+W)
        self.button_graphs=Button(self.window,text="GRAPH",bg="firebrick2",height=3,width=15,command=lambda:self.plotting(self.entry_start.get(),self.entry_end.get(),self.entry_function.get())).grid(row=3, column=1, pady=30,padx=10,stick=E+W)
        
                
    def plotting(self,start,end,fuction):
        try:
            x = np.linspace((int)(start),(int)(end))
            plt.plot(x, eval(fuction))
            plt.xlabel('x axis')
            plt.ylabel('y axis')
            plt.axis('tight')
            plt.show()
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")
        
    def stat(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.advanced()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_binomial=Button(self.window,text="binomial",bg="medium sea green",height=3,width=15,command=lambda:self.dist_binomial()).grid(row=1, column=0, pady=30,padx=10,stick=E+W)
        self.button_hypergeometric=Button(self.window,text="hypergeometric",bg="medium sea green",height=3,width=15,command=lambda:self.dist_hypergeometric()).grid(row=1, column=1, pady=30,padx=10,stick=E+W)
        self.button_poisson=Button(self.window,text="poisson",bg="medium sea green",height=3,width=15,command=lambda:self.dist_poisson()).grid(row=2, column=0, pady=30,padx=10,stick=E+W)
        self.button_discrete=Button(self.window,text="discrete",bg="medium sea green",height=3,width=15,command=lambda:self.dist_discrete()).grid(row=2, column=1, pady=30,padx=10,stick=E+W)

    def dist_binomial(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("n,x,p")).grid(row=4, column=0, pady=300,padx=10,stick=E+W)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.stat()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.entry_binomial = Entry(self.window,font=("Centaur",20),width=30,borderwidth=1)
        self.entry_binomial.grid(row=0,column=0,columnspan=3,stick=E+W)
        self.label_result_binomial = Label(self.window,text = "", font=("Centaur",20),bg="snow")
        self.label_result_binomial.grid(row=3, column=0,columnspan=2)      
        self.button_ok = Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.binomial()).grid(row=2, column=0, pady=30,padx=10,stick=E+W)

    def binomial(self):
        try:
            temp = ast.literal_eval("["+self.entry_binomial.get()+"]")
            n, x, p = temp[0], temp[1], temp[2]
            result = factorial(n)/(factorial(n-x)*factorial(x))*(p**x)*(1-p)**(n-x)
            self.label_result_binomial.config(text = f"x~B()= {result}")
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def dist_hypergeometric(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.stat()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("x,N,k,n")).grid(row=4, column=0, pady=300,padx=10,stick=E+W)
        self.entry_hypergeometric = Entry(self.window,font=("Centaur",20),width=30,borderwidth=1)
        self.entry_hypergeometric.grid(row=0,column=0,columnspan=3,stick=E+W)
        self.button_ok = Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.hyper_geo()).grid(row=2, column=0, pady=30,padx=10,stick=E+W)
        self.label_result_hyper_geo = Label(self.window,text = "", font=("Centaur",20),bg="snow")
        self.label_result_hyper_geo.grid(row=3, column=0,columnspan=2)

    def hyper_geo(self):
        try:
            temp = ast.literal_eval("["+self.entry_hypergeometric.get()+"]")
            x,N,k,n = temp[0], temp[1], temp[2], temp[3] 
            result=(self.comb(k,x)*self.comb(N-k,n-x))/self.comb(N,n)
            self.label_result_hyper_geo.config(text = f"x~H()= {result}")
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def dist_poisson(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.stat()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("x,l")).grid(row=4, column=0, pady=300,padx=10,stick=E+W)
        self.entry_poisson = Entry(self.window,font=("Centaur",20),width=30,borderwidth=1)
        self.entry_poisson.grid(row=0,column=0,columnspan=3,stick=E+W)
        self.button_ok = Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.poisson()).grid(row=2, column=0, pady=30,padx=10,stick=E+W)
        self.label_result_poisson = Label(self.window,text = "", font=("Centaur",20),bg="snow")
        self.label_result_poisson.grid(row=3, column=0,columnspan=2)

    def poisson(self):
        try:
            temp = ast.literal_eval("["+self.entry_poisson.get()+"]")
            x,l = temp[0], temp[1] 
            result=(e**-l*l**x)/factorial(x) 
            self.label_result_poisson.config(text = f"x~P()= {result}")
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def dist_discrete(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.stat()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("x,y")).grid(row=4, column=0, pady=300,padx=10,stick=E+W)
        self.entry_discrete = Entry(self.window,font=("Centaur",20),width=30,borderwidth=1)
        self.entry_discrete.grid(row=0,column=0,columnspan=3,stick=E+W)
        self.button_ok = Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.var_discrete()).grid(row=2, column=0, pady=30,padx=10,stick=E+W)
        self.label_result_discrete = Label(self.window,text = "", font=("Centaur",20),bg="snow")
        self.label_result_discrete.grid(row=3,column=0,columnspan=2)        

    def var_discrete(self):
        try:
            temp = ast.literal_eval("["+self.entry_discrete.get()+"]")
            x,y = temp[0], temp[1] 
            E = sum([xi*yi for xi,yi in zip(x,y)]) 
            V = sum([(xi-E)**2 *yi for xi,yi in zip(x,y) ]) 
            self.label_result_discrete.config(text = f"E= {E} V= {V}")
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def circuits(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.advanced()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_resistance_eq=Button(self.window,text="equivalent resistance",bg="medium sea green",height=3,width=15,command=lambda:self.resistance_equivalent()).grid(row=0, column=0, pady=30,padx=10,stick=E+W)
        self.button_vol_curr=Button(self.window,text="vol/curr divider",bg="medium sea green",height=3,width=15,command=lambda:self.divisor()).grid(row=1, column=0, pady=30,padx=10,stick=E+W)
        self.button_capacitor_eq=Button(self.window,text="capacitor",bg="medium sea green",height=3,width=15,command=lambda:self.capacitance()).grid(row=0, column=1, pady=30,padx=10,stick=E+W)
    
    def resistance_equivalent(self):
        self.clear(self.window)
        self.column_config(3)
        self.button_return=Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.circuits()).grid(row=4, column=1, pady=100,stick=E+W)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("resistance in ohms")).grid(row=4, column=0, pady=300,padx=10,stick=E+W)       
        self.entry_resistance1=Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_resistance2=Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_resistance1.grid(row=0,column=0,columnspan=2,pady=10,padx = 5,stick=E+W)
        self.entry_resistance2.grid(row=1,column=0,columnspan=2,pady=10, padx = 5,stick=E+W)
        self.button_parallel_resistance=Button(self.window,text="parallel",bg="yellow green",height=3,width=15,command=lambda:self.equivalent_parallel()).grid(row=2, column=0,stick=E+W)
        self.button_serie_resistance=Button(self.window,text="serie",bg="yellow green",height=3,width=8,command= lambda:self.equivalent_serie()).grid(row=2, column=1,stick=E+W)
        self.label_result_parallel = Label(self.window, text = "", font=("Centaur",20),bg="snow")
        self.label_result_parallel.grid(row=3, column=0,columnspan=2,stick=E+W)
        self.label_result_serie = Label(self.window, text = "", font=("Centaur",20),bg="snow")
        self.label_result_serie.grid(row=3, column=0,columnspan=2,stick=E+W)
        
    def capacitance(self):
        self.clear(self.window)
        self.column_config(3)
        self.button_return=Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.circuits()).grid(row=4, column=1, pady=100,stick=E+W)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("capacitance in µF")).grid(row=4, column=0, pady=300,padx=10,stick=E+W)     
        self.entry_resistance1=Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_resistance2=Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_resistance1.grid(row=0,column=0,columnspan=2,pady=10,padx = 5,stick=E+W)
        self.entry_resistance2.grid(row=1,column=0,columnspan=2,pady=10, padx = 5,stick=E+W)
        self.button_parallel_resistance=Button(self.window,text="parallel",bg="yellow green",height=3,width=15,command=lambda:self.equivalent_serie()).grid(row=2, column=0,stick=E+W)
        self.button_serie_resistance=Button(self.window,text="serie",bg="yellow green",height=3,width=8,command= lambda:self.equivalent_parallel()).grid(row=2, column=1,stick=E+W)
        self.label_result_parallel = Label(self.window, text = "", font=("Centaur",20),bg="snow")
        self.label_result_parallel.grid(row=3, column=0,columnspan=2,stick=E+W)
        self.label_result_serie = Label(self.window, text = "", font=("Centaur",20),bg="snow")
        self.label_result_serie.grid(row=3, column=0,columnspan=2,stick=E+W)

    def equivalent_parallel(self):
        try:
            result = 1/((1/(int)(self.entry_resistance1.get()))+(1/(int)(self.entry_resistance2.get())))
            self.label_result_parallel.config(text = f"Req = {result}")
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def equivalent_serie(self):
        try:
            self.result = (int)(self.entry_resistance1.get())+(int)(self.entry_resistance2.get())
            self.label_result_serie.config(text = f"Req = {self.result}")
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")
        
    def divisor(self):
        self.clear(self.window)
        self.column_config(3)
        self.button_return=Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.circuits()).grid(row=6, column=1, pady=100,stick=E+W)
        self.label_vol_curr=Label(self.window, text="type voltage or current").grid(row =0, column=0,stick=E+W)
        self.label_resistance=Label(self.window, text="resistance").grid(row=1,column=0,stick=E+W)
        self.label_eq_resistance=Label(self.window, text="sum resistance").grid(row=2, column=0,stick=E+W)
        self.entry_vol_curr=Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_resistance1=Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_resistance2=Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_vol_curr.grid(row=0,column=1,columnspan=2,pady=10,padx = 5,stick=E+W)
        self.entry_resistance1.grid(row=1,column=1,columnspan=2,pady=10, padx = 5,stick=E+W)
        self.entry_resistance2.grid(row=2,column=1,columnspan=2,pady=10, padx = 5,stick=E+W)
        self.button_divirsor=Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.divisor_vol_curr()).grid(row=3, column=0,stick=E+W)
        self.label_result_divisor = Label(self.window, text = "", font=("Centaur",20),bg="snow")
        self.label_result_divisor.grid(row=5, column=0,columnspan=2,stick=E+W)

    def divisor_vol_curr(self):
        try:
            result = (int(self.entry_resistance1.get())/(int(self.entry_resistance1.get())+int(self.entry_resistance2.get())))*int(self.entry_vol_curr.get())
            self.label_result_divisor.config(text = f"result = {result}")
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def physics(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.advanced()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_mechanics=Button(self.window,text="mechanics",bg="medium sea green",height=3,width=15,command=lambda:self.mechanics()).grid(row=0, column=0, pady=30,padx=10,stick=E+W)
        self.button_electro=Button(self.window,text="electromagnetism",bg="medium sea green",height=3,width=15,command=lambda:self.electro()).grid(row=0, column=1, pady=30,padx=10,stick=E+W)

    def electro(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.physics()).grid(row=3, column=1, pady=70,padx=10,stick=E+W)
        self.button_columb_law=Button(self.window,text="columb's law",bg="medium sea green",height=3,width=15,command=lambda:self.coulomb_law()).grid(row=0, column=0, pady=30,padx=10,stick=E+W)
        self.button_electric_field=Button(self.window,text="electric field",bg="medium sea green",height=3,width=15,command=lambda:self.electric_field()).grid(row=0, column=1, pady=30,padx=10,stick=E+W)
        self.button_electric_potential=Button(self.window,text="electric potential",bg="medium sea green",height=3,width=15,command=lambda:self.electric_potential()).grid(row=1, column=0, pady=30,padx=10,stick=E+W)
        self.button_gauss_law=Button(self.window,text="gauss law",bg="medium sea green",height=3,width=15,command=lambda:self.gauss_law()).grid(row=1, column=1, pady=30,padx=10,stick=E+W)
   
    def gauss_law(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.electro()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("first entry integration and second entry limits")).grid(row=4, column=0, pady=300,padx=10,stick=E+W)
        self.entry_gauss_law = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_gauss_law.grid(row=0,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.entry_limit = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_limit.grid(row=1,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.button_ok = Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.calculate_gauss_law()).grid(row=2, column=1,stick=E+W)
        self.label_result_gauss = Label(self.window, text="", font=("Centaur",20),bg="snow")
        self.label_result_gauss.grid(row=3, column=0,columnspan=2,stick=E+W)

    def calculate_gauss_law(self):
        try:
            aux = eval("["+self.entry_limit.get()+"]")
            inf_limit, sup_limit = aux[0], aux[1]
            result = quad(lambda x: eval(self.entry_gauss_law.get()), inf_limit, sup_limit)
            self.label_result_gauss.config(text=f" V= {result[0], result[1]}")
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def electric_potential(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.electro()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("q,r")).grid(row=4, column=0, pady=300,padx=10,stick=E+W)
        self.entry_electric_potential = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_electric_potential.grid(row=1,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.button_ok = Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.calculate_electric_potential()).grid(row=2, column=1,stick=E+W)
        self.label_result_electric_potential = Label(self.window, text="", font=("Centaur",20),bg="snow")
        self.label_result_electric_potential.grid(row=3, column=0,columnspan=2,stick=E+W)

    def calculate_electric_potential(self):
        try:
            temp = ast.literal_eval("["+self.entry_electric_potential.get()+"]")
            q,r = temp[0], temp[1]
            result = (k_constant)*((q)/(r))
            self.label_result_electric_potential.config(text=f" V= {result}")
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def electric_field(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.electro()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("q,r/ F,q")).grid(row=4, column=0, pady=300,padx=10,stick=E+W)
        self.entry_electric_field = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_electric_field.grid(row=1,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.button_electric_with_force = Button(self.window,text="with force",bg="yellow green",height=3,width=15,command=lambda:self.calculate_electric_field(True)).grid(row=2, column=0,stick=E+W)
        self.button_electric_with_radius = Button(self.window,text="with radius",bg="yellow green",height=3,width=15,command=lambda:self.calculate_electric_field(False)).grid(row=2, column=1,stick=E+W)
        self.label_result_electric_field = Label(self.window, text="", font=("Centaur",20),bg="snow")
        self.label_result_electric_field.grid(row=3, column=0,columnspan=2,stick=E+W)

    def calculate_electric_field(self, force):
        try:
            temp = ast.literal_eval("["+self.entry_electric_field.get()+"]")
            if force:
                F,q = temp[0], temp[1]
                result = F/q
            else:
                q,r = temp[0], temp[1]
                result = (k_constant)*((q)/(r**2))
            self.label_result_electric_field.config(text=f"|E|= {result}")
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def coulomb_law(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.electro()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("q1,q1,r")).grid(row=4, column=0, pady=300,padx=10,stick=E+W)
        self.entry_coulomb_l = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_coulomb_l.grid(row=1,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.button_ok = Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.calculate_coulomb_law()).grid(row=2, column=1,stick=E+W)
        self.label_result_coulomb = Label(self.window, text="", font=("Centaur",20),bg="snow")
        self.label_result_coulomb.grid(row=3, column=0,columnspan=2,stick=E+W)

    def calculate_coulomb_law(self):
        try:
            temp = ast.literal_eval("["+self.entry_coulomb_l.get()+"]")
            q1,q2,r = temp[0], temp[1], temp[2]
            result = (k_constant)*((q1*q2)/(r**2))
            self.label_result_coulomb.config(text=f"|F|= {result}")
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def mechanics(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.physics()).grid(row=4, column=1, pady=70,padx=10,stick=E+W)
        self.button_final_position=Button(self.window,text="final position",bg="medium sea green",height=3,width=15,command=lambda:self.final_position()).grid(row=0, column=0, pady=30,padx=10,stick=E+W)
        self.button_final_velocity=Button(self.window,text="final velocity",bg="medium sea green",height=3,width=15,command=lambda:self.final_velocity()).grid(row=0, column=1, pady=30,padx=10,stick=E+W)
        self.button_force=Button(self.window,text="force",bg="medium sea green",height=3,width=15,command=lambda:self.force()).grid(row=1, column=0, pady=30,padx=10,stick=E+W)
        self.button_kinetic_energy=Button(self.window,text="kinetic energy",bg="medium sea green",height=3,width=15,command=lambda:self.kinetic_energy()).grid(row=1, column=1, pady=30,padx=10,stick=E+W)
        self.button_potential_energy=Button(self.window,text="potential energy",bg="medium sea green",height=3,width=15,command=lambda:self.potential()).grid(row=2, column=0, pady=30,padx=10,stick=E+W)
        self.button_law_gravitation=Button(self.window,text="law gravitation",bg="medium sea green",height=3,width=15,command=lambda:self.law_gratitation()).grid(row=2, column=1, pady=30,padx=10,stick=E+W)

    def law_gratitation(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.physics()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_force_gravitation=Button(self.window,text="law of gravitation",bg="dark slate blue",height=3,width=15,command=lambda:self.force_gravitation()).grid(row=0, column=0, pady=30,padx=10,stick=E+W)
        self.button_potential_gravitation=Button(self.window,text="potential",bg="dark slate blue",height=3,width=15,command=lambda:self.potential_gravitation()).grid(row=0, column=1, pady=30,padx=10,stick=E+W)
        self.button_velocity_gravitation=Button(self.window,text="velocity",bg="dark slate blue",height=3,width=15,command=lambda:self.velocity_gravitation()).grid(row=1, column=0, pady=30,padx=10,stick=E+W)
        self.button_period_gravitation=Button(self.window,text="period",bg="dark slate blue",height=3,width=15,command=lambda:self.period_gravitation()).grid(row=1, column=1, pady=30,padx=10,stick=E+W)

    def period_gravitation(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.law_gratitation()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("v,r")).grid(row=4, column=0, pady=300,padx=10,stick=E+W)
        self.entry_period_g = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_period_g.grid(row=1,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.button_ok = Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.calculate_period_gravity()).grid(row=2, column=1,stick=E+W)
        self.label_result_period_gravity = Label(self.window, text="", font=("Centaur",18),bg="snow")
        self.label_result_period_gravity.grid(row=3, column=0,columnspan=2,stick=E+W)

    def calculate_period_gravity(self):
        try:
            temp = ast.literal_eval("["+self.entry_period_g.get()+"]")
            v,r = temp[0], temp[1]
            result = (2*π*r)/(v)
            self.label_result_period_gravity.config(text=f"T of orbit= {result}")
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def velocity_gravitation(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.law_gratitation()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("Mt,r")).grid(row=4, column=0, pady=300,padx=10,stick=E+W)
        self.entry_velocity_g = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_velocity_g.grid(row=1,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.button_ok = Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.calculate_velocity_gravity()).grid(row=2, column=1,stick=E+W)
        self.label_result_velocity_gravity = Label(self.window, text="", font=("Centaur",18),bg="snow")
        self.label_result_velocity_gravity.grid(row=3, column=0,columnspan=2,stick=E+W)

    def calculate_velocity_gravity(self):
        try:
            temp = ast.literal_eval("["+self.entry_velocity_g.get()+"]")
            Mt,r = temp[0], temp[1]
            result = sqrt((G_constant*Mt)/(r))
            self.label_result_velocity_gravity.config(text=f"v of orbit= {result}")
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def potential_gravitation(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.law_gratitation()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("Mt,m,r")).grid(row=4, column=0, pady=300,padx=10,stick=E+W)
        self.entry_potential_g = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_potential_g.grid(row=1,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.button_ok = Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.calculate_potential_gravity()).grid(row=2, column=1,stick=E+W)
        self.label_result_potential_gravity = Label(self.window, text="", font=("Centaur",20),bg="snow")
        self.label_result_potential_gravity.grid(row=3, column=0,columnspan=2,stick=E+W)

    def calculate_potential_gravity(self):
        try:
            temp = ast.literal_eval("["+self.entry_potential_g.get()+"]")
            Mt,m,r = temp[0], temp[1],temp[2]
            result = -((G_constant)*Mt*m)/(r)
            self.label_result_potential_gravity.config(text=f"U= {result}")
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def force_gravitation(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.law_gratitation()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("m1,m2,r")).grid(row=4, column=0, pady=300,padx=10,stick=E+W)
        self.entry_force_g = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_force_g.grid(row=1,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.button_ok = Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.calculate_force_gravity()).grid(row=2, column=1,stick=E+W)
        self.label_result_force_gravity= Label(self.window, text="", font=("Centaur",20),bg="snow")
        self.label_result_force_gravity.grid(row=3, column=0,columnspan=2,stick=E+W)

    def calculate_force_gravity(self):
        try:
            temp = ast.literal_eval("["+self.entry_force_g.get()+"]")
            m1,m2,r = temp[0], temp[1],temp[2]
            result = ((G_constant)*m1*m2)/(r**2)
            self.label_result_force_gravity.config(text=f"F= {result}")
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def potential(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.mechanics()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("m,h")).grid(row=4, column=0, pady=300,padx=10,stick=E+W)
        self.entry_potential = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_potential.grid(row=1,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.button_ok = Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.calculate_potential()).grid(row=2, column=1,stick=E+W)
        self.label_result_potential_mec = Label(self.window, text="", font=("Centaur",20),bg="snow")
        self.label_result_potential_mec.grid(row=3, column=0,columnspan=2,stick=E+W)

    def calculate_potential(self):
        try:
            temp = ast.literal_eval("["+self.entry_potential.get()+"]")
            m,h = temp[0], temp[1]
            result = m*(9.81)*h
            self.label_result_potential_mec.config(text=f"U= {result}")
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def kinetic_energy(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.mechanics()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("m,v")).grid(row=4, column=0, pady=300,padx=10,stick=E+W)
        self.entry_kinetic = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_kinetic.grid(row=1,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.button_ok = Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.calculate_kinetic()).grid(row=2, column=1,stick=E+W)
        self.label_result_kinetic = Label(self.window, text="", font=("Centaur",20),bg="snow")
        self.label_result_kinetic.grid(row=3, column=0,columnspan=2,stick=E+W)

    def calculate_kinetic(self):
        try:
            temp = ast.literal_eval("["+self.entry_kinetic.get()+"]")
            m,v = temp[0], temp[1]
            result = (1/2)*m*(v**2)
            self.label_result_kinetic.config(text=f"K= {result}")
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def force(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.mechanics()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("m,a")).grid(row=4, column=0, pady=300,padx=10,stick=E+W)
        self.entry_force = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_force.grid(row=1,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.button_ok = Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.calculate_force()).grid(row=2, column=1,stick=E+W)
        self.label_result_force_mec = Label(self.window, text="", font=("Centaur",20),bg="snow")
        self.label_result_force_mec.grid(row=3, column=0,columnspan=2,stick=E+W)

    def calculate_force(self):
        try:
            temp = ast.literal_eval("["+self.entry_force.get()+"]")
            m,a = temp[0], temp[1]
            result = m*a
            self.label_result_force_mec.config(text=f"F= {result}")
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")


    def final_velocity(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.mechanics()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("vo,t,a / vo,x,a")).grid(row=4, column=0, pady=300,padx=10,stick=E+W)
        self.entry_velocity = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_velocity.grid(row=1,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.button_with_time = Button(self.window,text="with time",bg="yellow green",height=3,width=15,command=lambda:self.calculate_velocity(True)).grid(row=2, column=0,stick=E+W)
        self.button_without_time = Button(self.window,text="without time",bg="yellow green",height=3,width=15,command=lambda:self.calculate_velocity(False)).grid(row=2, column=1,stick=E+W)
        self.label_result_velocity = Label(self.window, text="", font=("Centaur",20),bg="snow")
        self.label_result_velocity.grid(row=3, column=0,columnspan=2,stick=E+W)

    def calculate_velocity(self, time):
        try:
            temp = ast.literal_eval("["+self.entry_velocity.get()+"]")
            if time:
                vo,a,t = temp[0], temp[1], temp[2]
                result = vo + (a*t)
            else:
                vo,a,x = temp[0], temp[1], temp[2]
                result = sqrt((vo**2)+(2*a*x))
            self.label_result_velocity.config(text=f"Vf= {result}")
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def final_position(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.mechanics()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("xo,vo,t,a")).grid(row=4, column=0, pady=300,padx=10,stick=E+W)
        self.entry_move = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_move.grid(row=1,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.button_ok = Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.calculate_move()).grid(row=2, column=1,stick=E+W)
        self.label_result_move = Label(self.window,text = "", font=("Centaur",20),bg="snow")
        self.label_result_move.grid(row=3,column=0,columnspan=2,stick=E+W)

    def calculate_move(self):
        try:
            temp = ast.literal_eval("["+self.entry_move.get()+"]")
            xo, vo, t, a = temp[0], temp[1], temp[2], temp[3]
            result = xo + vo*t +((a*t**2)/2)
            self.label_result_move.config(text = f"xf = {result}")
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def linear_algebra(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.advanced()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_cross=Button(self.window,text="cross",bg="medium sea green",height=3,width=15,command=lambda:self.do_cross()).grid(row=0, column=0, pady=30,padx=10,stick=E+W)
        self.button_transpose=Button(self.window,text="transpose",bg="medium sea green",height=3,width=15,command=lambda:self.do_transpose()).grid(row=1, column=0, pady=30,padx=10,stick=E+W)
        self.button_determinant=Button(self.window,text="determinant",bg="medium sea green",height=3,width=15,command=lambda:self.do_determinant()).grid(row=0, column=1, pady=30,padx=10,stick=E+W)
        self.button_determinant=Button(self.window,text="multiplication",bg="medium sea green",height=3,width=15,command=lambda:self.do_mult_matrix()).grid(row=1, column=1, pady=30,padx=10,stick=E+W)

    def do_cross(self):
        self.clear(self.window)
        self.column_config(3)
        self.entry_vector1 = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_vector2 = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_vector1.grid(row=0,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.entry_vector2.grid(row=1,column=0,columnspan=2, stick=E+W,pady=10,padx=5) 
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.linear_algebra()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("the vector must be 2 or 3 dimensions")).grid(row=4, column=0, pady=300,padx=10,stick=E+W)
        self.button_ok = Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.calculate_cross()).grid(row=2, column=1,stick=E+W)
        self.label_result_cross= Label(self.window,text = "", font=("Centaur",20),bg="snow")
        self.label_result_cross.grid(row=3,column=0, columnspan=2,stick=E+W)

    def calculate_cross(self):
        try:
            result = np.cross(np.array(ast.literal_eval(self.entry_vector1.get())),np.array(ast.literal_eval(self.entry_vector2.get())))
            self.label_result_cross.config(text = f"cross = {result}")
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def do_determinant(self):
        self.clear(self.window)
        self.column_config(3)
        self.entry_matrix = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_matrix.grid(row=0,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("must be squart")).grid(row=4, column=0, pady=70,padx=10,stick=E+W)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.linear_algebra()).grid(row=4, column=1, pady=70,padx=10,stick=E+W)
        self.button_ok = Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.calculate_determinant()).grid(row=1, column=1,stick=E+W)
        self.label_result_det = Text(self.window, font=("Centaur",20), bg="snow",width=10, height=10)
        self.label_result_det.grid(row=2, column=0, columnspan=2,stick=E+W)

    def calculate_determinant(self):
        try:
            self.result= np.linalg.det(np.array(ast.literal_eval(self.entry_matrix.get())))
            self.label_result_det.insert("1.0",str(self.result))
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def do_transpose(self):
        self.clear(self.window)
        self.column_config(3)
        self.entry_matrix = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_matrix.grid(row=0,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.linear_algebra()).grid(row=4, column=1, pady=70,padx=10,stick=E+W)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("[[],[],...,[]]")).grid(row=4, column=0, pady=70,padx=10,stick=E+W)
        self.button_ok = Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.calculate_transpose()).grid(row=2, column=1,stick=E+W)
        self.label_result_trans = Text(self.window, font=("Centaur",20), bg="snow",width=10, height=10)
        self.label_result_trans.grid(row=3, column=0, columnspan=2,stick=E+W)

    def calculate_transpose(self):
        try:
            self.result= np.array(ast.literal_eval(self.entry_matrix.get())).T   
            self.label_result_trans.insert("1.0",(self.result))
            
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def do_mult_matrix(self):
        self.clear(self.window)
        self.column_config(3)
        self.entry_matrix1 = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_matrix2 = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_matrix1.grid(row=0,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.entry_matrix2.grid(row=1,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("[[],[],...,[]]")).grid(row=4, column=0, pady=70,padx=10,stick=E+W)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.linear_algebra()).grid(row=4, column=1, pady=10,padx=10,stick=E+W)
        self.button_ok = Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.calculate_mult_matrix()).grid(row=2, column=1,stick=E+W)
        self.label_result_det = Text(self.window,  font=("Centaur",20), bg="snow",width=20, height=20)
        self.label_result_det.grid(row=3, column=0, columnspan=2,stick=E+W)


    def calculate_mult_matrix(self):
        try:
            self.result= np.dot(np.array(ast.literal_eval(self.entry_matrix1.get())),np.array(ast.literal_eval(self.entry_matrix2.get())))
            self.label_result_det.insert("1.0",(self.result))
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def calculus(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.advanced()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_integration = Button(self.window,text="integration",bg="medium sea green",height=3,width=15,command=lambda:self.integration()).grid(row=0, column=0, pady=5,padx=5,stick=E+W)
        self.button_derivation = Button(self.window,text="derivation",bg="medium sea green",height=3,width=15,command=lambda :self.derivation()).grid(row=0,column=1,pady=5,padx=5,stick=E+W)
        self.button_convert = Button(self.window,text="Rad/Deg",bg="medium sea green", height=3,width=15,command=lambda:self.convert_rad_deg()).grid(row=1,column=0,pady=5,padx=5,stick=E+W)

    def convert_rad_deg(self):
        self.clear(self.window)
        self.column_config(2)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.calculus()).grid(row=4, column=1, pady=300,padx=10,stick=E+W)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("angle, show pi like number")).grid(row=4, column=0, pady=300,padx=10,stick=E+W)
        self.entry_angle = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.entry_angle.grid(row=1,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.button_to_rad = Button(self.window,text="rad to deg",bg="yellow green",height=3,width=15,command=lambda:self.do_convert_rad_deg(True)).grid(row=2, column=0,stick=E+W)
        self.button_to_deg = Button(self.window,text="deg to rad",bg="yellow green",height=3,width=15,command=lambda:self.do_convert_rad_deg(False)).grid(row=2, column=1,stick=E+W)
        self.label_result_angle = Label(self.window, text="",font=("Centaur",20), bg="snow")
        self.label_result_angle.grid(row=3, column=0,columnspan=2,stick=E+W)

    def do_convert_rad_deg(self,rad):
        try:
            if rad:
                result = np.rad2deg(eval(self.entry_angle.get()))
            else:
                result = np.deg2rad(float(self.entry_angle.get()))
            self.label_result_angle.config(text=f"α = {result}")
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def derivation(self):
        self.clear(self.window)
        self.column_config(2)
        self.entry_integration = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("derivate in function of x")).grid(row=3, column=0, pady=300,padx=10,stick=E+W)
        self.entry_integration.grid(row=0,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.calculus()).grid(row=3, column=1, pady=10,padx=10,stick=E+W)
        self.button_ok = Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.calculate_derivation()).grid(row=1, column=1,stick=E+W)
        self.label_result_integration = Label(self.window,text = " ", font=("Centaur",20),bg="snow")
        self.label_result_integration.grid(row=2,column=0,columnspan=2,stick=E+W)

    def calculate_derivation(self):
        try:
            x = sp.Symbol("x")
            result= sp.diff(eval(self.np_to_sp(self.entry_integration.get())),x)
            self.label_result_integration.config(text = result)

        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def integration(self):
        self.clear(self.window)
        self.column_config(2)
        self.entry_integration = Entry(self.window,font=("Centaur",20),width=25,borderwidth=1)
        self.button_help = Button(self.window, text="help", bg = "slate blue", height=3,width=15,command=lambda:self.equations_help("integrate in function of x")).grid(row=3, column=0, pady=300,padx=10,stick=E+W)
        self.entry_integration.grid(row=0,column=0,columnspan=2, stick=E+W,pady=10,padx=5)
        self.button_return = Button(self.window,text="Return",bg="peach puff",height=3,width=15,command=lambda:self.calculus()).grid(row=3, column=1, pady=10,padx=10,stick=E+W)
        self.button_ok = Button(self.window,text="OK",bg="yellow green",height=3,width=15,command=lambda:self.calculate_integration()).grid(row=1, column=1,stick=E+W)
        self.label_result_integration = Label(self.window,text = " ", font=("Centaur",20),bg="snow")
        self.label_result_integration.grid(row=2,column=0,columnspan=2,stick=E+W)

    def calculate_integration(self):
        try:
            x = sp.Symbol("x")
            result= sp.integrate(eval(self.np_to_sp(self.entry_integration.get())),x)
            self.label_result_integration.config(text = result)
            
        except Exception as Err:
            if self.debug:
                messagebox.showerror(title="Error",message=Err)
            else:
                messagebox.showerror(title="Error",message="incorrect information")

    def scientific(self):
        self.clear(self.window)
        self.simple()
        self.button_simple = Button(self.window,text="Simple",bg="DarkOrange3",height=3,width=15,command=lambda:self.simple()).grid(row=1, column=5, pady=5,padx=5,stick=E+W)
        self.button_sin = Button(self.window,text="SIN",bg="honeydew3",height=4,width=3,command=lambda :self.click("sin(")).grid(row=6,column=0,pady=5,padx=5,stick=E+W)
        self.button_cos = Button(self.window,text="COS",bg="honeydew3",height=4,width=3,command=lambda :self.click("cos(")).grid(row=6,column=1,pady=5,padx=5,stick=E+W)
        self.button_tan = Button(self.window,text="TAN",bg="honeydew3",height=4,width=3,command=lambda :self.click("tan(")).grid(row=6,column=2,pady=5,padx=5,stick=E+W)
        self.button_arccos = Button(self.window,text="ARCCOS",bg="honeydew3",height=4,width=3,command=lambda :self.click("arccos(")).grid(row=6,column=3,pady=5,padx=5,stick=E+W)
        self.button_arcsin = Button(self.window,text="ARCSIN",bg="honeydew3",height=4,width=3,command=lambda :self.click("arcsin(")).grid(row=6,column=4,pady=5,padx=5,stick=E+W)
        self.button_arctan = Button(self.window,text="ARCTAN",bg="honeydew3",height=4,width=3,command=lambda :self.click("arctan(")).grid(row=7,column=0,pady=5,padx=5,stick=E+W)
        self.button_tanh = Button(self.window,text="TANH",bg="honeydew3",height=4,width=3,command=lambda :self.click("tanh(")).grid(row=7,column=1,pady=5,padx=5,stick=E+W)
        self.button_sinh = Button(self.window,text="SINH",bg="honeydew3",height=4,width=3,command=lambda :self.click("sinh(")).grid(row=7,column=2,pady=5,padx=5,stick=E+W)
        self.button_cosh = Button(self.window,text="COSH",bg="honeydew3",height=4,width=3,command=lambda :self.click("cosh(")).grid(row=7,column=3,pady=5,padx=5,stick=E+W)
        self.button_ln = Button(self.window,text="LN",bg="honeydew3",height=4,width=3,command=lambda :self.click("ln(")).grid(row=7,column=4,pady=5,padx=5,stick=E+W)
        self.button_log = Button(self.window,text="LOG",bg="honeydew3",height=4,width=3,command=lambda :self.click("log(")).grid(row=8,column=0,pady=5,padx=5,stick=E+W)
        self.button_arctanh = Button(self.window,text="ARCTANH",bg="honeydew3",height=4,width=3,command=lambda :self.click("arctanh(")).grid(row=8,column=1,pady=5,padx=5,stick=E+W)
        self.button_arcsinh = Button(self.window,text="ARCSINH",bg="honeydew3",height=4,width=3,command=lambda :self.click("arcsinh(")).grid(row=8,column=2,pady=5,padx=5,stick=E+W)
        self.button_arccosh = Button(self.window,text="ARCCOSH",bg="honeydew3",height=4,width=3,command=lambda :self.click("arccosh(")).grid(row=8,column=3,pady=5,padx=5,stick=E+W)
        self.button_abs = Button(self.window,text="ABS",bg="honeydew3",height=4,width=3,command=lambda :self.click("abs(")).grid(row=8,column=4,pady=5,padx=5,stick=E+W)
    
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
        self.button_calculus = Button(self.window,text="calculus",bg="LightSkyBlue2", height=3, width=15, command=lambda: self.calculus()).grid(row=4,column=1,pady=30,padx=50,stick=E+W)
    
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
        self.coulomb_constant = Label(self.window_constants, text = "coulomb constant (k)= 8.9875517923x10⁹ N*m²/C²",font=("Soho",16),bg="snow",wraplength=520).pack()
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
calculator = Calculator(debug=True)
calculator.window.mainloop()
#atribuciones Icons made by <a href="https://www.flaticon.com/authors/dinosoftlabs" title="DinosoftLabs">DinosoftLabs</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
