import sys
import optparse , os
import encryption , decryption

if __name__ == '__main__':
    opts = optparse.OptionParser()
    opts.add_option('-e' , '--encrypt' , dest='encrypt' , action='store_true' , default=False)
    opts.add_option('-d' , '--decrypt' , dest='decrypt' , action='store_true' , default=False)
    
    option, arg = opts.parse_args()

    
    if option.encrypt and option.decrypt:
        print('You can only choose one of the two options')
        sys.exit(1)

    if option.encrypt:
        if not os.path.exists(arg[0]):
            print("File",arg[0],"does not exist!")
            sys.exit(1)
        encryption.main(arg[0] , arg[1])
        
    elif option.decrypt:
        if not os.path.exists(arg[0]):
            print("File",arg[0],"does not exist!")
            sys.exit(1)
        if not os.path.exists(arg[1]):
            print("File",arg[1],"does not exist!")
            sys.exit(1)
        decryption.main(arg[0] , arg[1])
    else:
        print("Usage : python secret_music.py -e <file_name> <text> \n\t python secret_music.py -d <file_name> <encrypt_file_name>")