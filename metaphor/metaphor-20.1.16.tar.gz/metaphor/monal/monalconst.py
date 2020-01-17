# -*- coding: UTF-8 -*-
#===============================================================================
# $Id: monalconst.py 4793 2018-09-13 11:27:59Z jeanluc $
#
#    module monalconst.py
#    projet MonalPy
#
#
# Copyright 2016 Jean-Luc PLOIX 
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#===============================================================================
#
#  ATTENTION  ce fichier ne doit pas etre modifie sans une extreme attention
#
#  Les valeurs qu'il contient ne doivent pas etre modifiees par programmation

"""monalconst module.
Common constants for all implementations of Neuron Engine 'Monal'.
Mandatory for modules 'monal.ndk', 'monal.model' and 'monal.driver'.

New data can be written to this module, but nothing must be modified or
 deleted. 
"""
import sys

PYTHON_MAJOR = sys.version_info.major
PYTHON_MINOR = sys.version_info.minor
PYTHON_MICRO = sys.version_info.micro
PYTHON_VERSION = "%d.%d.%d" % (PYTHON_MAJOR, PYTHON_MINOR, PYTHON_MICRO) 

from collections import OrderedDict

USE_INTEGRATED_LEVERAGE = 1
MAX_JOB = 1000

LEV_EARLY = 0
LEV_MONARI = 1
LEV_LATE = 2

LEV_METHOD = LEV_EARLY

# constantes pour monal 'computelevel'
(ID_COMPUTE, ID_DIFF, ID_DIFF_SEC) = list(range(3))

# constante de trainstyle de calcul train, getcost, getprime, 
CS_MODERATE = 0x0001
CS_LIMITED_LEVERAGE = 0x0002
CS_SUPER_TRAIN = 0x0004
CS_USE_DEBUG_COST = 0x0100
CS_USE_DEBUG_PRIME = 0x0200
CS_USE_DEBUG_PRESS = 0x0400
CS_USE_DEBUG_TRAIN = 0x0800
CS_DEBUG_SUPER_TRAIN = 0x1000
CS_DEBUG_MULTITRAIN = 0x2000

CS_DEBUG = CS_USE_DEBUG_COST | CS_USE_DEBUG_PRIME | CS_USE_DEBUG_PRESS | CS_USE_DEBUG_TRAIN | CS_DEBUG_SUPER_TRAIN | CS_DEBUG_MULTITRAIN

def debugFromStr(descro):
    result = 0
    if isinstance(descro, str): 
        deslist = [val.strip() for val in descro.split(',')]
        for val in deslist:
            if val == 'all':
                result |= CS_DEBUG
            elif val == 'cost':
                result |= CS_USE_DEBUG_COST
            elif val == 'prime':
                result |= CS_USE_DEBUG_PRIME
            elif val == 'press':
                result |= CS_USE_DEBUG_PRESS
            elif val == 'train':
                result |= CS_USE_DEBUG_TRAIN
            elif val == 'super':
                result |= CS_DEBUG_SUPER_TRAIN
            elif val == 'multi':
                result |= CS_DEBUG_MULTITRAIN
    return result

GC_MULTI_DATA = 0x1
GC_MULTI_OUTPUT = 0x2


MODEL_TAGS = ["MULTIMODEL", "NETWORK", "NORMALIZER", "LINMODEL"]
CONTAINER_TAGS = ["MULTIMODEL"]
NODE_TAGS = ["NODE"]
LINK_TAGS = ["LINK"]

FIX_LIMIT = 0x7FFF  #= 32767

ROOT_TAG = "MODEL"
NET_TAG = "NETWORK"
CONF_TAG = "CONFIDENCE"
MonalCfgDef = "Monal.cfg"
DLLKey = 'general.monaldll'

MONALVER = 34

# Constantes de verbosite
VERB_DETAIL = 0x0001
VERB_TRAIN = 0x0002
VERB_TRAINPROGRESS = 0x0004
VERB_TRANSFER = 0x000
VERB_MATRIX_BROWSE = 0x0010
VERB_RESAMPLING = 0x0020

VERB_ALL_TRAIN = VERB_TRAIN or VERB_TRAINPROGRESS
VERB_ALL = 0xFFFF


# Codes d'erreur
NDK_ERROR_EXCEPTION = -1
NDK_ERROR_TARGET = -2
NDK_ERROR_SOURCE = -3
NDK_ERROR_OUT_OF_LIST = -4
NDK_ERROR_NAN_VALUE = -5
NDK_ERROR_FUNCTION_NOT_FOUND = -6
NDK_ERROR_FORBIDDEN_MODEL_TYPE = -7
NDK_ERROR_FILE = -8
NDK_FILE_NOT_EXISTS = -9

NDK_ERROR_STR = {
    NDK_ERROR_EXCEPTION: "ERROR_EXCEPTION",
    NDK_ERROR_TARGET: "ERROR_TARGET",
    NDK_ERROR_SOURCE: "ERROR_SOURCE",
    NDK_ERROR_OUT_OF_LIST: "ERROR_OUTOFLIST",
    NDK_ERROR_NAN_VALUE: "ERROR_NANVALUE",
    NDK_ERROR_FUNCTION_NOT_FOUND: "ERROR_FUNCTIONNOTFOUND",
    NDK_ERROR_FORBIDDEN_MODEL_TYPE: "ERROR_FORBIDDENMODELTYPE",
    NDK_ERROR_FILE: "ERROR_FILE",
    NDK_FILE_NOT_EXISTS: "FILE_NOT_EXISTS"
    }

# constantes de fonctions d'activation
(IDENTITY, # 0
UNIT, # 1
TANH, # 2
STEP, # 3
GAUSS, # 4
SINE, # 5
EXP, # 6
QUADRATIC, # 7
ATAN, # 8
MOMENT0, # 9
MOMENT1, # 10
REVERSE, # 11
LOG, # 12
CUBIC, # 13
QUASIABS, # 14
SIGMOID, # 15
COMPLEMENT, # 16
ROOT, # 17
ARCSH, # 18
SQR , # 19
COS, # 20
ERF          # 21
) = list(range(22))

# constantes des fonction de cout
(NONE, # 0
SQUAREDELTA, # 1
SQUARELOGDELTA, # 2
LEASTSQUAREDELTA, # 3
WEIGHTEDSQUAREDELTA, # 4
UNCLASSIFIED, # 5
WEIGHTEDCLASSIFICATION, # 6
RELATIVESQUAREDELTA, # 7
GAUSSSQUAREDELTA, # 8
CROSSEDENTROPY, # 9
EXPSQUAREDELTA           # 10
) = list(range(11))

# constantes de manipulation de noeuds et de couche
PS_BEGIN = 0
PS_END = 1
PS_KEEP_LINKS = 0x4000  # réserver les numeros des liens lors de suppression de synapses 

# constantes des fonction de proximite (Kohonen)
PSQUARE, PGAUSS = list(range(2))

# constantes des fonction de decroissance (Kohonen)
DREVERSE, DREVERSEROOT, DEXPONENT = list(range(3))

# constantes de type de fonction    
ACTIVATION, COST, PROXY, DECAY = list(range(4))

# constantes de format d'enregistrement
FMT_AUTO, FMT_BINARY, FMT_XML, FMT_ASCII = list(range(4))

INFO_COUNT = 92
# constantes d'appel a getInfo et setIValue
(INPUT_COUNT, # 0  nombre d'entree du modele
OUTPUT_COUNT, # 1  nombre de sortie du modele
ORDER, # 2  ordre du modele
TRAINABLE, # 3  apprentissage possible du modele
TRANSPOSED, # 4  reserve pour les modeles lineaires
DIMENSION, # 5  nombre de parametres de l'azpprentissage
LAYER_COUNT, # 6  nombre de couches du modele
DRIVER_CLASS, # 7  classe du pilote de modele
HIDDEN_COUNT, # 8  nombre de noeuds caches
TRAIN_SIZE, # 9  nombre total de donnees enregistrees pour l'apprentissage (test inclus)
RESAMPLING, # 10 nombre de reechantillonnage
STATUS, # 11 statut du modele: combinaison des parametres nc_
NODE_COUNT, # 12 nombre de noeuds du modele
MODEL_INPUT_COUNT, # 13 nombre d'entrees du modele
SYNAPSE_COUNT, # 14 nombre de synapses du modele
DATA_COUNT, # 15 nombre de donnees enregistrees pour l'apprentissage (test exclus)
TRAIN_FUNC_INDEX, # 16 indice de la fonction de cout (SQUAREDELTA par defaut)
TRAINING_END, # 17 motif de l'arret de l'apprentissage (cf liste des motifs de fin d'apprentissage)
DATA_LOADED, # 18 booleen donnees chargees
IS_LIN, # 19 booleen modele lineaire
COMMENT_COUNT, # 20 nombre de commentaires du modele
MODEL_COUNT, # 21 nombre de modeles si le modele est un multimodele  
FUNC_ACT_COUNT, # 22 nombre de fonction d'activations
FUNC_COST_COUNT, # 23 nombre de fonction de cout
FUNC_PROX_COUNT, # 24 nombre de fonction proximite (Kohonen)
FUNC_DECAY_COUNT, # 25 nombre de fonction decroissance (Kohonen)
VALID_HANDLE, # 26 boolean Index est un handle valide
SAVING_FORMAT, # 27 format de l"enregistrement
TRAIN_MODEL_COUNT, # 28 nombre de modeles prets a l'apprentissage en mode 'data driven' 
RESAMPLING_TYPE, # 29 style de reechantillonnage (cf. style de ré-échantillonnage)
TRAINING_ALGORITHM, # 30 algorithme d'apprentissage (cf. liste des algorithmes d'apprentissage)
SELECTED_OUTPUT, # 31 sortie selectionnee
PROXIMITY, # 32 function de proximite (Kohonen)
DECAY, # 33 function de decroissance (Kohonen)
PROXIMITYDECAY, # 34 function de proximite et decroissance (Kohonen)
REVERSEMODE, # 35 style de mode inverse (cf.  modes de minimisation des entrées)
BEST_INDEX, # 36 index du meilleur apprentissage en mode 'multiple' ou 'data driven'. En affectation, chargement du modele indexe
CRITERION, # 37 critere de choix de modele en  mode 'multiple' ou 'data driven'.
MULTITRAIN_COUNT, # 38 nombre d'apprentissage en mode 'data driven'
TEST_SIZE, # 39 nombre d'exemples de l'ensemble de test 
TEST_GROUP, # 40 boolean: garger les exemples de test groupes
SAVE_TEMP, # 41 boolean: effectuer les sauvegardes temporaires sur disque
ONFLIGHT_CRITERION, # 42 critere de choix de modele en mode simple apprentissage
EPOCHS, # 43 nombre de cycles d'apprentissage a realiser ou realises Old: TRAIN_COUNT
TRAINING_RESULT_COUNT, # 44 nombre de resultats d'apprentissdage enregistres en mode 'data driven'
JACOBIAN_RANK, # 45 rang du Jacobien de la sortie #0
VERBOSE, # 46 niveau de bavardage
RESAMPLING_EPOCHS, # 47 nombre d'epoque demandees pour les apprentissage de reechantillonnage 
LANG_ID, # 48 lit ert ecrit la langue active. Disponibles 0x0409 (ENU), 0x040C (FRA)
RESERVE_49, # 49 deprecated. use SetArray, with style "VE_DATA_FORMAT"
LOAD_WITH_WEIGHTING, # 50 deprecated. use SetArray, with style "VE_DATA_FORMAT"
MODEL_STYLE, # 51 style du modele, combinaison des 'TSR_xxx'
DIRECT_GRADIENT, # 52 methode directe de calcul du gradient
HANDLE, # 53 index = 0 -> Nombre de modeles vivants; index > 0 -> handle du modele d'indice index - 1
COST_HISTORY_COUNT, # 54 nombre de couts enregistres
CRITERIA_COUNT, # 55 longueur du vecteur de criteres de choix d'apprentissage
UNICODE, # 56 boolean codage unicode
INTEGRATED_NORM, # 57 normalisation intégrée
RAND_SEED, # 58
DRIVER_COUNT,            # 59
ACTIV_FUNC_INDEX, # 60
COST_FUNC_INDEX, #61
ACTIV_FUNC_RANK, #62
COST_FUNC_RANK, #63
OK_CLOSE, #64    ipOKClose,
IS_MODIF, #65    ipIsModif,
CONSTANT_COUNT, #66    ipNConstant,
LEVERAGE_ACTIVE, #67    ipLeverageActif,
SAMPLING_AVTIVE, #68    ipReSamplingActif,
ADAPTATIVE_ACTIVE, #69    ipAdaptativeActive,
K_DIMENSION, #70    ipKDimension,
HAS_RESAMPLING, #71    ipHasResampling,
DATA_SAMPLING, #72    ipDataSampling,
USE_COUNT, #73    ipUseCount,
USERID, #74    ipUserID,
INI_STATE_INDEX, #75    ipRgIniState,
WEIGHTING_INDEX, #76    ipRgPond,
RANK_INDEX, #76=7    ipRgIndex,
LOADING_FORMAT, #78    ipLoadingFormat,
CELL_LENGTH, #79    ipCellLength,
ZERO_ONE_ONLY, #80    ipOnly01,
COMMON_DELAY, #81    ipCommonDelay,
MAX_DELAY, #82    ipMaxDelay,
TRAIN_PRIORITY, #83    ipTrainPriority,
ITERATION, #84    ipIteration,
PROC_DESC, #85    ipProcDesc,
HAS_CONFIDENCE, #86    ipHasConfidence,
ERROR, #87    ipError,
DEBUGDLL,     # 88
SAVE_COUNT, #89
SAVE_COUNT_MAX,
OLD_NML_FORMAT      
) = list(range(INFO_COUNT))

LOAD_TRAINED_MODEL = BEST_INDEX # compatibilite amont
# constantes d'appel a getRealValue et setRealValue
INFO_R_COUNT = 48
INFO_R_THRESHOLD = INFO_COUNT  # a la suite du precedent
(RP_NONE, #            rien
RP_NOISE_VAR, #       1 ecart-type sans biais
RP_INPUT_POTENTIEL, # 3 Potentiel d'entrée
RP_MAX_ERROR, #       1 Residu Max
RP_TRAIN_ACCURACY, #  1 Précision de l'apprentissage
RP_STD_DEV, #         1 EQMA
RP_PRESS, #          1 EQVC
RP_MU, #             1 Mu
RP_TRAIN_PARAM, #     3 Parametre supplémentaire de la fonction de coût
RP_COST, #           1 Coût d'apprentissage
RP_INI_DEV, #         1 Affectation des valeurs d'initialisation par defaut (enveloppe, bias0=bool(index))
RP_SCALE, #          1 Echelle de normalisation
RP_CONF_LEVEL, #      2 Niveau de confiance  
RP_WEIGHTING, #          Ponderation de l'exemple
RP_BOOTSTRAP_ACCURACY, #  precision de bootstrap
RP_AMPLITUDE_PARAM, #     Kohonen
RP_DECAY_PARAM, #         Kohonen
RP_PROXIMITY_PARAM, #     Kohonen
RP_PROXIMITY_INIT_PARAM, # Kohonen
RP_EIGEN_MIN, #           valeur propre minimum de la matrice de Fisher
RP_EIGEN_MAX, #           valeur propre maximum de la matrice de Fisher
RP_CONDITIONNING, #      conditionnement de la matrice de Fisher
RP_DETERMINANT, #        determinant de la matrice de Fisher
RP_TRACE, #              trace de la matrice de Fisher
RP_CORREL_MAX, #          correlation maximum entre parametes
RP_CORREL_MEAN, #         correlation moyenne entre parametres
RP_CORREL_MAX_ADDR, #      adresse i, j de la correlation maximum entre parametes
RP_COST_REF, #            cout de reference d'un modele dynamique d'ordre 0
RP_COST_REF_1, #           cout de reference d'un modele dynamique d'ordre 0  
RP_SIGMA_INPUT, #         info d'entree: point central
RP_SIGMA_OUTPUT, #        info de sortie: point central
RP_PI_INPUT, #            info d'entree: demi amplitude
RP_PI_OUTPUT,#            info de sortie: demi amplitude
RP_STATISTICAL_RATIO,
RP_DATA_RATIO,
RP_PARTITION_COST,
RP_CONFIDENCE_MULTIPLYER,
RP_RELATIVE_EPOCH,
RP_RELATIVE_ITERATION,
RP_PRESS_G,
RP_RESAMPLING_COST,
RP_RESAMPLING_DEV,
RP_MIN_VALUE,
RP_MAX_VALUE,
RP_AMPLIFIER,
RP_PRUNING_THRESHOLD,
RP_STUDENT,
RP_LOW_PASS
) = list(range(INFO_R_THRESHOLD, INFO_R_THRESHOLD + INFO_R_COUNT))

# synomymes
RP_STD_DEV_BIAS_LESS = RP_NOISE_VAR

# constantes d'appel de GetIndexInfo
INFO_I_THRESHOLD = INFO_COUNT + INFO_R_COUNT # a la suite du precedent
INFO_I_COUNT = 22
(II_P_IS_TEST, #   1 Data line is it in test set ?
II_P_NODE_CLASS, #   2 Node class index. Cf NodeClassIndex below.
II_P_LAYER, #   1 Node layer index in its model.
II_P_NODE_LAYER_INDEX, #   1 Node index in its layer.    
II_P_LAYER_LENGTH, #   2 Layer length.
II_P_SYN_CHILDREN, #   2 Number of child synapses of the indexed node.
II_P_SYN_CHILD_CHILD, #   2 ID of childnode indexed Hi(Index) of node indexed Lo(Index).
II_P_SYN_CHILD_TYPE, #   2 Link type of Hi(Index) childlink of node indexed Lo(Index).
II_P_SYN_CHILD_NUM, #   2 ID of Child synapse indexed Hi(Index) of node indexed Lo(Index).
II_STATE_LAYER, #   3 Output state layer.
II_STATE_NODE_LAYER_INDEX, #   3 Output state index in its layer.
II_NODE_NET_INDEX, #   1 Index of model including the node (Multi-model case).
II_N_LAYER, #   1 Number of layers in the model (Multi-model case).
II_JACOB_RANK, #   2 Jacobian rank for indexed output.
II_BEST_TRAIN, #   0 Best train index for chosen criterion.
II_K_SIZE, #   2 Length of indexed dimension of Kohonen map.
II_P_MODEL_CLASS, #   2 Model class index. Cf ModelClassIndex below
II_P_HIDDEN_INDEX,
II_NEURON_ACTIVATION,    #     Node(index) Activation
II_OUTPUT_ACTIVE_PARENTS,
II_REVERSE_INDEX,
II_P_SYN_PARENTS
) = list(range(INFO_I_THRESHOLD, INFO_I_THRESHOLD + INFO_I_COUNT))

INFO_TOTAL_COUNT = II_P_SYN_PARENTS + 1
    
LOADABLE_INFOS = frozenset((
    DATA_COUNT,
    BEST_INDEX,
    SAVING_FORMAT,
    SELECTED_OUTPUT,
    RESAMPLING,
    RESAMPLING_TYPE,
    REVERSEMODE,
    OUTPUT_COUNT,
    TRANSPOSED,
    LOAD_WITH_WEIGHTING,
    #LANG_ID,
    VERBOSE,
    PROXIMITY,
    DECAY,
    PROXIMITYDECAY,
    TRAIN_FUNC_INDEX,
    CRITERION,
    EPOCHS,  #TRAIN_COUNT,
    RESAMPLING_EPOCHS,
    TRAINING_ALGORITHM,
    TEST_SIZE,
    TEST_GROUP,
    SAVE_TEMP,
    ONFLIGHT_CRITERION,
    UNICODE, #56 boolean codege unicode
    INTEGRATED_NORM, #57  
    OLD_NML_FORMAT,
    DEBUGDLL,
    RP_INI_DEV, # load only
    RP_SCALE,
    RP_AMPLITUDE_PARAM,
    RP_DECAY_PARAM,
    #rpProximityParam,
    RP_PROXIMITY_PARAM,
    RP_NOISE_VAR,
    RP_CONF_LEVEL,
    RP_WEIGHTING,
    RP_INPUT_POTENTIEL,
    RP_TRAIN_ACCURACY,
    RP_TRAIN_PARAM,
    RP_BOOTSTRAP_ACCURACY,
    RP_SIGMA_INPUT,
    RP_SIGMA_OUTPUT,
    RP_PI_INPUT,
    RP_PI_OUTPUT, # et d'autres peut-etre
    RP_LOW_PASS))

INFO_DICT = {
    INPUT_COUNT: "INPUT_COUNT", # 0
    OUTPUT_COUNT: "OUTPUT_COUNT", # 1
    ORDER: "ORDER", # 2
    TRAINABLE: "TRAINABLE", # 3
    TRANSPOSED: "TRANSPOSED", # 4
    DIMENSION: "DIMENSION", # 5
    LAYER_COUNT: "LAYER_COUNT", # 6
    DRIVER_CLASS: "DRIVER_CLASS", # 7
    HIDDEN_COUNT: "HIDDEN_COUNT", # 8
    EPOCHS: "EPOCHS",
    #TRAIN_COUNT: "TRAIN_COUNT", # 9
    RESAMPLING: "", # 10
    STATUS: "STATUS", # 11
    NODE_COUNT: "NODE_COUNT", # 12
    MODEL_INPUT_COUNT: "", # 13
    SYNAPSE_COUNT: "", # 14
    DATA_COUNT: "DATA_COUNT", # 15
    TRAIN_FUNC_INDEX: "TRAIN_FUNC_INDEX", # 16
    TRAINING_END: "TRAINING_END", # 17
    DATA_LOADED: "DATA_LOADED", # 18
    IS_LIN: "IS_LIN", # 19
    COMMENT_COUNT: "COMMENT_COUNT", # 20
    MODEL_COUNT: "MODEL_COUNT", # 21
    FUNC_ACT_COUNT: "FUNC_ACT_COUNT", # 22
    FUNC_COST_COUNT: "FUNC_COST_COUNT", # 23
    FUNC_PROX_COUNT: "FUNC_PROX_COUNT", # 24
    FUNC_DECAY_COUNT: "FUNC_DECAY_COUNT", # 25
    VALID_HANDLE: "VALID_HANDLE", # 26
    SAVING_FORMAT: "SAVING_FORMAT", # 27
    TRAIN_MODEL_COUNT: "TRAIN_MODEL_COUNT", # 28
    RESAMPLING_TYPE: "RESAMPLING_TYPE", # 29
    TRAINING_ALGORITHM: "TRAINING_ALGORITHM", # 30
    SELECTED_OUTPUT: "SELECTED_OUTPUT", # 31
    PROXIMITY: "PROXIMITY", # 32
    DECAY: "DECAY", # 33
    PROXIMITYDECAY: "PROXIMITYDECAY", # 34
    REVERSEMODE: "REVERSEMODE", # 35
    BEST_INDEX: "BEST_INDEX", # 36
    CRITERION: "CRITERION", # 37
    MULTITRAIN_COUNT: "MULTITRAIN_COUNT", # 38
    TEST_SIZE: "TEST_SIZE", # 39
    TEST_GROUP: "TEST_GROUP", # 40
    SAVE_TEMP: "SAVE_TEMP", # 41
    ONFLIGHT_CRITERION: "ONFLIGHT_CRITERION", # 42
    EPOCHS: "EPOCHS", # 43
    #TRAIN_COUNT: "TRAIN_COUNT", # 43
    TRAINING_RESULT_COUNT: "TRAINING_RESULT_COUNT", # 44
    JACOBIAN_RANK: "JACOBIAN_RANK", # 45
    VERBOSE: "VERBOSE", # 46
    RESAMPLING_EPOCHS: "RESAMPLING_EPOCHS", # 47
    #LANG_ID: "LANG_ID", # 48
    
    LOAD_WITH_WEIGHTING: "LOAD_WITH_WEIGHTING", # 50
    MODEL_STYLE: "MODEL_STYLE", # 51
    DIRECT_GRADIENT: "DIRECT_GRADIENT", # 52
    HANDLE: "HANDLE", # 53
    COST_HISTORY_COUNT: "COST_HISTORY_COUNT", # 54
    CRITERIA_COUNT: "CRITERIA_COUNT", # 55
    UNICODE: "UNICODE", # 56
    INTEGRATED_NORM: "INTEGRATED_NORM", # 57
    RAND_SEED: "RAND_SEED", # 58
    DRIVER_COUNT: "DRIVER_COUNT", # 59
    RP_NOISE_VAR: "RP_NOISE_VAR", #       1 ecart-type du bruit
    RP_INPUT_POTENTIEL: "RP_INPUT_POTENTIEL", # 3 Potentiel d'entrée
    RP_MAX_ERROR: "RP_MAX_ERROR", #       1 Residu Max
    RP_TRAIN_ACCURACY: "RP_TRAIN_ACCURACY", #  1 Précision de l'apprentissage
    RP_STD_DEV: "RP_STD_DEV", #         1 EQMA
    RP_PRESS: "RP_PRESS", #          1 EQVC
    RP_MU: "RP_MU", #             1 Mu
    RP_TRAIN_PARAM: "RP_TRAIN_PARAM", #     3 Parametre supplémentaire de la fonction de coût
    RP_COST: "RP_COST", #           1 Coût d'apprentissage
    RP_INI_DEV: "RP_INI_DEV", #
    RP_SCALE: "RP_SCALE", #          1 Echelle de normalisation
    RP_CONF_LEVEL: "RP_CONF_LEVEL", #      2 Niveau de confiance  
    RP_WEIGHTING: "RP_WEIGHTING",
    RP_BOOTSTRAP_ACCURACY: "RP_BOOT_STRAP_ACCURACY",
    RP_AMPLITUDE_PARAM: "RP_AMPLITUDE_PARAM",
    RP_DECAY_PARAM: "RP_DECAY_PARAM",
    RP_PROXIMITY_PARAM: "RP_PROXIMITY_PARAM",
    RP_PROXIMITY_INIT_PARAM: "RP_PROXIMITY_INIT_PARAM",
    RP_EIGEN_MIN: "RP_EIGEN_MIN",
    RP_EIGEN_MAX: "RP_EIGEN_MAX",
    RP_CONDITIONNING: "RP_CONDITIONNING",
    RP_DETERMINANT: "RP_DETERMINANT",
    RP_TRACE: "RP_TRACE",
    RP_CORREL_MAX: "RP_CORREL_MAX",
    RP_CORREL_MEAN: "RP_CORREL_MEAN",
    RP_CORREL_MAX_ADDR: "RP_CORREL_MAX_ADDR",
    RP_COST_REF: "RP_COST_REF",
    RP_COST_REF_1: "RP_COST_REF_1",
    RP_SIGMA_INPUT: "RP_SIGMA_INPUT",
    RP_SIGMA_OUTPUT: "RP_SIGMA_OUTPUT",
    RP_PI_INPUT: "RP_PI_INPUT",
    RP_PI_OUTPUT: "RP_PI_OUTPUT",
    RP_STATISTICAL_RATIO: "RP_STATISTICAL_RATIO",
    RP_DATA_RATIO: "RP_DATA_RATIO",
    RP_PARTITION_COST: "RP_PARTITION_COST",
    RP_CONFIDENCE_MULTIPLYER: "RP_CONFIDENCE_MULTIPLYER",
    RP_RELATIVE_EPOCH: "RP_RELATIVE_EPOCH",
    RP_RELATIVE_ITERATION: "RP_RELATIVE_ITERATION",
    RP_PRESS_G: "RP_PRESS_G",
    RP_RESAMPLING_COST: "RP_RESAMPLING_COST",
    RP_RESAMPLING_DEV: "RP_RESAMPLING_DEV",
    RP_MIN_VALUE: "RP_MIN_VALUE",
    RP_MAX_VALUE: "RP_MAX_VALUE",
    RP_AMPLIFIER: "RP_AMPLIFIER",
    RP_PRUNING_THRESHOLD: "RP_PRUNING_THRESHOLD",
    RP_STUDENT: "RP_STUDENT",
    RP_LOW_PASS: "RP_LOW_PASS"
    }

# constantes de style de transfer
(TFR_STD, # 0  /* Constantes pour le transfer */
TFR_GRADIENT, # 1
TFR_LEVERAGE, # 2
TFR_GRADIENTLEVERAGE, # 3
TFR_GRADIENTCONFIDENCE, # 4
TFR_GRADIENTINPUTS, # 5
TFR_GRADIENTHESSIAN) = list(range(7)) # 6

# constantes de foramt de sauvegarde
(SF_AUTO,
SF_BINARY,   # binaire
SF_XML,       # NML
SF_ASCII,     # ASCII jlp
SF_DLM,       # DLM obsolete
SF_JSON,      # JSON
SF_CCODE,     # code C
SF_CPYTHON,   # Module Extension C Python
SF_CCODEMULTI,# Shared Library grouped
SF_DLL,       # Shared Library isolated
SF_DLLTRAIN   # trainable isolated library 
) = list(range(11))

# extension par defaut des fichiers de modeles pour chaque format
extfmt = ["", ".net", ".nml", ".ntt", ".dlm", ".json", "", "", "", ".so", ".so"]
    
# constantes de compactage modele
CM_INPUT = 1
CM_LAYER = 2
CM_PARAMETERS = 4
CM_LINKS = 8

# liste des algorithmes d'apprentissage
(TA_GRADIENT, # ta = training algorithm
TA_QN,
TA_LM,
TA_QNWP,
TA_LOOLM,
TALOOQN
) = list(range(6))

# Info(s) appelable depuis ndk, sans creation de modele
NDK_INFO = frozenset((FUNC_ACT_COUNT, FUNC_COST_COUNT, FUNC_PROX_COUNT,
                 FUNC_DECAY_COUNT, HANDLE, UNICODE, INTEGRATED_NORM, 
                 DRIVER_COUNT, SAVING_FORMAT, DEBUGDLL))  #, LANG_ID

# constantes d'ecriture et lecture de fonctions exterieures
# appels à GetPtrInfo et SetPtrInfo
(CALLBACK_FUNC, # fonction de callback
SELECT_FUNC, # fonction de selection des modeles apres multi train
#MODIFY_DATA_FUNC, # fonction de modification des donnes au chargement
) = list(range(2))

#TRANSLATE_DATA_FUNC a ete supprime

# index de resultat d'azpprentissage
(TRR_CODE, 
TRR_EPOCHS, 
TRR_PARAMS, 
TRR_INDEX, 
TRR_INITINDEX, 
TRR_RETURNINDEX,
TRR_COST, 
TRR_PRESS, 
TRR_OUT, 
TRR_LEV) = list(range(10))

(TRRS_INDEX, 
TRRS_INITINDEX, 
TRRS_COST, 
TRRS_PRESS, 
TRRS_OUT, 
TRRS_LEV) = list(range(6))

# const de criteres de choix et informations des modeles
TCR_COUNT = 19

(TCR_STDDEV, # 0;         cout
TCR_SHII, # 1;          cout de test
TCR_PRESS, # 2;         Press
TCR_MU, # 3;            Mu
TCR_STD_DEV_BIAS_LESS, # 4;  Ecart-type sans biais
TCR_R2, # 5;            R2
TCR_R2_ADJUST, # 6;      R2 ajuste
TCR_CORREL, # 7;        Correlation
TCR_DELTA_RANK, # 8;     Defaut de rang du jacobien
TCR_DETERMINANT, # 9;    Determinant de la matrice de Fisher
TCR_EIGEN_MIN, # 10;      Valeur propre minimum de la matrice de Fisher
TCR_EIGEN_MAX, # 11;      Valeur propre maximum de la matrice de Fisher
TCR_CONDITIONNING, # 12; Conditionnement de la matrice de Fisher
TCR_TRACE, # 13;         Trace de la matrice de Fisher
TCR_CORREL_MAX, # 14;     correlation maximum entre parametres
TCR_CORREL_MEAN, # 15     correlation moyenne entre parametres
TCR_CORREL_MAX_ADDR, # 16; adresse i, j (long * 2) de la correlation maximum entre parametres
TCR_HIDDEN, #17           neurones caches
TCR_EPOCHS #18
) = list(range(TCR_COUNT))

TCR_NOSORT = -2
TCR_COST = TCR_STDDEV
TCR_INT = (TCR_DELTA_RANK, TCR_HIDDEN, TCR_EPOCHS)
    
# liste des criteres qui ne sont pas des criteres de choix
TCR_DONT_CARE = [TCR_CORREL_MAX_ADDR, TCR_HIDDEN, TCR_EPOCHS, TCR_NOSORT]
# liste des criteres pour lesquels le meilleur est le plus grand  
TCR_MAXIMIZE = [TCR_MU, TCR_R2, TCR_R2_ADJUST, TCR_CORREL]
# liste des criteres pour lesquels le meilleur est le plus petit  
TCR_MINIMIZE = [x for x in range(TCR_COUNT) if not x in (TCR_MAXIMIZE + TCR_DONT_CARE)] + [-1]
# liste des criteres pour lesquels la vaeur 0 a du sens
TCR_ZEROINCLUDED = [TCR_DELTA_RANK]

RESFIELDNAMES = [
            "StdDev",
            "Round-off",
            "PRESS",
            "Mu",
            "BiasLessStdDev",
            "R2",
            "AdjustedR2",
            "Correlation",
            "DeltaRank",
            "Determinant",
            "EigenMin",
            "EigenMax",
            "Conditionning",
            "Trace",
            "CorrelMax",
            "MeanCorrel",
            "CorrelMaxAddr",
            "Hidden",
            "Epochs"]

# dictionnaire des noms criteres de choix
CRITERION_NAME = OrderedDict({     
    TCR_STDDEV: 'StdDev', # 0;
    TCR_SHII: "RoundoffTest", # 1;
    TCR_PRESS: "PRESS", # 2;
    TCR_MU: "Mu", # 3;
    TCR_STD_DEV_BIAS_LESS: "StdDevBiasless", # 4;
    TCR_R2: "R2", # 5;
    TCR_R2_ADJUST: "AdjustedR2", # 6;
    TCR_CORREL: "Correl", # 7;  modifie le 10/02/16 old Correl
    TCR_DELTA_RANK: "DeltaRank", # 8;
    TCR_DETERMINANT: "Determinant", # 9;
    TCR_EIGEN_MIN: "EigenMin", # 10;
    TCR_EIGEN_MAX: "EigenMax", # 11;
    TCR_CONDITIONNING: "Conditionning", # 12;
    TCR_TRACE: "Trace", # 13;
    TCR_CORREL_MAX: "CorrelMax", # 14;
    TCR_CORREL_MEAN: "CorrelMean", # 15;
    TCR_CORREL_MAX_ADDR: "CorrelMaxAddr", #16
    TCR_HIDDEN: "Hidden", #17
    TCR_EPOCHS: "Epochs"}) #18

# correction des noms de champs
CORRECTED_FIELD = {
    'press': 'PRESS', 
    'PRESS': 'PRESS', 
    'vloo': 'PRESS',
    'VLOO': 'PRESS',
    'VLOOS': 'PRESS',
    'VLOO score': 'PRESS',
    'VLOO Score': 'PRESS',
    'VLOO_Score': 'PRESS',
    'vloos': 'PRESS',
    'VLOOScore': 'PRESS',
    'rmse': 'StdDev', 
    'RMSE': 'StdDev',
    'STDDEV': 'StdDev',
    'stddev': 'StdDev',
    'mu': 'Mu',
    'MU': 'Mu',
    'r2': 'R2',
    'TRACE': 'Trace',
    'ADJUSTEDR2': 'AdjustedR2',
    'CORRELATION': 'Correlation',
    'DETERMINANT': 'Determinant',
    'CONDITIONNING': 'Conditionning',
    }


# dico inverse de CORRECTED_FIELD
SUBSTITUTE_FIELD = {
    'PRESS': 'VLOO score',
    'StdDev': 'RMSE',
    'StdDevBiasless': 'biasless RMSE',
    }

tabledict = {val: CRITERION_NAME[ind] for ind, val in enumerate(RESFIELDNAMES)}
#tabledict["Traintype"] = "traintype"
tabledict.update({'Traintype': 'traintype', 'RMSE': 'StdDev', 'VLOO_score': 'PRESS'})  #,
tabledisplaydict = {'StdDev': 'RMSE', 'PRESS': 'VLOO_score'}

CRITERION_TYPE = {   #   
    TCR_STDDEV: float, # 0;
    TCR_SHII: float, # 1;
    TCR_PRESS: float, # 2;
    TCR_MU: float, # 3;
    TCR_STD_DEV_BIAS_LESS: float, # 4;
    TCR_R2: float, # 5;
    TCR_R2_ADJUST: float, # 6;
    TCR_CORREL: float, # 7;
    TCR_DELTA_RANK: int, # 8;
    TCR_DETERMINANT: float, # 9;
    TCR_EIGEN_MIN: float, # 10;
    TCR_EIGEN_MAX: float, # 11;
    TCR_CONDITIONNING: float, # 12;
    TCR_TRACE: float, # 13;
    TCR_CORREL_MAX: float, # 14;
    TCR_CORREL_MEAN: float, # 15;
    TCR_CORREL_MAX_ADDR: float, #16
    TCR_HIDDEN: int, #17
    TCR_EPOCHS: int} #18

# if PYTHON_MAJOR <= 2:
#     CRITERION_TYPE_STR = {key: 'float' if val==float else 'int'  for (key, val) in iteritems(CRITERION_TYPE)}#.iteritems()}
# else:
CRITERION_TYPE_STR = {key: 'float' if val==float else 'int'  for (key, val) in CRITERION_TYPE.items()}#.iteritems()}

# Schema de la table de donnees des resultats d'apprentissage
# TRAIN_DATA = OrderedDict({'ID': 'INTEGER PRIMARY KEY AUTOINCREMENT',
#                           'prevID': 'int'})  
TRAIN_DATA = OrderedDict({'ID': 'int',
                          'prevID': 'int'})  
# if PYTHON_MAJOR <= 2:
#     TRAIN_DATA.update(OrderedDict({value: CRITERION_TYPE_STR[tcr] for (tcr, value) in iteritems(CRITERION_NAME)}))  #.iteritems()  }))
# else:
TRAIN_DATA.update(OrderedDict({value: CRITERION_TYPE_STR[tcr] for (tcr, value) in CRITERION_NAME.items()}))  #.iteritems()  }))
TRAIN_DATA.update(OrderedDict({   
#        'ind': 'int',
        'ini_stddev': 'float',
        'end_stddev': 'float',
        'training_end': 'int',
        'param_start': 'array',
        'param_start0': 'float',
        'param_end': 'array',
        'param_end0': 'float',
        'dispersion': 'array',
        'dispersion0': 'float',
        'leverages': 'array',
        'leverages0': 'float',
        'traintype': 'int',
        'inittype': 'int',
        'code': 'int',
        'seed': 'int'}))

# Schema des tables de donnees des apprentissages complementaires
EXTRA_TRAIN_DATA = OrderedDict({'ID': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'ind': 'int',
        'indtrain': 'int',
        'inittype': 'str',
        'param_start': 'array',
        'param_start0': 'float',
        'param_end': 'array',
        'param_end0': 'float',
        'dispersion': 'array',
        'dispersion0': 'float',
        'out': 'float',
        'leverages': 'float',
        'code': 'int',
        'target': 'float',
        'seed': 'int'})
EXTRA_TRAIN_DATA.update(OrderedDict({value: CRITERION_TYPE_STR[tcr] for (tcr, value) in CRITERION_NAME.items()}))  

#Liste des champs affichables dans l'ordre avec le defaut
prefdisplay = [
    (TCR_STDDEV, "stddev", True), 
    (TCR_PRESS, "press", True), 
    (TCR_MU, "mu", False), 
    (TCR_STD_DEV_BIAS_LESS, "stddevbiasless", False), 
    (TCR_R2, "r2", True), 
    (TCR_R2_ADJUST, "r2adjust", False), 
    (TCR_CORREL, "correl", False), 
    (TCR_SHII, "roundoff", True), 
    (TCR_DELTA_RANK, "deltarank", True), 
    (TCR_DETERMINANT, "determinant", False), 
    (TCR_EIGEN_MIN, "eigenmin", False),  
    (TCR_EIGEN_MAX, "eigenmax", False), 
    (TCR_CONDITIONNING, "conditionning", False),  
    (TCR_TRACE, "trace", False), 
    (TCR_CORREL_MAX, "correlmax", False),  
    (TCR_CORREL_MEAN, "meancorrel", False), 
    (TCR_HIDDEN, "hidden", True),
    (TCR_EPOCHS, "epochs", True)] 

ConditionningError = 3.3333333e+033  

# style de reseau  ??? que faire avec 
TSR_Std = 0x0000
#Entrées connectées aux sorties par des liens variables}
TSR_IO = 0x0001  #            {0}
#la couche cachée est complètement connectée}
TSR_AllConnect = 0x0002  #            {1}
#Disponible}
#    TSR_IOState       = 0x0004 #             {2}
#échelon de réseaux ayant les entrées communes}
TSR_Parallel = 0x0008  #            {3}
#sortie monitorée par une fonction de l'entrée}
TSR_Monitor = 0x0010  #           {4}
#entrée star ajoutée à la 1ère sortie, lien 1 fixe}
TSR_AddInFirst = 0x0020  #            {5}
#entrées ajoutées à la sortie, lien 1 fixe}
TSR_AddIn = 0x0040  #            {6}
#balayage des E/S fait à l'envers pendant la construction}
#    TSR_Retro         = 0x0080  #            {7}
#réseau à réponse nulle}
TSR_R_NULLE = 0x0100  #            {8}
TSR_POLYNOM = 0x0200  #
TSR_RADIAL_BASIS = 0x0400  #
TSR_IN_NORM = 0x0800  #
TSR_OUT_NORM = 0x1000  #
TSR_IN_MATRIX = 0x2000  #
TSR_IDENTITY = 0x4000  #
TSR_NUMINPUT = 0x8000  #
#Numérotation des synapses à partir de la couche d'entrée}
#    TSR_NumEntree     = 0x8000  #            {9}

TSR_Norm = TSR_IN_NORM | TSR_OUT_NORM;
TSR_NORM_MATRIX = TSR_IN_NORM | TSR_OUT_NORM | TSR_IN_MATRIX;

# const de creation de modele
MC_NO_SQUARE = 0x0001
MC_NO_OUTPUT_BIAS = 0x0002
MC_NO_HIDDEN_BIAS = 0x0004

MC_KOHONEN = 0x0010
MC_POLYNOM = 0x0020
MC_CLASSIFICATION = 0x0040
MC_LIN_IN_OUT = 0x0080
MC_LIN = 0x1000
MC_DYN = 0x2000

# constantes de style de neurone (partiellement combinable)
# style de position}
NS_STD = 0x0000;
NS_HIDEDEN = 0x0000
NS_DIRECT = 0x0000
NS_STATE = 0x0002
NS_INPUT = 0x0004
NS_STATE_INPUT = NS_INPUT | NS_STATE
NS_OUTPUT = 0x0008
NS_STATE_OUTPUT = NS_OUTPUT | NS_STATE
NS_CONST = -1

NS_ANYPOS = 0x00FF
NS_NOPOS = 0xFF00
# Style de nature}
NS_SIGMA = 0x0100
NS_PI = 0x0200
NS_SIGMA2 = 0x0400
NS_SIGMAPLUS = 0x0800
NS_ASITIS = 0x4000  # { copie conservant la position }
NS_REVERSE = 0x8000  # { le parent du neurone Pi est traité en inverse}

# const de style de liens synaptiques
LS_STD = 0
_LIBRE = 0           # { Synapse libre }
LS_FIXE = 0x0001      #      { Synapse définitivement fixe }
LS_POS1 = 0x0002      #      { Synapse fixe de coeff 1 }
LS_NEG1 = 0x0004      #      { Synapse fixe de coeff -1 }
LS_BorneeInf = 0x0010#
LS_BorneeSup = 0x0020#
LS_SIGMA_FACTOR = 0x0100     #       { Synapse Facteur Sigma }
LS_PI_FACTOR = 0x0200     #       { Synapse Facteur Pi }
LS_TELQUEL = 0x4000#
LS_INVERSE = 0x8000 #{ La synapse est traité en inverse: L'entrée de la

# modes de minimisation des entrées
(IC_NONE,
 IC_MINIMISATION,
 IC_MAXIMISATION,
 IC_REVERSE,
 IC_REVERSE_SQR_MIN,
 IC_REVERSE_SQR_DELTA_MIN) = list(range(6))

# NodeClassIndex
(NamedNode_CLASS_INDEX, # = 0
LinkedNode_CLASS_INDEX      # = 1
) = list(range(2))

(NEURON_CLASS_INDEX, # = 10
NEURON_SIGMA_CLASS_INDEX, # = 11
NEURON_PI_CLASS_INDEX, # = 12
NEURON_SIGMA_Plus_CLASS_INDEX, # = 13
NEURON_SIGMA_2_CLASS_INDEX    # = 14
) = list(range(10, 15))

NC_CLASS_LIST = ["Neuron", "NeuronSigma", "NeuronPi"]
NC_CLASS_LIST1 = [item.lower() for item in NC_CLASS_LIST]

# ModelClassIndex
(MODEL_CLASS_INDEX, # = 0
NEURON_NETWORK_CLASS_INDEX, # = 1
LIB_MODEL_CLASS_INDEX, # = 2
KOHONEN_CLASS_INDEX, # = 3
NODE_MODEL_CLASS_INDEX, # = 4
MULTI_PARALLEL_MODEL_CLASS_INDEX, # = 5
MULTI_SERIE_MODEL_CLASS_INDEX, # = 6
MULTI_MODEL_CLASS_INDEX, # = 7
LIN_MODEL_CLASS_INDEX, # = 8
MATRIX_MODEL_CLASS_INDEX, # = 9
NORMALIZER_CLASS_INDEX, # = 10
POLYNOM_MODEL_CLASS_INDEX, # = 11
IDENTITY_MODEL_CLASS_INDEX        # = 12
) = list(range(13))

# ModelClassDict
MODEL_CLASS_DICT = {
NEURON_NETWORK_CLASS_INDEX: "NeuronNetwork",
LIB_MODEL_CLASS_INDEX: "CompiledModel",
KOHONEN_CLASS_INDEX: "KohonenModel",
MULTI_PARALLEL_MODEL_CLASS_INDEX: "MultiParallelModel",
MULTI_SERIE_MODEL_CLASS_INDEX: "MultiSerieModel",
LIN_MODEL_CLASS_INDEX: "LinearModel",
MATRIX_MODEL_CLASS_INDEX: "MatrixModel",
NORMALIZER_CLASS_INDEX: "NormalizerModel",
POLYNOM_MODEL_CLASS_INDEX: "PolynomialModel",
IDENTITY_MODEL_CLASS_INDEX: "IdentityModel"}  

# DriverClassList
DRIVER_CLASS_LIST = {
1: "Illinear",
2: "Static",
3: "Dynamic",
4: "InputsVariables",
5: "Kohonen",
11: "Linear.SymetricRealMatrix",
12: "Linear.SquareRealMatrix",
13: "Linear.RealMatrix",
14: "Linear.RealVector"}

# const de NeuronType    
(ntNone,
ntSigma, # neurone somme pondéré
ntSigma2, # obsolete (somme des carrés pondérés)
ntPi, # neurone produit pondéré
ntSigmaPlus # reserve
) = list(range(5))

# const de fin d'apprentissage (retour de TRAINING_END)
(Current, # 0
OKTarget, # 1
EpochCount, # 2
Accuracy, # 3
HighWeight, # 4
ComputeError, # 5
UserDemand, # 6
BestValid      # 7
) = list(range(8))

# constantes de type de fichier model (retour de TestFile)
(NotAModel, # 0
BinaryModelFile, # 1
ASCIIModelFile, # 2
XMLModelFile, # 3
XMLModelString, # 4
XMLMetaModelFile, # 5
CompiledModelFile, # 6
MGLFile, # 7
MGLString, # 8
ASCIIString        # 9
) = list(range(10))

XMLFile = 64
MMLFileCost = 65
MMLFileActiv = 66

# constantes de type de fichier paramétres (retour de TestFile)
(BinaryParamFile, # 128
ASCIIParamFile, # 129
XMLParamFile, # 130
XMLParamString, # 131
) = list(range(128, 128 + 4))

(CSVsemicol,
CSVtab
) = list(range(257, 257 + 2))

# descripteurs des fichiers analyses par TestFile    
FILE_DESC = {
    NotAModel: "Unknown",
    BinaryModelFile: "Binary Model File",
    ASCIIModelFile: "ASCII Model File",
    XMLModelFile: "XML Model File",
    XMLModelString: "XML Model String",
    XMLMetaModelFile: "XML MetaModel File",
    CompiledModelFile: "Compiled Model File",
    MGLFile: "MGL Model File",
    MGLString: "MGL Model String",
    ASCIIString: "ASCII Model String",
    MMLFileCost: 'MML File Cost',
    MMLFileActiv: "MML File Activ",
    XMLFile: 'XML File',
    BinaryParamFile: "Binary Param File",
    ASCIIParamFile: "ASCII Param File",
    XMLParamFile: "XML Param File",
    XMLParamString: "XML Param String",
    CSVsemicol: "CSV File",
    CSVtab: "TXT File"}

# const de Classes de driver (retour de DRIVER_CLASS)
(UnknownClass,
 TRnDrv,
 TRnDrv_Stat,
 TRnDrv_Dyn,
 TRnDrvReseauFonction) = list(range(5))
 
(TRealVector,
 TRealMatrix,
 TSquareRealMatrix,
 TSymetricRealMatrix) = list(range(11, 15))
TLibModel = 32
ClassList = list(range(5))
ClassList.extend(list(range(11, 15)))
ClassList.append(32) 

# const de Classes de modeles (retour de MODEL_CLASS) 
#    (Unknown, TNeuronNetwork, TLibModel, T KohonenNetwork, TNodeModel, 
#     TMultiParallelModel, TMultiSerieModel, TMultiModel, TModel) = range(9)  

#  styles de modification de reseau, avec le type du parametre
(UNKNOWN, # 0 
FIXMODEL, # 1  -> NA
MODIFYNODE, # 2  -> TNodeData
ADDLOOP, # 3  -> TLoopDataEx 
DIFFERENTIALLOOP, # 4  -> TBoucleDiff
ADDNODE, # 5  -> TNodeData 
DELETENODE, # 6  -> TNodeData
MOVENODE, # 7  -> TSynapseData
MERGENODE, # 8  -> TSynapseData
ADDLINK, # 9  -> TSynapseData
DELETELINK, # 10 -> TSynapseData
MODIFYLINK, # 11 -> TSynapseData
ADDLAYER, # 12 -> TLayerData
DELETELAYER, # 13 -> TLayerData 
MERGEMODEL, # 14 -> TMergeData
COMPACTMODEL,  # 15 -> compactparam Compactage du modèle
INTEGRATETEMPSERIE  # 16 -> NA Integration des series temporelles 
) = list(range(17))
#ModificationStyles = range(17)  # ex StyleModifList

# listes de styles de modification    
_NodeActions = [MODIFYNODE, ADDNODE, DELETENODE]
_LinkActions = [MOVENODE, MERGENODE, ADDLINK, DELETELINK, MODIFYLINK]
_LayerActions = [ADDLAYER, DELETELAYER]
_ModelActions = [FIXMODEL, COMPACTMODEL]

# constantes de position de noeud lors d'un ajout
(AN_DONT_CARE,
 AN_CONSTANT,
 AN_INPUT,
 AN_OUTPUT,
 AN_OUT_STATE) = list(range(5))

# constantes de lecture de diagnostique
(DIAG_0, # = 0;
DIAG_RESULT, # = 1;
DIAG_PARAM, # = 2;
DIAG_PARAM_CI, # = 3;
DIAG_PARAM_CORREL, # = 4;
DIAG_PARAM_VAR_COVAR, # = 5;
DIAG_PARAM_CIMC, # = 6;
DIAG_PARAM_CORREL_MC, # = 7;
DIAG_PARAM_VAR_COVAR_MC #= 8;
) = list(range(9))

DIAG_MAX = DIAG_PARAM_VAR_COVAR_MC

# differential looping    
(BD_EULER, # Euler loop
BD_RK2, # order 2 Runge-Kuta
BD_RK4                  # order 4 Runge-Kuta
) = list(range(3))
TBoucleDiff = list(range(3))    

# liste des motifs de fin d'apprentissage
(EN_COURS,
OK_OBJECTIF,
NB_EPOQUE,
PRECISION,
FORT_POIDS,
ERREUR_CALCUL,
USER_DEMAND,
BEST_VALID
) = list(range(8))

# Style de callback dans les fonctions de training
(cbk_None, # = 0
CBK_ERROR, # = 1
CBK_TRAIN_PROGRESS, # = 2
CBK_TRAIN_END, # = 3
CBK_INIT_PARAM, # = 4
CBK_START_CYCLE, # = 5
CBK_END_CYCLE, # = 6
CBK_TRANSFER, # = 7
CBK_RESAMPLING, # = 8
CBK_LOAD_PROGRESS, # = 9
CBK_LOAD_END        # = 10
) = list(range(11))
cbkstr = ["None", "Error", "TrainProgress", "TrainEnd", "InitWeight",
           "StartCycle", "EndCycle", "Transfer", "Resampling", "LoadProgress",
           "LoadEnd"]

# style d'action modele
(MA_INIT_PARAMS, #  Initialisation des paramètres
MA_LOAD_TRAINING_DATA, #  Chargement des données d'apprentissage
MA_NORMALIZE_DATA, #  Normalisation des données 
MA_CLEAR_COMMENT, #  Effacement des commentaires.  
MA_CONFIDENCE_COMPUTATION, #  Calcul de la matrice de dispersion 
MA_CLEAR_TRAIN_MODEL_LIST, #  Effacement de la liste de modèles d'apprentissage
MA_LOAD_BEST_TRAIN,
MA_CLEAR_DATA,
MA_READ_MEAN_DEV,
MA_CLEAR_MULTITRAIN_DIRECTORY,
MA_INCLUDE_NORMALIZATION,
MA_CLEAR_SAVE_DIR,
MA_CLEAR_OBJECT_FILES,
MA_BUILD_DESIRE_NETWORK,
MA_CLEZAR_STATE_MEMORY,
MA_UPDATES_NAMES,
MA_CLEAR_TRAINING_DATA,
MA_COMPUTE_RESAMPLING_RESULT,
MA_FREE_ALL,
MA_COMPUTE_ALL,
MA_FREEZE_RBF_BASIS,
MA_PRUNING_NODE,
MA_REINIT_MODEL) = list(range(23))
#MA_PRUNING_PARAMETERS) = range(23)

# style d'apprentissage
TR_S_STD = 0    #      1  Apprentissage standard
TR_S_SIMPLE = 0 #      1  Apprentissage standard
(
TR_S_INIT_PARAM, # = 1  0x1  1  Apprentissage avec initialisation des poids dès le premier cycle
TR_S_QUIET, # = 2  0x2  1  Apprentissage silencieux (pas d'envoi d'information dans ACallBack)
TR_S_LEVERAGE, # = 4  0x4  1  Apprentissage puis calcul des leviers.
TR_S_RE_SAMPLING, # = 8  0x8  3  Apprentissage de bootstrap
TR_S_EPOCH_X_IDDEN, # = 16 0x10 1  Apprentissage avec nb d'initialisation multiple du nb de noeuds caches
TR_S_LOO, # = 32 0x20
) = (2 ** i for i in range(6))

TR_S_INIT_PARAM_LEVERAGE = TR_S_INIT_PARAM | TR_S_LEVERAGE

# # style de ré-échantillonnage
# (RE_NONE,
# RE_BS_STD,  # Bootstrap standard
# RE_BS_RESIDU, # Bootstrap des résidus
# RE_RESERVE1,
# RE_RESERVE2,
# RE_LOO,      # Leave-One-Out integre
# RE_SUPER     # Super train
# ) = list(range(7))

# tableTemplate = {
#     "": "trainingResults%03d",
#     "BS": "BS%03d", 
#     "bs": "BS%03d", 
#     "bootstrap": "BS%03d", 
#     "loo" : "LOO%03d",
#     "LOO" : "LOO%03d",
#     RE_NONE:"trainingResults%03d",
#     RE_BS_STD: "BS%03d",
#     RE_BS_RESIDU: "BS%03d",
#     RE_RESERVE1: "BS%03d",
#     RE_RESERVE2: "BS%03d",
#     RE_LOO: "LOO%03d",
#     RE_SUPER: "trainingResults%03d",}


# BSGROUP = (RE_BS_STD, RE_BS_RESIDU, RE_RESERVE1, RE_RESERVE2)

# critere de choix apres reechantillonnage multi init
(CRITER_STDDEV,
CRITER_PRESS,
CRITER_LEV) = list(range(3))

criterFields = ["stddev", "PRESS", "leverages"]
criterindex = [TRR_COST, TRR_PRESS, TRR_LEV]

#style d'init de 'ré-échantillonnage
(INIT_START_PARAM,
INIT_END_PARAM,
INIT_RANDOM
) = list(range(3))

INIT_NAME = ["start_parameters", 'end_parameters', 'random']


# constantes d'appel a getVector et setVector    
(VE_TRAINING_DATA, #         1 : table interne, complet, dans l'ordre de la table
VE_TRAINING_DATA_LONG,
VE_TRAIN, #                 1 : table interne, apprentissage, ordre de l'apprentissage
VE_TEST, #                  1 : table interne, test
VE_OUTPUT_VECTOR, #          1 : table interne, sorties
VE_STATE_VECTOR, #          putnorm 3 : table interne, états
VE_LOCAL_COST, #             2 : table interne, cout local
VE_ERRORDS,
VE_VARIABLES, #             1 : poids ( ou entrées pour les pilotes d'optimisation)
VE_NORMALIZATION_SET, #      1 : jeu de normalisation
VE_IN_OUT_NORMALIZATION_SET, # 1 : Obsolete, remplace par VE_IN_NORMALIZATION_SET et VE_OUT_NORMALIZATION_SET 
VE_EXPERIMENTAL_DOMAIN, #    2 : domaine expérimental
VE_OUTPUT_DOMAIN, #          2 : domaine de sortie
VE_PARAM_DOMAIN, #           2 : domaine paramètrique
VE_PARAM_INI, #              1 : paramètres d'initialisation des poids
VE_JACOBIAN, #              2 : matrice jacobienne
VE_DISPERSION_MATRIX, #      2 : matrice de dispersion.  
VE_CONFIDENCE_PARAM, #
VE_CONFIDENCE_MULTIPLYER, #
VE_PARAM_UP_DOWN_LIST, #
VE_BOOL_INPUTS, # vecteur de longbool
VE_TRAINING_RESULT,
VE_BOOT_STRAP_PARAM,
VE_LEVERAGES, # 2 : table interne, leviers
VE_RESIDUALS, # 2 : table interne, residus
VE_INPUTS,  # colonne de valeurs d'entree
VE_OUTPUTS, # colonne de valeurs de sortie
VE_STATES,  # colonne de valeurs d'etat
VE_COMPUTED_OUTPUTS,
VE_WEIGHTING,
VE_COMPUTED_OUTPUTS_CI,
VE_PARAM_CORREL_MATRIX, #       2: Matrice de correlation entre parametres (NSynapse*NSynapse)
VE_PARAMETERS_CI, #           2: Liste des paramètres +- IC
VE_RESAMPLING_SERIE,
VE_MULTI_RESULTS,
VE_OUTPUT_DERIVATIVE,
VE_IN_NORMALIZATION_SET, # matrice de normalisation des entrees
VE_OUT_NORMALIZATION_SET, # matrice de normalisation des sorties
VE_DATA_FORMAT, # LongInt: format des donnes en lecture 
VE_PARAMETERS              # Parametres du modele (poids neuronaux)
) = list(range(40))

#useMatrix = 0x100          # a ajouter au descripteur de vecteur pour obtenir une sortie de type numpy.matrix
M_TRANSPOSE = 0x200
MNO_KEEP_MATRIX = 0x400         # ajouté au descripteur de vecteur pour signaler

SingleColMatrices = frozenset((VE_VARIABLES, VE_ERRORDS, VE_BOOT_STRAP_PARAM, VE_LEVERAGES,
    VE_RESIDUALS, VE_INPUTS, VE_OUTPUTS, VE_STATES, VE_COMPUTED_OUTPUTS,
    VE_WEIGHTING, VE_RESAMPLING_SERIE, VE_CONFIDENCE_PARAM, VE_CONFIDENCE_MULTIPLYER,
    VE_BOOL_INPUTS, VE_OUTPUT_VECTOR, VE_STATE_VECTOR, VE_LOCAL_COST, VE_DATA_FORMAT))

SETTABLE_ARRAYS = frozenset((
    VE_TRAINING_DATA,
    VE_PARAM_INI,
    VE_VARIABLES,
    VE_NORMALIZATION_SET,
    VE_IN_NORMALIZATION_SET,
    VE_OUT_NORMALIZATION_SET,
    VE_EXPERIMENTAL_DOMAIN,
    VE_OUTPUT_DOMAIN,
    VE_PARAM_DOMAIN,
    VE_BOOL_INPUTS,
    VE_WEIGHTING,
    VE_INPUTS,
    VE_OUTPUTS,
    VE_STATES,
    VE_STATE_VECTOR,
    VE_DATA_FORMAT))

doNormIndex = 0x1000 #  combiner avec l'indice dans setArray avec les styles 
                    # VE_INPUTS ou VE_OUTPUTS pour obtenir une normalisation locale

VECT_DICT = {
    VE_TRAINING_DATA: "VE_TRAINING_DATA", #         1 : table interne, complet, dans l'ordre de la table
    VE_TRAINING_DATA_LONG: "VE_TRAINING_DATA_LONG",
    VE_TRAIN: "VE_TRAIN", #                 1 : table interne, apprentissage, ordre de l'apprentissage
    VE_TEST: "VE_TEST", #                  1 : table interne, test
    VE_OUTPUT_VECTOR: "VE_OUTPUT_VECTOR", #          1 : table interne, sorties
    VE_STATE_VECTOR: "VE_STATE_VECTOR", #           3 : table interne, états
    VE_LOCAL_COST: "VE_LOCAL_COST", #        2 : table interne, cout local
    VE_ERRORDS: "VE_ERRORDS",
    VE_VARIABLES: "VE_VARIABLES", #             1 : poids ( ou entrées pour les pilotes d'optimisation)
    VE_NORMALIZATION_SET: "VE_NORMALIZATION_SET", #      1 : jeu de normalisation
    VE_IN_OUT_NORMALIZATION_SET: "VE_IN_OUT_NORMALIZATION_SET", # 1 : Obsolete, remplace par VE_IN_NORMALIZATION_SET et VE_OUT_NORMALIZATION_SET 
    VE_EXPERIMENTAL_DOMAIN: "VE_EXPERIMENTAL_DOMAIN", #    2 : domaine expérimental
    VE_OUTPUT_DOMAIN: "VE_OUTPUT_DOMAIN", #          2 : domaine de sortie
    VE_PARAM_DOMAIN: "VE_PARAM_DOMAIN", #           2 : domaine paramètrique
    VE_PARAM_INI: "VE_PARAM_INI", #              1 : paramètres d'initialisation des poids
    VE_JACOBIAN: "VE_JACOBIAN", #              2 : matrice jacobienne
    VE_DISPERSION_MATRIX: "VE_DISPERSION_MATRIX", #      2 : matrice de dispersion.  
    VE_CONFIDENCE_PARAM: "VE_CONFIDENCE_PARAM", #
    VE_CONFIDENCE_MULTIPLYER: "VE_CONFIDENCE_MULTIPLYER", #
    VE_PARAM_UP_DOWN_LIST: "VE_PARAM_UP_DOWN_LIST", #
    VE_BOOL_INPUTS: "VE_BOOL_INPUTS",
    VE_TRAINING_RESULT: "VE_TRAINING_RESULT",
    VE_BOOT_STRAP_PARAM: "VE_BOOT_STRAP_PARAM",
    VE_LEVERAGES: "VE_LEVERAGES", # 2 : table interne, leviers
    VE_RESIDUALS: "VE_RESIDUALS", # 2 : table interne, residus
    VE_INPUTS: "VE_INPUTS",
    VE_OUTPUTS: "VE_OUTPUTS",
    VE_STATES: "VE_STATES",
    VE_COMPUTED_OUTPUTS: "VE_COMPUTED_OUTPUTS",
    VE_WEIGHTING: "VE_WEIGHTING",
    VE_COMPUTED_OUTPUTS_CI: "VE_COMPUTED_OUTPUTS_CI",
    VE_PARAM_CORREL_MATRIX: "VE_PARAM_CORREL_MATRIX", #       2: Matrice de correlation entre parametres (NSynapse*NSynapse)
    VE_PARAMETERS_CI: "VE_PARAMETERS_CI", #           2: Liste des paramètres +- IC
    VE_RESAMPLING_SERIE: "VE_RESAMPLING_SERIE",
    VE_MULTI_RESULTS: "VE_MULTI_RESULTS",
    VE_OUTPUT_DERIVATIVE: "VE_OUTPUT_DERIVATIVE",
    VE_IN_NORMALIZATION_SET: "VE_IN_NORMALIZATION_SET", # matrice de normalisation des entrees
    VE_OUT_NORMALIZATION_SET: "VE_OUT_NORMALIZATION_SET",
    VE_DATA_FORMAT: "VE_DATA_FORMAT"}     # matrice de normalisation des sorties

# style de transfert
(TR_SIMPLE, # 1 Transfert simple
TR_CONFIDENCE, # 2 Transfert avec confiance
TR_GRAD_LEV, # 2 Transfert avec gradient et leviers
TR_GRAD_DIR, # 3 Transfert avec gradient direct
TR_GRADS, # 2 Transfert avec gradient/poids et gradient/entrées
TR_GRAD_HESS, # 2 Transfert avec gradient et leviers
TR_IN_GRAD_HESS, # 2 Transfert avec gradeint/entrées et hessien/entrées
TR_MIX_HESS, # 3 Transfert avec Hessien mixte.
TR_RE_SAMPLING, # 2 Transfert avec bootstrap.
TR_KOHONEN, # 2 Transfert de Kohonen.
TR_RE_SAMPLINGC # 2 Transfert avec bootstrap -> moyenne, +IC et -IC
) = list(range(11))

TR_1_OUT = [TR_SIMPLE, TR_RE_SAMPLING]
TR_2_OUT = [TR_GRAD_DIR, TR_MIX_HESS]
TR_3_OUT = [TR_CONFIDENCE, TR_GRAD_LEV, TR_GRADS, TR_GRAD_HESS, TR_IN_GRAD_HESS,
          TR_KOHONEN, TR_RE_SAMPLINGC]

# Style de creation de code
#===============================================================================
# (CD_UNKNOWN, #     = 0
# CD_MAIN_USE, #     = 1
# CD_MAIN_TRAIN, #   = 2
# CD_TRANSFER, #    = 3
# CD_GRADIENT, #    = 4
# CD_TRANSFER_LEV, # = 5
# CD_TRAINING, #    = 6
# CD_MAKE_USE, #     = 7
# CD_MAKE_TRAIN, #   = 8
# CD_MAKE_DLM, #     = 9
# CD_SOURCE_DLM  #   = 10 
# ) = range(11)
#===============================================================================

# Style de lecture/écriture de texte
#                valeur   Handle  Ind0     Ind1      Level Retourne :
(GT_PRODUCT_INFO, # = 0   NA      0        NA        1     : infos sur NDK
                   #               1                        : caller
                   #               2                        : nom complet DLL
                   #               3                        : version de la DLL
                   #               4                        : numero de serie
                   #               5                        : indicatif de langue
                   #               6                        : nom du fichier d'initialisation
                   #               7                        : date de compilation
                   #               8                        : date limite de fonctionnement
                   #               251                      : convention d'appel des fonctions
                   #               252                      : statut du compilateur
                   #               253                      : nom du compilateur
                   #               254                      : origine de la lidence
                   #               255                      : rapport d'installation
                   #               255      1               : licence max 
GT_FUNCTION_NAME, # = 1   NA      fType    Index     2     fonctions disponibles(activation, co￻t, voisinnage, decroissance)
GT_MODEL_NAME, # = 2   Handle  ind      NA        1          Ind0
                   #                                             0: nom du modele
                   #                                             1: fichier du modele
                   #                                             2: fichier de parametres:
                   #                                             3: fichier de donnees
GT_FORMULA, # = 3   Handle  NA       NA        1     formule de calcul du modele
GT_COMMENT, # = 4   Handle  Index    NA        1     Commentaire
GT_INPUT_NAME, # = 5   Handle  Index    NA        1     Nom d'entree
GT_OUTPUT_NAME, # = 6   Handle  Index    NA        1     Nom de sortie
GT_STICKER, # = 7   Handle  IndLayer IndNeuron 2     Etiquette d'un noeud
GT_PARAMETER_NAME, # = 8   Handle  Index    NA        1     Nom d'un poids
GT_MODEL_CLASS_NAME, # = 9   Handle  NA       NA        3     Nom de classe du modele
GT_STATE_NAME, # = 10  Handle  Index    NA        3     Nom d'￩tat
GT_NODE_NAME, # = 11  Handle  IndLayer IndNeuron 2     Nom d'un noeud
GT_SAVE_DIR, # = 12  Handle  Dir      NA        2     Repertoire de sauvegarde(Ind0=0: SaveDir; 1: SubDir; 2: TempDir)
GT_PARAM_FILE, # = 13  Handle  Index    NA        0     Fichier de sauvegarde des apprentissages indexé
GT_NOISE_MODEL_FILE, # = 14  Handle  NA       NA        3     Fichier de modèle de bruit (Ecart-typa fonction des entrées)
GT_MML_FUNCTION, # = 15  Handle  NA       NA        3     Enregistrement d'une fonction MathML (Activation, Cost, Proxy, Decay)
GT_ADD_TRAIN_MODEL, # = 16  Handle  NA       NA        2     Enregistrement d'un fichier de modele en liste pour l'apprentissage
GT_DIAGNOSTIC, # = 17  Handle  Level
                   #                                          Ind0: 
                   #                                          Ind1:
GT_SEPARATOR, # = 18  Handle
GT_CODE, # = 19  Handle  IndLang  IndFct    3     code du mod￨le      / a developper
                   #                                          IndLang : 1: C
                   #                                          IndFct  : Style de creation de code     
GT_INI_FILE_NAME, # = 20
#gt_ModelData       # = 21  Handle  Train     NA             ModelData String   
GT_LINK_NAME, # = 21;
GT_START_SEQUENCE, # = 22;
GT_SYSTEM_NAME, # = 23;
GT_MASTER_NET_FILE_NAME # = 24;
) = list(range(25))

# sub style for GT_SYSTEM_NAME
(GT_FILE_NAME,
GT_COMMON_PATH,
GT_CCOMPILER,
GT_CODE_FILE_NAME,
GT_LAST_ERROR
) = list(range(3, 8))

# product info index
INFO_NDK_FILE = 1
INFO_CALLER = 2
INFO_VERSION = 3
INFO_SERIAL = 4
INFO_LANG = 5
INFO_CONFIG_FILE = 6
INFO_COMPILE_DATE = 7
INFO_LIMIT_DATE = 8
INFO_LICENSE_MAX = (255, 1)
INFO_CALLING_CONVENTION = 251
INFO_COMPILER_STATUS = 252
INFO_COMPILER_NAME = 253
INFO_LICENSE_ORIGIN = 254
INFO_INSTALLATION_REPORT = 255

#verbosity index
VERB_0 = 0
VERB_DETAIL = 0x0001
VERB_TRAIN = 0x0002
VERB_TRAINPROGRESS = 0x0004
VERB_TRANSFER = 0x0008
VERB_MATRIX_BROWSE = 0x0010
VERB_RESAMPLING = 0x0020

VERB_ALL_TRAIN = VERB_TRAIN | VERB_TRAINPROGRESS
VERB_ALL = 0xFFFF

# Index des types de fichiers
(TG_NONE, 
TG_BINARY, 
TG_ASCII_FILE, 
TG_XML_FILE, 
TG_XML_STRING,
TG_XML_MRTA, 
TG_COMPILED_MODEL, 
TG_MGL_FILE, 
TG_MGL_STRING, 
TG_ASCII_STRING) = list(range(10))

FT_MODEl = 0
FT_PARAM = 127
FT_XML = 64
FT_MML_ACTIV = 65
FT_MML_COST = 66
FT_CSV_SEMICOLON = 257
FT_CSV_TAB = 258
FT_CSV_COLON = 259
FT_CSV_SPACE = 260
FT_DONT_EXISTS = 1023

# IndLang du code fourni avec GT_CODE
(cl_XML, # 0  chaîne XML
cl_C, # 1  C (IndFct=1: en-tête) et (IndFct=0: corps)
cl_VB, # 2 Visual Basic Inutilisé
cl_XL, # 4  Macro Excel
cl_MGL, # 4  MGL
cl_String # 5  Model String
) = list(range(6))

# IndFct du code fourni avec GT_CODE
(CD_UNKNOWN, # = 0
CD_MAIN_USE, # = 1
CD_MAIN_TRAIN, # = 2
CD_TRANSFER, # = 3
CD_GRADIENT, # = 4
CD_TRANSFER_LEV, # = 5
CD_TRAINING, # = 6
CD_MAKE_USE, # = 7
CD_MAKE_TRAIN, # = 8
CD_MAKE_DLM, # = 9
CD_SOURCE_DLM    # = 10  
) = list(range(11))

# Indice des diagnostiques avec GT_DIAGNOSTIC    
#===============================================================================
# (diag_Header, # = 0;
# DIAG_RESULT, # = 1;
# DIAG_PARAM, # = 2;
# DIAG_PARAM_CI, # = 3;
# DIAG_PARAM_CORREL, # = 4;
# DIAG_PARAM_VAR_COVAR, # = 5;
# DIAG_PARAM_CIMC, # = 6;
# DIAG_PARAM_CORREL_MC, # = 7;
# DIAG_PARAM_VAR_COVAR_MC  # = 8;
# ) = range(9)
#===============================================================================

# dictionnaire des noms des classes de pilotes
driverClassNames = {
    UnknownClass: 'Unknown',
    TRnDrv: 'TRnDrv',
    TRnDrv_Stat: 'TRnDrv_Stat',
    TRnDrv_Dyn: 'TRnDrv_Dyn',
    TRnDrvReseauFonction: 'TRnDrvReseauFonction',
    TRealVector: 'TRealVector',
    TRealMatrix: 'TRealMatrix',
    TSquareRealMatrix: 'TSquareRealMatrix',
    TSymetricRealMatrix: 'TSymetricRealMatrix',
    TLibModel: 'TLibModel'}

# dictionnaire des noms des motifs d'arrete d'apprentissage
trainingEndNames = {
    Current: 'Current',
    OKTarget: 'OKTarget',
    EpochCount: 'EpochCount',
    Accuracy: 'Accuracy',
    HighWeight: 'HighWeight',
    ComputeError: 'ComputeError',
    UserDemand: 'UserDemand',
    BestValid: 'BestValid'}

# dictionnaire des noms de fonctions d'activation
ACTIV_NAME = {
    IDENTITY: "IDENTITY",
    UNIT: "UNIT",
    TANH: "TANH",
    STEP: "STEP",
    GAUSS: "GAUSS",
    SINE: "SINE",
    EXP: "EXP",
    QUADRATIC: "QUADRATIC",
    ATAN: "ATAN",
    MOMENT0: "MOMENT0",
    MOMENT1: "MOMENT1",
    REVERSE: "REVERSE",
    LOG: "LOG",
    CUBIC: "CUBIC",
    QUASIABS: "QUASIABS",
    SIGMOID: "SIGMOID",
    COMPLEMENT: "COMPLEMENT",
    ROOT: "ROOT",
    ARCSH: "ARCSH",
    SQR: "SQR",
    COS: "COS",
    ERF: "ERF"}

activLongName = {
    IDENTITY: "Identity",
    UNIT: "Unit",
    TANH: "Hyperbolic tangent",
    STEP: "Step",
    GAUSS: "Gaussian",
    SINE: "Sine",
    EXP: "Exponential",
    QUADRATIC: "Qadratic",
    ATAN: "Arc tangent",
    MOMENT0: "Moment 0",
    MOMENT1: "Moment 1",
    REVERSE: "Reverse",
    LOG: "Logarithm",
    CUBIC: "Cubic",
    QUASIABS: "Quasi absolute",
    SIGMOID: "Sigmoïd",
    COMPLEMENT: "Complement to 1",
    ROOT: "Root",
    ARCSH: "Argument hyperbolic cosine",
    SQR: "Square",
    COS: "Cosine",
    ERF: "Error function"}

activDisplay = [
    IDENTITY,
    UNIT,
    TANH,
    SINE,
    COS,
    EXP,
    QUADRATIC,
    ATAN,
    GAUSS,
    MOMENT0,
    MOMENT1,
    REVERSE,
    LOG,
    CUBIC,
    SIGMOID,
    COMPLEMENT,
    ROOT,
    ARCSH,
    SQR,
    ERF]

shortActivDisplay = [
    IDENTITY,
    TANH,
    SINE,
    COS,
    EXP,
    QUADRATIC,
    ATAN,
    GAUSS,
    MOMENT0,
    MOMENT1,
    REVERSE,
    LOG,
    CUBIC,
    ARCSH,
    ERF]

activDisplayNames = [activLongName[item] for item in activDisplay]
shortActivDisplayNames = [activLongName[item] for item in shortActivDisplay]

# dictionnaire des indices de fonction d'activation
activByName = {
    '': IDENTITY,
    'IDENT': IDENTITY,
    'IDENTITY': IDENTITY,
    'UNIT': UNIT,
    'UNITY': UNIT,
    'TANH': TANH,
    'TH': TANH,
    'STEP': STEP,
    'GAUSS': GAUSS,
    'GAUSSIAN': GAUSS,
    'SINE': SINE,
    'SIN': SINE,
    'EXP': EXP,
    'EXPONENT': EXP,
    'QUADRATIC': QUADRATIC,
    'ATAN': ATAN,
    'ARCTAN': ATAN,
    'MOMENT0': MOMENT0,
    'MOMENT1': MOMENT1,
    'REVERSE': REVERSE,
    'LOG': LOG,
    'LOGARITHM': LOG,
    'CUBIC': CUBIC,
    'QUASIABS': QUASIABS,
    'SIGMOID': SIGMOID,
    'SIG': SIGMOID,
    'COMPLEMENT': COMPLEMENT,
    'ROOT': ROOT,
    'ARCSH': ARCSH,
    'SQR': SQR,
    'SQARE': SQR,
    'COS': COS,
    'COSINE': COS,
    'ERF': ERF,
    'ERRORFUNCTION': ERF}

# dictionnaire des indices des fonctions de cout
costByName = {
    'NULL': NONE,
    'SQUAREDELTA': SQUAREDELTA,
    'LEASTSQUAREDELTA': LEASTSQUAREDELTA,
    'WEIGHTEDSQUAREDELTA': WEIGHTEDSQUAREDELTA,
    'UNCLASSIFIED': UNCLASSIFIED,
    'BADCLASSICATION': UNCLASSIFIED,
    'WEIGHTEDCLASSIFICATION': WEIGHTEDCLASSIFICATION,
    'RELATIVESQUAREDELTA': RELATIVESQUAREDELTA,
    'GAUSSSQUAREDELTA': GAUSSSQUAREDELTA,
    'CROSSEDENTROPY': CROSSEDENTROPY,
    'EXPSQUAREDELTA': EXPSQUAREDELTA,
    'EXPONENTSQUAREDELTA': EXPSQUAREDELTA}

# dictionnaire des indices de fonctions de proximite de Kohonen
proxyByName = {
    'SQUARE': PSQUARE,
    'GAUSS': PGAUSS}

# dictionnaire des indices des fonctions de decroissance de Kohonen
decayByName = {
    'REVERSE': DREVERSE,
    'REVERSEROOT': DREVERSEROOT,
    'EXPONENT': DEXPONENT}

# def criterionName(index):
#     """Retourne le nom du critere. L'index est soit la valeur entiere TCR, 
#     soit le nom de champ prefdisplay
#     """
#     if isinstance(index, int):
#         try:
#             return CRITERION_NAME[index]
#         except:
#             return ""
#     for key, value in prefdisplay.iteritems():
#         if value.lower() == index:
#             return  CRITERION_NAME[key]
#     return ""
# 
# def fieldName(index):
#     """Retourne le nom du champ. L'index est soit la valeur entiere TCR, 
#     soit le nom de critere CRITERION_NAME
#     """
#     if isinstance(index, int):
#         try:
#             return prefdisplay[index]
#         except:
#             return ""
#     for key, value in prefdisplay.iteritems():
#         if value == index:
#             return  prefdisplay[key]
#     return ""

LEV_TEST_THRESHOLD = 1E-3

# dictionnaire des fins d'apprentisages
END_TRAINING_DICT = {
    EN_COURS: 'running',
    OK_OBJECTIF: 'Objective OK',
    NB_EPOQUE: 'Epochs OK',
    PRECISION: 'Accuracy',
    FORT_POIDS: 'High parameter',
    ERREUR_CALCUL: 'Computation error',
    USER_DEMAND: 'User demand',
    BEST_VALID: 'Best validation'}

#  dictionnaire des info de nombre de vecteurs indexes du type
INFO_VECTOR = {
    VE_TRAINING_DATA: DATA_COUNT,
    VE_TRAINING_DATA_LONG: DATA_COUNT,
    VE_OUTPUT_VECTOR: DATA_COUNT,
    VE_STATE_VECTOR: DATA_COUNT,
    VE_LOCAL_COST: DATA_COUNT,
    VE_EXPERIMENTAL_DOMAIN: INPUT_COUNT,
    VE_INPUTS: INPUT_COUNT,
    VE_OUTPUT_DOMAIN: OUTPUT_COUNT,
    VE_JACOBIAN: OUTPUT_COUNT,
    VE_LEVERAGES: OUTPUT_COUNT,
    VE_RESIDUALS: OUTPUT_COUNT,
    VE_OUTPUTS: OUTPUT_COUNT,
    VE_COMPUTED_OUTPUTS: OUTPUT_COUNT,
    VE_COMPUTED_OUTPUTS_CI: OUTPUT_COUNT,
    VE_STATES: ORDER,
    VE_TRAINING_RESULT: TRAINING_RESULT_COUNT} 
    # to be extended with other vector types

#dictionnaire des dimension matricielles des vecteurs appelés avec index = -1
#===============================================================================
# Regles de fonctionnement :
#
#   - une valeur negative est le negatif de la dimension fixe
#   - une valeur positive est l'indice de la propriete info qui donne la dimension.
#   - si la valeur absolue est > 512 (0x200).(M_TRANSPOSE)
#         les dimensions sont celles de la matrice transposée
#
#  Le resultat est le nombre de colonnes de la matrice (dimension Y)
#
#===============================================================================
MATRIX_DIM = {  # dimension transversale de matrice
    VE_TRAINING_DATA: DATA_COUNT, #         1 : table interne, complet, dans l'ordre de la table
    VE_TRAINING_DATA_LONG: DATA_COUNT | M_TRANSPOSE,
    VE_TRAIN: TRAIN_SIZE, #                 1 : table interne, apprentissage, ordre de l'apprentissage
    VE_TEST: TEST_SIZE, #                  1 : table interne, test
    VE_OUTPUT_VECTOR: OUTPUT_COUNT, #          1 : table interne, sorties
    VE_STATE_VECTOR: ORDER, #           3 : table interne, états
    VE_LOCAL_COST: OUTPUT_COUNT, #             2 : table interne, cout local
    VE_ERRORDS:-1,
    VE_VARIABLES:-1, #             1 : poids ( ou entrées pour les pilotes d'optimisation)
    VE_NORMALIZATION_SET:-2, #      1 : jeu de normalisation
    VE_IN_OUT_NORMALIZATION_SET: None, # 1 : Obsolete, remplace par VE_IN_NORMALIZATION_SET et VE_OUT_NORMALIZATION_SET 
    VE_EXPERIMENTAL_DOMAIN:-2, #    2 : domaine expérimental
    VE_OUTPUT_DOMAIN:-2, #          2 : domaine de sortie
    VE_PARAM_DOMAIN:-2, #           2 : domaine paramètrique
    VE_PARAM_INI:-2, #              1 : paramètres d'initialisation des poids
    VE_JACOBIAN: DATA_COUNT | M_TRANSPOSE, #              2 : matrice jacobienne
    VE_DISPERSION_MATRIX: SYNAPSE_COUNT, #      2 : matrice de dispersion.  
    VE_CONFIDENCE_PARAM:-1, #
    VE_CONFIDENCE_MULTIPLYER:-1, #
    VE_PARAM_UP_DOWN_LIST:-3, #
    VE_BOOL_INPUTS:-1,
    VE_TRAINING_RESULT: CRITERIA_COUNT,
    VE_BOOT_STRAP_PARAM: SYNAPSE_COUNT,
    VE_LEVERAGES: DATA_COUNT, # 2 : table interne, leviers
    VE_RESIDUALS: DATA_COUNT, # 2 : table interne, residus
    VE_INPUTS: DATA_COUNT,
    VE_OUTPUTS: DATA_COUNT,
    VE_STATES: DATA_COUNT,
    VE_COMPUTED_OUTPUTS: DATA_COUNT,
    VE_WEIGHTING:-1,
    VE_COMPUTED_OUTPUTS_CI:-2,
    VE_PARAM_CORREL_MATRIX: SYNAPSE_COUNT, #       2: Matrice de correlation entre parametres (NSynapse*NSynapse)
    VE_PARAMETERS_CI:-2, #           2: Liste des paramètres +- IC
    VE_RESAMPLING_SERIE:-1,
    VE_MULTI_RESULTS: CRITERIA_COUNT,
    VE_OUTPUT_DERIVATIVE: OUTPUT_COUNT,
    VE_IN_NORMALIZATION_SET: INPUT_COUNT | M_TRANSPOSE, # matrice de normalisation des entrees
    VE_OUT_NORMALIZATION_SET: OUTPUT_COUNT | M_TRANSPOSE, # matrice de normalisation des sorties
    VE_DATA_FORMAT:-1}    

INFO_D = {
    "inputcount": INPUT_COUNT,
    "outputcount": OUTPUT_COUNT,
    "order": ORDER, # 2
    "trainable": TRAINABLE, # 3
    "dimension": DIMENSION, # 5
    "layercount": LAYER_COUNT, # 6
    "driverclass": DRIVER_CLASS, # 7
    "hiddencount": HIDDEN_COUNT, # 8
    "trainsize": TRAIN_SIZE, # 9
    "resampling": RESAMPLING, # 10
    "status": STATUS, # 11
    "nodecount": NODE_COUNT, # 12
    "modelinputcount": MODEL_INPUT_COUNT, # 13
    "synapsecount": SYNAPSE_COUNT, # 14
    "datacount": DATA_COUNT, # 15
    "trainfuncindex": TRAIN_FUNC_INDEX, # 16
    "trainingend": TRAINING_END, # 17
    "dataloaded": DATA_LOADED, # 18
    "islin": IS_LIN, # 19
    "commentcount": COMMENT_COUNT, # 20
    "modelcount": MODEL_COUNT, # 21
    "activationfunccount": FUNC_ACT_COUNT, # 22
    "costfunccount": FUNC_COST_COUNT, # 23
    "proxfunccount": FUNC_PROX_COUNT, # 24
    "decayfunccount": FUNC_DECAY_COUNT, # 25
    "valishandle": VALID_HANDLE, # 26
    "savingformat": SAVING_FORMAT, # 27
    "trainmodelcount": TRAIN_MODEL_COUNT, # 28
    "resamplingtype": RESAMPLING_TYPE, # 29
    "trainingalgorithm": TRAINING_ALGORITHM, # 30
    "selectedoutput": SELECTED_OUTPUT, # 31
    "proximity": PROXIMITY, # 32
    "decay": DECAY, # 33
    "proximitydecay": PROXIMITYDECAY, # 34
    "reversemode": REVERSEMODE, # 35
    "bestindex": BEST_INDEX, # 36
    "criterion": CRITERION, # 37
    "multitrainciunt": MULTITRAIN_COUNT, # 38
    "testsize": TEST_SIZE, # 39
    "testgroup": TEST_GROUP, # 40
    "savetemp": SAVE_TEMP, # 41
    "epochs": EPOCHS, #43
    #"traincount": TRAIN_COUNT, # 43
    "trainingresultcount": TRAINING_RESULT_COUNT, # 44
    "verbose": VERBOSE, # 46
    "resamplingtraincount": RESAMPLING_EPOCHS, # 47
    #"langid": LANG_ID, # 48 lit ert ecrit la langue active. Disponibles 0x0409 (ENU), 0x040C (FRA)

    "loadwithweighting": LOAD_WITH_WEIGHTING, # 50
    "modelstyle": MODEL_STYLE, # 51
    "directgradient": DIRECT_GRADIENT, # 52 methode directe de calcul du gradient
    "handle": HANDLE, # 53 index = 0 -> Nombre de modeles vivants; index > 0 -> handle du modele d'indice index - 1
    "costhistorycount": COST_HISTORY_COUNT, # 54
    "criteriacount": CRITERIA_COUNT,         # 55
    "unicode": UNICODE, # 56 boolean codege unicode
    "integratednorm": INTEGRATED_NORM, # 57
    "randseed": RAND_SEED, # 58
    "drivercount": DRIVER_COUNT,            # 59
    }           

def getActivIndex(activ):
    """Recherche de l'indice de la fonction d'activation decrite par activ.
    "activ" peut etre un indice entierou un nom raccourci de fonction. Les noms 
    acceptes sont :
    '': Identite
    'IDENTITY': Identite
    'UNIT': Unite
    'UNITY': Unite
    'TANH': Tangente hyperbolique
    'TH': Tangente hyperbolique
    'STEP': Echelon
    'GAUSS': Gaussienne
    'GAUSSIAN': Gaussienne
    'SINE': Sinus
    'SIN': Sinus
    'EXP':Exponentielle,
    'EXPONENT': Exponentielle
    'QUADRATIC': Demi carre
    'ATAN': Arc tangente
    'ARCTAN': Arc tangente
    'MOMENT0': Moment 0
    'MOMENT1': Moment 1
    'REVERSE': REVERSE,
    'LOG': Logarithme
    'LOGARITHM': Logarithme
    'CUBIC': Cibique
    'QUASIABS': Quasi absolu
    'SIGMOID': Sigmoïde,
    'COMPLEMENT': Complement à 1
    'ROOT': Racine carree
    'ARCSH': Argument Sinus Hyperbolique
    'SQR': Carre,
    'SQARE': Carre,
    'COS': Cosinus
    'COSINE': Cosinus
    'ERF': Fonction d'erreur
    'ERRORFUNCTION': Fonction d'erreur
    'NORMALIZEDGAUSS':Gaussienne normalisee
    'GAUSSN': Gaussienne normalisee"""
    try:
        if isinstance(activ, int): return activ
        if isinstance(activ, str):
            try:
                return int(activ) 
            except:
                return activByName[activ.upper()]
    except: pass
    raise Exception("Cannot find activation function %s" % str(activ))
    
    