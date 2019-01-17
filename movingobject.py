
import rospy
from std_msgs.msg import String
from gazebo_msgs.msg import ModelState
global poseX
msg=ModelState()
def talker():
    pub = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
    rospy.Subscriber('/reset_pedestrian', String, listener)
    rospy.init_node('talker', anonymous=True)
    #rate = rospy.Rate(10) # 10hz

    poseX=0
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        
        msg.model_name='coke_can'
        msg.reference_frame='world'
        msg.twist.linear.x=0.01
        msg.pose.position.x=msg.pose.position.x+0.01
        #rospy.loginfo(msg)
        pub.publish(msg)
        #rate.sleep()
        #print("messageeeee ",msg)
        print(msg.pose.position.x)
        for i in range(1000000):
		poseX=poseX

def listener(data):
    print(data)
    msg.pose.position.x=2

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

