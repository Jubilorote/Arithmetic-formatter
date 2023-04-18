import re
def arithmetic_arranger(problems, affres=False):
  opelist=[]
  resultat=0 #INT
  resultats=[]
  showing=[]
  sign=None
  signs=[]
  operand1=[]
  operand2=[]
  arranged_problems=""
  wspace=" "

  if len(problems)<=5:
    for problem in problems:
      #print(problem) # "32 + 8"
      if (problem.find("*")>-1) or (problem.find("/")>-1):
        return "Error: Operator must be '+' or '-'."
        break
      number = problem.replace('+','-').strip()
      number = number.split('-') ##['5611','5615']
      #print(number)
      if problem.find("+")>-1:
        try:
          #print('It is an add')
          sign='+'
          resultat= int(number[0])+int(number[1])
        except:
          return 'Error: Numbers must only contain digits.'
      else:
        try:
          #print("It is a subs")
          sign="-"
          resultat=int(number[0])-int(number[1])
        except: 
          return'Error: Numbers must only contain digits.'
      #print(resultat)
      resultats.append(resultat) 
      operand1.append(number[0].replace(" ", ""))
      operand2.append(number[1].replace(" ", ""))
      signs.append(sign)
      


    #print(resultats) #[40, -3800, 19998, 474]
    #print(operand1) #['32', '1', '9999', '523']
    #print(operand2) #['8', '3801', '9999', '49']
    #print(signs) #['+', '-', '+', '-']
    #print(len(signs))
    ligne1=""
    ligne2=""
    ligne3=""
    i=0
    diff=0
    tiret=""
    a=""
    while i<= len(signs)-1:   
          if len(operand1[i])>4 or len(operand2[i])>4:
            return "Error: Numbers cannot be more than four digits."
            break
          nbC1=len(operand1[i])
          nbC2=len(operand2[i])
          strr=str(resultats[i])
          nbR=len(strr)
          #print(diff)
          #print(type(operand1[i]))
          if operand1[i]>operand2[i]:
                diff=nbC1-nbC2+2
                ligne1+=2*wspace+(operand1[i])
                ligne2+=signs[i]+(diff-1)*wspace+(operand2[i])
                a=(len(operand1[i])+2)*'-'
          else:
                diff=nbC2-nbC1+2
                ligne1+=diff*wspace+(operand1[i])     
                ligne2+=signs[i]+wspace+operand2[i]
                a=(len(operand2[i])+2)*'-'
          ligne3+=(len(a)-nbR)*wspace+str(resultats[i])+4*wspace
          ligne1+=4*wspace
          ligne2+=4*wspace 
          tiret+=a+4*wspace    
          i=i+1 
    #print(ligne1)
    #print(ligne2)
    #print(tiret)
    arranged_problems=ligne1 +"\n"+ligne2+"\n"+tiret+"\n"
    if affres is True:
        arranged_problems+="\n"+ligne3 
    return arranged_problems
  else:
        return "Error: Too many problems."
