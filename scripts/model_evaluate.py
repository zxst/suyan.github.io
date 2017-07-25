#script of model evaluate
#author ：zxst
#time : 2017/07/24
def R_square(x,y):
    if ('numpy.ndarray' in str(type(x)))&('numpy.ndarray' in str(type(y))):
        sse = sum((x-y)**2)
        sst = sum((y-np.mean(y))**2)
        R_square = 1-sse/sst
        return(R_square)
    else:
        print("please input array")

##接下来是分类为题
