import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import subprocess
import os
import random
import time
import multiprocessing
from patterns1 import *
from statsmodels.tsa.arima_model import ARIMA

def trapezoideToRectangleInterpolation(a, nnum):
    for i in range(0,len(a)):
        if a[i] != 1.0 and  a[i] != 0.0:
            a[i] = 0.0
    return a

class state:
    def __init__(self, time, volume, temperature, energyComsuption ):
        self.t = time
        self.V = volume 
        self.T = temperature
        self.E = energyComsuption
class action:
    def __init__(self, piston=0, resistor=0, valve=0, expand=0):
        self.p   = piston
        self.r   = resistor 
        self.v   = valve   
        self.f   = expand

class automaton:
    def __init__(self):
        dataRead = pd.read_csv("Solargis_min15_Almeria_Spain.csv")
        valveRead= pd.read_csv("valve.csv")  # t1,t2,dur  
        dt_      = 15*60                          # Real time of the data 
        self.H   = 2*24*60*60                # Real time Interval from  [0-Horizont]
        num_ = int(self.H/dt_)               # Num of intervals         [0 - num*tau]  , but there are num+1 points  t[0] - t[num]
        t_  = np.linspace(0,self.H,num_+1)
        self.T_e = dataRead['Temperature'].values.tolist()[0:num_+1]
        self.I_  = dataRead['GTI'].values.tolist()[0:num_+1]
        v_  = valveRead['Flow'].values.tolist()[0:num_+1] 
        self.dt  = 60.0
        self.num = int(self.H/self.dt)+1
        self.t   = np.linspace(0,self.H,self.num)
        self.Te  = np.interp(self.t,t_,self.T_e)
        self.I   = np.interp(self.t,t_,self.I_)
        self.v   = trapezoideToRectangleInterpolation(np.interp(self.t,t_ ,v_),self.num)  
        self.Ti  = np.ones(self.num+1)*TwaterIn  # In c++ 25
        #self.si  = state(200*60 ,0.23,50,0) #state(0,0.23,50,0)   # start in the future
        self.si  = state(24*60*60 ,0.23,50,0) 
        self.state_curr   = self.si
        self.pattern_curr = []
        self.ai      = action()   #?
        self.actions = []
        self.states  = []
        self.actions.append(self.ai)        
        self.states.append(self.si)
        self.target = { 'Td' : 40, 'Vd' : 100,}, #data['Target'],   # 21 temperatura de comfort humanos
        self.modes  = [action(1,0,0,0), action(1,1,0,0), action(2,0,0,0), action(2,1,0,0), action(3,0,0,1), action(3,1,0,1), action(2,0,0,1),action(2,1,0,1)]
        #print(self.t[0:3])       # ????????????

    def forecast(self,X,pivotWindow,predictionSize):
        days_in_year = pivotWindow
        differenced = list()
        #print(X)   
        for i in range(days_in_year, len(X)):
            value = X[i] - X[i - days_in_year]
            differenced.append(value)
        # fit model
        model = ARIMA(differenced, order=(7,0,1))
        model_fit = model.fit(disp=0)
        # multi-step out-of-sample forecast
        start_index = len(differenced)
        end_index   = start_index + predictionSize
        #end_index   = start_index + 49#6
        forecast    = model_fit.predict(start=start_index, end=end_index)
        #print(forecast)
        # invert the differenced forecast to something usable
        history = [x for x in X]
        day = 1
        pred = []
        for yhat in forecast:
            #inverted = inverse_difference(history, yhat, days_in_year)
            inverted = yhat + history[-days_in_year] 
            #print('Day %d: %f' % (day, inverted))
            pred.append(inverted)
            history.append(inverted)
            day += 1
        return pred
                        
    def configXML(self, f):
        fin = open (f[0], "r")
        fout= open (f[1], "w+")
        t_min = int(self.state_curr.t/60)
        H_uppaal = 25*2+10   # minutes #print( self.Te[ t_min : t_min + H_uppaal ] )
        print("Predicting perturbations ..  ")
        # 15 min to min, tau=5min,  
        #pTe = self.forecast(list(self.Te[t_min-60*24:t_min]), 5*60, 59)
        #pI  = self.forecast(list(self.I[t_min-60*24:t_min]), 5*60, 59)
        #print("size pTe: ",len(pTe)," Te:",pTe)
        #print("size pI: ",len(pI)," I: ",pI)
        #print("t_min: ",t_min," H_uppaal: ",H_uppaal)
        #print("size Ti: ",len(self.Ti)," Ti: ",self.Ti[ t_min : t_min + H_uppaal])
        pat_size = len(self.pattern_curr)
        T_env_string = '{'+','.join([str(elem) for elem in self.Te[ t_min : t_min + H_uppaal] ])+'}'
        I_string     = '{'+','.join([str(elem) for elem in self.I [ t_min : t_min + H_uppaal] ])+'}'
        #T_env_string = '{'+','.join([str(elem) for elem in pTe ])+'}'
        #I_string     = '{'+','.join([str(elem) for elem in pI  ])+'}'
        T_in_string  = '{'+','.join([str(elem) for elem in self.Ti[ t_min : t_min + H_uppaal] ])+'}'
        t_string     = '{'+','.join([str(elem) for elem in self.t [ t_min : t_min + H_uppaal] ])+'}'
        va_string    = '{'+','.join([str(elem) for elem in self.v [ t_min : t_min + H_uppaal] ])+'}'
        pat_ans_string = '{'+','.join([str(elem) for elem in self.pattern_curr[ 0: pat_size] ]) +'}'
        print("pattern_curr: ",self.pattern_curr)
        print("pat sent to uppaal: ",pat_ans_string)
        print("size: ",pat_size)
        while True:
            line = fin.readline()
            if (line == "//HOLDER_T_ini\n"):
                fout.write('const double T_ini    = %5.2f; \n' % self.state_curr.T)
            if (line == "//HOLDER_V_ini\n"):
                fout.write('const double V_ini    = %5.2f; \n' % self.state_curr.V)
            if (line == "//HOLDER_E_ini\n"):
                fout.write('const double E_ini    = %5.2f; \n' % self.state_curr.E)
            if (line == "//HOLDER_t_ini\n"):
                fout.write('const double t_ini    = %5.2f; \n' % self.state_curr.t)
            if (line == "//HOLDER_u\n"):
                fout.write('int u                 = %d; \n' % int(self.state_curr.t/60) )
            if (line == "//HOLDER_taumin\n"):
                fout.write('int taumin            = %d; \n' % int(tau/60) )
            if (line == "//HOLDER_factorTe\n"):
                fout.write('const double factorTe = %5.2f; \n' % factorTe)
            if (line == "//HOLDER_factorI\n"):
                fout.write('const double factorI  = %5.2f; \n' % factorI)
            if (line == "//HOLDER_factorKe\n"):
                fout.write('const double factorKe = %5.2f; \n' % factorKe)
            if (line == "//HOLDER_rateVo\n"):
                fout.write('const double rateVo   = %5.2f; \n' % rate)
            if (line == "//HOLDER_TwaterIn\n"):
                fout.write('const double TwaterIn = %5.2f; \n' % TwaterIn)
            if (line == "//HOLDER_tau\n"):
                fout.write('const double tau      = %5.2f; \n' % tau)
            if (line == "//HOLDER_T_env[H+1]\n"):
                fout.write('const double T_env[%d]= %s; \n' % (H_uppaal,T_env_string) )
            if (line == "//HOLDER_T_in[H+1]\n"):
                fout.write('const double T_in[%d] = %s; \n' % (H_uppaal,T_in_string) )
            if (line == "//HOLDER_I[H+1]\n"):
                fout.write('const double I[%d]    = %s; \n' % (H_uppaal,I_string) )
            if (line == "//HOLDER_t[H+1]\n"):
                fout.write('const double t[%d]    = %s; \n' % (H_uppaal,t_string) )
            if (line == "//HOLDER_va[H+1]\n"):                                                  # ????
                fout.write('const double va[%d]   = %s; \n' % (H_uppaal,va_string) )		
            if (line == "//HOLDER_pat_ans\n"):
                fout.write('const int patAns[%d]   = %s; \n' % (pat_size,pat_ans_string) )
            if (line == "//HOLDER_pat_ans_size\n"):
                fout.write('const int patAnsSize   = %d; \n' % (pat_size) )
            else:
                fout.write(line)
            if not line :
                break
        return

    def callUppaal(self,f):
        print("calling .. ")
        line = "/home/serendipita/Documents/software/uppaal64-4.1.20-stratego-7/bin-Linux/verifyta " + f[1] + " " + f[2] 
        n = os.popen(line).readlines()
        i = 0
        while(1):
            if n[i] == "ppos:\n":
                ppos = n[i+1].split()
            if n[i] == "visitedPatterns:\n":
                visitedPatterns = n[i+1].split()
            if n[i] == "mode:\n":
                mode = n[i+1].split()
            if n[i] == "flag:\n":
                flag = n[i+1].split()
                break
            i = i + 1
        ppos.pop(0)
        visitedPatterns.pop(0)
        mode.pop(0)
        flag.pop(0)

        #print("ppos")
        for i in range(0,len(ppos)):
            ppos[i] = ppos[i][1:len(ppos[i])-1].split(",")
            ppos[i][0] = float(ppos[i][0])
            ppos[i][1] = float(ppos[i][1])
            #print(ppos[i])
        for i in range(0,len(visitedPatterns)):
            visitedPatterns[i] = visitedPatterns[i][1:len(visitedPatterns[i])-1].split(",")
            visitedPatterns[i][0] = float(visitedPatterns[i][0])
            visitedPatterns[i][1] = float(visitedPatterns[i][1])
        #print("mode")
        for i in range(0,len(mode)):
            mode[i] = mode[i][1:len(mode[i])-1].split(",")
            mode[i][0] = float(mode[i][0])
            mode[i][1] = float(mode[i][1])
            #print(mode[i])
        
        print("flag")
        for i in range(0,len(flag)):
            flag[i] = flag[i][1:len(flag[i])-1].split(",")
            flag[i][0] = float(flag[i][0])
            flag[i][1] = float(flag[i][1])
            print("ojo:", flag[i])


        obj={}
        for i in range(0,len(mode)-1):
            if mode[i][0] == mode[i+1][0]:
                obj[ mode[i][0] ] = mode[i+1][1]
        #print("obj: ",obj)
        pat = []
        for i in range(0,len(ppos)-1):
            if ppos[i+1][1] > ppos[i][1] and ppos[i+1][0] == ppos[i][0] :
                #print("pat: ",pat," ppost_0_t: ", ppos[i][0])                
                if ppos[i][1] == 0.0 and i!=0:            # ????  
                    pat.append(-1)                        # ????
                    if ppos[i][0] in obj:
                        pat.append( int(obj[ppos[i][0]]) )
                    else:
                        if len(pat)==0:
                            pat.append(0)                 # ????
                        else:
                            pat.append( int(pat[len(pat)-1]) )
                else: 
                    if ppos[i][0] in obj:
                        pat.append( int(obj[ppos[i][0]]) )
                    else:
                        if len(pat)==0:
                            pat.append(0)
                        else:
                            pat.append( int(pat[len(pat)-1]) )        
        #print("p1: ",pat)
        while(1):
            if pat.pop() == -1:
                break  
        pat = [value for value in pat if value != -1]
        #print("p2: ",pat)
        return pat

    def randomControllerOnce(self,s):
        patterns = query(s)
        h = int( (s.t)/(60*60) ) 
        m = (s.t)/60- h*60
        p = patterns[ random.randint(0,len(patterns)-1) ]
        print("time: %d h - %d min"%(h,m) , "-  patterns controller: ",p)
        return p

    def randomController(self,q,s):  # pat , ans size of pat'
        pat = self.pattern_curr
        E = s.E 
        V = s.V 
        T = s.T 
        for u in range(0,len(pat)):
            mode = action( self.modes[pat[u]].p,self.modes[pat[u]].r,self.v[u],self.modes[pat[u]].f )
            for i in range(0,int(tau/60)):
                E = E + self.dt*mode.r*2  # dt = 0.1
                V = V + self.dt*rate*( 0.1*mode.p - s.V ) # 0.5 = rate 0.01 = rate            self.rate_volume_change = 0.0002 # 0.193 
                T = T + self.dt*(1/(0.1*mode.p))*( 
                            - factorTe*2.8811059759131854e-06*(s.T-self.Te[i]) 
                            - mode.v*9.34673995175876e-05*(s.T-self.Ti[i])                 # valve
                            - mode.f*factorKe*0.001005026*(0.1*mode.p-V)*(s.T-self.Ti[i])
                            + factorI*0.7*0.7*8.403225763080125e-07*self.I[i]
                            + mode.r*0.008801843 )#0.00048018432931886426
                t = s.t + self.dt
                s = state(t,V,T,E)            
        patterns = query(s)
        n  = len(patterns)               
        h = int( (s.t)/(60*60) ) 
        m = (s.t)/60- h*60
        p = patterns[random.randint(0,n-1)]
        print("time: %d h - %d min"%(h,m) , "-  patterns controller: ",p)
        q.put(p)
    
    def uppaalController(self,q,s):
        f = ["1.xml","1c.xml","1c.q"] 
        self.configXML(f)
        p = self.callUppaal(f)
        h = int( (s.t)/(60*60) ) 
        m = (s.t)/60- h*60
        print("time: %d h - %d min"%(h,m) , "-  patterns controller: ",p)
        q.put(p)
    

    def simulation(self,controlName):
        # initial
        controllers = {"random":self.randomController,"uppaal":self.uppaalController,}
        s        = self.si        
        dt       = self.dt 
        num_tau  = tau/dt                  
        pat      = self.randomControllerOnce(s)
        self.pattern_curr = list(pat)
        self.d   = pat.pop(0)
        q = multiprocessing.Queue()
        p = multiprocessing.Process(target=controllers[controlName], args=(q,s))
        p.start()
        #for i in range(0,self.num-60):     # (0,self.num-1)         
        for i in range(24*60,self.num-60):
            if i%(num_tau) == 0 and i!=0: 
                if( len(pat) == 0 ):
                    pat = q.get()                  
                    self.pattern_curr = list(pat)
                    self.d = pat.pop(0)
                    p.join()
                    p = multiprocessing.Process(target=controllers[controlName], args=(q,s))
                    p.start()
                else:
                    self.d = pat.pop(0)              
            mode = action(self.modes[self.d].p,self.modes[self.d].r,self.v[i],self.modes[self.d].f)
            E = s.E + dt*mode.r*2  # dt = 0.1
            V = s.V + dt*rate*( 0.1*mode.p - s.V ) # 0.5 = rate 0.01 = rate            self.rate_volume_change = 0.0002 # 0.193 
            T = s.T + dt*(1/(0.1*mode.p))*( 
                        - factorTe*2.8811059759131854e-06*(s.T-self.Te[i]) 
                        - mode.v*9.34673995175876e-05*(s.T-self.Ti[i])                 # valve
                        - mode.f*factorKe*0.001005026*(0.1*mode.p-V)*(s.T-self.Ti[i])
                        + factorI*0.7*0.7*8.403225763080125e-07*self.I[i]
                        + mode.r*0.008801843 )#0.00048018432931886426
            t = s.t + dt
            s = state(t,V,T,E)
            self.state_curr = s
            self.actions.append(mode)  
            self.states.append( s )
        #return 
        return {"s": self.states, "a": self.actions, "H":self.H}



def plot(data,data2):
    T = []
    V = []
    E = []
    r = []
    p = []
    v = []

    T2 = []
    V2 = []
    E2 = []
    r2 = []
    p2 = []
    v2 = []

    time = []
    for i in data["s"]:
        T.append(i.T)
        V.append(i.V)
        E.append(i.E)
        time.append(i.t)
    for i in data["a"]:
        r.append(i.r)
        p.append(i.p+4)
        v.append(i.v+2)
    
    for i in data2["s"]:
        T2.append(i.T)
        V2.append(i.V)
        E2.append(i.E)
        #time.append(i.t)
    for i in data2["a"]:
        r2.append(i.r)
        p2.append(i.p+4)
        v2.append(i.v+2)

    plt.figure( figsize=(11, 11))
    grid = plt.GridSpec(4, 4, wspace=0.8, hspace=0.7)
    plt.subplot( grid[0,:2] )
    #plt.plot(t, A.getT() ,label='T')
    plt.plot(time,T , 'red',linewidth=0.8, label='Random')
    plt.plot(time,T2 , 'purple',linewidth=0.8, label='with Opt')                        # ?
    plt.ylabel('T(Celsius)')
    plt.xlabel('time(s)')
    plt.legend()
    plt.grid(True)
    plt.subplot( grid[0:1,2:4] )
    plt.plot(time,E,'red',linewidth=0.8,label="Random Patterns")
    plt.plot(time,E2,'purple',linewidth=0.8,label="Optimal Patterns")
    plt.ylabel('E(kJ)')
    plt.xlabel('time(s)')
    plt.legend()
    plt.grid(True)
    plt.subplot( grid[1:3,0:2] )
    plt.plot(T,V,'black',linewidth=0.5)
    plt.plot([R[1][0] , R[1][1], R[1][1], R[1][0],R[1][0]],
                [R[0][0] , R[0][0], R[0][1], R[0][1],R[0][0] ],
                'red',label="R region")
    plt.plot([S[1][0] , S[1][1], S[1][1], S[1][0],S[1][0]],
                [S[0][0] , S[0][0], S[0][1], S[0][1],S[0][0]],
                'purple',label="S region")
    plt.axis([10,100,0,0.4])
    plt.title('Random Controller')
    plt.ylabel('V(L)')
    plt.xlabel('T(C)')
    plt.legend()
    plt.subplot( grid[1:3,2:4] )
    plt.plot(T2,V2,'black',linewidth=0.5)
    plt.grid(True)
    plt.plot([R[1][0] , R[1][1], R[1][1], R[1][0],R[1][0]],
                [R[0][0] , R[0][0], R[0][1], R[0][1],R[0][0] ],
                'red',label="R region")
    plt.plot([S[1][0] , S[1][1], S[1][1], S[1][0],S[1][0]],
                [S[0][0] , S[0][0], S[0][1], S[0][1],S[0][0]],
                'purple',label="S region")
    plt.axis([10,100,0,0.4])
    plt.title('Optimal Controller')
    plt.ylabel('V(L)')
    plt.xlabel('T(C)')
    plt.legend()
    plt.grid(True)
    # but have shapes (2881,) and (576,)
    plt.subplot( grid[3,:2] )
    plt.plot(time,r,'red',linewidth=0.8)
    plt.plot(time,v,'purple',linewidth=0.8)
    plt.plot(time,p,'orange',linewidth=0.8)
    plt.axis([0,data["H"],0,8])
    plt.ylabel('{r,v,p}')
    plt.xlabel('time(s)')
    plt.legend()
    plt.grid(True)
    plt.subplot( grid[3,2:4] )
    plt.plot(time,r2,'red',linewidth=0.8)
    plt.plot(time,v2,'purple',linewidth=0.8)
    plt.plot(time,p2,'orange',linewidth=0.8)
    plt.axis([0,data2["H"],0,8])
    plt.ylabel('{r,v,p}')
    plt.xlabel('time(s)')
    plt.legend()
    plt.grid(True)
    plt.show()

A = automaton()
data = A.simulation("random") 
B = automaton()
data2 = B.simulation("uppaal")
plot(data,data2)