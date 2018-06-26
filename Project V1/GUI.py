import easygui
import sys
import os.path
import kinematics as k
import cPickle as pickle
import paho.mqtt.publish as publish

#title_center = "Zero the robot"
#msg_center = "Center?"
#choices = ["Yes", "No"]
#default_choice = choices[0]
#cancel_choice = choices[1]
#center_box = easygui.ynbox(msg_center, title_center, choices)

#if center_box:
#    k.write_origin()
    
msg = "Enter Change in X and Y"
title = "Test"
field_names = ["Change in X","Change in Y", "Time"]
input_values = []  # blank values
input_values = easygui.multenterbox(msg,title, field_names)


# make sure that none of the fields was left blank
while 1:
    if input_values == None: break
    errmsg = ""
    for i in range(len(field_names)):
      if input_values[i].strip() == "":
        errmsg = errmsg + ('"%s" is a required field.\n\n' % field_names[i])
    if errmsg == "": break # no problems found
    input_values = easygui.multenterbox(errmsg, title, field_names, input_values)

MQTT_SERVER1 = "143.215.103.106" #sub to which message should be sent
MQTT_SERVER2 = "143.215.106.181"
MQTT_PATH_X = "X_channel"
MQTT_PATH_Y = "Y_channel"
MQTT_PATH_T = "T_channel"

publish.single(MQTT_PATH_X, input_values[0], hostname = MQTT_SERVER1)
publish.single(MQTT_PATH_X, input_values[0], hostname = MQTT_SERVER2)

publish.single(MQTT_PATH_Y, input_values[1], hostname = MQTT_SERVER1)
publish.single(MQTT_PATH_Y, input_values[1], hostname = MQTT_SERVER2)

publish.single(MQTT_PATH_T, input_values[2], hostname = MQTT_SERVER1)
publish.single(MQTT_PATH_T, input_values[2], hostname = MQTT_SERVER2)

#origin = [21.5, 52.0]

#try:
#    pos = pickle.load(open('data_pickle.pickle', 'rd'))
#except (OSError, IOError) as e:
#    pos = origin
#    pickle.dump(pos, open('data_pickle.pickle', 'wb'))

#print pos

#k.dist_time(float(input_values[0]), float(input_values[1]), float(input_values[2]))


#x1 = float(pos[0]) + float(input_values[0])
#y1 = float(pos[1]) - float(input_values[1])
#updated_data = [x1, y1]
#pickle.dump(updated_data, open('data_pickle.pickle', 'wb'))

#print updated_data
