import os,sys,platform

#sys.argv ilə terminaldan argument göndərmək və ekrana yazmaq olur
def my_func(x=sys.argv):
   print(x[1])
   print(str(sys.argv))
   #os.name vasitəsi ilə əməliyyat sistemi görmək mümkündür
   print(os.name)
   #sys..getdefaultencoding vasitəsi ilə kodlamamızın utf-8 və ya hansı olduğunu görə bilərik
   print(sys.getdefaultencoding())
   #platform.architecture Linux və ya Windows ƏS görmək olur
   print(platform.architecture())


if __name__=="__main__":
   my_func()
