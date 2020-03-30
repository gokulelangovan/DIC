import numpy as np 
import matplotlib.pyplot as plt 
def regression(x, y, b): 
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30) 
  
 
    y_pred = b[0] + b[1]*x 
  
    
    plt.plot(x, y_pred, color = "g") 
  
  
    plt.xlabel('x') 
    plt.ylabel('y') 
  
 
    plt.show() 
def coef_estimation(x, y):  
    n = np.size(x) 
  
  
    m_x, m_y = np.mean(x), np.mean(y) 
  
   
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 
  
   
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 
  
    return(b_0, b_1) 
def main(): 
 
    x = np.array([509,748,757,818,911,1211,1451,1537,1611,1684,1911,1961,2111,3783]) 
    y = np.array([24.1,31.85,35,37.22,40,38,60.56,53.5,53,78,75,73,110,133]) 
  

    b = coef_estimation(x, y) 
    
  
    regression(x, y, b) 
    print("Regression - m and c are:\nm = {}  \nc = {}".format(b[0], b[1]))
if __name__ == "__main__": 
    main()