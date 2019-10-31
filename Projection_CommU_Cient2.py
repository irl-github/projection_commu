

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

host2 = "192.168.1.24"


port = 8079

port2 = 8078

port3 = 7007


#port3 = 12345


command_list = ['ojigi', 'walk', 'shakehand', 'baibai', 'nod_fast', 'nod_normal', 'hidarimuku', 'migimuku', 'eyeblink', 'eyeblinkInteri', 'eyeblinkTwiceInteri', 'hi', 'nod2', 'sugoi' ]

fukidashi_list = ['fukidashi_part1', 'fukidashi_part2', 'fukidashi_part3', 'fukidashi_part4', 'fukidashi_part5', 'fukidashi_part6', 'fukidashi_part7', 'fukidashi_part8', 'fukidashi_part9', 'fukidashi_part10', 'fukidashi_part11', 'fukidashi_part12', 'fukidashi_part13', 'fukidashi_part14', 'fukidashi_part15', 'fukidashi_part16', 'fukidashi_part17', 'fukidashi_part18', 'fukidashi_part19', 'fukidashi_part20', 'fukidashi_part21' ]


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

                output_text = "/gesture " + command_list[11]

                client.send(str(output_text).encode('utf-8'))

                print("duff_time = ", diff_time)

                print("Sending command:", str(output_text))

                time.sleep(wait_for_talk)

                client_voice.send(str("/say 僕、いちごが好きなんだ[EOF]").encode('utf-8'))

                projection_mes = "json_projector_" + fukidashi_list[0]
                
                print(projection_mes)

                client_projection.send(str(projection_mes).encode('utf-8'))

                time.sleep(beh_period-3)

            if (count == 2):

                output_text = "/gesture " + command_list[12]

                client.send(str(output_text).encode('utf-8'))

                print("duff_time = ", diff_time)

                print("Sending command:", str(output_text))

                time.sleep(wait_for_talk)

                client_voice.send(str("/say 僕、映画が好きなんだ[EOF]").encode('utf-8'))

                projection_mes = "json_projector_" + fukidashi_list[1]

                client_projection.send(str(projection_mes).encode('utf-8'))

                time.sleep(beh_period-3)


            if (count == 3):

                output_text = "/gesture " + command_list[5]

                client.send(str(output_text).encode('utf-8'))

                print("duff_time = ", diff_time)

                print("Sending command:", str(output_text))

                time.sleep(wait_for_talk)

                client_voice.send(str("/say 僕、パスタが好きなんだ[EOF]").encode('utf-8'))

                projection_mes = "json_projector_" + fukidashi_list[2]

                client_projection.send(str(projection_mes).encode('utf-8'))

                time.sleep(beh_period-3)

            if (count == 4):

                output_text = "/gesture " + command_list[11]

                client.send(str(output_text).encode('utf-8'))

                print("duff_time = ", diff_time)

                print("Sending command:", str(output_text))

                time.sleep(wait_for_talk)

                client_voice.send(str("/say 僕、メロンソーダが好きなんだ[EOF]").encode('utf-8'))

                projection_mes = "json_projector_" + fukidashi_list[3]

                client_projection.send(str(projection_mes).encode('utf-8'))

                time.sleep(beh_period-3)

            if (count == 5):

                output_text = "/gesture " + command_list[8]

                client.send(str(output_text).encode('utf-8'))

                print("duff_time = ", diff_time)

                print("Sending command:", str(output_text))

                time.sleep(wait_for_talk)

                client_voice.send(str("/say 僕、ケーキが好きなんだ[EOF]").encode('utf-8'))

                projection_mes = "json_projector_" + fukidashi_list[4]

                client_projection.send(str(projection_mes).encode('utf-8'))

                time.sleep(beh_period-3)

            if (count == 6):

                output_text = "/gesture " + command_list[5]

                client.send(str(output_text).encode('utf-8'))

                print("duff_time = ", diff_time)

                print("Sending command:", str(output_text))

                time.sleep(wait_for_talk)

                client_voice.send(str("/say 僕、野菜が苦手なんだ[EOF]").encode('utf-8'))

                projection_mes = "json_projector_" + fukidashi_list[5]

                client_projection.send(str(projection_mes).encode('utf-8'))

                time.sleep(beh_period-3)

            if (count == 7):

                output_text = "/gesture " + command_list[11]

                client.send(str(output_text).encode('utf-8'))

                print("duff_time = ", diff_time)

                print("Sending command:", str(output_text))

                time.sleep(wait_for_talk)

                client_voice.send(str("/say 僕、コーヒーが苦手なんだ[EOF]").encode('utf-8'))

                projection_mes = "json_projector_" + fukidashi_list[6]

                client_projection.send(str(projection_mes).encode('utf-8'))

                time.sleep(beh_period-3)

            if (count == 8):

                output_text = "/gesture " + command_list[12]

                client.send(str(output_text).encode('utf-8'))

                print("duff_time = ", diff_time)

                print("Sending command:", str(output_text))

                time.sleep(wait_for_talk)

                client_voice.send(str("/say 僕、運動が苦手なんだ[EOF]").encode('utf-8'))

                projection_mes = "json_projector_" + fukidashi_list[7]

                client_projection.send(str(projection_mes).encode('utf-8'))

                time.sleep(beh_period-3)

            if (count == 9):

                output_text = "/gesture " + command_list[8]

                client.send(str(output_text).encode('utf-8'))

                print("duff_time = ", diff_time)

                print("Sending command:", str(output_text))

                time.sleep(wait_for_talk)

                client_voice.send(str("/say 僕、虫が苦手なんだ[EOF]").encode('utf-8'))

                projection_mes = "json_projector_" + fukidashi_list[8]

                client_projection.send(str(projection_mes).encode('utf-8'))

                time.sleep(beh_period-3)

            if (count == 10):

                output_text = "/gesture " + command_list[2]

                client.send(str(output_text).encode('utf-8'))

                print("duff_time = ", diff_time)

                print("Sending command:", str(output_text))

                time.sleep(wait_for_talk)

                client_voice.send(str("/say 僕、寒いのが苦手なんだ[EOF]").encode('utf-8'))

                projection_mes = "json_projector_" + fukidashi_list[9]

                client_projection.send(str(projection_mes).encode('utf-8'))

                time.sleep(beh_period-3)

                break


                break
