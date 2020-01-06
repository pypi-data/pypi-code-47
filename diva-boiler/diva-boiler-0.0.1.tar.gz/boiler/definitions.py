import enum


class ActorType(enum.Enum):
    BAG = 'Bag'
    BIKE = 'Bike'
    OBJECT = 'Object'
    PERSON = 'Person'
    VEHICLE = 'Vehicle'


actor_codes = {
    ActorType.BAG: 'b',
    ActorType.BIKE: 'k',
    ActorType.OBJECT: 'o',
    ActorType.PERSON: 'p',
    ActorType.VEHICLE: 'v',
}


class ActivityType(enum.Enum):
    ABANDON_PACKAGE = 'Abandon_Package'
    CARRY_IN_HANDS = 'Carry_in_Hands'
    CARRY_ON_BACK = 'Carry_on_Back'
    CASING_FACILITY = 'Casing_Facility'
    CLOSE_FACILITY_DOOR = 'Close_Facility_Door'
    CLOSE_TRUNK = 'Close_Trunk'
    CLOSE_VEHICLE_DOOR = 'Close_Vehicle_Door'
    EMBRACE_INTERACTION = 'Embrace_Interaction'
    ENTER_FACILITY = 'Enter_Facility'
    ENTER_THROUGH_STRUCTURE = 'Enter_Through_Structure'
    ENTER_VEHICLE = 'Enter_Vehicle'
    EXIT_THROUGH_STRUCTURE = 'Exit_Through_Structure'
    EXIT_VEHICLE = 'Exit_Vehicle'
    HAND_INTERACTION = 'Hand_Interaction'
    HEAVY_CARRY = 'Heavy_Carry'
    JOINING_QUEUE = 'Joining_Queue'
    LAPTOP_INTERACTION = 'Laptop_Interaction'
    LOAD_VEHICLE = 'Load_Vehicle'
    OBJECT_TRANSFER = 'Object_Transfer'
    OPEN_FACILITY_DOOR = 'Open_Facility_Door'
    OPEN_TRUNK = 'Open_Trunk'
    OPEN_VEHICLE_DOOR = 'Open_Vehicle_Door'
    PEOPLE_TALKING = 'People_Talking'
    PICK_UP_OBJECT = 'Pick_Up_Object'
    PURCHASING = 'Purchasing'
    PUT_DOWN_OBJECT = 'Put_Down_Object'
    READ_DOCUMENT = 'Read_Document'
    RIDING = 'Riding'
    SIT_DOWN = 'Sit_Down'
    STAND_UP = 'Stand_Up'
    TALK_ON_PHONE = 'Talk_on_Phone'
    TEXT_ON_PHONE = 'Text_On_Phone'
    THEFT = 'Theft'
    UNLOAD_VEHICLE = 'Unload_Vehicle'
    VEHICLE_DROPSOFF_PERSON = 'Vehicle_DropsOff_Person'
    VEHICLE_MOVING = 'Vehicle_Moving'
    VEHICLE_PICK_UP_PERSON = 'Vehicle_PicksUp_Person'
    VEHICLE_REVERSING = 'Vehicle_Reversing'
    VEHICLE_STARTING = 'Vehicle_Starting'
    VEHICLE_STOPPING = 'Vehicle_Stopping'
    VEHICLE_TURNING_LEFT = 'Vehicle_Turning_Left'
    VEHICLE_TURNING_RIGHT = 'Vehicle_Turning_Right'
    VEHICLE_UTURN = 'Vehicle_UTurn'


# activity validations are described as regular expressions
# individual actors are encoded as single characters (mapping below)
# words separated by | must be internally sorted in alphabetical order
# because candidates will be sorted before testing to avoid using regex
# lookaround.
#
# for example:
#   `bop` is a valid spec, but `pob` is not.
#   `(kpv|bo)` is valid because each individual word is sorted.
activity_spec = {
    ActivityType.ABANDON_PACKAGE: '(bp|op)',
    ActivityType.CARRY_IN_HANDS: None,
    ActivityType.CARRY_ON_BACK: None,
    ActivityType.CASING_FACILITY: None,
    ActivityType.CLOSE_FACILITY_DOOR: 'p',
    ActivityType.CLOSE_TRUNK: 'p?v',
    ActivityType.CLOSE_VEHICLE_DOOR: 'p?v',
    ActivityType.EMBRACE_INTERACTION: 'p{2,}',
    ActivityType.ENTER_FACILITY: 'p',
    ActivityType.ENTER_THROUGH_STRUCTURE: 'p',
    ActivityType.ENTER_VEHICLE: 'pv',
    ActivityType.EXIT_THROUGH_STRUCTURE: 'p',
    ActivityType.EXIT_VEHICLE: 'pv',
    ActivityType.HAND_INTERACTION: 'p{2,}',
    ActivityType.HEAVY_CARRY: '(bp+|o+p+|p{2,})',
    ActivityType.JOINING_QUEUE: None,
    ActivityType.LAPTOP_INTERACTION: 'p',
    ActivityType.LOAD_VEHICLE: '(o*pv|b*pv)',
    ActivityType.OBJECT_TRANSFER: '(o*p{2}|b*p{2}|o*pv|b*pv)',
    ActivityType.OPEN_FACILITY_DOOR: 'p',
    ActivityType.OPEN_TRUNK: 'p?v',
    ActivityType.OPEN_VEHICLE_DOOR: 'pv',
    ActivityType.PEOPLE_TALKING: 'p{2,}',
    ActivityType.PICK_UP_OBJECT: '(bp|op+)',
    ActivityType.PURCHASING: 'p+',
    ActivityType.PUT_DOWN_OBJECT: '(bp|op+)',
    ActivityType.READ_DOCUMENT: 'p',
    ActivityType.RIDING: 'kp',
    ActivityType.SIT_DOWN: 'p',
    ActivityType.STAND_UP: 'p',
    ActivityType.TALK_ON_PHONE: 'p',
    ActivityType.TEXT_ON_PHONE: 'p',
    ActivityType.THEFT: '(bo*p|o+p)',
    ActivityType.UNLOAD_VEHICLE: '(o*pv|b*pv)',
    ActivityType.VEHICLE_DROPSOFF_PERSON: 'p+v',
    ActivityType.VEHICLE_MOVING: 'v',
    ActivityType.VEHICLE_PICK_UP_PERSON: 'p+v',
    ActivityType.VEHICLE_REVERSING: 'v',
    ActivityType.VEHICLE_STARTING: 'v',
    ActivityType.VEHICLE_STOPPING: 'v',
    ActivityType.VEHICLE_TURNING_LEFT: 'v',
    ActivityType.VEHICLE_TURNING_RIGHT: 'v',
    ActivityType.VEHICLE_UTURN: 'v',
}


class CameraLocation(enum.Enum):
    ADMIN = 'admin'
    BUS = 'bus'
    SCHOOL = 'school'
    HOSPITAL = 'hospital'


class DataCollects(enum.Enum):
    M1 = 'm1'
    M2 = 'm2'


class ReleaseBatches(enum.Enum):
    SEQUESTERED = 'sequestered'
    MEVA = 'meva'
    TESTING = 'testing'


class CameraTypes(enum.Enum):
    VISIBLE = 'eo'
    INFRARED = 'ir'
