import os

"""
MORSE_COMPONENTS:
path to the Morse components
"""

MORSE_COMPONENTS = os.path.join(os.getenv('MORSE_ROOT', '/usr/local'), \
                                'share', 'morse', 'data')

MORSE_RESOURCE_PATH = ':'.join([MORSE_COMPONENTS, \
                                os.getenv('MORSE_RESOURCE_PATH', '')])

"""
MORSE_MODIFIERS:
path to the modifiers modules
"""
MORSE_MODIFIERS = {
    'NED': 'morse.modifiers.ned.MorseNEDClass',
    'UTM': 'morse.modifiers.utm.MorseUTMClass',
    'GPSNoise': 'morse.modifiers.gps_noise.MorseGPSNoiseClass',
    'OdometryNoise': 'morse.modifiers.odometry_noise.MorseOdometryNoiseClass',
    'IMUNoise': 'morse.modifiers.imu_noise.MorseIMUNoiseClass',
    'PoseNoise': 'morse.modifiers.pose_noise.MorsePoseNoiseClass',
}

"""
MORSE_DATASTREAM_MODULE:
path to the middleware modules
"""
MORSE_DATASTREAM_MODULE = {
    'ros': 'morse.middleware.ros_datastream.ROS',
    'socket': 'morse.middleware.socket_datastream.Socket',
    'yarp': 'morse.middleware.yarp_datastream.Yarp',
    'pocolibs': 'morse.middleware.pocolibs_datastream.Pocolibs',
    'text': 'morse.middleware.text_datastream.Text',
}

"""
MORSE_MODIFIER_DICT:
associate a modifier function to a component.
"""
MORSE_MODIFIER_DICT = {
    'NED': {
        'pose': [MORSE_MODIFIERS['NED'], 'blender_to_ned'],
        'gps': [MORSE_MODIFIERS['NED'], 'blender_to_ned'],
        'gyroscope': [MORSE_MODIFIERS['NED'], 'blender_to_ned_angle'],
        'destination': [MORSE_MODIFIERS['NED'], 'ned_to_blender'],
        'waypoint': [MORSE_MODIFIERS['NED'], 'ned_to_blender'],
        'orientation': [MORSE_MODIFIERS['NED'], 'ned_angle_to_blender'],
        'teleport': [MORSE_MODIFIERS['NED'], 'ned_to_blender'],
    },
    'UTM' : {
        'pose': [MORSE_MODIFIERS['UTM'], 'blender_to_utm'],
        'gps': [MORSE_MODIFIERS['UTM'], 'blender_to_utm'],
        'destination': [MORSE_MODIFIERS['UTM'], 'utm_to_blender'],
        'waypoint': [MORSE_MODIFIERS['UTM'], 'utm_to_blender'],
    },
    'OdometryNoise' : {
        'odometry': [MORSE_MODIFIERS['OdometryNoise'], 'noisify']
    },
    'Noise' : {
        'imu': [MORSE_MODIFIERS['IMUNoise'], 'noisify'],
        'pose': [MORSE_MODIFIERS['PoseNoise'], 'noisify'],
    }
}

"""
middleware-dictionary-convention:
{
    .blend-middleware: {
        .blend-component: ['MW', 'method', 'path']
    }
}
"""
MORSE_DATASTREAM_DICT = {
    'ros': {
        'accelerometer': [MORSE_DATASTREAM_MODULE['ros'], 'post_twist', 'morse/middleware/ros/accelerometer'],
        'battery': [MORSE_DATASTREAM_MODULE['ros'], 'post_float32', 'morse/middleware/ros/battery'],
        'clock': [MORSE_DATASTREAM_MODULE['ros'], 'post_clock', 'morse/middleware/ros/clock'],
        'gps': [MORSE_DATASTREAM_MODULE['ros'], 'post_message'],
        'gyroscope': [MORSE_DATASTREAM_MODULE['ros'], 'post_message'],
        'infrared': [MORSE_DATASTREAM_MODULE['ros'], 'post_range', 'morse/middleware/ros/infrared'],
        'imu': [MORSE_DATASTREAM_MODULE['ros'], 'post_imu', 'morse/middleware/ros/imu'],
        'light': [MORSE_DATASTREAM_MODULE['ros'], 'read_switch', 'morse/middleware/ros/light'],
        'odometry': [MORSE_DATASTREAM_MODULE['ros'], 'post_odometry', 'morse/middleware/ros/odometry'],
        'pose': [MORSE_DATASTREAM_MODULE['ros'], 'post_odometry', 'morse/middleware/ros/pose'],
        'proximity': [MORSE_DATASTREAM_MODULE['ros'], 'post_message'],
        'pr2_posture': [MORSE_DATASTREAM_MODULE['ros'], 'post_jointState', 'morse/middleware/ros/pr2_posture'],
        'semantic_camera': [MORSE_DATASTREAM_MODULE['ros'], 'post_string', 'morse/middleware/ros/semantic_camera'],
        'sick': [MORSE_DATASTREAM_MODULE['ros'], 'post_2DLaserScan', 'morse/middleware/ros/sick'],
        'video_camera': [MORSE_DATASTREAM_MODULE['ros'], 'post_image', 'morse/middleware/ros/camera'],
        'depth_camera': [MORSE_DATASTREAM_MODULE['ros'], 'post_pointcloud2', 'morse/middleware/ros/depth_camera'],

        'light': [MORSE_DATASTREAM_MODULE['ros'], 'read_switch', 'morse/middleware/ros/light'],
        'ptu': [MORSE_DATASTREAM_MODULE['ros'], 'read_Vector3', 'morse/middleware/ros/platine'],
        'kuka_lwr': [MORSE_DATASTREAM_MODULE['ros'], 'read_jointState', 'morse/middleware/ros/kuka_jointState'],
        'v_omega': [MORSE_DATASTREAM_MODULE['ros'], 'read_twist', 'morse/middleware/ros/read_vw_twist'],
        'v_omega_diff_drive': [MORSE_DATASTREAM_MODULE['ros'], 'read_twist', 'morse/middleware/ros/read_vw_twist'],
        'xy_omega': [MORSE_DATASTREAM_MODULE['ros'], 'read_twist', 'morse/middleware/ros/read_xyw_twist'],
        'destination': [MORSE_DATASTREAM_MODULE['ros'], 'read_point', 'morse/middleware/ros/destination'],
        'force_torque': [MORSE_DATASTREAM_MODULE['ros'], 'read_wrench', 'morse/middleware/ros/read_wrench'],
        'orientation': [MORSE_DATASTREAM_MODULE['ros'], 'read_quaternion', 'morse/middleware/ros/read_quaternion'],
        'teleport': [MORSE_DATASTREAM_MODULE['ros'], 'read_pose', 'morse/middleware/ros/read_pose'],
        'rotorcraft_waypoint': [MORSE_DATASTREAM_MODULE['ros'], 'read_pose', 'morse/middleware/ros/read_pose'],
    },

    'socket': {
        'accelerometer': [MORSE_DATASTREAM_MODULE['socket'], 'post_message'],
        'battery': [MORSE_DATASTREAM_MODULE['socket'], 'post_message'],
        'gps': [MORSE_DATASTREAM_MODULE['socket'], 'post_message'],
        'gyroscope': [MORSE_DATASTREAM_MODULE['socket'], 'post_message'],
        'imu': [MORSE_DATASTREAM_MODULE['socket'], 'post_message'],
        'odometry': [MORSE_DATASTREAM_MODULE['socket'], 'post_message'],
        'pose': [MORSE_DATASTREAM_MODULE['socket'], 'post_message'],
        'proximity': [MORSE_DATASTREAM_MODULE['socket'], 'post_message'],
        'ptu_posture': [MORSE_DATASTREAM_MODULE['socket'], 'post_message'],
        'rosace': [MORSE_DATASTREAM_MODULE['socket'], 'post_message'],
        'thermometer': [MORSE_DATASTREAM_MODULE['socket'], 'post_message'],
        'semantic_camera' : [MORSE_DATASTREAM_MODULE['socket'], 'post_message'],
        'video_camera' : [MORSE_DATASTREAM_MODULE['socket'], 'post_video_camera', 'morse/middleware/sockets/video_camera'],

        'destination': [MORSE_DATASTREAM_MODULE['socket'], 'read_message'],
        'gripper': [MORSE_DATASTREAM_MODULE['socket'], 'read_message'],
        'light': [MORSE_DATASTREAM_MODULE['socket'], 'read_message'],
        'orientation': [MORSE_DATASTREAM_MODULE['socket'], 'read_message'],
        'ptu': [MORSE_DATASTREAM_MODULE['socket'], 'read_message'],
        'steer_force': [MORSE_DATASTREAM_MODULE['socket'], 'read_message'],
        'v_omega': [MORSE_DATASTREAM_MODULE['socket'], 'read_message'],
        'v_omega_diff_drive': [MORSE_DATASTREAM_MODULE['socket'], 'read_message'],
        'waypoint': [MORSE_DATASTREAM_MODULE['socket'], 'read_message'],
        'teleport': [MORSE_DATASTREAM_MODULE['socket'], 'read_message'],
    },

    'yarp': {
        'accelerometer': [MORSE_DATASTREAM_MODULE['yarp'], 'post_message'],
        'battery': [MORSE_DATASTREAM_MODULE['yarp'], 'post_message'],
        'gps': [MORSE_DATASTREAM_MODULE['yarp'], 'post_message'],
        'gyroscope': [MORSE_DATASTREAM_MODULE['yarp'], 'post_message'],
        'imu': [MORSE_DATASTREAM_MODULE['yarp'], 'post_message'],
        'odometry': [MORSE_DATASTREAM_MODULE['yarp'], 'post_message'],
        'pose': [MORSE_DATASTREAM_MODULE['yarp'], 'post_message'],
        'proximity': [MORSE_DATASTREAM_MODULE['yarp'], 'post_dictionary_data', 'morse/middleware/yarp/dictionary'],
        'ptu_posture': [MORSE_DATASTREAM_MODULE['yarp'], 'post_message'],
        'rosace': [MORSE_DATASTREAM_MODULE['yarp'], 'post_message'],
        'semantic_camera': [MORSE_DATASTREAM_MODULE['yarp'], 'post_message'],
        'sick': [MORSE_DATASTREAM_MODULE['yarp'], 'post_sick_message', 'morse/middleware/yarp/sick'],
        'thermometer': [MORSE_DATASTREAM_MODULE['yarp'], 'post_message'],
        'video_camera': [MORSE_DATASTREAM_MODULE['yarp'], 'post_image_RGBA'],

        'armature_actuator': [MORSE_DATASTREAM_MODULE['yarp'], 'read_message'],
        'destination': [MORSE_DATASTREAM_MODULE['yarp'], 'read_message'],
        'gripper': [MORSE_DATASTREAM_MODULE['yarp'], 'read_message'],
        'kuka_lwr': [MORSE_DATASTREAM_MODULE['yarp'], 'read_message'],
        'light': [MORSE_DATASTREAM_MODULE['yarp'], 'read_message'],
        'orientation': [MORSE_DATASTREAM_MODULE['yarp'], 'read_message'],
        'ptu': [MORSE_DATASTREAM_MODULE['yarp'], 'read_message'],
        'steer_force': [MORSE_DATASTREAM_MODULE['yarp'], 'read_message'],
        'v_omega': [MORSE_DATASTREAM_MODULE['yarp'], 'read_message'],
        'v_omega_diff_drive': [MORSE_DATASTREAM_MODULE['yarp'], 'read_message'],
        'waypoint': [MORSE_DATASTREAM_MODULE['yarp'], 'read_message'],
        'teleport': [MORSE_DATASTREAM_MODULE['yarp'], 'read_message'],
    },

    'yarp_json': {
        'rosace': [MORSE_DATASTREAM_MODULE['yarp'], 'post_json_message', 'morse/middleware/yarp/json_mod'],
        'gps': [MORSE_DATASTREAM_MODULE['yarp'], 'post_json_message', 'morse/middleware/yarp/json_mod'],
        'proximity': [MORSE_DATASTREAM_MODULE['yarp'], 'post_json_message', 'morse/middleware/yarp/json_mod'],

        'waypoint': [MORSE_DATASTREAM_MODULE['yarp'], 'read_json_message', 'morse/middleware/yarp/json_mod'],
    },


    'pocolibs': {
        'stereo_unit': [MORSE_DATASTREAM_MODULE['pocolibs'], 'write_viam', 'morse/middleware/pocolibs/sensors/viam', 'viamMorseBench'],
        'ptu': [MORSE_DATASTREAM_MODULE['pocolibs'], 'read_platine', 'morse/middleware/pocolibs/actuators/platine', 'platine_orientation'],
        'kuka_lwr': [MORSE_DATASTREAM_MODULE['pocolibs'], 'read_lwr_config', 'morse/middleware/pocolibs/actuators/lwr', 'lwrCurrentPoseArmRight'],
        'gyroscope': [MORSE_DATASTREAM_MODULE['pocolibs'], 'write_pom', 'morse/middleware/pocolibs/sensors/pom', 'MorseGyroscopeMEPos'],
        'odometry': [MORSE_DATASTREAM_MODULE['pocolibs'], 'write_pom', 'morse/middleware/pocolibs/sensors/pom', 'MorseOdometryMEPos'],
        'pose': [MORSE_DATASTREAM_MODULE['pocolibs'], 'write_pom', 'morse/middleware/pocolibs/sensors/pom', 'MorsePoseMEPos'],
        'GPS': [MORSE_DATASTREAM_MODULE['pocolibs'], 'write_pom', 'morse/middleware/pocolibs/sensors/pom', 'MorseGPSMEPos'],
        'v_omega': [MORSE_DATASTREAM_MODULE['pocolibs'], 'read_genpos', 'morse/middleware/pocolibs/actuators/genpos', 'simu_locoSpeedRef'],
        'v_omega_diff_drive': [MORSE_DATASTREAM_MODULE['pocolibs'], 'read_genpos', 'morse/middleware/pocolibs/actuators/genpos', 'simu_locoSpeedRef'],
        'semantic_camera': [MORSE_DATASTREAM_MODULE['pocolibs'], 'write_viman', 'morse/middleware/pocolibs/sensors/viman', 'morse_viman'],
        'human_posture': [MORSE_DATASTREAM_MODULE['pocolibs'], 'export_posture', 'morse/middleware/pocolibs/sensors/human_posture', 'human_posture'],
        'rosace': [MORSE_DATASTREAM_MODULE['pocolibs'], 'write_target', 'morse/middleware/pocolibs/sensors/target', 'targetPos'],
        'ptu_posture': [MORSE_DATASTREAM_MODULE['pocolibs'], 'write_platine_posture', 'morse/middleware/pocolibs/sensors/platine_posture', 'platineState'],
        'ik_control': [MORSE_DATASTREAM_MODULE['pocolibs'], 'read_niut_ik_positions', 'morse/middleware/pocolibs/actuators/niut', 'niutHuman'],
        'mocap_control': [MORSE_DATASTREAM_MODULE['pocolibs'], 'read_niut_ik_positions', 'morse/middleware/pocolibs/actuators/niut', 'niutHuman']
    },

    'text': {
        'accelerometer': [MORSE_DATASTREAM_MODULE['text'], 'write_data'],
        'battery': [MORSE_DATASTREAM_MODULE['text'], 'write_data'],
        'gps': [MORSE_DATASTREAM_MODULE['text'], 'write_data'],
        'gyroscope': [MORSE_DATASTREAM_MODULE['text'], 'write_data'],
        'imu': [MORSE_DATASTREAM_MODULE['text'], 'write_data'],
        'odometry': [MORSE_DATASTREAM_MODULE['text'], 'write_data'],
        'pose': [MORSE_DATASTREAM_MODULE['text'], 'write_data'],
        'proximity': [MORSE_DATASTREAM_MODULE['text'], 'write_data'],
        'ptu_posture': [MORSE_DATASTREAM_MODULE['text'], 'write_data'],
        'rosace': [MORSE_DATASTREAM_MODULE['text'], 'write_data'],
        'thermometer': [MORSE_DATASTREAM_MODULE['text'], 'write_data'],
    },


}


MORSE_SERVICE_DICT = {
    "socket": "morse.middleware.socket_request_manager.SocketRequestManager",
    "yarp": "morse.middleware.yarp_request_manager.YarpRequestManager",
    "yarp_json": "morse.middleware.yarp_json_request_manager.YarpRequestManager",
    "pocolibs": "morse.middleware.pocolibs_request_manager.PocolibsRequestManager",
    "ros": "morse.middleware.ros_request_manager.RosRequestManager",
}
