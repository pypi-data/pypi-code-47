__version__ = "0.0.2"

import argparse
import os
import sys

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("-path", required=True, help="Pass the path to the project")
parser.add_argument("-s" , type= bool ,help="Create files in screens folder")
parser.add_argument("-c" , type= bool, help="Create files in components folder")
parser.add_argument("-rn" , type= bool, help="Whether platform is react-native")
parser.add_argument("-r" , type= bool, help="Whether platform is react")
parser.add_argument("-n" , required=True, help="Name of the Component")
args = parser.parse_args()
_path = args.path
_s = args.s
_c = args.c
_n = args.n
_r = args.r
_rn = args.rn

def main():

    cond_1 = _s != True and _c != True
    cond_2 = _r != True and _rn != True

    if( cond_1 ):
        print('\nProvide either --s or --c flag')
        sys.exit()

    if( len(_n) == 0 ):
        print('\nProvide the name for the component')
        sys.exit()

    if( cond_2 ):
        print('\nPlease specify the platform either react-native(--rn) or react(--r)')
        sys.exit()
    
    if( _s == True ):
        create( "Screens" )
    
    if( _c == True ):
        create( "Components" )

def createFiles_RN( _name ):
    os.chdir("{}/{}".format(_path,_name))
    os.makedirs(str(_n))
    os.chdir("{}/{}/{}".format(_path,_name,str(_n)))
    with open( 'index.js', 'w') as f:
        data = "import React,{Component} from \'react\'\nimport { View } from \'react-native\'\nimport Styles from \'./Styles.js\'\nexport default class "+str(_n)+" extends Component{\n\nconstructor(props){\nsuper(props)\nthis.state={\n}\n}\n\nrender(){\nreturn(\n<View style={Styles.Container}></View>\n)\n}\n}"
        f.write(data)
    with open( 'Styles.js', 'w') as f:
        data = "import { StyleSheet } from \'react-native\'\n\nexport default Styles = StyleSheet.create({\n\nContainer: {\n flex: 1,\n backgroundColor: \'red\'\n}\n});"
        f.write(data)
    print('\nSuccessfully created {}.'.format(_n))
    sys.exit()

def createFiles_R( _name ):
    os.chdir("{}/{}".format(_path,_name))
    os.makedirs(str(_n))
    os.chdir("{}/{}/{}".format(_path,_name,str(_n)))
    with open( 'index.js', 'w') as f:
        data = "import React,{Component} from \'react\'\nimport \'./Styles.css\'\nexport default class "+str(_n)+" extends Component{\n\nconstructor(props){\nsuper(props)\nthis.state={\n}\n}\n\nrender(){\nreturn(\n<div className=\"Container\"></div>\n)\n}\n}"
        f.write(data)
    with open( 'Styles.css', 'w') as f:
        data = ".Container{\n  background-color: red\n}"
        f.write(data)

    print('\nSuccessfully created {}.'.format(_n))
    sys.exit()


def create( _name ):
    if not os.path.exists("{}/{}".format(_path,_name)):
        os.chdir(_path)
        os.makedirs(_name)
        if( _rn ):
            createFiles_RN( _name )
        elif( _r ):
            createFiles_R(_name)
    else:
        if( _rn ):
            createFiles_RN( _name )
        elif( _r ):
            createFiles_R(_name)

