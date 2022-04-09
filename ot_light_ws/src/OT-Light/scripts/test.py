joint_list = ["base-pipe1"
,"pipe1-gear"
,"pipe1-pipe2"
,"pipe2-fixedset1"
,"fixedset1-pipe3"
,"pipe3-gear2"
,"pipe3-pipe4"
,"pipe4-fixedset2"
,"fixedset2-pipe5"
,"pipe5-gear"
,"pipe5-gimba"
,"gimbal-motorholder"
,"motorholder-pinion" 
,"pinion-crown"
,"crown-light"
"gimbal-linkconnect" ]

controller_joint_names= ['', 'base-pipe1', 'fixedset1-pipe3', 'fixedset2-pipe5', 'motorholder-pinion', 'gimbal-linkconnect', ]

statement = """
{joint}_position_controller:
    type: effort_controllers/JointPositionController
    joint: {joint}
    pid: {pid}
            """

with open('transmission_joint.txt','w') as tj :
    for join in controller_joint_names:
        print(statement.format(joint=join,pid="{p: 100.0, i: 0.01, d: 10.0}"),file=tj,end='\n')
       
    
