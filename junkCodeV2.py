import time, os, random, string
from os import system, name
from math import *
try:
    import getpass
except:
    os.system('pip install getpass')
try:
    user = getpass.getuser()   # get user name \ can add dynamic location
except:
    pass

if name == 'nt':
    try:
        PATH = 'C:\\Users\\{}\\Desktop\\junkCode.txt'.format(user)
    except:
        PATH = 'D:\\Users\\{}\\Desktop\\junkCode.txt'.format(user)
else:
	PATH = "/tmp/junkCode.txt"

print('How much to generate? (Max 50/per. run)')
lista = []
choose_modeCode = int(input('>'))

def main():
    if choose_modeCode <= 1000 and choose_modeCode > 0:
        letters = string.ascii_letters
        for k in range(choose_modeCode):
            Lenght_extreme = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26]
            RLenght_extreme = random.choice(Lenght_extreme)
        ShitResult = ''.join(random.sample(letters, RLenght_extreme))
        def other():
            for i in range(RLenght_extreme):
                def Class_easy(length):
                    scriere_def = open(PATH, 'w')
                    result_str_Function_easy = ''.join(random.sample(letters, length))
                    scriere_def.write('class '+ result_str_Function_easy+':')
                Class_easy(RLenght_extreme)
                def Function_easy(length):
                    scriere_def = open(PATH, 'a')
                    for mata in range(RLenght_extreme):
                        result_str_Function_easy = ''.join(random.sample(letters, length))
                        scriere_def.write('\n'+ '\t'+ 'def '+ result_str_Function_easy+'():')
                        scriere_def.write('\n'+'\t'+ '\t'+ ShitResult+' = '+ "'{}'".format(ShitResult))
                        scriere_def.write('\n'+'\t'+ '\t'+ ShitResult+' = '+ str(RLenght_extreme ** RLenght_extreme * RLenght_extreme))
                        scriere_def.write('\n'+'\t'+ '\t'+ '#' + result_str_Function_easy+ result_str_Function_easy)
                Function_easy(RLenght_extreme)
                def Variabiles_easy(length):
                    result_str_Variabiles_easy = ''.join(random.sample(letters, length))
                    scriere_def = open(PATH, 'a')
                    scriere_def.write('\n'+'\t'+ '\t'+ '#' + result_str_Variabiles_easy+ "'{}'".format(result_str_Variabiles_easy))
                    scriere_def.write('\n'+'\t'+ '\t'+ result_str_Variabiles_easy+' = '+ str(RLenght_extreme ** RLenght_extreme * RLenght_extreme))
                    scriere_def.write('\n'+'\t'+ '\t'+ result_str_Variabiles_easy+' = '+ "'{}'".format(result_str_Variabiles_easy))        
                Variabiles_easy(RLenght_extreme)
    else:
        print('This option is invalid!')
        exit(0)

if __name__=='__main__':
    main()
