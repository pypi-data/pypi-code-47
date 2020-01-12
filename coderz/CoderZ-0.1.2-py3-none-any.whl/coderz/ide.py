from .robot import Robot

conf = {
    "communication": {
        "communication_manager_type": "ide"
    }
}

robot = Robot(conf)
robot.print_manual();
