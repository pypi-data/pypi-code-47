"""
File: interacter.py
Author: Edwinn Gamborino
Institution: NTU Center for Artificial Intelligence and Advanced Robotics
Version: v0.2.6
"""
import os
import grpc
from interacter import interaction_pb2
import time
from random import randrange
from concurrent import futures
from hanziconv import HanziConv
import socket
import logging

class Server(interaction_pb2.InteractServicer):
    """ 
    This is the only class in the interacter package.
    It creates a gRPC server with the computer's local ip address with a specified port.
    """

    logging.basicConfig(level=os.environ.get("LOGLEVEL","INFO"))
    log = logging.getLogger(__name__)
    
    locale = ''
    is_robot_connected = False
    robot_type = ''
    robot_command = None
    user_utterance = ''

    motions = {
        "en":["Face Up", "Face Down", "Face Right", "Face Left", "Turn Right", "Turn Left", "Right Hand Up", "Left Hand Up", "Both Hands Up", "Walk", "Walk Back", "Walk Right", "Walk Left", "Push Ups", "Kick Ball", "Sit Up", "Brisk Walking", "Handstand", "Stand Up", "Sit Down", "Finish Mobile", "Shot Pose", "Enchant"],
        "zh":["向上看", "向下看", "向右看", "向左看", "向右转", "向左转", "举起右手", "举起左手", "举起双手", "走路", "后退", "向右走", "向左走", "俯卧撑", "踢球", "仰卧起坐", "快速走", "倒立", "站起来", "坐下", "结束外出姿势", "拍照姿势", "著迷"],
        "jp":["顔上向き", "顔下向き", "顔右向き", "顔左向き", "右向き", "左向き", "右手挙げ", "左手挙げ", "両手挙げ", "歩き", "後ろ歩き", "右歩き", "左歩き", "腕立て", "ボール蹴り", "腹筋", "早歩き", "逆立ち", "立つ", "座る", "お出かけ姿勢終了", "写真ポーズ", "メロメロ"]
    }
    
    dances = {
        "en":["A Little Night Music", "Under the Spreading Chestnut Tree", "Awa Odori", "Air Guitar", "Wind the Bobbin Up", "Greenville", "Tanuki Pup", "Symphony No.", "Jingle Bells", "Kung Fu", "80's Disco", "Sakura", "Military March", "Flamenco", "The Hula", "Baseball Cheer", "Che Che Kule", "Head Sholder Knees and Toes", "Japanese Drum", "Joy to the World", "Kabuki", "The Nutcracker", "Doll's Festival", "RoBoHoN Exercises", "Orpheus in the Underworld", "70's Disco", "I am an Ocean Boy", "RoBoHoN Ondo", "Air Violin", "Tap Dance", "Para Para Dance", "We Wish You a Merry Christmas", "Rabbit Dance", "Cossack Dance", "Lullaby", "Cheerleading", "Marching Band", "The Other Day I Met a Bear", "Radio Exercises", "RoBoHoN's Bootcamp", "Haka", "Chanbara", "Wotagei", "Silent Night", "Spring Sea"],
        "zh":["小夜曲", "在很大的栗子樹下", "阿波舞", "吉他空彈", "卷線歌", "打開結", "拳頭山的狸先生", "第九交響曲", "鈴兒響叮噹", "功夫", "八十年代迪斯科", "櫻花", "軍隊進行曲", "佛朗明哥", "草裙舞", "棒球助威", "加納民歌", "頭兒肩膀膝腳趾", "日本鼓", "普世歡騰", "歌舞伎", "胡桃夾子", "雛祭", "RoBoHoN體操", "天國與地獄", "七十年代迪斯科", "我是大海的兒子", "RoBoHoN集体舞", "小提琴空彈", "踢踏舞", "芭啦芭啦舞", "祝你聖誕快樂", "兔子舞", "哥薩克舞蹈", "搖籃曲", "啦啦隊", "遊行樂隊", "森林裡的熊先生", "廣播體操", "RoBoHoN的訓練兵営", "哈卡舞", "劍鬥", "御宅藝", "平安夜", "春海"],
        "jp":["アイネ・クライネ・ナハトムジーク", "大きな栗の木の下で", "阿波踊り", "エアギター", "糸巻きの歌", "結んで開いて", "げんこつ山の狸さん", "交響曲第９番", "ジングルベル", "カンフー", "80年代ディスコ", "さくら", "ミリタリーマーチ", "フラメンコ", "フラダンス", "野球応援", "チェッコリ", "体遊びの歌", "和太鼓", "もろびとこぞりて", "歌舞伎", "くるみ割り人形", "ひな祭り", "ロボホン体操", "天国と地獄", "70年代ディスコ", "我は海の子", "ロボホン音頭", "エアバイオリン", "タップダンス", "パラパラ", "おめでとうクリスマス", "うさぎのダンス", "コサックダンス", "子守唄", "チアリーディング", "マーチングバンド", "森のくまさん", "ラジオ体操", "ロボホンズブートキャンプ", "ハカ", "ちゃんばらごっこ", "ヲタ芸", "きよしこの夜", "春の海"]
    }

    def __init__(self, port, locale):
        """ 
        The constructor for Server class. 
  
        Arguments: 
           port (int): The port where the server will be listening for incoming client connections. 
           locale (String): The language the robot should speak in. Currently only English (en), Chinese (zh) and Japanese (jp) are supported.
        """

        common_actions = ['take_photo', 'take_video', 'show_photo', 'show_video', 'play_youtube']
        self.robohon_actions = common_actions + ['dance', 'motion']
        self.zenbo_actions = common_actions

        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        interaction_pb2.add_InteractServicer_to_server(self, self.server)
        self.server.add_insecure_port('[::]:' + str(port))
        self.log.info('gRPC server started on address '+ self.get_ip() + ':' + str(port))
        
        if locale in ['zh','en','jp']:
            self.locale = locale
            self.server.start()
        else:
            raise ValueError('Interacter locale supports only Chinese (zh), English (en) or Japanese (jp).')

    def RobotConnect(self, request, context):
        """ 
        This method is called when a client connects to the server. 
        """

        self.is_robot_connected = True
        self.robot_type = request.status
        return interaction_pb2.RobotConnectReply(status=self.locale)

    def RobotSend(self, request, context):
        """ 
        This method is called every time a message is received from the client. 
        """

        if(request.utterance == 'locale_mismatch'):
            log.warning("Server and client locales do not match!")
        
        self.user_utterance = request.utterance
        if self.locale == 'zh':
            self.user_utterance = self.toTraditional(self.user_utterance)

        self.log.debug('received message: ' + self.user_utterance)
        self.robot_command = None
        while self.robot_command == None:
            time.sleep(.5)

        return interaction_pb2.RobotOutput(utterance=self.robot_command)

    def say(self, speech, listen=False):
        """ 
        Call this method to make the robot say something.

        Arguments:
            speech (String): The actual sentence you want the robot to say.
            listen (bool): When set to False, the robot will say a sentence and immediately expect the next command.
            When set to True, after talking the robot will wait for the user to speak, parse the speech and send it back to the server.
        Returns:
            message (String): If listen=True, you can get the user's speech as the return value of this function, otherwise it will return None.
        """

        if speech != '':
            if listen:
                self.log.info('say and listen: ' + speech)
                self.robot_command = 'mgetreply#' + speech
                while self.robot_command != None:
                    time.sleep(0.1)
                return self.user_utterance
            else:
                self.log.info('say: ' + speech)
                self.robot_command = 'mcont#' + speech
                while self.robot_command != None:
                    time.sleep(0.1)
                return None
        else:
            raise ValueError('Speech cannot be empty!')

    def move(self, x=0, y=0, theta=0, pitch=0):
        """ 
        Call this method to make the robot move to a specific goal pose [x,y,theta,pitch]. Available only for Zenbo Junior.

        Arguments:
            x (float): Distance to move in the x-axis in meters.
            y (float): Distance to move in the y-axis in meters.
            theta (int): Orientation of the robot in degrees.
            pitch (int): Angle of the head in degrees.

        Notes:
            All cordinates are relative to the current position of the robot.
            The positive x-axis is the direction the robot is facing.
            The positive y-axis is to the left side of the robot.
            Theta is measured clockwise from a top-view relative to the initial orientation of the x axis.
            Pitch ranges from -20 (lowest) to 40 (highest) degrees.
            
            The robot will traverse the shortest linear path between the current postion and the goal position.
            Curved trajectories are not supported.
            If the robot senses an obstacle or the edge of the moving surface (e.g. table), it will automatically stop until the obstacle is cleared.
        """

        if self.robot_type == 'zenbo':
            self.log.info('moving robot to (' + str(x) + ',' + str(y) + ',' + str(theta) + ',' + str(pitch) + ')')
            self.robot_command = 'mmove_cmd,' + str(x) + ',' + str(y) + ',' + str(theta) + ',' + str(pitch)
            while self.robot_command != None:
                time.sleep(0.1)
            return
        else:
            raise ValueError('move() method not available for ' + self.robot_type)

    def action(self, value, args=None):
        """
        Call this method to make the robot execute an action.

        Arguments:
            value: The name of the action
            args: If required, any arguments specific for the action chosen.

        Please refer to the documentation for more details on how to use the action library.
        """

        if self.robot_type == 'zenbo' and value in self.zenbo_actions or self.robot_type == 'robohon' and value in self.robohon_actions: 
            if value == 'dance':
                value = self.getDance(value, args)
            elif value == 'motion':
                value = self.getMotion(value, args)
            elif value == 'take_video' or  value == 'show_photo' or value == 'show_video' or value == 'play_youtube':
                if(args == None):
                    raise ValueError('Cannot have empty args!')
                value += ',' + str(args)

            self.log.info('Performing action ' + value) 
            self.robot_command = 'm' + value
            while self.robot_command != None:
                time.sleep(0.1)
            return
        else:
            raise ValueError('action(' + value + ') not available for ' + self.robot_type)
    
    def getDance(self, value, args):
        """
        This method is called to determine if the selected dance (index or name) is defined in the dances array.
        If it is, it returns the index of the item. Otherwise it will raise an exception.
        """

        if args == None:
            raise ValueError('Cannot have empty args!')
        if args.isdigit():
            if int(args) - 1 in range(len(self.dances[self.locale])):
                value += ',' + str(args)
            elif int(args) == 0:
                value += ',' +str(randrange(len(self.dances[self.locale])))
            else:
                raise ValueError(args + ' not in dances array')
        else:
            if args in self.dances[self.locale]:
                value += ',' + str(self.dances[self.locale].index(args) + 1)
            else:
                raise ValueError(args + ' not in dances array')
        return value

    def getMotion(self, value, args):
        """
        This method is called to determine if the selected motion (index or name) is defined in the motions array.
        If it is, it returns the index of the item. Otherwise it will raise an exception.
        """
        
        if args == None:
            raise ValueError('Cannot have empty args!')
        if args.isdigit():
            if int(args) in range(len(self.motions[self.locale])):
                value += ',' + str(args)
            elif int(args) == 0:
                value += ',' +str(randrange(len(self.motions[self.locale])))
            else:
                raise ValueError(args + ' not in motions array')
        else:
            if args in self.motions[self.locale]:
                value += ',' + str(self.motions[self.locale].index(args) + 1)
            else:
                raise ValueError(args + ' not in motions array')
        return value
    
    def toTraditional(self, term):
        """
        This method converts traditional Chinese to simplified Chinese characters.
        """
        return HanziConv.toTraditional(term)
    
    def get_ip(self):
        """
        This method returns the current ip address of the computer.
        """
        
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP