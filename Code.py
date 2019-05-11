#linear regression, here we come

from numpy import *


def run():

	gradient_descent_runner()
	
	#required equation is y=mx+b


def cost_function(get_m,get_b,length):
	b=get_b
	m=get_m
	size=length
	dataset=genfromtxt("Desktop\\data.csv",delimiter =",")
	hypothesis=0
	sumerr=0
	sumerrx=0

	for i in range(0,size):
		hypothesis=(m*dataset[i,0])+b
		sumerr+=(hypothesis-dataset[i,1])
		sumerrx+=((hypothesis-dataset[i,1])*dataset[i,0])

	return [sumerr, sumerrx]


def gradient_descent(this_b,this_m,rate,sum_errors,sum_errors_x,length):

	b=this_b
	m=this_m
	size=length

	b-=((rate/size)*(sum_errors))
	m-=((rate/size)*(sum_errors_x))

	return[m,b]

def gradient_descent_runner():


	dataset=genfromtxt("Desktop\\data.csv",delimiter =",")

	m_actual=0
	b_actual=0
	size=float(len(dataset))
	rate=0.0001


	for i in range(1,1000):
		err=0
		errx=0
		[err,errx]=cost_function(m_actual,b_actual,len(dataset))
		[m_actual,b_actual]=gradient_descent(b_actual,m_actual,rate,err,errx,size)
		continue

	print("m final value is: ",m_actual)
	print("b final value is: ",b_actual)

run()
