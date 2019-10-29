

# -*- coding: utf-8 -*

import sys

import socket

from socket import error as socket_error



import time

import random




host = "commu-042.local"

#host2 = "DESCTOP-MBC1RGT.local"

#host2 = "projector-pc-01.local"

#host2 = "projector-pc-02.local"

#host2 = "Lenovo-projection-01.local"

host2 = "192.168.1.17"


port = 8079

port2 = 8078

port3 = 7007


#port3 = 12345


command_list = ['ojigi', 'walk', 'shakehand', 'baibai', 'nod_fast', 'nod_normal', 'hidarimuku', 'migimuku', 'eyeblink', 'eyeblinkInteri', 'eyeblinkTwiceInteri', 'hi', 'nod2', 'sugoi' ]

fukidashi_list = ['fukidashi_normal', 'fukidashi_emphasize', 'fukidashi_nigate' ]

icon_list = ['question', 'ase', 'kakusei', 'shonbori', 'question_2' ]


wait_for_talk = 2

beh_period = 7 



if __name__ == '__main__':



    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_voice = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_projection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:

        client.connect((host, port))

        client_voice.connect((host, port2))

        client_projection.connect((host2,port3))

    except socket_error as serr:

        print("Connection:"+str(host)+":"+str(port)+" refused.")

        sys.exit()




    startTime = time.time()

    count = 0

    time.sleep(4)

    while(True):

        currentTime = time.time()

        diff_time = round(currentTime - startTime)

        if(diff_time % beh_period == 0):
            count +=1

            if (count == 1):

                output_text = "/gesture " + command_list[0]

                client.send(str(output_text).encode('utf-8'))

                print("duff_time = ", diff_time)

                print("Sending command:", str(output_text))

                time.sleep(wait_for_talk)

                client_voice.send(str("/say こんにちは[EOF]").encode('utf-8'))

                projection_mes = "json_projector_" + fukidashi_list[0]
                
                print(projection_mes)

                client_projection.send(str(projection_mes).encode('utf-8'))

                time.sleep(beh_period-3)

            if (count == 2):

                output_text = "/gesture " + command_list[11]

                client.send(str(output_text).encode('utf-8'))

                print("duff_time = ", diff_time)

                print("Sending command:", str(output_text))

                time.sleep(wait_for_talk)

                client_voice.send(str("/say きょうはあついね[EOF]").encode('utf-8'))

                projection_mes = "json_projector_" + icon_list[1]

                client_projection.send(str(projection_mes).encode('utf-8'))

                time.sleep(beh_period-3)


            if (count == 3):

                output_text = "/gesture " + command_list[11]

                client.send(str(output_text).encode('utf-8'))

                print("duff_time = ", diff_time)

                print("Sending command:", str(output_text))

                time.sleep(wait_for_talk)

                client_voice.send(str("/say 暑いときは怖い話をするといいらしいね[EOF]").encode('utf-8'))

                projection_mes = "json_projector_" + icon_list[0]

                client_projection.send(str(projection_mes).encode('utf-8'))

                time.sleep(beh_period-3)

            if (count == 4):

                output_text = "/gesture " + command_list[11]

                client.send(str(output_text).encode('utf-8'))

                print("duff_time = ", diff_time)

                print("Sending command:", str(output_text))

                time.sleep(wait_for_talk)

                client_voice.send(str("/say 怖い話はすき？[EOF]").encode('utf-8'))

                projection_mes = "json_projector_" + icon_list[4]

                client_projection.send(str(projection_mes).encode('utf-8'))

                time.sleep(beh_period-3)

            if (count == 5):

                output_text = "/gesture " + command_list[13]

                client.send(str(output_text).encode('utf-8'))

                print("duff_time = ", diff_time)

                print("Sending command:", str(output_text))

                time.sleep(wait_for_talk)

                client_voice.send(str("/say そうなんだ[EOF]").encode('utf-8'))

                projection_mes = "json_projector_" + icon_list[2]

                client_projection.send(str(projection_mes).encode('utf-8'))

                time.sleep(beh_period-3)

            if (count == 6):

                output_text = "/gesture " + command_list[5]

                client.send(str(output_text).encode('utf-8'))

                print("duff_time = ", diff_time)

                print("Sending command:", str(output_text))

                time.sleep(wait_for_talk)

                client_voice.send(str("/say もちろん好きだよ[EOF]").encode('utf-8'))

                projection_mes = "json_projector_" + fukidashi_list[2]

                client_projection.send(str(projection_mes).encode('utf-8'))

                time.sleep(beh_period-3)

            if (count == 7):

                output_text = "/gesture " + command_list[8]

                client.send(str(output_text).encode('utf-8'))

                print("duff_time = ", diff_time)

                print("Sending command:", str(output_text))

                projection_mes = "json_projector_" + icon_list[2]

                client_projection.send(str(projection_mes).encode('utf-8'))

                time.sleep(beh_period-3)

            if (count == 8):

                output_text = "/gesture " + command_list[13]

                client.send(str(output_text).encode('utf-8'))

                print("duff_time = ", diff_time)

                print("Sending command:", str(output_text))

                time.sleep(wait_for_talk)

                client_voice.send(str("/say なんでわかったの[EOF]").encode('utf-8'))

                projection_mes = "json_projector_" + fukidashi_list[1]

                client_projection.send(str(projection_mes).encode('utf-8'))

                time.sleep(beh_period-3)

            if (count == 9):

                output_text = "/gesture " + command_list[8]

                client.send(str(output_text).encode('utf-8'))

                print("duff_time = ", diff_time)

                print("Sending command:", str(output_text))

                time.sleep(wait_for_talk)

                client_voice.send(str("/say ええええ[EOF]").encode('utf-8'))

                projection_mes = "json_projector_" + icon_list[3]

                client_projection.send(str(projection_mes).encode('utf-8'))

                time.sleep(beh_period-3)

                break
