# Automatically generated by pb2py
# fmt: off
if False:
    from typing_extensions import Literal

Initialize = 0  # type: Literal[0]
Ping = 1  # type: Literal[1]
Success = 2  # type: Literal[2]
Failure = 3  # type: Literal[3]
ChangePin = 4  # type: Literal[4]
WipeDevice = 5  # type: Literal[5]
GetEntropy = 9  # type: Literal[9]
Entropy = 10  # type: Literal[10]
LoadDevice = 13  # type: Literal[13]
ResetDevice = 14  # type: Literal[14]
Features = 17  # type: Literal[17]
PinMatrixRequest = 18  # type: Literal[18]
PinMatrixAck = 19  # type: Literal[19]
Cancel = 20  # type: Literal[20]
ClearSession = 24  # type: Literal[24]
ApplySettings = 25  # type: Literal[25]
ButtonRequest = 26  # type: Literal[26]
ButtonAck = 27  # type: Literal[27]
ApplyFlags = 28  # type: Literal[28]
BackupDevice = 34  # type: Literal[34]
EntropyRequest = 35  # type: Literal[35]
EntropyAck = 36  # type: Literal[36]
PassphraseRequest = 41  # type: Literal[41]
PassphraseAck = 42  # type: Literal[42]
PassphraseStateRequest = 77  # type: Literal[77]
PassphraseStateAck = 78  # type: Literal[78]
RecoveryDevice = 45  # type: Literal[45]
WordRequest = 46  # type: Literal[46]
WordAck = 47  # type: Literal[47]
GetFeatures = 55  # type: Literal[55]
SetU2FCounter = 63  # type: Literal[63]
SdProtect = 79  # type: Literal[79]
GetNextU2FCounter = 80  # type: Literal[80]
NextU2FCounter = 81  # type: Literal[81]
ChangeWipeCode = 82  # type: Literal[82]
FirmwareErase = 6  # type: Literal[6]
FirmwareUpload = 7  # type: Literal[7]
FirmwareRequest = 8  # type: Literal[8]
SelfTest = 32  # type: Literal[32]
GetPublicKey = 11  # type: Literal[11]
PublicKey = 12  # type: Literal[12]
SignTx = 15  # type: Literal[15]
TxRequest = 21  # type: Literal[21]
TxAck = 22  # type: Literal[22]
GetAddress = 29  # type: Literal[29]
Address = 30  # type: Literal[30]
SignMessage = 38  # type: Literal[38]
VerifyMessage = 39  # type: Literal[39]
MessageSignature = 40  # type: Literal[40]
CipherKeyValue = 23  # type: Literal[23]
CipheredKeyValue = 48  # type: Literal[48]
SignIdentity = 53  # type: Literal[53]
SignedIdentity = 54  # type: Literal[54]
GetECDHSessionKey = 61  # type: Literal[61]
ECDHSessionKey = 62  # type: Literal[62]
CosiCommit = 71  # type: Literal[71]
CosiCommitment = 72  # type: Literal[72]
CosiSign = 73  # type: Literal[73]
CosiSignature = 74  # type: Literal[74]
DebugLinkDecision = 100  # type: Literal[100]
DebugLinkGetState = 101  # type: Literal[101]
DebugLinkState = 102  # type: Literal[102]
DebugLinkStop = 103  # type: Literal[103]
DebugLinkLog = 104  # type: Literal[104]
DebugLinkMemoryRead = 110  # type: Literal[110]
DebugLinkMemory = 111  # type: Literal[111]
DebugLinkMemoryWrite = 112  # type: Literal[112]
DebugLinkFlashErase = 113  # type: Literal[113]
DebugLinkLayout = 9001  # type: Literal[9001]
EthereumGetPublicKey = 450  # type: Literal[450]
EthereumPublicKey = 451  # type: Literal[451]
EthereumGetAddress = 56  # type: Literal[56]
EthereumAddress = 57  # type: Literal[57]
EthereumSignTx = 58  # type: Literal[58]
EthereumTxRequest = 59  # type: Literal[59]
EthereumTxAck = 60  # type: Literal[60]
EthereumSignMessage = 64  # type: Literal[64]
EthereumVerifyMessage = 65  # type: Literal[65]
EthereumMessageSignature = 66  # type: Literal[66]
NEMGetAddress = 67  # type: Literal[67]
NEMAddress = 68  # type: Literal[68]
NEMSignTx = 69  # type: Literal[69]
NEMSignedTx = 70  # type: Literal[70]
NEMDecryptMessage = 75  # type: Literal[75]
NEMDecryptedMessage = 76  # type: Literal[76]
LiskGetAddress = 114  # type: Literal[114]
LiskAddress = 115  # type: Literal[115]
LiskSignTx = 116  # type: Literal[116]
LiskSignedTx = 117  # type: Literal[117]
LiskSignMessage = 118  # type: Literal[118]
LiskMessageSignature = 119  # type: Literal[119]
LiskVerifyMessage = 120  # type: Literal[120]
LiskGetPublicKey = 121  # type: Literal[121]
LiskPublicKey = 122  # type: Literal[122]
TezosGetAddress = 150  # type: Literal[150]
TezosAddress = 151  # type: Literal[151]
TezosSignTx = 152  # type: Literal[152]
TezosSignedTx = 153  # type: Literal[153]
TezosGetPublicKey = 154  # type: Literal[154]
TezosPublicKey = 155  # type: Literal[155]
StellarSignTx = 202  # type: Literal[202]
StellarTxOpRequest = 203  # type: Literal[203]
StellarGetAddress = 207  # type: Literal[207]
StellarAddress = 208  # type: Literal[208]
StellarCreateAccountOp = 210  # type: Literal[210]
StellarPaymentOp = 211  # type: Literal[211]
StellarPathPaymentOp = 212  # type: Literal[212]
StellarManageOfferOp = 213  # type: Literal[213]
StellarCreatePassiveOfferOp = 214  # type: Literal[214]
StellarSetOptionsOp = 215  # type: Literal[215]
StellarChangeTrustOp = 216  # type: Literal[216]
StellarAllowTrustOp = 217  # type: Literal[217]
StellarAccountMergeOp = 218  # type: Literal[218]
StellarManageDataOp = 220  # type: Literal[220]
StellarBumpSequenceOp = 221  # type: Literal[221]
StellarSignedTx = 230  # type: Literal[230]
CardanoSignTx = 303  # type: Literal[303]
CardanoTxRequest = 304  # type: Literal[304]
CardanoGetPublicKey = 305  # type: Literal[305]
CardanoPublicKey = 306  # type: Literal[306]
CardanoGetAddress = 307  # type: Literal[307]
CardanoAddress = 308  # type: Literal[308]
CardanoTxAck = 309  # type: Literal[309]
CardanoSignedTx = 310  # type: Literal[310]
RippleGetAddress = 400  # type: Literal[400]
RippleAddress = 401  # type: Literal[401]
RippleSignTx = 402  # type: Literal[402]
RippleSignedTx = 403  # type: Literal[403]
MoneroTransactionInitRequest = 501  # type: Literal[501]
MoneroTransactionInitAck = 502  # type: Literal[502]
MoneroTransactionSetInputRequest = 503  # type: Literal[503]
MoneroTransactionSetInputAck = 504  # type: Literal[504]
MoneroTransactionInputsPermutationRequest = 505  # type: Literal[505]
MoneroTransactionInputsPermutationAck = 506  # type: Literal[506]
MoneroTransactionInputViniRequest = 507  # type: Literal[507]
MoneroTransactionInputViniAck = 508  # type: Literal[508]
MoneroTransactionAllInputsSetRequest = 509  # type: Literal[509]
MoneroTransactionAllInputsSetAck = 510  # type: Literal[510]
MoneroTransactionSetOutputRequest = 511  # type: Literal[511]
MoneroTransactionSetOutputAck = 512  # type: Literal[512]
MoneroTransactionAllOutSetRequest = 513  # type: Literal[513]
MoneroTransactionAllOutSetAck = 514  # type: Literal[514]
MoneroTransactionSignInputRequest = 515  # type: Literal[515]
MoneroTransactionSignInputAck = 516  # type: Literal[516]
MoneroTransactionFinalRequest = 517  # type: Literal[517]
MoneroTransactionFinalAck = 518  # type: Literal[518]
MoneroKeyImageExportInitRequest = 530  # type: Literal[530]
MoneroKeyImageExportInitAck = 531  # type: Literal[531]
MoneroKeyImageSyncStepRequest = 532  # type: Literal[532]
MoneroKeyImageSyncStepAck = 533  # type: Literal[533]
MoneroKeyImageSyncFinalRequest = 534  # type: Literal[534]
MoneroKeyImageSyncFinalAck = 535  # type: Literal[535]
MoneroGetAddress = 540  # type: Literal[540]
MoneroAddress = 541  # type: Literal[541]
MoneroGetWatchKey = 542  # type: Literal[542]
MoneroWatchKey = 543  # type: Literal[543]
DebugMoneroDiagRequest = 546  # type: Literal[546]
DebugMoneroDiagAck = 547  # type: Literal[547]
MoneroGetTxKeyRequest = 550  # type: Literal[550]
MoneroGetTxKeyAck = 551  # type: Literal[551]
MoneroLiveRefreshStartRequest = 552  # type: Literal[552]
MoneroLiveRefreshStartAck = 553  # type: Literal[553]
MoneroLiveRefreshStepRequest = 554  # type: Literal[554]
MoneroLiveRefreshStepAck = 555  # type: Literal[555]
MoneroLiveRefreshFinalRequest = 556  # type: Literal[556]
MoneroLiveRefreshFinalAck = 557  # type: Literal[557]
EosGetPublicKey = 600  # type: Literal[600]
EosPublicKey = 601  # type: Literal[601]
EosSignTx = 602  # type: Literal[602]
EosTxActionRequest = 603  # type: Literal[603]
EosTxActionAck = 604  # type: Literal[604]
EosSignedTx = 605  # type: Literal[605]
BinanceGetAddress = 700  # type: Literal[700]
BinanceAddress = 701  # type: Literal[701]
BinanceGetPublicKey = 702  # type: Literal[702]
BinancePublicKey = 703  # type: Literal[703]
BinanceSignTx = 704  # type: Literal[704]
BinanceTxRequest = 705  # type: Literal[705]
BinanceTransferMsg = 706  # type: Literal[706]
BinanceOrderMsg = 707  # type: Literal[707]
BinanceCancelMsg = 708  # type: Literal[708]
BinanceSignedTx = 709  # type: Literal[709]
WebAuthnListResidentCredentials = 800  # type: Literal[800]
WebAuthnCredentials = 801  # type: Literal[801]
WebAuthnAddResidentCredential = 802  # type: Literal[802]
WebAuthnRemoveResidentCredential = 803  # type: Literal[803]
